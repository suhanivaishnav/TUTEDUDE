import numpy as np  
import cv2
img = cv2.imread(r'C:\Users\pc\Downloads\highway.jpg')
threshold_value = 100
_,binary_threshold = cv2.threshold(img,threshold_value,255,cv2.THRESH_BINARY)
cv2.imshow('Original',img)
cv2.imshow('Binary Threshold',binary_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()