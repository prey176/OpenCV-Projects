### PREYANSH RASTOGI
### 2017176

from cv2 import *
from numpy import *

ans = 0 

def color(img ,red , circle_color) :

    global ans

    kernel = ones((5,5),'uint8')
    kernel1 = ones((7,7),'uint8')
    
    red = dilate(red , kernel1)
    red = erode(red , kernel)
    
    (no_need_variable_1 , contours , h ) =  findContours(red , RETR_TREE , CHAIN_APPROX_SIMPLE)

    for no_need_variable_2 ,contour in enumerate(contours) :

        area = contourArea(contour)

        if (area > 1000)  :

            (x,y) , radius = minEnclosingCircle(contour)
            center = (int(x) , int(y))
            radius = int(radius)
            circle(img,center,radius,circle_color,2)
            if circle_color[1]==255 :
                print(center)
                ans+=1


def get_black_mask(img, hsv) :

    col = 10

    mask_final = inRange(hsv , array([0,0,0]),array([0,0,0]))

    while (col <= 160) :

        lower = array([col ,col-20 , col -20] ,uint8)
        upper = array([col , col+20 , col +20] ,uint8)

        temporary_mask = inRange(img , lower , upper)
        mask_final = temporary_mask + mask_final
        col+=1

    return mask_final

def solve(img) :
    
    global ans
    ans = 0

    hsv = cvtColor(img,COLOR_BGR2HSV)

    lower = array([136,87,111] , uint8)
    upper = array([180,255,255] ,uint8)

    circle_color = (0,255,0)

    red  = inRange(hsv,lower , upper)

    color(img , red , circle_color)

    circle_color = (0,0,255)
    
    black = get_black_mask(img,hsv)  

    color(img , black , circle_color)

    print(ans)

    imshow("Aurora Level 2" , img)
    waitKey(0)


if __name__ == '__main__':

    #  Hey Harsh, How are you :)


    img = imread("/home/preyansh/Pictures/Webcam/test1.jpg")
    solve(img)
    img = imread("/home/preyansh/Pictures/Webcam/test2.jpg")
    solve(img)
    img = imread("/home/preyansh/Pictures/Webcam/test3.jpg")
    solve(img)
    img = imread("/home/preyansh/Pictures/Webcam/test4.jpg")
    solve(img)

    destroyAllWindows()



