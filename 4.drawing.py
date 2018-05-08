
# https://docs.opencv.org/3.1.0/dc/da5/tutorial_py_drawing_functions.html
import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8) # (height, length, 3 = BGR) uint8 for 8 bits as opencv stores in 8 bits

image2 = np.zeros((512, 512), np.uint8) # Grayscale

line = cv2.line(image, (0, 0), (511,511),(255,0,0),5) # (image, pt1, pt2, color, thickness)

cv2.imshow("h", line)

cv2.waitKey()
cv2.destroyAllWindows()