import cv2
img = cv2.imread(r"C:\Users\pc\Downloads\highway.jpg")
print("Dimensions of image: ", img.shape)
width = 500
height = 500
dim=(width, height)
resized=cv2.resize(img, dim)
cv2.imshow("window", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()