
import cv2 as cv
from cv2 import CascadeClassifier
import sys

GREEN = (0, 255, 0)
DIM = (640, 480)

def detectFaces(pathToImage, res=None):
    img = cv.imread(pathToImage)

    if not res:
        img = cv.resize(img, DIM, interpolation=cv.INTER_AREA)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    haarCascade = CascadeClassifier("data/haarcascade_frontalface_default.xml")
    faces = haarCascade.detectMultiScale(gray, 1.1, 7)

    for x, y, w, h in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)

    if res:
        cv.imwrite(res, img)
    else:
        cv.imshow('Detected Faces', img)
        cv.waitKey(0)
        cv.destroyAllWindows()

if __name__ == '__main__':
    argv = sys.argv

    if len(argv) < 2:
        print(f"Use: {argv[0]} <path/to/image> [result filename]")
        exit(0)
    detectFaces(*argv[1:])