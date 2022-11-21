import cv2
import numpy as np

# video capture 0 for default
cap = cv2.VideoCapture(0) 

while True:
    # success is indicates if frame captured properly
    success, frame = cap.read()

    # get width and height of the video capture 
    width = int(cap.get(3))
    height = int(cap.get(4))

    # create a new frame as identical shape with webcam frame
    image = np.zeros(frame.shape, np.uint8)

    smallerFrame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # copy webcam frame to the image
    image[:height//2, :width//2] = cv2.rotate(smallerFrame, cv2.ROTATE_180)
    image[:height//2, width//2:] = cv2.rotate(smallerFrame, cv2.ROTATE_180)
    image[height//2:, :width//2] = smallerFrame
    image[height//2:, width//2:] = smallerFrame

    cv2.imshow("webcam", image)

    # display each frame for a 1 milisec and check if 'q' is pressed 
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()   # release capture device for other devices uses
cv2.destroyAllWindows()