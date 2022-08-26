import cv2 as cv
import mediapipe as mp
import time
import utils, math
import numpy as np
import datetime

# variables
CEF_COUNTER = 0
TOTAL_BLINKS = 0
# constants
CLOSED_EYES_FRAME = 3
FONTS = cv.FONT_HERSHEY_COMPLEX

# face bounder indices
FACE_OVAL = [10, 338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288, 397, 365, 379, 378, 400, 377, 152, 148, 176,
             149, 150, 136, 172, 58, 132, 93, 234, 127, 162, 21, 54, 103, 67, 109]

# lips indices for Landmarks
LIPS = [61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95, 185, 40, 39,
        37, 0, 267, 269, 270, 409, 415, 310, 311, 312, 13, 82, 81, 42, 183, 78]
LOWER_LIPS = [61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95]
UPPER_LIPS = [185, 40, 39, 37, 0, 267, 269, 270, 409, 415, 310, 311, 312, 13, 82, 81, 42, 183, 78]
# Left eyes indices
LEFT_EYE = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
LEFT_EYEBROW = [336, 296, 334, 293, 300, 276, 283, 282, 295, 285]

# right eyes indices
RIGHT_EYE = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
RIGHT_EYEBROW = [70, 63, 105, 66, 107, 55, 65, 52, 53, 46]

map_face_mesh = mp.solutions.face_mesh
# camera object
camera = cv.VideoCapture(0)

