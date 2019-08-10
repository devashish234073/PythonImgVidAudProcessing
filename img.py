import cv2
import numpy as np

def imshow(fName):
    img=cv2.imread(fName)
    imshowinner(img,fName)

def imshowinner(img,label):
    cv2.imshow(label,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def resizeimg(fName,wPer,hPer):
    img=cv2.imread(fName)
    size=img.shape
    w=size[1]*(wPer/100)
    h=size[0]*(hPer/100)
    resizeimgabsolute(img,w,h,fName)

def resizeimgabsolute(img,w,h,label):
    newimg=cv2.resize(img,(int(w),int(h)),interpolation=cv2.INTER_AREA)
    imshowinner(newimg,label)

