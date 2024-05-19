#OBJECT DETECTION (Template Matching)
import numpy as np
import cv2

original_img = cv2.resize(cv2.imread("assets/soccer_practice.jpg",-1),(0,0),fx=0.8,fy=0.8)
img = cv2.resize(cv2.imread("assets/soccer_practice.jpg",0),(0,0),fx=0.8,fy=0.8) #algorithm requires grayscale)
template = cv2.resize(cv2.imread('assets/shoe.png',0),(0,0),fx=0.8,fy=0.8)

h,w = template.shape
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]
i = 1

#font settings
font =cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.5
font_color = (255,0,0)
font_thickness = 1

for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template,method)  #Our template acts as a convolution/kernel #imgace source, template source, method
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result) #returns the given data

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w,location[1]+h) #getting bottom right for drawing triangle from top right corner
    #cv2.rectangle(img2, location,bottom_right,255,5)

    cv2.rectangle(original_img, location,bottom_right,(0,0,255),5)
    #cv2.imshow('Match',img2)

    #label positions
    label = 'Algo '+ str(i)
    i = i+1
    label_x = location[0]
    label_y = location[1] - 10
    cv2.putText(original_img,label, (label_x,label_y),font, font_scale, font_color, font_thickness)
    #cv2.imshow('lable',)

    cv2.imshow('match', original_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(min_loc,max_loc)

'''
methods of template matching are :

[cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCOR_NORMED, cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]
'''