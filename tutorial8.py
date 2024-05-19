#Live Face and Eye Detection/Tracking

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #get face template for fetection from open CV
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')  #get eye template for fetection from open CV

#font settings
font =cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.75
font_color = (255,0,0)
font_thickness = 2

while True:
    ret, frame = cap.read()         #read from my webcam
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #convert webcam video input to grayscale
    faces= face_cascade.detectMultiScale(gray, 1.3, 5) #returns all faces in terms of position from video
    for (x,y, w,h) in faces:    #x,y - top left, w,h gives height width
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),5)   #draw the rectangle around faces
        roi_gray = gray[y:y+h,x:x+w] #region of interest
        roi_color = frame[y:y+h,x:x+w]  #reference to original frame

        #label positions
        label = 'Face Detected'
        label_x = x
        label_y = y - 10
        cv2.putText(frame,label, (label_x,label_y),font, font_scale, font_color, font_thickness)

        eyes = eye_cascade.detectMultiScale(roi_gray,1.3, 5)    #finding eyes on the face
        for (ex,ey,ew,eh) in eyes:  #this telling location of our eyes relative to our face
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh),(0,255,0),5)    #draw the eyes in the face(grayscale for algorithm) in ROI_Color


    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()