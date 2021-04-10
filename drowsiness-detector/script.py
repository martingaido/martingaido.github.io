#!/usr/bin/env python

import cv2
import dlib
import time
import math
from scipy.spatial import distance

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

def convert_to_graysacale(frame, switch):
	if switch == True:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	else:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	return gray

def calculate_EAR(eye):
	A = distance.euclidean(eye[1], eye[5])
	B = distance.euclidean(eye[2], eye[4])
	C = distance.euclidean(eye[0], eye[3])
	ear_aspect_ratio = (A+B)/(2.0*C)
	return ear_aspect_ratio

# Init CAM
cap = cv2.VideoCapture(0)

hog_face_detector = dlib.get_frontal_face_detector()
dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
pTime = 0
counter = 0
minEar = 0
isColor = False

while True:
	_, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = hog_face_detector(gray)

	for face in faces:
		face_landmarks = dlib_facelandmark(gray, face)

		leftEye = []
		rightEye = []

		for n in range(36,42):
			x = face_landmarks.part(n).x
			y = face_landmarks.part(n).y
			leftEye.append((x,y))
			next_point = n+1
			if n == 41:
				next_point = 36
			x2 = face_landmarks.part(next_point).x
			y2 = face_landmarks.part(next_point).y
			cv2.line(frame,(x,y),(x2,y2),(255, 255, 255) ,1)

		for n in range(42,48):
			x = face_landmarks.part(n).x
			y = face_landmarks.part(n).y
			rightEye.append((x,y))
			next_point = n+1
			if n == 47:
				next_point = 42
			x2 = face_landmarks.part(next_point).x
			y2 = face_landmarks.part(next_point).y
			cv2.line(frame,(x,y),(x2,y2),(255, 255, 255) ,1)

		left_ear = calculate_EAR(leftEye)
		right_ear = calculate_EAR(rightEye)

		EAR = (left_ear+right_ear)/2
		EAR = round(EAR,2)

		if EAR < 0.26: # <---- Trigger
			cv2.putText(frame, 'Warning!', (30, 260), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
			cv2.putText(frame, 'Are you falling asleep?', (30, 300), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

			counter += 1

			if minEar < EAR:
				minEar = EAR

			# Play Sound
			# print('\a')
			print(f'--- Warning --- : {counter}')

		cv2.putText(frame, f'EAR: {EAR}', (30, 130), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
		cv2.putText(frame, f'Min EAR: {minEar}', (30, 170), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
		cv2.putText(frame, f'Counter: {counter}', (30, 210), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)

	# Calculate FPS
	cTime = time.time()
	fps = 1/(cTime - pTime)
	pTime = cTime

	# Print FPS Info & Instructions
	cv2.putText(frame, 'Press ESC to exit, C to switch mode', (30, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
	cv2.putText(frame, f'FPS: {int(fps)}', (30, 90), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)

	cv2.putText(frame, f'W: {frame.shape[1]} H: {frame.shape[0]} - Minimal AI', (30, frame.shape[0] - 30), cv2.FONT_HERSHEY_COMPLEX, .7, (255,255,255), 2)

	# Rescale Capture
	frame = rescale_frame(convert_to_graysacale(frame, isColor), percent=60)

	# Show Capture
	cv2.imshow("CAM Capture", frame)

	key = cv2.waitKey(1)

	if key == 67:
		if isColor == True:
			isColor = False
		else:
			isColor = True

	if key == 27:
		break

cap.release()
cv2.destroyAllWindows()
