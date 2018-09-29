# -*- coding: utf-8 -*-

import cv2
#import time
#import numpy as np

def process(img):

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2)
##        roi_gray = gray[y:y+h , x:x+w]
##        roi_color = img[y:y+h , x:x+w]
##        eyes= eye_cascade.detectMultiScale(roi_gray,1.3,5)
##        for (ex,ey,ew,eh) in eyes:
##            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
            
    return img,faces

def track(img):
    print("sa")






cap =cv2.VideoCapture(0)
find=False


old_faces=[]
##tracker = cv2.Tracker_create("MIL")

while (True):
 face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
 eye_cascade =  cv2.CascadeClassifier('haarcascade_eye.xml')  
 ret , frame = cap.read()
 frame,faces = process(frame)
 if len(faces)==0:
     if find:
         pass
        #  a=old_faces[0,1]
        #  b=old_faces[0,2]
        #  c=old_faces[0,1]+old_faces[0,3]
        #  d=old_faces[0,2]+old_faces[0,4]
        #  rec=[a,b,c,d]
        #  ok=tracker.init(frame,rec)
        #  print ("track")
 else:
     cv2.imshow('vid',frame)
     old_faces=faces
     old_frame =frame
     find=True

 if cv2.waitKey(20)==ord('q'):
     break
    
cv2.destroyAllWindows() 
cap.release()
