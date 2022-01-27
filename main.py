import cv2
import numpy as np
from matplotlib import pyplot as plt
from viewer import *


def main():
    cv2.namedWindow("origin", cv2.WINDOW_NORMAL)
    test = cv2.imread("images/test.bmp")
    viewimage(test)

if __name__ == '__main__':
    main()