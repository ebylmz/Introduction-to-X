import cv2
import numpy as np

def empty(x):
    pass

# Trackbar
window  = "frame"
cv2.namedWindow(window)
cv2.resizeWindow(window, 640, 240)

cv2.createTrackbar("H", window, 0, 179, empty)
cv2.createTrackbar("S", window, 255, 255, empty)
cv2.createTrackbar("V", window, 255, 255, empty)

# 3D array
imgHSV = np.zeros((240, 640, 3), np.uint8)

while True:
    h = cv2.getTrackbarPos("H", window)
    s = cv2.getTrackbarPos("S", window)
    v = cv2.getTrackbarPos("V", window)

    # assign each of the element hsv value
    imgHSV[:] = (h, s, v) 
    imgBGR = cv2.cvtColor(imgHSV, cv2.COLOR_HSV2BGR)

    cv2.imshow(window, imgBGR)
    if cv2.waitKey(1) == ord('q'):
        # print the selected color
        print("Selected HSV color: " + f"{(h, s, v)}")
        break 
    

cv2.destroyAllWindows()    