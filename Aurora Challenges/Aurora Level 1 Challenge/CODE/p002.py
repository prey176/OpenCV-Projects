# TASK 2

import cv2
import numpy

if __name__ == '__main__':
	


	img =  cv2.imread('/home/preyansh/Pictures/Webcam/hand.jpg')
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	new = cv2.adaptiveThreshold(gray , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY,25,1)

	cv2.imshow('original',img)
	cv2.imshow('new',new)

	cv2.waitKey(0)
	cv2.destroyAllWindows()
