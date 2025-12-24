import os
import cv2

image_path = os.path.join('./','assets', '2.jpg')
image = cv2.imread(image_path)
resized_image = cv2.resize(image, (600, 400))
cv2.imshow('Image', resized_image)
image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB Image', image_rgb)
image_gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', image_gray)
image_hsv = cv2.cvtColor(resized_image, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Image', image_hsv)
cv2.waitKey(0)