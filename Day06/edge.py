import os
import cv2
import numpy as np
image = cv2.imread(os.path.join('./','assets', 'Rashid-Khan.jpeg'))
image_edge = cv2.Canny(image, 100, 200)
cv2.imshow('Original Image', image)
image_edge_d = cv2.dilate(image_edge, np.ones((3, 3), dtype=np.uint8))
image_edge_e = cv2.erode(image_edge_d, np.ones((3, 3), dtype=np.uint8))
cv2.imshow('edged Image', image_edge)
cv2.imshow('dilated Image', image_edge_d)
cv2.imshow('eroded Image', image_edge_e)
i
cv2.waitKey(0)
