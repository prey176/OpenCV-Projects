# TASK 1
from cv2 import *


if __name__ == '__main__':
	
	cap = VideoCapture(0)

	while True:

	    temp, frame = cap.read()

	    imshow('frame',frame)
	    if waitKey(1) !=-1:
	        break

	cap.release()
	destroyAllWindows()