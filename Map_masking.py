import cv2
import numpy as np
img = cv2.imread("SatMap1.png")
frame = img[100:900, 100:900]
frame1 = cv2.resize(frame,(1000,1000))
lower_range = np.array([0,0,0])
upper_range =np.array([255,115,255])
mask = cv2.inRange(frame1, lower_range, upper_range)
cv2.imshow("Map",mask)
cv2.imwrite("Test.jpg",mask)
