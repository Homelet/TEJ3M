import sys
from threading import Thread

import cv2 as cv


class WebcamVideoStream:
	
	def __init__(self, src=0):
		# initialize the video camera stream and read the first frame
		# from the stream
		self.stream = cv.VideoCapture(src)
		_, self.frame = self.stream.read()
		self.stopped = False
		self.face_det = cv.CascadeClassifier("front_face.xml")
		self.hand_det = cv.CascadeClassifier("hand.xml")
		self.eye_det = cv.CascadeClassifier("eye.xml")
	
	def start(self):
		# start the thread to read frames from the video stream
		Thread(target=self.update, args=()).start()
		return self
	
	def update(self):
		# keep looping infinitely until the thread is stopped
		while True:
			# if the thread indicator variable is set, stop the thread
			if self.stopped:
				return
			
			# otherwise, read the next frame from the stream
			grabbed, frame = self.stream.read()
			if not grabbed:
				stop(self)
				break
			cv.flip(frame, 1, dst=frame)
			gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
			faces = self.face_det.detectMultiScale(gray, 1.2, 3)
			for (x, y, w, h) in faces:
				eyes = self.eye_det.detectMultiScale(gray[x:x + w, y:y + h], 1.1, 2)
				for (e_x, e_y, e_w, e_h) in eyes:
					cv.rectangle(frame, (e_x + x, e_y + y), (e_x + e_y + x, e_x + e_y + y), (255, 255, 0), thickness=2)
					cv.putText(frame, "Eye", (e_x + x, e_y + y - 5), 0, 1.4, (0, 255, 0))
				cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)
				cv.putText(frame, "Face", (x, y - 5), 0, 1.4, (0, 255, 0))
			# hands = self.hand_det.detectMultiScale(gray, 1.3, 4)
			# for (x, y, w, h) in hands:
			# 	cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), thickness=2)
			# 	cv.putText(frame, "Hand", (x, y - 5), 0, 1.4, (0, 255, 0))
			self.frame = frame
	
	def read(self):
		# return the frame most recently read
		return self.frame
	
	def stop(self):
		# indicate that the thread should be stopped
		self.stopped = True
		self.stream.release()


def main():
	f = WebcamVideoStream().start()
	
	while True:
		cv.imshow("face", f.read())
		if cv.waitKey(1) == 113:
			stop(f)
			break


def stop(f):
	f.stop()
	cv.destroyAllWindows()
	sys.exit(0)


if __name__ == '__main__':
	main()
