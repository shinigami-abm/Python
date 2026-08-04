import numpy as np
import cv2 as cv


img = cv.imread("fih1.jpeg")

#kernel = np.ones((5,5), np.float32) / 25
#new = cv.filter2D(img, -1, kernel)

#blur = cv.blur(img, (3,5))
#blur = cv.GaussianBlur(img, (7,7), 0)
#blur = cv.medianBlur(img, 21)
blur = cv.bilateralFilter(img, -1, 10, 90)

cv.imshow("yoy", img)
cv.imshow("test", blur)
cv.waitKey(0)
cv.destroyAllWindows()
