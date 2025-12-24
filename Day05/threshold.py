import os
import cv2
import numpy as np


image_gray = cv2.imread(os.path.join("./","assets", "handwriting.png"), cv2.IMREAD_GRAYSCALE)
# gray_image = cv2.cvtColor(image_gray, cv2.COLOR_BGR2GRAY)
# ret , threshold = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)
# resized_image = cv2.resize(threshold, (400, 400))
# cv2.imshow("resized_image", resized_image)
# print("Threshold Value: ", ret)
# print(threshold)
# cv2.waitKey(0)
 
#adaptive thresholding
adaptive_thresh = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow("Adaptive Thresholding", adaptive_thresh)
cv2.waitKey(0)