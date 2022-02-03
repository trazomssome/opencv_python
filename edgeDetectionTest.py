import cv2
import time
import numpy as np

img = cv2.imread('images/test.bmp')
img2 = img.copy()

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

firstValue = (-1,-1)
endValue = (0,0)

start = time.time()
for row in range(0, 399, 50):
    for column in range (200, 300):
        #imgray[column,row]
        if(imgray[row, column] < 10):
            img2[row, column] = (0,255,0)
            if firstValue is (-1, -1):
                firstValue = (column, row)
            else:
                endValue = (column, row)
            break

cv2.line(img2, firstValue, endValue, (0, 255, 0), 1)

cv2.imshow('result', img2)
cv2.waitKey()
cv2.destroyAllWindows()

# Todo
# 튀는 값을 제외한 평균 구하기
# 직선이라면 같은 간격간의 변화 값을 구해 현 값의 신뢰도를 파악할 수 있을 것으로 보임