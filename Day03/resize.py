import os
import cv2

image_path = os.path.join('./','assets','1.jpg')

image = cv2.imread(image_path)
print(image.shape)
image_resized = cv2.resize(image, (300, 300))
print(image_resized.shape)

cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', image_resized)
cv2.waitKey(0)