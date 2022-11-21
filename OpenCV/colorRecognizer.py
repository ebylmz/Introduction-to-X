import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = cap.read()

    # get the center of the frame 
    cx = int(frame.shape[1] / 2)
    cy = int(frame.shape[0] / 2)

    # pick pixel value
    pixelCenter = frame[cy, cx]
    print(frame[cx, cy])

    # recognize the color at center
    color = "Undefined"
    if pixelCenter[0] < 7:
        color = "Red"
    elif pixelCenter[0] < 20:
        color = "Orange"
    elif pixelCenter[0] < 34:
        color = "Yellow"
    elif pixelCenter[0] < 75:
        color = "Green"
    elif pixelCenter[0] < 95:
        color = "Aqua"
    elif pixelCenter[0] < 125:
        color = "Blue"
    elif pixelCenter[0] < 142:
        color = "Purple"
    elif pixelCenter[0] < 170:
        color = "Pink"
    else:
        color = "Red"

    b, g, r = int(pixelCenter[0]), int(pixelCenter[1]), int(pixelCenter[2])

    cv2.putText(frame, color, (10, 50), 0, 1, (b, g, r), 2)
    cv2.circle(frame, (cx, cy), 5, (0, 0, 0), 3)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()