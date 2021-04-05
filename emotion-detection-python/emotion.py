# Script to detect gender, age, race and emotion of an image

# pip install opencv-python
# pip install deepface -- https://pypi.org/project/deepface/
import cv2
from deepface import DeepFace
import pprint

# Load Image
img = cv2.imread('image1.jpg')

# Process Image (returns a dictionary)
predictions = DeepFace.analyze(img)

# Print Prediction
# pprint.pprint(predictions)

print("Gender  : ", predictions["gender"])
print("Age     : ", predictions["age"])
print("Race    : ", predictions["dominant_race"])
print("Emotion : ", predictions["dominant_emotion"])
