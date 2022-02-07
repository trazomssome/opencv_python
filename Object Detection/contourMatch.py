import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images/Mark_S_Tilted.bmp')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
res, thr = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt1 = contours[1]
cv2.drawContours(img, [cnt1], -1, (255, 0, 0), 3)

img2 = cv2.imread('images/test.bmp')
img_gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
res, thr2 = cv2.threshold(img_gray2, 127, 255, cv2.THRESH_BINARY)
contours2, hierarchy = cv2.findContours(thr2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

match_list1 = []
for i in range(len(contours2)):
    cnt2 = contours2[i]
    ret = cv2.matchShapes(cnt1, cnt2, cv2.CONTOURS_MATCH_I1, 0.0)
    match_list1.append(ret)

match_list2 = []
for i in range(len(contours2)):
    cnt2 = contours2[i]
    ret = cv2.matchShapes(cnt1, cnt2, cv2.CONTOURS_MATCH_I2, 0.0)
    match_list2.append(ret)
    
match_list3 = []
for i in range(len(contours2)):
    cnt2 = contours2[i]
    ret = cv2.matchShapes(cnt1, cnt2, cv2.CONTOURS_MATCH_I3, 0.0)
    match_list3.append(ret)
    
max_index = match_list1.index(max(match_list1))
min_index1 = match_list1.index(min(match_list1))
min_index2 = match_list2.index(min(match_list2))
min_index3 = match_list3.index(min(match_list3))
cv2.drawContours(img2, [contours2[max_index]], -1, (0, 255, 0), 3)    # 초록
cv2.drawContours(img2, [contours2[min_index1]], -1, (0, 0, 255), 3)   # 파랑
cv2.drawContours(img2, [contours2[min_index2]], -1, (255, 0, 255), 3) # 보라
cv2.drawContours(img2, [contours2[min_index3]], -1, (0, 255, 255), 3) # 청록
    
print("cv2.CONTOURS_MATCH_I1 사용 결과 :", min_index1, "번째 인덱스, ", min(match_list1))
print("cv2.CONTOURS_MATCH_I2 사용 결과 :", min_index2, "번째 인덱스, ", min(match_list2))
print("cv2.CONTOURS_MATCH_I3 사용 결과 :", min_index3, "번째 인덱스, ", min(match_list3))
    
plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(img2)
plt.title('Match Shapes')
plt.axis('off')
plt.tight_layout()
plt.show()