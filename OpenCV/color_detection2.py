# Colors & Color Detection

import cv2
import numpy as np


def redMask(hsvFrame):
    lowerb = np.array([161, 155, 84])
    higherb = np.array([179, 255, 255])
    return cv2.inRange(hsvFrame, lowerb, higherb)

def blueMask(hsvFrame):
    lowerb = np.array([94, 80, 2])
    upperb = np.array([126, 255, 255])
    return cv2.inRange(hsvFrame, lowerb, upperb)

def greenMask(hsvFrame):
    lowerb = np.array([25, 52, 72])
    upperb = np.array([102, 255, 255])
    return cv2.inRange(hsvFrame, lowerb, upperb)

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    while True:
        # get the frame from video capture
        success, frame = cap.read()
        width = int(cap.get(3))
        height = int(cap.get(4))

        smallerFrame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

        hsvFrame = cv2.cvtColor(smallerFrame, cv2.COLOR_BGR2HSV)
        
        frame[:height//2, :width//2] = cv2.bitwise_and(smallerFrame, smallerFrame, mask=redMask(hsvFrame))
        frame[height//2:, :width//2] = cv2.bitwise_and(smallerFrame, smallerFrame, mask=greenMask(hsvFrame))
        frame[:height//2, width//2:] = cv2.bitwise_and(smallerFrame, smallerFrame, mask=blueMask(hsvFrame))
        frame[height//2:, width//2:] = smallerFrame

        cv2.imshow("color detection", frame)

        if cv2.waitKey(1) == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()