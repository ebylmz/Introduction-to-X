from sys import argv
import cv2
from cv2 import imread

# resize the image with given ratio
def imageResizer(filename, ratio):
    img = imread(filename)
    return cv2.resize(img, (0, 0), fx=ratio, fy=ratio)

if len(argv) != 3:
    print("Usage: py (program name) (filename) (resize ratio)")
else:
    img = imageResizer(argv[1], float(argv[2]))

    cv2.imshow("resized image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # save resized img
    answer = input("Save image (y/n): ").lower()
    if answer in ["y", "yes"]:
        filename = input("Save as ")
        cv2.imwrite(filename, img)