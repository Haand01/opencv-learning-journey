import os
import cv2
import numpy as np

image_path =cv2.resize(cv2.imread(os.path.join('./', 'assets', '6.jpg')), (900, 1200))
# line drawing
cv2.line(image_path, (300, 200), (400, 300), (255, 0, 0), 5)

# rectangle drawing
cv2.rectangle(image_path, (500, 200), (700, 400), (0, 0, 255), 3)

# circle drawing
cv2.circle(image_path, (600, 600), 100, (0, 255, 0), 2)

#text drawing
cv2.putText(image_path, 'OpenCV Drawing', (250, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 3)
cv2.imshow('image', image_path)
cv2.waitKey(0)