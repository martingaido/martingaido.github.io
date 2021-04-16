import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Load an image
img = cv.imread("lena.jpg")

# Split image into BGR values
blue, green, red = cv.split(img)

# Render the original image
cv.imshow("Image", img)
cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

# Configure the histogram
plt.hist(img.ravel(), 256, [0, 256])
plt.hist(blue.ravel(), 256, [0, 256])
plt.hist(green.ravel(), 256, [0, 256])
plt.hist(red.ravel(), 256, [0, 256])

# Show the histogram
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
