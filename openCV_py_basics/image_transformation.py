import cv2 as cv
import numpy as np

img = cv.imread('/home/saud/Desktop/saudpy/2021576_Saud Ahmad/my.png')


#Translation
def translate(img,x,y):
    transMat  =  np.float32([[1,0,x],[0,1,y]])
    dimentions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimentions)

# -x ---> Left
# -y ---> Down
#  x ---> Right
#  y ---> UP

translated = translate(img,100,100)
cv.imshow('Trans',translated)


#Rotation of image
def rotate(img,angle,rotPoint = None):
    (height,width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,.5)
    dimentions = (width,height)
    
    return cv.warpAffine(img,rotMat,dimentions)

rotated = rotate(img,-45)
cv.imshow('Rotated',rotated)


#Resize an image
resized = cv.resize(img,(100,500),interpolation = cv.INTER_CUBIC)
cv.imshow('resized',resized)


#Flip an image
flip = cv.flip(img,0)
cv.imshow('Flip',flip)

cv.destroyAllWindows()

#Crope an image
cropped = img[200:400,300:400]
cv.imshow('Croped',cropped)



cv.waitKey(0)




 

