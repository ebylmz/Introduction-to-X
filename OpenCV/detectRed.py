from sys import argv
import cv2
import numpy as np

def redMask(frame):
    # convert frame format to HSV
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerb = np.array([161, 155, 84])
    upperb = np.array([179, 255, 255])
    return cv2.inRange(hsvFrame, lowerb, upperb)

if __name__ == "__main__":
    # detect red in given image
    if len(argv) > 1:
        frame = cv2.imread(argv[1])
        
        frame = cv2.bitwise_and(frame, frame, mask=redMask(frame))
        cv2.imshow("frame", frame)
        cv2.waitKey(0)
    # detect red at webcam
    else:
        cap = cv2.VideoCapture(0)

        while True:
            # get the frame from video capture
            _, frame = cap.read()
            h = frame[0]
            w = frame[1]

            # create a red mask
            frame = cv2.bitwise_and(frame, frame, mask=redMask(frame))
            
            cv2.imshow("frame", frame)
            if cv2.waitKey(1) == ord('q'):
                break

        cap.release()
    cv2.destroyAllWindows()