import argparse
import time
import winsound
from pathlib import Path

import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random

from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized, TracedModel

import csv
import datetime
import winsound

def zeroAdd(tmp):
    if len(tmp) == 1:
        tmp = '0' + tmp
    return tmp

def draw_text(img, text, x, y, r, g, b, bgr, bgg, bgb, center=False, thinkness = 2):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thinkness = thinkness
    text_color = (r, g, b)
    text_color_bg = (bgr, bgg, bgb)

    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thinkness)
    text_w, text_h = text_size
    offset = 5
    if center:
        cv2.rectangle(img, (320 - offset - text_w // 2, y - offset), (320 + text_w // 2 + offset, y + text_h + offset), text_color_bg, -1)
        cv2.putText(img, text, (320 - text_w // 2, y + text_h + font_scale - 1), font, font_scale, text_color, font_thinkness)
    else:
        cv2.rectangle(img, (x - offset, y - offset), (x + text_w + offset, y + text_h + offset), text_color_bg, -1)
        cv2.putText(img, text, (x, y + text_h + font_scale - 1), font, font_scale, text_color, font_thinkness)

def detect(save_img=False):
    #winsound.PlaySound('./src/start.wav', winsound.SND_FILENAME)
    #winsound.PlaySound('./src/warning.wav', winsound.SND_FILENAME)
    source, weights, view_img, save_txt, imgsz, trace = opt.source, opt.weights, opt.view_img, opt.save_txt, opt.img_size, not opt.no_trace
    save_img = not opt.nosave and not source.endswith('.txt')  # save inference images
    webcam = source.isnumeric() or source.endswith('.txt') or source.lower().startswith(
        ('rtsp://', 'rtmp://', 'http://', 'https://'))

    # Directories
    save_dir = Path(increment_path(Path(opt.project) / opt.name, exist_ok=opt.exist_ok))  # increment run

    # Initialize
    set_logging()
    device = select_device(opt.device)
    half = device.type != 'cpu'  # half precision only supported on CUDA

    # Load model
    model = attempt_load(weights, map_location=device)  # load FP32 model
    stride = int(model.stride.max())  # model stride
    imgsz = check_img_size(imgsz, s=stride)  # check img_size

    if trace:
        model = TracedModel(model, device, opt.img_size)

    if half:
        model.half()  # to FP16

    # Second-stage classifier
    classify = False
    if classify:
        modelc = load_classifier(name='resnet101', n=2)  # initialize
        modelc.load_state_dict(torch.load('weights/resnet101.pt', map_location=device)['model']).to(device).eval()

    # Set Dataloader
    vid_path, vid_writer = None, None
    if webcam:
        view_img = check_imshow()
        cudnn.benchmark = True  # set True to speed up constant image size inference
        dataset = LoadStreams(source, img_size=imgsz, stride=stride)
    else:
        dataset = LoadImages(source, img_size=imgsz, stride=stride)

    # Get names and colors
    names = model.module.names if hasattr(model, 'module') else model.names
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in names]

    # Run inference
    if device.type != 'cpu':
        model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))  # run once
    old_img_w = old_img_h = imgsz
    old_img_b = 1

    blink_cnt = 0
    prev_blink = False
    blink_arr_int = []
    blink_arr_float = []
    t0 = time.time()
    for path, img, im0s, vid_cap in dataset:
        start_time = time.time()

        img = torch.from_numpy(img).to(device)
        img = img.half() if half else img.float()  # uint8 to fp16/32
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        # Warmup
        if device.type != 'cpu' and (old_img_b != img.shape[0] or old_img_h != img.shape[2] or old_img_w != img.shape[3]):
            old_img_b = img.shape[0]
            old_img_h = img.shape[2]
            old_img_w = img.shape[3]
            for i in range(3):
                model(img, augment=opt.augment)[0]

        # Inference
        t1 = time_synchronized()
        pred = model(img, augment=opt.augment)[0]
        t2 = time_synchronized()

        # Apply NMS
        pred = non_max_suppression(pred, opt.conf_thres, opt.iou_thres, classes=opt.classes, agnostic=opt.agnostic_nms)
        t3 = time_synchronized()

        # Apply Classifier
        if classify:
            pred = apply_classifier(pred, modelc, img, im0s)

        # Process detections
        for i, det in enumerate(pred):  # detections per image
            if webcam:  # batch_size >= 1
                p, s, im0, frame = path[i], '%g: ' % i, im0s[i].copy(), dataset.count
            else:
                p, s, im0, frame = path, '', im0s, getattr(dataset, 'frame', 0)

            p = Path(p)  # to Path
            txt_path = str(save_dir / 'labels' / p.stem) + ('' if dataset.mode == 'image' else f'_{frame}')  # img.txt
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh

            oe_cnt = 0
            ce_cnt = 0
            if len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                # Print results
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s += f"{n} {names[int(c)]}{'s' * (n > 1)}"  # add to string
                    n = int(n)
                    if 'open eye' == names[int(c)]:
                        oe_cnt = n
                    if 'closed eye' == names[int(c)]:
                        ce_cnt = n

                # Write results
                for *xyxy, conf, cls in reversed(det):
                    if save_txt:  # Write to file
                        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                        line = (cls, *xywh, conf) if opt.save_conf else (cls, *xywh)  # label format
                        with open(txt_path + '.txt', 'a') as f:
                            f.write(('%g ' * len(line)).rstrip() % line + '\n')

                    if save_img or view_img:  # Add bbox to image
                        label = f'{names[int(cls)]} {conf:.2f}'
                        plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=1)

            # Stream results
            if view_img:
                terminate_time = time.time()
                run_time = terminate_time - t0
                if len(blink_arr_int) != int(run_time) + 1:
                    blink_arr_int.append(0)

                # calculate blinkResult per minute
                if oe_cnt == 0 and ce_cnt == 2:  # closed
                    prev_blink = True
                    blink_arr_float.append([run_time, 1])

                if oe_cnt == 2 and ce_cnt == 0:  # open
                    blink_arr_float.append([run_time, -1])
                    if prev_blink == True:
                        blink_arr_int[int(run_time)] += 1
                        blink_cnt += 1
                        prev_blink = False

                if not(oe_cnt == 2 and ce_cnt == 0) and not(oe_cnt == 0 and ce_cnt == 2):
                    blink_arr_float.append([run_time, 0])


                fps = terminate_time - start_time

                fps_string = f'{1./fps:.2f} fps'
                sec_string = f'RunTime {str(datetime.timedelta(seconds=int(run_time)))}'
                draw_text(im0, fps_string, 10, 10, 255, 255, 255, 0, 0, 0)
                draw_text(im0, sec_string, 10, 450, 255, 255, 255, 0, 0, 0)

                bpm_at = blink_cnt * 60 / run_time # bpm all time
                bpm_com = sum(blink_arr_int[int(run_time) - 60:int(run_time)]) # bpm current one min
                cv2.ellipse(im0, ((320, 240), (240, 360), 0), (0, 255, 0), 2)
                if run_time <= 60:
                    draw_text(im0, f'Analyzing Blink, {60 - int(run_time)}sec left', 0, 400, 255, 255, 255, 0, 0, 0, True)
                else:
                    draw_text(im0, f'{bpm_at:.2f}BPM [all time]', 0, 360, 255, 255, 255, 0, 0, 0, True, 1)
                    draw_text(im0, f'{bpm_com:.2f}BPM [current 1 min]', 0, 400, 255, 255, 255, 0, 0, 0, True, 1)
                    if bpm_com <= 7:
                        draw_text(im0, 'Warning', 0, 120, 0, 255, 255, 255, 0, 0, True, 1)

                cv2.imshow(str(p), im0)
                if run_time >= 90:
                    break

                if cv2.waitKey(1) == ord('q'):
                    break

            print('current time: ', f'{terminate_time-t0:.2f}', 'sec', '   | open eye: ', oe_cnt, '   | closed eye: ', ce_cnt, '   | blink_per_minute: ', f'{bpm_com:.2f}')

    print(f'Detecting Exit. ({time.time() - t0:.3f}s)')
    #winsound.PlaySound('./src/end.wav', winsound.SND_FILENAME)

    now = datetime.datetime.now()
    month = zeroAdd(str(now.month))
    day = zeroAdd(str(now.day))
    hour = zeroAdd(str(now.hour))
    min = zeroAdd(str(now.minute))
    sec = zeroAdd(str(now.second))

    path_result = 'C:/Users/choi/PycharmProjects/yolo7/blinkResult/'
    filename_int = path_result + "bi" + str(now.year) + month + day + '_' + hour + min + sec + '.csv'
    filename_float = path_result + "bf" + str(now.year) + month + day + '_' + hour + min + sec + '.csv'

    with open(filename_int, 'w', newline='') as f:
        write = csv.writer(f)
        write.writerow(['idx', 'sec', 'blink_cnt'])
        for i in range(len(blink_arr_int)):
            write.writerow([i, i, blink_arr_int[i]])

    with open(filename_float, 'w', newline='') as f:
        write = csv.writer(f)
        write.writerow(['idx', 'sec', 'closed'])
        for i in range(len(blink_arr_float)):
            write.writerow([i, blink_arr_float[i][0], blink_arr_float[i][1]])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='yolov7.pt', help='model.pt path(s)')
    parser.add_argument('--source', type=str, default='inference/images', help='source')  # file/folder, 0 for webcam
    parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='object confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--view-img', action='store_true', help='display results')
    parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
    parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
    parser.add_argument('--nosave', action='store_true', help='do not save images/videos')
    parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--update', action='store_true', help='update all models')
    parser.add_argument('--project', default='runs/detect', help='save results to project/name')
    parser.add_argument('--name', default='exp', help='save results to project/name')
    parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
    parser.add_argument('--no-trace', action='store_true', help='don`t trace model')
    opt = parser.parse_args()
    print(opt)
    #check_requirements(exclude=('pycocotools', 'thop'))

    with torch.no_grad():
        if opt.update:  # update all models (to fix SourceChangeWarning)
            for opt.weights in ['yolov7.pt']:
                detect()
                strip_optimizer(opt.weights)
        else:
            detect()
