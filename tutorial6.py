#CORNER DETECTION IN AN IMAGE

import numpy as np
import cv2


img = cv2.imread('assets/chess.jpg',-1)
img = cv2.resize(img, (0,0), fx=0.6, fy=0.6)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.5, 10) # source, gives N best corner(customizable), min quality of corner(range = 0 to 1) , min distance between 2 corners(eucledian distance)
corners = np.int0(corners) #takes numpy array of floating point into integers

# we get array inside array, so we need to decompose
for corner in corners:
    x, y = corner.ravel()  
    cv2.circle(img, (x,y), 5, (255,0,0) , -1)
    '''  
    Working of Ravel:
    [[[0,1,2]]] --> [0,1,2]
    [[0,1],[2,3]] --> [0,1,2,3]
    '''

#Drawing randomly coloured lines between every corner
for i in range(len(corners)):
    for j in range(i+1,len(corners)):
        corner1 = tuple(corners[i][0])  # this format gives the interior array as it is not ravelled
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x:int(x), np.random.randint(0,255, size=3))) #applying lambda function to convert to regular python integer from numpy value
        cv2.line(img, corner1 , corner2, color,1)



cv2.imshow('Frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows()