import numpy as np
import cv2 as cv


img = cv.imread("fih.jpeg")
Gimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#fram = cv.adaptiveThreshold(Gimg, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 15, 5)
c, fram = cv.threshold(Gimg,0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
#print(img, fram)
cv.imshow("yoy",fram) #cv.cvtColor(fram, cv.COLOR_GRAY2BGR))
cv.waitKey(0)
cv.destroyAllWindows()
