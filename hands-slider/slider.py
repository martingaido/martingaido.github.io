import cv2
import time
import numpy as np
import HandsTrackerModule as htm
import math

cap = cv2.VideoCapture(0)
pTime = 0
finalRange = 0
finalRangeBar = 400

detector = htm.handDetector()

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

while True:
	success, img = cap.read()

	# Find Hands
	img = detector.findHands(img)

	# Detect Position
	lmList = detector.findPosition(img, draw=False)

	if len(lmList) != 0:
		# Print Array of Results (landmark no.4 and 8)
		# print(lmList[4], lmList[8])

		x1, y1 = lmList[4][1], lmList[4][2]
		x2, y2 = lmList[8][1], lmList[8][2]
		cx, cy = (x1+x2)//2, (y1 + y2) // 2

		# Draw circles in every finger
		cv2.circle(img, (x1, y1), 15, (255,255,255), cv2.FILLED)
		cv2.circle(img, (x2, y2), 15, (255,255,255), cv2.FILLED)

		# Draw line that connects fingers
		cv2.line(img, (x1, y1), (x2, y2), (255,255,255), 3)

		# Draw circle in between (optional)
		cv2.circle(img, (cx, cy), 15, (255,255,255), cv2.FILLED)

		# Find the length between points
		length = math.hypot(x2 - x1, y2 - y1)
		#print(length)

		# Hand range 50 - 300
		finalRange = np.interp(length, [50, 400], [0, 100])
		finalRangeBar = np.interp(length, [50, 400], [400, 150])
		print(round(finalRange))

		if length < 50:
			# Draw green circle if lenght < 50
			cv2.circle(img, (cx, cy), 15, (0,255,0), cv2.FILLED)

	# Draw vertical bar
	cv2.rectangle(img, (50, 150), (85, 400), (255,255,255), 2)
	cv2.rectangle(img, (50, int(finalRangeBar)), (85, 400), (255,255,255), cv2.FILLED)

	# Calculate FPS
	cTime = time.time()
	fps = 1/(cTime - pTime)
	pTime = cTime

	# Print FPS Info
	cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
					1, (255,255,255), 2)

	# Rescale Capture
	frame = rescale_frame(img, percent=50)

	cv2.imshow("CAM Capture", frame)
	cv2.waitKey(1)
	cv2.destroyAllWindows()
