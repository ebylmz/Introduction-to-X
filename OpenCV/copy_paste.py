import cv2

img = cv2.imread("resources/lambo.png")

row = img.shape[0]
col = img.shape[1]

# copying & pasting parts of the image
part = img[0:200, 0:200]    # slice the first 200 rows first 200 col
img[row-200:row, col-200:col] = part

cv2.imshow("shapes", img)
cv2.waitKey(0)