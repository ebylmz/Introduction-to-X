from sys import argv
import numpy as np
import cv2

# empty function
def empty(e):
    pass

def createHSVColorPicker():
    # create a new window which will be HSV color setter
    winname = "HSV Color Picker"
    cv2.namedWindow(winname)
    cv2.resizeWindow(winname, 640, 240)

    # create trackbars (can be used lambda exp (lamda x:x) for onChange function)
    cv2.createTrackbar("Hue Min", winname, 0, 179, empty)
    cv2.createTrackbar("Hue Max", winname, 179, 179, empty)
    cv2.createTrackbar("Sat Min", winname, 0, 255, empty)
    cv2.createTrackbar("Sat Max", winname, 255, 255, empty)
    cv2.createTrackbar("Val Min", winname, 0, 255, empty)
    cv2.createTrackbar("Val Max", winname, 255, 255, empty)
    return winname


# returns lower and higher bound of HSV to use in mask creation process
# returns a numpy array [[hmin, smin, vmin], [hmax, smax, vmax]])
def getHSVTrackbarBoundries(winname):
    # getTrackbarPos returns the current position of the specified trackbar
    # first argument is trackbarname and second one is the window which contain the trackbar
    hmin = cv2.getTrackbarPos("Hue Min", winname) 
    hmax = cv2.getTrackbarPos("Hue Max", winname)
    smin = cv2.getTrackbarPos("Sat Min", winname)
    smax = cv2.getTrackbarPos("Sat Max", winname)
    vmin = cv2.getTrackbarPos("Val Min", winname)
    vmax = cv2.getTrackbarPos("Val Max", winname)
    return np.array([[hmin, smin, vmin], [hmax, smax, vmax]])

if __name__ == "__main__":
    if len(argv) < 2:
        print("usage: py <program name> <image path>")
    else:
        img = cv2.imread(argv[1])
        # get the HSV version of image
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # create trackbar window to select HSV color boundries
        winname = createHSVColorPicker()

        # display the color detection in while loop
        while True:
            boundries = getHSVTrackbarBoundries(winname)
            
            mask = cv2.inRange(imgHSV, lowerb=boundries[0], upperb=boundries[1])
            
            # apply mask to original img and display it as result
            imgResult = cv2.bitwise_and(img, img, mask=mask)

            cv2.imshow("Result", imgResult)
            # cv2.imshow("Pure", img)
            # cv2.imshow("HSV", imgHSV)
            # cv2.imshow("Mask", mask)
            
            if cv2.waitKey(1) == ord('q'):
                break
        
        # print the HSV range
        print(f"lowerb: {boundries[0]}")
        print(f"upperb: {boundries[1]}")
        cv2.destroyAllWindows()