import cv2

img = cv2.imread("resources/lambo.png", 0)

# -1 cv2.IMREAD_COLOR
#  0 cv2.IMREAD_GRAYSCALE
#  1 cv2.IMREAD_UNCHANGED

img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) # half size
img = cv2.resize(img, (0, 0), fx=2, fy=2) # double size
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite("newlambo.png", img)

cv2.imshow("lambo", img)
cv2.waitKey(0) # waits to press any key
cv2.destroyAllWindows()