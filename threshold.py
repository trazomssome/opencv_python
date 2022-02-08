import cv2
from cv2 import THRESH_BINARY
from cv2 import THRESH_OTSU
import numpy as np

img = cv2.imread('images/alignmark.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, th = cv2.threshold(imgray, 200, 255, THRESH_OTSU)

cv2.imshow("result", th)
cv2.waitKey()