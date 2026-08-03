import numpy as np 
import cv2 as cv

img = cv.imread("fih.jpeg")
big = cv.imread("fih2.jpeg")

roi = img[60:360, 16:645]
roi = cv.resize(roi, (100, 50), cv.INTER_LINEAR)

mask = np.ones((big.shape[0], big.shape[1]), np.uint8)
mask[80:130, 400:500] = 0
imask = cv.bitwise_and(big, big, mask = mask)

roi = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
roi = cv.adaptiveThreshold(roi, 200, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 5, 2)
roi = cv.bitwise_not(roi)
roi = cv.cvtColor(roi, cv.COLOR_GRAY2BGR)
#print(roi.shape)
#imask[80:130, 400:500] = roi

target = imask[80:130, 400:500]
temp = cv.add(target, roi)
imask[80:130, 400:500] = temp
print(target.shape)

cv.imshow("fih", imask)
cv.waitKey(0)
cv.destroyAllWindows()
