import numpy as np
import cv2 as cv
import sys
import os

os.environ['DISPLAY'] = '0:0'

img = cv.imread('cat.jpg')
cv.imshow("Cat", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("cat.png", img)