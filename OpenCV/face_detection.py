# Face and Eye Detection

# https://stackoverflow.com/questions/20801015/recommended-values-for-opencv-detectmultiscale-parameters

import cv2

cap = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# load haar cascade classifiers

while True:
    success, frame = cap.read()

    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # face cascade returns all the locations of faces
    # shrink ratio: 1.3 (size reduced by %30) 
    # smaller shrink ratio results slower but more accurate execution
    # minNeighbors: specifies how many neighbors each candidate rectangle should correspond
    #               This parameter will affect the quality of the detected faces. 
    #               Higher value results in less detections but with higher quality. 3~6 is a good value for it.
    faces = faceCascade.detectMultiScale(imgGray, 1.3, 3)
    for (fx, fy, fw, fh) in faces:
        cv2.rectangle(frame, (fx, fy), (fx + fw, fy + fh), (255, 0, 0), 3)

        # here we have a face, eyes are must be somewhere in faces
        # so it's much more efficient to search eyes in face rather than whole frame
        # region of interest 
        roiGray = imgGray[fy:fy+fh, fx:fx+fw]
        roiColored = frame[fy:fy+fh, fx:fx+fw]

        eyes = eyeCascade.detectMultiScale(roiGray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roiColored, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 3)

    cv2.imshow("Face & Eye Detection", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()