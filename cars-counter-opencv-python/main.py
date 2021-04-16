import cv2
import time
import datetime
from tracker import *

# Create tracker object
tracker = EuclideanDistTracker()

cap = cv2.VideoCapture("video.mov")

# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

counter = 0
pTime = 0

def convert_to_graysacale(frame):
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	return gray

while True:

    ret, frame = cap.read()
    height, width, _ = frame.shape

    # Extract Region of interest
    # roi = frame[340: 720, 500: 800]

    roi = frame[890:920, 300:1450]

    # 1. Object Detection
    mask = object_detector.apply(convert_to_graysacale(roi))

    # remove the shadows
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    detections = []

    for cnt in contours:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)

        if area > 2500:
            cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 1)
            x, y, w, h = cv2.boundingRect(cnt)
            detections.append([x, y, w, h])

    # 2. Object Tracking
    boxes_ids = tracker.update(detections)

    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        cv2.putText(roi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
        #cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)
        counter += 1
        
        start_time = datetime.datetime.now()
        end_time = datetime.datetime.now()
        time_diff = (end_time - start_time)
        execution_time = time_diff.total_seconds() * 1000
        print(execution_time)
        counter = execution_time
        

    if(counter > 0.00010):
        cv2.putText(frame, f'Objects: {str(id)}', (30, 130), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 2)
    
    cv2.rectangle(frame, (250, 800), (1500, 1000), (0, 255, 0), 3)
    
    # Calculate FPS
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

	# Print FPS Info & Instructions
    cv2.putText(frame, 'Press ESC to exit, C to switch mode', (30, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
    cv2.putText(frame, f'FPS: {int(fps)}', (30, 90), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)

    #cv2.imshow("roi", roi)
    cv2.imshow("Frame", frame)
    #cv2.imshow("Mask", mask)

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()