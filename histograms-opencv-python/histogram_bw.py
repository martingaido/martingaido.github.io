import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Create a black image (200x200px)
img = np.zeros((200, 200), np.uint8)

# Add a white rectangle
cv.rectangle(img, (0, 100), (200, 200), (255), -1)

# Add another rectangle
cv.rectangle(img, (0, 50), (100, 100), (127), -1)

# Render the image
cv.imshow("Image", img)

# Configure the histogram
plt.hist(img.ravel(), 256, [0, 256])

# Show the histogram
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
