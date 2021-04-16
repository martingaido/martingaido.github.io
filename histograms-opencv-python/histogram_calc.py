import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Load Image
img = cv.imread("lena.jpg", 0) # grayscale

hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)

# Show Histogram
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
