# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 23:22:59 2017

@author: Gokul
"""

import cv2


img=cv2.imread("color_001.jpg" ,cv2.IMREAD_GRAYSCALE) 
#res = cv2.resize(img,None,fx=4, fy=4, interpolation = cv2.INTER_CUBIC)
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
mouth_cascade=cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
faces=face_cascade.detectMultiScale(img,1.1,5)
for(x,y,w,h) in faces:
    mouth=mouth_cascade.detectMultiScale(img,1.7,11)
    for(mx,my,mw,mh) in mouth:
        my = int(my - 0.15*mh)
        #cv2.rectangle(img,(mx,my),(mx+mw,my+mh),(0,0,255),2)
        crop_img = img[my:my+mh, mx:mx+mw]
        #cv2.imshow('cropped', crop_img)
        #cv2.imshow('image',img)
        cv2.imwrite("X:\\cropped.png" ,crop_img)
cv2.waitKey(0)