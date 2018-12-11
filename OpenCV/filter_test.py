import cv2 as cv


img = cv.imread("image.jpg")
img - cv.cvtColor(img, cv.COLOR_BGR2HSV)

low_bound = (140, 140, 140)
up_bound = (170, 170, 170)

logo = cv.inRange(img, low_bound, up_bound)

res = cv.bitwise_and(img, img, mask=logo)

cv.imshow('result', res)
cv.waitKey(0)
cv.destroyAllWindows()
