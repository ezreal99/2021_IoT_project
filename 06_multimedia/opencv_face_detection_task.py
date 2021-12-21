import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

face_cascade = cv2.CascadeClassifier('./xml/face.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    fr2 = cv2.resize(frame, (600,400))
    gray = cv2.cvtColor(fr2, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(fr2, (x,y), (x+w,y+h), (255, 0, 0), 2)
    cv2.imshow('frame', fr2)
    if cv2.waitKey(10) == 13:
        break

cap.release()
cv2.destroyAllWindows() 