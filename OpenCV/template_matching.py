# Template Matching (Object Detection)

import cv2

# get image and template with gray scale (again most of the cv method uses gray scaled frame)
# template size should be close the it's original size of the img
img = cv2.imread("resources/soccer_practice.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread("resources/ball.png", 0)
# template = cv2.imread("resources/shoe.png", 0)

# gray scaled image has two values height and width 
# (no channels field since it is represented as 1 bit black or white)
# print(template.shape)

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

# try each method and display the result
for method in methods:
    result = cv2.matchTemplate(imgGray, template, method)
    # result is 2D array which contains matching accuricy of the pixels

    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    # min and max values are specific to methods

    # sometimes min is the best sometimes max is the best depends on the method we use
    # location is the top left corner of the detected object inside image
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        startLoc = minLoc
    else:
        startLoc = maxLoc

    # calculate end location
    endLoc = (startLoc[0] + template.shape[0], startLoc[1] + template.shape[1])

    # use seperate image to draw rectangle to show matching
    imgResult = img.copy()

    cv2.rectangle(imgResult, startLoc, endLoc, (255, 255, 255), 5)
    cv2.imshow("Match", imgResult)
    cv2.waitKey(0)

cv2.destroyAllWindows()


# result = cv2.matchTemplate(imgResult, template, method)
# result is 2D array which contains matching accuricy of the pixels
# size of result array is (W - w + 1, H - h + 1)

# How template matching works

# image
# [[255, 255, 255, 255],
#  [255, 255, 255, 255],
#  [255, 255, 255, 255],
#  [255, 255, 255, 255]]

# template
# [[255, 255],
#  [255, 255]]

# algorithm compare the rows and columns by slicing and create result 
# matching result (contains matching accuricty)
# [[1, 1, 1],
#  [1, 1, 1],
#  [1, 1, 1]]

# after matching done the most closest area location finded
# and than draw rectangle that place