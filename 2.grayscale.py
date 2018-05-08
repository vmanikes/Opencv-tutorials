import cv2


image = cv2.imread("Master_OpenCV/images/input.jpg")

gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Easier to process as it is basically in 2D and takes less processing

cv2.imshow("Hello", gray_scale) # Name on window and image

cv2.waitKey()
cv2.destroyAllWindows()