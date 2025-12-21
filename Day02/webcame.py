import cv2

#read webcame
webcame = cv2.VideoCapture(0)

#visualize webcame
while True:
    ret, frame = webcame.read()
    if not ret:
        break
    cv2.imshow('Webcame', frame)
    
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

webcame.release()
cv2.destroyAllWindows()
