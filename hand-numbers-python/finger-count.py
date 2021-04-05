import cv2
import time
import os
import HandsTrackerModule as hdm

cap = cv2.VideoCapture(0)
pTime = 0


def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

# Instance detector with hardcoded confidence
detector = hdm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]

while True:

	success, img = cap.read()
	img = detector.findHands(img)

	# Find nodes in hands
	lmList = detector.findPosition(img, draw=False)

	if len(lmList) != 0:

		fingers = []

		# Thumb
		if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
			fingers.append(1)
		else:
			fingers.append(0)

		# 4 fingers
		for id in range(1, 5):
			if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
				fingers.append(1)
			else:
				fingers.append(0)

		# Debug, print fingers states
		# print(fingers)

		totalFingers = fingers.count(1)

		# Print Number
		cv2.putText(img, f'Num: {int(totalFingers)}', (20, 120), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)


	cTime = time.time()
	fps = 1/(cTime-pTime)
	pTime = cTime

	cv2.putText(img, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

	frame = rescale_frame(img, percent=50)
	cv2.imshow("Capture", frame)
	cv2.moveWindow("Capture", 50,50)
	cv2.waitKey(1)
	cv2.destroyAllWindows()
