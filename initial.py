import cv2

import numpy as np

image = cv2.imread("Master_OpenCV/images/input.jpg")
cv2.imshow("Hello", image) # Name on window and image

cv2.waitKey()
cv2.destroyAllWindows()

shape = image.shape # (Height, width, breadth) in pixels
print(shape)

cv2.imwrite("filename.jpg", image)