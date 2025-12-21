import os
import cv2
image_path = os.path.join('./','assets','image1.jpg')

# imread() function is used to read an image from the specified file.
img = cv2.imread(image_path)
# print(img) # it will print the pixel values of the image in the form of a multi-dimensional array.

# writing image
cv2.imwrite(os.path.join('./','assets','image1_copy.jpg'),img)

# visualize image
cv2.imshow('image',img)

# the waitKey() function is used to display the image window until a key is pressed.
cv2.waitKey(0)