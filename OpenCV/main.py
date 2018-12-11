import cv2 as cv
import numpy as np


def decrease(value, byHow):
	res = value - byHow
	return res if res >= 0 else 0


img = cv.imread('image.jpg')

newRGB = []

for row in img:
	temp = []
	for color in row:
		mean = np.mean(color)
		temp.append([mean, mean, mean])
	newRGB.append(temp)

cv.imwrite("image_2.png", np.array(newRGB))
# cv.imshow("My Image", img)
# cv.waitKey(0)
# cv.destroyAllWindows()
