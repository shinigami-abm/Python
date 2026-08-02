import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while cap.isOpened():
      ctrl, fram = cap.read()
      #fram = np.flip(np.flip(fram, 0), 1)
      cv.circle(fram, (int(fram.shape[1]/2),int(fram.shape[0]/2)), 50, (255,0,0), 1)
      cv.imshow("yoy", fram)
      if cv.waitKey(1) == ord("k"):
          break
      
cap.release()
cv.destroyAllWindows()
