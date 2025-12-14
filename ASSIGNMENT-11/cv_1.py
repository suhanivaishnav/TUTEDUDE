import cv2
img = cv2.imread("C:\\Users\\pc\\Downloads\\highway.jpg")   # Read the image
cv2.imshow("Output Image", img) # Show image
cv2.waitKey(0)                  # Wait for key press
cv2.destroyAllWindows()         # Close window
