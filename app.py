
import cv2 as cv


img = cv.imread("build/teste.jpeg")

cv.imshow("Image", img)
k = cv.waitKey(0)