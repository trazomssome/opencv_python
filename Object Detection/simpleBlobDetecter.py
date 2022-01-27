# 객체 검출 및 라벨링
# 크기와 면적이 나옴

# Standard imports
import sys
import cv2
from cv2 import connectedComponentsWithStats
import numpy as np;

src = cv2.imread('images/test.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()
    

_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY_INV)

cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)

dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

# 각각의 객체 정보에 들어가기 위해 반복문. 범위를 1부터 시작한 이유는 배경을 제외
for i in range(1, cnt):
    (x, y, w, h, area) = stats[i]

    # 필터링
    if area < 1500 or area > 5000 or h > 200:
        continue

    cv2.rectangle(dst, (x, y, w, h), (0, 255, 255))

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()