import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while cap.isOpened():
     ret, f= cap.read()
     gray = cv.cvtColor(f, cv.COLOR_BGR2GRAY)
     _, thresh = cv.threshold(gray, 100, 255, 0)
     contours , hir= cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
     cv.drawContours(f, contours, -1, 0, 10)
     cv.putText(f, "openCV", (400,200), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv.LINE_AA)
     cv.imshow("openCV", f)
     if cv.waitKey(1) == ord("e"):
         break
cap.release()
cv.destroyAllWindows()
