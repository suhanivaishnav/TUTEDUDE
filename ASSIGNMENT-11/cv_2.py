import cv2
img = cv2.imread(r"C:\Users\pc\Downloads\highway.jpg",0)
cv2.imshow("window", img)
cv2.imwrite('new_image.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
