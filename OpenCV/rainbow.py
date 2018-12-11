import cv2 as cv
import numpy as np


def to(val, scale):
	value = scale - int(val)
	return min(255, max(0, value))


bgr = []

width, height = 500, 1000

color_each_step = (3 * 255) / height

staked = 0

for row in range(height):
	staked += color_each_step
	print([(to(staked, 255 * 3), to(staked, 255 * 2), to(staked, 255 * 1))])
	bgr.append([(to(staked, 255 * 3), to(staked, 255 * 2), to(staked, 255 * 1)) for i in range(width)])

cv.imwrite("rainbow.png", np.array(bgr))
