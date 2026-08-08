import numpy as np 
import cv2 as cv

img = cv.imread("fih2.jpeg")
fih = cv.imread("fih1.jpeg")

temp = img.copy()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(fih, cv.COLOR_BGR2GRAY)
#thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 15, 2)
ret, thresh = cv.threshold(gray, 127, 255, 0)
ret, thr = cv.threshold(gray2, 200, 255, 0)

countor, hi = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
co , h = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, countor, -1,0, 10)

#print(cv.matchShapes(countor, co, 0, 0))

#m = cv.moments(countor[20])
#cx = int(m['m10'] / m['m00'])
#cy = int(m['m01'] / m['m00'])  


#print(cv.contourArea(countor[20]))
#print(cx, cy)

#test = cv.bitwise_and(temp, temp , img)

#print(hi)
print(len(countor))

#apox = cv.approxPolyDP(countor[20], 0.02*cv.arcLength(countor[0], True), True)

#hull = cv.convexHull(countor[5])
#print(hull.shape, hull)
#cv.drawContours(img, [hull], -1, 0, 5)

#rect = cv.minAreaRect(countor[5])
#cv.drawContours(img, [np.intp(cv.boxPoints(rect))], 0, 0, 5)

#print(rect)

#x, y, w, h = cv.boundingRect(countor[5])
#cv.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 4)

#(x,y), r=cv.minEnclosingCircle(countor[5])
#cv.circle(img,(int(x), int(y)), int(r), 0, 4)

#print(cv.pointPolygonTest(countor[5], (276,166), True))



cv.imshow("test", img)
cv.waitKey(0)
cv.destroyAllWindows()
