import cv2 as cv
import numpy as np

img = cv.imread("fih2.jpeg")
print(img.shape)

IMG = cv.resize(img,( 2*img.shape[0] , 2*img.shape[1]), cv.INTER_NEAREST)
IMG = IMG.transpose(1,0,2)
print(IMG.shape)

cv.imshow("img", img)
cv.imshow("IMG", IMG)
cv.waitKey(0)
cv.destroyAllWindows()
