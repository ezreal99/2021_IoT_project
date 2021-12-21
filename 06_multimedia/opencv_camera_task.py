import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

while True:
    ret, frame = cap.read()
    fr2 = cv2.resize(frame, (600,400))
    edge = cv2.Canny(fr2, 50, 100)
    gray = cv2.cvtColor(fr2, cv2.COLOR_BGR2GRAY)
    if not ret:
        break

    cv2.imshow('frame', fr2)
    cv2.imshow('edge', edge)
    cv2.imshow('gray',gray)
    #out.write(frame)
    if cv2.waitKey(10) == 13:
        break


cap.release()
cv2.destroyAllWindows() 