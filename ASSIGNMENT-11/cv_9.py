import cv2
img= cv2.imread(r'C:\Users\pc\Downloads\highway.jpg')
row=img.shape[1]
column=img.shape[0]
center=(column/2, row/2)
angle=180
r = cv2.getRotationMatrix2D(center,angle,1)
rotate = cv2.warpAffine(img,r,(column,row))
cv2.imshow('Rotated ',rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()