def draw_text(img, text, x, y, r, g, b, bgr, bgg, bgb, center=False, thinkness = 2):
    font = cv.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thinkness = thinkness
    text_color = (r, g, b)
    text_color_bg = (bgr, bgg, bgb)

    text_size, _ = cv.getTextSize(text, font, font_scale, font_thinkness)
    text_w, text_h = text_size
    offset = 5
    if center:
        cv.rectangle(img, (320 - offset - text_w // 2, y - offset), (320 + text_w // 2 + offset, y + text_h + offset), text_color_bg, -1)
        cv.putText(img, text, (320 - text_w // 2, y + text_h + font_scale - 1), font, font_scale, text_color, font_thinkness)
    else:
        cv.rectangle(img, (x - offset, y - offset), (x + text_w + offset, y + text_h + offset), text_color_bg, -1)
        cv.putText(img, text, (x, y + text_h + font_scale - 1), font, font_scale, text_color, font_thinkness)

# landmark detection function
def landmarksDetection(img, results, draw=False):
    img_height, img_width = img.shape[:2]
    # list[(x,y), (x,y)....]
    mesh_coord = [(int(point.x * img_width), int(point.y * img_height)) for point in
                  results.multi_face_landmarks[0].landmark]
    if draw:
        [cv.circle(img, p, 2, (0, 255, 0), -1) for p in mesh_coord]

    # returning the list of tuples for each landmarks
    return mesh_coord


# Euclaidean distance
def euclaideanDistance(point, point1):
    x, y = point
    x1, y1 = point1
    distance = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
    return distance


# Blinking Ratio
def blinkRatio(img, landmarks, right_indices, left_indices):
    # Right eyes
    # horizontal line
    rh_right = landmarks[right_indices[0]]
    rh_left = landmarks[right_indices[8]]
    # vertical line
    rv_top = landmarks[right_indices[12]]
    rv_bottom = landmarks[right_indices[4]]
    # draw lines on right eyes
    # cv.line(img, rh_right, rh_left, utils.GREEN, 2)
    # cv.line(img, rv_top, rv_bottom, utils.WHITE, 2)

    # LEFT_EYE
    # horizontal line
    lh_right = landmarks[left_indices[0]]
    lh_left = landmarks[left_indices[8]]

    # vertical line
    lv_top = landmarks[left_indices[12]]
    lv_bottom = landmarks[left_indices[4]]

    rhDistance = euclaideanDistance(rh_right, rh_left)
    rvDistance = euclaideanDistance(rv_top, rv_bottom)

    lvDistance = euclaideanDistance(lv_top, lv_bottom)
    lhDistance = euclaideanDistance(lh_right, lh_left)

    reRatio = rhDistance / rvDistance
    leRatio = lhDistance / lvDistance

    ratio = (reRatio + leRatio) / 2
    return ratio


# Eyes Extrctor function,
def eyesExtractor(img, right_eye_coords, left_eye_coords):
    # converting color image to  scale image
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # getting the dimension of image
    dim = gray.shape

    # creating mask from gray scale dim
    mask = np.zeros(dim, dtype=np.uint8)

    # drawing Eyes Shape on mask with white color
    cv.fillPoly(mask, [np.array(right_eye_coords, dtype=np.int32)], 255)
    cv.fillPoly(mask, [np.array(left_eye_coords, dtype=np.int32)], 255)

    # showing the mask
    # cv.imshow('mask', mask)

    # draw eyes image on mask, where white shape is
    eyes = cv.bitwise_and(gray, gray, mask=mask)
    # change black color to gray other than eys
    # cv.imshow('eyes draw', eyes)
    eyes[mask == 0] = 155

    # getting minium and maximum x and y  for right and left eyes
    # For Right Eye
    r_max_x = (max(right_eye_coords, key=lambda item: item[0]))[0]
    r_min_x = (min(right_eye_coords, key=lambda item: item[0]))[0]
    r_max_y = (max(right_eye_coords, key=lambda item: item[1]))[1]
    r_min_y = (min(right_eye_coords, key=lambda item: item[1]))[1]

    # For LEFT Eye
    l_max_x = (max(left_eye_coords, key=lambda item: item[0]))[0]
    l_min_x = (min(left_eye_coords, key=lambda item: item[0]))[0]
    l_max_y = (max(left_eye_coords, key=lambda item: item[1]))[1]
    l_min_y = (min(left_eye_coords, key=lambda item: item[1]))[1]

    # croping the eyes from mask
    cropped_right = eyes[r_min_y: r_max_y, r_min_x: r_max_x]
    cropped_left = eyes[l_min_y: l_max_y, l_min_x: l_max_x]

    # returning the cropped eyes
    return cropped_right, cropped_left


# Eyes Postion Estimator
def positionEstimator(cropped_eye):
    # getting height and width of eye
    h, w = cropped_eye.shape

    # remove the noise from images
    gaussain_blur = cv.GaussianBlur(cropped_eye, (9, 9), 0)
    median_blur = cv.medianBlur(gaussain_blur, 3)

    # applying thrsholding to convert binary_image
    ret, threshed_eye = cv.threshold(median_blur, 130, 255, cv.THRESH_BINARY)

    # create fixd part for eye with
    piece = int(w / 3)

    # slicing the eyes into three parts
    right_piece = threshed_eye[0:h, 0:piece]
    center_piece = threshed_eye[0:h, piece: piece + piece]
    left_piece = threshed_eye[0:h, piece + piece:w]

    # calling pixel counter function
    eye_position, color = pixelCounter(right_piece, center_piece, left_piece)

    return eye_position, color


# creating pixel counter function
def pixelCounter(first_piece, second_piece, third_piece):
    # counting black pixel in each part
    right_part = np.sum(first_piece == 0)
    center_part = np.sum(second_piece == 0)
    left_part = np.sum(third_piece == 0)
    # creating list of these values
    eye_parts = [right_part, center_part, left_part]

    # getting the index of max values in the list
    max_index = eye_parts.index(max(eye_parts))
    pos_eye = ''
    if max_index == 0:
        pos_eye = "RIGHT"
        color = [utils.BLACK, utils.GREEN]
    elif max_index == 1:
        pos_eye = 'CENTER'
        color = [utils.YELLOW, utils.PINK]
    elif max_index == 2:
        pos_eye = 'LEFT'
        color = [utils.GRAY, utils.YELLOW]
    else:
        pos_eye = "Closed"
        color = [utils.GRAY, utils.YELLOW]
    return pos_eye, color


with map_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
    t0 = time.time()
    # starting Video loop here.
    while True:
        # starting time here
        start_time = time.time()
        ret, frame = camera.read()  # getting frame from camera

        if not ret:
            break  # no more frames break
        #  resizing frame
        frame = cv.resize(frame, None, fx=1, fy=1, interpolation=cv.INTER_CUBIC)

        frame_height, frame_width = frame.shape[:2]
        rgb_frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
        results = face_mesh.process(rgb_frame)
        if results.multi_face_landmarks:
            mesh_coords = landmarksDetection(frame, results, False)
            ratio = blinkRatio(frame, mesh_coords, RIGHT_EYE, LEFT_EYE)

            if ratio > 7.5:
                CEF_COUNTER += 1
            else:
                if CEF_COUNTER > CLOSED_EYES_FRAME:
                    TOTAL_BLINKS += 1
                    CEF_COUNTER = 0
            cv.polylines(frame, [np.array([mesh_coords[p] for p in LEFT_EYE], dtype=np.int32)], True, utils.GREEN, 1,
                         cv.LINE_AA)
            cv.polylines(frame, [np.array([mesh_coords[p] for p in RIGHT_EYE], dtype=np.int32)], True, utils.GREEN, 1,
                         cv.LINE_AA)

            # Blink Detector Counter Completed
            right_coords = [mesh_coords[p] for p in RIGHT_EYE]
            left_coords = [mesh_coords[p] for p in LEFT_EYE]
            crop_right, crop_left = eyesExtractor(frame, right_coords, left_coords)
            eye_position, color = positionEstimator(crop_right)
            utils.colorBackgroundText(frame, f'R: {eye_position}', FONTS, 1.0, (20, 300), 1, color[0], color[1], 8, 8)
            eye_position_left, color = positionEstimator(crop_left)
            utils.colorBackgroundText(frame, f'L: {eye_position_left}', FONTS, 1.0, (20, 340), 1, color[0], color[1], 8, 8)

        # calculating  frame per seconds FPS
        terminate_time = time.time()
        fps = terminate_time - start_time
        run_time = terminate_time - t0
        sec_string = f'RunTime {str(datetime.timedelta(seconds=int(run_time)))}'
        cv.ellipse(frame, ((320, 240), (240, 360), 0), (0, 255, 0), 2)
        draw_text(frame, f'{1./fps:.2f} fps', 10, 10, 255, 255, 255, 0, 0, 0)
        draw_text(frame, sec_string, 10, 450, 255, 255, 255, 0, 0, 0)
        cv.imshow('frame', frame)
        key = cv.waitKey(2)
        if key == ord('q') or key == ord('Q'):
            break
    cv.destroyAllWindows()
    camera.release()