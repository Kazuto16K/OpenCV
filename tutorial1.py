#OPENCV BASICS - IMPORT, READ, WRITE, DISPLAY, RESIZE

import cv2

img = cv2.imread('assets/DeBruyne.jpg', cv2.IMREAD_COLOR)
#img = cv2.resize(img,(400,400)) #resizing the image with pixel values
img = cv2.resize(img , (0,0), fx=0.5,fy=0.5)    #resizing the image with comparative values to original

#rotating the image
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

#creating new file with the modified image
cv2.imwrite('modified_deBruyne.jpg', img)

#-1 or cv2.IMREAD_COLOR : Loads a color image.Any transparency will be ignored
#0 or cv2.IMREAD_GRAYSCALE : Loads in grayscale mode
#1 or cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel


#displaying an image
cv2.imshow('Image', img)
cv2.waitKey(0)  # wait an infinite amount of time until a key is pressed and move to next Line
cv2.destroyAllWindows()

