import easyocr
import cv2
import numpy as np

# Capture from Webcam
cap = cv2.VideoCapture(0)

# Set Language
reader = easyocr.Reader(['en'])

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

def convert_to_graysacale(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray

while True:
    
    success, img = cap.read()
    result = reader.readtext(convert_to_graysacale(img))
    font = cv2.FONT_HERSHEY_COMPLEX

    # img = cv2.imread(img)
    spacer = 50
    for detection in result: 
        top_left = tuple(detection[0][0])
        bottom_right = tuple(detection[0][2])
        text = detection[1]
        img = cv2.putText(img, text, (20, spacer), font, 1, (255,255,255), 2, cv2.LINE_AA)
        spacer+=35

    frame = rescale_frame(convert_to_graysacale(img), percent=50)
    
    cv2.imshow("Webcam Capture", frame)
    cv2.waitKey(1)
