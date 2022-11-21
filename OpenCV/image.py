import numpy as np
import cv2
import random


# extracts the pixels from image and loaded into the numpy array (ndarray)
img = cv2.imread("resources/cards.jpg")

# prints values (height/row, width/column, channels)
print(img.shape) 
# channel is the number of values to represent one pixel 
# standart is RBG but OpenCV uses BGR

# so an image represented as 3D array (ndarray)
# blue green red
# [0, 0, 0]

# [
#     [[0, 0, 0], [255, 255, 255], [0, 0, 0]],
#     [[0, 0, 0], [255, 255, 255], [0, 0, 0]],
#     [[0, 0, 0], [255, 255, 255], [0, 0, 0]],
#     [[0, 0, 0], [255, 255, 255], [0, 0, 0]],
#     [[0, 0, 0], [255, 255, 255], [0, 0, 0]]
# ]

print(img[257][45:400]) # row 257 and all the cols 45 between 400

# randomly set values first 100 row
for i in range(100):
    for j in range(img.shape[1]): 
        # img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        img[i][j] = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))

cv2.imshow("randomized", img)
cv2.waitKey(0)
cv2.destroyAllWindows()