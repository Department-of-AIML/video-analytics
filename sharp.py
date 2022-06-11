import cv2
import numpy as np
img_original = cv2.imread('fruits.png')
cv2.imshow('Original Image', img_original)
cv2.waitKey(0)
sharp_filter = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
sharp_image = cv2.filter2D(img_original, -1, sharp_filter)
cv2.imshow('Sharpened Image', sharp_image)
cv2.waitKey(0)
