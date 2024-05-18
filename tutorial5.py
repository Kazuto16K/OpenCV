#COLOURS AND COLOUR DETECTION

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    #Converting BGR into HSV as extracting colour requires HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90,50,50])   #setting range for blue colour detection
    upper_blue = np.array([130,255,255])

    #creating mask to show only blue colour
    mask = cv2.inRange(hsv,lower_blue, upper_blue)  #returns only those pixels that are blue , others blacked out
    result = cv2.bitwise_and(frame, frame, mask=mask)


    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)
     
    if cv2.waitKey(1) == ord('q'):
        break

    '''
    Colour Schemes:

    RGB : Red Green Blue
    BGR: Blue Green Red
    HSV : Hue Saturation and Lightness/Brightness
    
    '''

cap.release()
cv2.destroyAllWindows()

'''
To convert our own colours

BGR_color = np.array([[[255,0,0]]])
x = cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV)
'''