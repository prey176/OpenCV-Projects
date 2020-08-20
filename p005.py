# TASK 4

import cv2
import numpy 


img = cv2.imread('/home/preyansh/Pictures/Webcam/gunda.jpg',0)
img1 = cv2.imread('/home/preyansh/Pictures/Webcam/gunda.jpg',0)
img = cv2.equalizeHist(img)
hist = cv2.calcHist([img],[0],None,[256],[0,256]) 
hist1 = cv2.calcHist([img1],[0],None,[256],[0,256]) 
new1 = numpy.zeros((256,256))	
new = numpy.zeros((256,256))
for x,y in enumerate(hist) :
	cv2.line(new,(x,0),(x,y),(200,200,200))
for x,y in enumerate(hist1) :
	cv2.line(new1,(x,0),(x,y),(200,200,200))
cv2.imshow('EQUALIZED IMAGE',img)
cv2.imshow('ORIGINAL IMAGE',img1)
cv2.imshow('EQUALIZED HISTOGRAPH',new)
cv2.imshow('ORIGINAL HISTOGRAPH',new1)
cv2.waitKey(0)
cv2.destroyAllWindows()