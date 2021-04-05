# Script to detect gender, age, race and emotion of an image

# pip install opencv-python
# pip install deepface -- https://pypi.org/project/deepface/
import cv2
from deepface import DeepFace
import pprint

# not working?
DeepFace.stream("database")
