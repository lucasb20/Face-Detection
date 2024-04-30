
import cv2 as cv
from cv2 import CascadeClassifier


img = cv.imread("build/teste.jpeg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

detec = CascadeClassifier("data/haarcascade_frontalface_default.xml")
faces = detec.detectMultiScale(gray, 1.1, 4)

for x, y, width, height in faces:
    ret = cv.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)

cv.imshow("image", img)
cv.waitKey(0)
