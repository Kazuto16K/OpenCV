#DRAWING LINES AND SHAPES

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    #drawing lines
    img = cv2.line(frame, (0,0), (width,height), (255,0,0), 10) # source image/video , starting position , ending position, colour(B,G,R) format, line thickness
    img = cv2.line(img, (0,height), (width,0), (0,255,0), 10)   #drawing another line on the prev img/frame

    #drawing rectangles
    img = cv2.rectangle(img, (100,100), (200,200), (128,128,128), 5) #source img, center position , radius, colour, line thickness(use -1 to fill)

    #drawing circle
    img = cv2.circle(img, (300,300), 60, (0,0,255), -1) #source , center posi, radius, colour, line thickess(-1 to fill)

    #drawing TEXT
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img , 'Hello World!', (20,height - 10),font,2,(0,0,0), 5, cv2.LINE_AA) #source , target text , position from bottom left(EXCEPTION),font, scale of font ,color, thickness, mentioned in documentation(helps in looking better)

     

    '''
    How X and Y axis are taken in Computer Vision :

    (0,0) x-axis ----->
    y-axis
      |
      |
      |
      V
    '''

    cv2.imshow('frame',img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()