# BONUS

from cv2 import *
import numpy

if __name__ == '__main__':
	
	cap = VideoCapture(0)

	while True:

	    ret, frame = cap.read()

	    # gray = cvtColor(frame,COLOR_BGR2GRAY)
	    # gray = equalizeHist(gray)
	    gray=frame
	    hist = calcHist([gray],[0],None,[256],[0,256]) 
	    new = numpy.zeros((256,256))
	    for x,y in enumerate(hist) :
	    	line(new,(x,0),(x,y),(200,200,200))

	    imshow('hist',new)
	    imshow('gray' , gray)

			    

		
	    
	    if waitKey(1) !=-1:
	        break

	cap.release()
	destroyAllWindows()