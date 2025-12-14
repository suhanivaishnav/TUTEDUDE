import cv2

cap = cv2.VideoCapture(0)

# Check camera opened
if not cap.isOpened():
    print("Error: Camera not accessible")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    cv2.imshow('Live', frame)
    if cv2.waitKey(1) & 0xFF == ord('z'):
        break

cap.release()
cv2.destroyAllWindows()
