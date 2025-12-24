import os
import numpy as np
import cv2


image = cv2.imread(os.path.join('./','assets', 'birds.jpg'))
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image_thresholded = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY_INV)[1]
contours, hierarchy = cv2.findContours(image_thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
# x1,y1, h ,w = cv2.boundingRect(contours)
# cv2.rectengle(img,(x1,y1),(x1+w,y1+h),(0,255,0),2)


cv2.imshow('Original Image', image)
cv2.imshow('Gray Image', image_gray)
cv2.imshow('Thresholded Image', image_thresholded)
cv2.waitKey(0)