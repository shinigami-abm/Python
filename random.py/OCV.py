import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
cc = cv.VideoWriter_fourcc(*'MJPG')
out = cv.VideoWriter('video_output.avi', cc, 20, (640, 480))

while cap.isOpened():
      ret , f = cap.read()
      f = np.flip(f, 1)
      out.write(f)
      cv.imshow("look", f)
      if cv.waitKey(1) == ord("k"):
         break
cap.release()
out.release()
cv.destroyAllWindows()
