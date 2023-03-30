import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('/home/saud/Desktop/saudpy/2021576_Saud Ahmad/my.png')
cv.imshow('Image ',img)

#This will play the original image read by open cv 
plt.imshow(img)
plt.show()

#BGR to gray scale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('BGR to gray',gray)

#BGR to hsv
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('BGR to HSV',hsv)

#BGR to L.A.B
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('BGR to LAB',lab)


#Note that is you want to convert from gray scale to LAB  there is no direct method
#instead convert grayscale to BGR and then to LAB
cv.waitKey(0)