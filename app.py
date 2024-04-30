
import cv2 as cv
from cv2 import CascadeClassifier
import sys

argv = sys.argv
GREEN = (0, 255, 0)

def detectFaces(pathToImage):
    img = cv.imread(pathToImage)
    img = cv.resize(img, (640, 480))
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    haarCascade = CascadeClassifier("data/haarcascade_frontalface_default.xml")
    faces = haarCascade.detectMultiScale(gray, 1.1, 4)

    for x, y, w, h in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)

    cv.imshow(sys.argv[1], img)
    cv.waitKey(0)

if __name__ == '__main__':
    if len(argv) != 2:
        print(f"Use: {argv[0]} <path/to/image>")
        exit(0)

    detectFaces(argv[1])