import cv2
video = cv2.VideoCapture(r'C:\Users\pc\Downloads\nature.mp4')
while video.isOpened():
    _, frame = video.read()
    frame = cv2.resize(frame, (400, 420))
    cv2.imshow('Output', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()