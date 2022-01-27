import cv2
import numpy as np

img = cv2.imread('images/test.bmp')
img2 = img.copy()

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

for row in range(0, 399):
    for column in range (200, 300):
        #imgray[column,row]
        if(imgray[row, column] < 10):
            img2[row, column] = (0,0,255)
            break


cv2.imshow('result', img2)
cv2.waitKey()
cv2.destroyAllWindows()