import cv2 as cv
import numpy as np

img = cv.imread('/home/saud/Desktop/saudpy/2021576_Saud Ahmad/my.png')

#created this to draw countors on this 
blank = np.zeros(img.shape,dtype = 'uint8')


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# This is used to menimize the countours
blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)


canny = cv.Canny(blur,125,175)
cv.imshow('CAnny Edges',canny)

#This will convert all the bits to 0 less than 125 and to 1 greater than 125
ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('THRESH',thresh)


contours,hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

#draw Contours on blank image
cv.drawContours(blank,contours,-1,(0,100,255),1)
cv.imshow('Contours Drawn',blank)


blank2 = np.zeros(img.shape,dtype = 'uint8')

contours,hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

#draw Contours on blank image
cv.drawContours(blank2,contours,-1,(0,100,255),1)
cv.imshow('Contours Drawn2',blank2)

cv.waitKey(0)

