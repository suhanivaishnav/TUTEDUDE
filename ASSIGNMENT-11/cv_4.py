import cv2
import numpy as np
img = cv2.imread(r'C:\Users\pc\Downloads\highway.jpg')
width = 400
height = 308
dim = (width, height)
resized = cv2.resize(img, dim)
kernel = np.ones((5,5), np.uint8)
# Morphological operations
#erosion = cv2.erode(resized, kernel, iterations=1)
#dilation = cv2.dilate(resized, kernel, iterations=1)
#opening=cv2.morphologyEx(resized,cv2.MORPH_OPEN,kernel)
#closing=cv2.morphologyEx(resized,cv2.MORPH_CLOSE,kernel)
#gradient=cv2.morphologyEx(resized,cv2.MORPH_GRADIENT,kernel)
tophat=cv2.morphologyEx(resized,cv2.MORPH_TOPHAT,kernel)
blackhat=cv2.morphologyEx(resized,cv2.MORPH_BLACKHAT,kernel)
# Show images
cv2.imshow("Original", resized)
#cv2.imshow("Erosion", erosion)
#cv2.imshow("Dilation", dilation)
#cv2.imshow("Openig",opening)
#cv2.imshow("Closing",closing)
#cv2.imshow("Gradient",gradient)
cv2.imshow("Tophat", tophat)
cv2.imshow("Blackhat", blackhat)
cv2.waitKey(0)   # Wait until key press
cv2.destroyAllWindows()