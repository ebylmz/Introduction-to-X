import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # cv2.line(img, startPoint, endPoint, color, thickness)
    # to fill the shape set thickness as -1
    img = cv2.line(frame, (0, 0), (width, height), (255, 255, 0), 3)
    img = cv2.line(img, (width, 0), (0, height), (255, 255, 0), 3)
    img = cv2.rectangle(img, (0, 0), (300, 300), (128, 128, 128), -1) 
    img = cv2.circle(img, (width//2, height//2), min(width//4, height//4), (0, 255, 255), -1)
    
    # cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType)
    img = cv2.putText(
        img, "Hello, World!", (10, height - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 5, cv2.LINE_AA
    )

    cv2.imshow("webcam", img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()