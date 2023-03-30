import cv2 as cv
import numpy as np

img = cv.imread('/home/saud/Desktop/saudpy/2021576_Saud Ahmad/my.png')
cv.imshow('Image',img)

blank = np.zeros(img.shape[:2],dtype='uint8' )
b,g,r = cv.split(img)
  
blue = cv.merge([b,blank,blank])
red =  cv.merge([blank,g,blank])
green = cv.merge([blank,blank,r])



#This will show color intensity of different colors in gray scale image

cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)


#Showing different colors of an image

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

#merging after spliting
blank = cv.merge([b,g,r])
cv.imshow('After merging',blank)

cv.waitKey(0)