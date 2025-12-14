import cv2
import numpy as np
img = cv2.imread(r'C:\Users\pc\Downloads\highway.jpg')
width = 400
height = 308
dim = (width, height)
resized = cv2.resize(img, dim)
cv2.imshow('Original', resized)
#flip = cv2.flip(resized,1)
#cv2.imshow('Horizontal', flip)
#flip_1 =cv2.flip(resized,0)
#cv2.imshow('Vertical', flip_1)
flip_2= cv2.flip(resized,1)
cv2.imshow('Horizontal & Vertical', flip_2)
cv2.waitKey(0)
cv2.destroyAllWindows()