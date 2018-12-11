import cv2 as cv


img = cv.imread("image.jpg")
img = cv.cvtColor(img, cv.COLOR_RGB2HSV)
cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()
