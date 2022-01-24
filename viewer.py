import cv2

def viewimage(img):
    if img.any() != None:
        cv2.imshow("origin", img)
        cv2.resizeWindow("origin", 200, 200)
        cv2.waitKey(0)
        cv2.destroyWindow("origin")  
        cv2.destroyAllWindows()   
    else:
        print("test is null")