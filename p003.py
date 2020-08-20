# TASK 3 PART 1

from cv2 import *
import numpy  

if __name__ == '__main__':
	
	cap =  VideoCapture(0)

	while True :

		ret, frame = cap.read()

		hsv =  cvtColor(frame,COLOR_BGR2HSV)


		lower = numpy.array([140 , 150,0])
		upper = numpy.array([180 , 255,255])

		a = inRange(hsv , lower,upper)

		output = bitwise_and(frame , frame , mask = a)

		imshow('image_mask',output)
		imshow('frame',frame)
		imshow('hsv',a)

		if waitKey(1)!=-1:
			break

	cap.release()
	destroyAllWindows()
