# TASK 3 PART 2

from cv2 import *
import numpy 

if __name__ == '__main__':
	
		frame =  imread('/home/preyansh/Pictures/Webcam/red1.png')

		hsv =  cvtColor(frame,COLOR_BGR2HSV)

		lower = numpy.array([140 , 150,0])
		upper = numpy.array([180 , 255,255])

		a = inRange(hsv , lower,upper)
		output = bitwise_and(frame , frame , mask = a)

		lower = numpy.array([0 , 100,100])
		upper = numpy.array([0 , 255,255])

		b = inRange(hsv , lower,upper)
		newoutput = bitwise_or(output,frame , mask = b)

		imshow('newoutput',newoutput)
		# imshow('output',output)
		imshow('original',frame)
		# imshow('frame11',frame)
		waitKey(0)
		destroyAllWindows()
