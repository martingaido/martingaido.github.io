# Script to match faces in multiple images

# pip install opencv-python
# pip install deepface -- https://pypi.org/project/deepface/
import cv2
from deepface import DeepFace
import pprint

result  = DeepFace.verify("elon4.jpg", "elon6.jpg")
#results = DeepFace.verify([['image1.jpg', 'image2.jpg'], ['image1.jpg', 'image3.jpg']])

pprint.pprint(result)

print("Is verified: ", result["verified"])
