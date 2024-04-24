import cv2 as cv
import numpy as np

def preprocess(img):
    kernel = np.ones((3,3), np.uint8)

    imgPre = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('example gray', imgPre)
    imgPre = cv.GaussianBlur(imgPre, (15,15), 2)
    # imgPre = cv.Canny(imgPre, 100, 160)
    _, thresh = cv.threshold(imgPre, 100, 255, cv.THRESH_BINARY_INV)
    cv.imshow("binarized", thresh)
    imgPre = cv.erode(imgPre, kernel, iterations=4)
    imgPre = cv.dilate(thresh, kernel, iterations=3)
    cv.imshow("img_open", imgPre)
    return imgPre

def searchAlpha(img):
    pass

img = cv.imread("images/example1.jpeg")
img = cv.resize(img, (640, 360))

imgPre = preprocess(img)

contours, h1 = cv.findContours(imgPre, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

for cnt in contours:
    area = cv.contourArea(cnt)
    print(area)
    if area > 1000:
        x, y, w, h = cv.boundingRect(cnt)
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        subImg = img[y: y+h, x : x+w]
        # cv.imwrite("teste.jpeg", subImg)

cv.imshow("img final", img)

cv.waitKey(0)