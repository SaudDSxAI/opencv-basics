import cv2 as cv 

capture = cv.VideoCapture(0)

img = cv.imread('/home/saud/Desktop/saudpy/2021576_Saud Ahmad/my.jpg')


cv.imshow('MY',img)
cv.waitKey(0)

def reScale(frame,scale = 2):
    
    width =  int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    reSize(width, height)
    
    dimen = (width,height)
    
    return cv.resize(frame,dimen,interpolation = cv.INTER_AREA)

def reSize(width,height):
    capture.set(5,width)
    capture.set(4,height)



while True:
    istrue,frame = capture.read()
    
    frame2 = reScale(frame)
    cv.imshow('Video',frame2)
    
    if  cv.waitKey(20) & 0xFF == ord('d'):
        break
    

capture.release()
cv.destroyAllWindows()