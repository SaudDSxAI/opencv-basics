import cv2 as cv

img = cv.imread('/home/saud/Desktop/saudpy/2021576_Saud Ahmad/my.jpg')


cv.imshow('Tasveer',img)


#Convert to gray scale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Tasveer',gray)



#How to blur an image
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)   
cv.imshow('Blur ',blur)


#Edge cascade
canny = cv.Canny(img,125,175)
cv.imshow('Canny',canny)



#Dilating the image
dilated = cv.dilate(canny,(7,7),iterations = 3)
cv.imshow('Dilated',dilated)

cv.destroyAllWindows()
#Eroding image
eroded = cv.erode(dilated,(7,7),iterations = 3)
cv.imshow("Eroded",eroded)



#How to resize an image
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)


cv.destroyAllWindows()


#How to crop an image
cropped = img[50:200,300:400]
cv.imshow('Cropped',cropped)



cv.waitKey(0)
