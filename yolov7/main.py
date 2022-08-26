import torch
import cv2
import numpy as np
import time

from utils.datasets import letterbox

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(3))
frame_height = int(camera.get(4))

weights = torch.load('C:\\Users\\choi\\PycharmProjects\\yolo7\\yolov7\\beset.pt')
model = weights['model']

while True:
    ret, frame = camera.read()
    if ret:
        #vid_write_image = letterbox(frame, (frame_width, frame_height), stride=64, auto=True)[0]
        #v2.imshow('test', vid_write_image)

        with torch.no_grad():
            output, _ = model(frame)

        cv2.imshow('image', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
              break

camera.release()
cv2.destroyAllWindows()
# https://www.youtube.com/watch?v=bkWeWmvYFvY
# python detect.windows --weights best.pt --conf 0.5 --img-size 640 --source 0 --view-img --no-trace