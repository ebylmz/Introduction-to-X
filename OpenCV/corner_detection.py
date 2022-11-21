# Corner Detection

import numpy as np
import cv2

img = cv2.imread("resources/chessboard.png")
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)

# most of the CV algorithms work with gray scale images, so convert to gray scale 
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# (src, maxCorners, qualityLevel, minEuclideanDistance)
corners = cv2.goodFeaturesToTrack(imgGray, 100, 0.01, 10)
corners = np.int0(corners) # casting from double to int

# print(corners)  

# draw a circle the each corner at original img  which are finded with gray img  
for corner in corners:
    x, y = corner.ravel() # [[0, 0]] --> [0, 0]
    cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

# connect each corner with randomly colored lines
for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0]) # [[[0, 0]...]...]
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)

cv2.imshow("Corner Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()