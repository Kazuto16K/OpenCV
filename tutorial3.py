#CAMERA AND VIDEO CAPTURE

import numpy as np
import cv2

#loading video capture device(webcam)
cap = cv2.VideoCapture(0)   #value inside depicts number of webcam

#loading video from assets
#cap =cv2.VideoCapture('assets/video.mp4')

while(True):        #keeps diplaying the video until interrupt
    ret, frame = cap.read() #frame gives the image itself(numpy array)      ret tells if its working properly
    width = int(cap.get(3)) # 3 and 4 are properties according to documentation
    height = int(cap.get(4))

    #Creating blank canvas to replicate my video frame (Mirroring Videos multiple times)
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame,cv2.ROTATE_180)    #placing the smaller frame into the top left corner of new image
    image[height//2:, :width//2] = smaller_frame    #bottom left
    image[:height//2, width//2:] = smaller_frame    #top right
    image[height//2:, width//2:] = cv2.rotate(smaller_frame,cv2.ROTATE_180)      #bottom right


    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):      #enter q to stop the video feed, we can customize it according to we want
        break

cap.release()       #release the camera
cv2.destroyAllWindows()