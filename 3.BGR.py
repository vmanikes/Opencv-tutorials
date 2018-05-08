import cv2


image = cv2.imread("Master_OpenCV/images/input.jpg")

B, G, R = image[0][0] # First pixel

print(B, G, R)
print("image shape ", image.shape)

gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print(gray_scale[0][0]) # First pixel and only 1 value

#H: 0 - 180, S: 0 - 255, V: 0 - 255

image = cv2.imread('./images/input.jpg')

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV image', hsv_image)
cv2.imshow('Hue channel', hsv_image[:, :, 0])
cv2.imshow('Saturation channel', hsv_image[:, :, 1])
cv2.imshow('Value channel', hsv_image[:, :, 2])

cv2.waitKey()
cv2.destroyAllWindows()

image = cv2.imread('./images/input.jpg')

# OpenCV's 'split' function splites the image into each color index
B, G, R = cv2.split(image)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Let's re-make the original image,
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)

# Let's amplify the blue color
merged = cv2.merge([B+100, G, R])
cv2.imshow("Merged with Blue Amplified", merged)

cv2.waitKey(0)
cv2.destroyAllWindows()
