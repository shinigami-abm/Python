import numpy as np
import cv2 as cv
e1 = cv.getTickCount()
def resize(i, r, c):
    new_c = (np.arange(c)*i.shape[1] / c).astype(int)
    new_r = (np.arange(r)*i.shape[0] / r).astype(int)
    return i[new_r][:,new_c]

fih1 = cv.imread("fih.jpeg")
fih2 = cv.imread("fih1.jpeg")
fih1 = resize(fih1, 450, 640)
fih2 = resize(fih2, 450, 640)

mask = np.zeros((fih1.shape[0],fih1.shape[1]), np.uint8)
mask[50:360, 16:620] = 255

mask2 = np.ones((fih1.shape[0], fih1.shape[1]), np.uint8)
mask2[350:450, 450:550] = 0

Imask2= cv.bitwise_and(fih2, fih2, mask= mask2)
Imask = cv.bitwise_and( fih1,fih1, mask = mask)
cv.imshow("end", cv.cvtColor((cv.bitwise_or(Imask,Imask2)), cv.COLOR_BGR2HSV))
#cv.imshow("ggg" , Imask2)
cv.waitKey(0)
print(f"the time that took this code to execute is : {int((cv.getTickCount() - e1)/ cv.getTickFrequency())} Second")
cv.destroyAllWindows()
