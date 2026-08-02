import numpy as np
import cv2 as cv

temp = cv.imread("fih.jpeg")
img = cv.imread("fih2.jpeg")

cv.circle(img, (260,165), 105, (0, 0, 255), 5)
cv.rectangle(temp, (13,60),(645,370),(255,0,0), 5)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(temp, "Fih", (305,425), font, 1, (255,0,0), 2, cv.LINE_AA)
cv.putText(img, "Fih2", (450,180), font, 1, (0,0,255), 2, cv.LINE_AA)
cv.imshow("yoy", temp)
cv.imshow("fih2", img)
cv.waitKey(0)
cv.destroyAllWindows()
