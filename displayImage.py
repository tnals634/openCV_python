import cv2
import numpy
import pytesseract
import matplotlib

img = cv2.imread('sampleimage.jpg',cv2.IMREAD_COLOR)
cv2.imshow('display image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()