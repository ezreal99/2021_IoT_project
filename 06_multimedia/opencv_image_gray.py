import cv2

img = cv2.imread('people.jpg')
img2 = cv2.resize(img, (600,400))

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow('people', img2)
cv2.imshow('people_gray', gray)

while True:
    if cv2.waitKey()==ord('q'):
        break

cv2.imwrite('people_gray.jpg', gray)

cv2.destroyAllWindows()