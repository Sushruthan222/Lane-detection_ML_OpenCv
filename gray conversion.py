import cv2

path = "resources/taylor.jpg"
img = cv2.imread(path, 0)

cv2.imshow("taylor", img)

cv2.waitKey(0)
