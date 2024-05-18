#CHANGING PART OF IMAGE, COPYING AND PASTING PART OF IMAGE INTO ANOTHER

import cv2
import random
img = cv2.imread('assets/DeBruyne.jpg',-1)    #loads the image in colour

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randrange(255),random.randrange(255),random.randrange(255)]   #randomly displaying the image

#copying part of the image
print(img.shape)
tag = img[500:700, 450:750] #copies a square of my image
img[100:300, 250:550] = tag  #placing then into another part (SAME DIMENSIONS)

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()