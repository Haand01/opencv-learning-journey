import os
import cv2

image_path = os.path.join('./','assets', '3.jpg')
image = cv2.resize(cv2.imread(image_path), (600, 400))
cv2.imshow('Original Image', image)
# tradational blur
blurred_image = cv2.blur(image, (15, 15))
cv2.imshow('Blurred Image', blurred_image)

# gaussian blur
gaussian_blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imshow('Gaussian Blurred Image', gaussian_blurred_image)

# median blur
median_blurred_image = cv2.medianBlur(image, 15)
cv2.imshow('Median Blurred Image', median_blurred_image)

cv2.waitKey(0)