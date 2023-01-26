import cv2
import numpy as np

# Read the image
img = cv2.imread("original.jpg")

# Compress the image
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

# Save the compressed image
cv2.imwrite("compressed.jpg", img)
