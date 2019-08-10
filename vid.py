import cv2
import numpy as np

def play(fName,delay):
    vid=cv2.VideoCapture(fName)
    ret,frm=vid.read()
    while(ret):
        cv2.imshow(fName,frm)
        ret,frm=vid.read()
        cv2.waitKey(delay)
    cv2.destroyAllWindows()

def addvid(fName1,fName2,delay):
    vid1=cv2.VideoCapture(fName1)
    vid2=cv2.VideoCapture(fName2)
    ret1,frm1=vid1.read()
    ret2,frm2=vid2.read()
    size1=frm1.shape
    size2=frm2.shape
    if(size1[0]==size2[0] and size1[0]==size2[0]):
        while(ret1 and ret2):
            cv2.imshow(fName1+"+"+fName2,frm1+frm2)
            ret1,frm1=vid1.read()
            ret2,frm2=vid2.read()
            cv2.waitKey(delay)
    cv2.destroyAllWindows()

def subvid(fName1,fName2,delay):
    vid1=cv2.VideoCapture(fName1)
    vid2=cv2.VideoCapture(fName2)
    ret1,frm1=vid1.read()
    ret2,frm2=vid2.read()
    size1=frm1.shape
    size2=frm2.shape
    if(size1[0]==size2[0] and size1[0]==size2[0]):
        while(ret1 and ret2):
            cv2.imshow(fName1+"-"+fName2,frm1-frm2)
            ret1,frm1=vid1.read()
            ret2,frm2=vid2.read()
            cv2.waitKey(delay)
    cv2.destroyAllWindows()

def getFPS(fName):
    vid=cv2.VideoCapture(fName)
    fps=vid.get(cv2.CAP_PROP_FPS)
    return fps

def getFrameCount(fName):
    vid=cv2.VideoCapture(fName)
    frmCount=vid.get(cv2.CAP_PROP_FRAME_COUNT)
    return frmCount
