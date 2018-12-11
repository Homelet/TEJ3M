from threading import Thread

import cv2 as cv


class WebcamVideoStream:
	
	def __init__(self, src=0):
		# initialize the video camera stream and read the first frame
		# from the stream
		self.stream = cv.VideoCapture(src)
		_, self.frame = self.stream.read()
		self.stopped = False
	
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
			cv.flip(frame, 1, dst=frame)
			
			hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
			mask = cv.inRange(hsv_frame, lower_limit, upper_limit)
			_, contours, _ = cv.findContours(mask, mode=cv.RETR_EXTERNAL, method=cv.CHAIN_APPROX_SIMPLE)
			for contour in contours:
				x, y, w, h = cv.boundingRect(contour)
				cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=5)
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


if __name__ == '__main__':
	upper_limit = (326, 255, 255)
	lower_limit = (0, 144, 100)
	main()
