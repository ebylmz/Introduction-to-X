# Colors & Color Detection

import cv2
import numpy as np

cap  = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    # convert each pixel value from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # define lower and upper bounds to display only the color which are in that boundry
    # lowerBlue = np.array([90, 50, 50]) 
    # upperBlue = np.array([130, 255, 255])
    lowerRed = np.array([161, 155, 84])
    upperRed = np.array([179, 255, 255])

    # mask is consist of two value [0, 0, 0] for 0 and [255, 255, 255] for 1 
    # so if the pixel's value in range than set mask pixel as 1 ow 0
    # later with bitwise and we can extract the color by using our mask
    mask = cv2.inRange(hsv, lowerRed, upperRed)
    # print(mask) to see mask 

    result = cv2.bitwise_and(frame, frame, mask=mask)

    for i in range(len(result)):
        for j in range(len(result[i])):
            if not np.array_equiv(result[i][j], [0, 0, 0]):
                print("Red object at " + str(tuple(result[i][j])))
                break

    cv2.imshow("webcam", result)

    if cv2.waitKey(1) == ord('q'): 
        break

cv2.destroyAllWindows()

# colorBGR = np.array([[[0, 255, 0]]],  dtype=np.uint8)
# x = cv2.cvtColor(colorBGR, cv2.COLOR_BGR2HSV)
# colorHSV = x[0][0]
