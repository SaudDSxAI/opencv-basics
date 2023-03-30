import cv2 as cv
import numpy as np


#blank image
blank = np.zeros((500,500),dtype= 'uint8')
cv.imshow('new',blank)
#cv.waitKey(0)

#make the image green
blank = np.zeros((500,500,3),dtype= 'uint8')
blank[100:400, 300:600] = 100,44,78
cv.imshow('new',blank)


#Draw rectangle 
cv.rectangle(blank,(0,0),(25,25),(0,255,0),thickness = 2)
cv.imshow('new',blank)


#Draw rectangle FILLED with colour
cv.rectangle(blank,(0,0),(25,25),(0,255,0),thickness = cv.FILLED)
cv.imshow('new',blank)


#draw circle
cv.circle(blank,(255,255),40,(0,255,0),thickness = 1)
cv.imshow('new',blank)

cv.destroyAllWindows()
#Draw Line on image
blank = np.zeros((500,500,3),dtype= 'uint8')
cv.line(blank,(50,0),(250,250),(100,255,34),thickness = 1)
cv.imshow('new',blank)



#How to write on Image
cv.putText(blank,'Text',(255,250),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,244,200),1)
cv.imshow('new',blank)


cv.waitKey(0)






