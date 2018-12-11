import cv2 as cv


face_det = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_det = cv.CascadeClassifier('haarcascade_eye.xml')

img = cv.imread("123123.jpg")

g_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

list = face_det.detectMultiScale(g_img, 1.2, 4)

for rect in list:
	x, y, w, h = rect
	point, size = (x, y), (x + w, y + h)
	eyes = eye_det.detectMultiScale(g_img[x:x + w, y:y + h], 1.001, 2)
	for eye_rect in eyes:
		x_e, y_e, w_e, h_e = eye_rect
		point_e, size_e = (x_e + x, y_e + y), (x_e + x + w_e, y_e + y + h_e)
		cv.rectangle(img, point_e, size_e, (255, 0, 0), thickness=1)
	cv.rectangle(img, point, size, (0, 255, 0), thickness=1)

cv.imshow("face", img)
cv.waitKey(0)
cv.destroyAllWindows()
