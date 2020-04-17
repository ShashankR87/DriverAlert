#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import cv2
from tkinter import *
import tkinter 
from PIL import Image, ImageTk
import time
import winsound
frequency=2500
duration=1000
eyescascade = cv2.CascadeClassifier('haarcascade_eye.xml')

window = Tk()
window.configure(bg="black")

Label (window, text="Drowsiness Alert System", bg="black", fg="white").grid(row=0,column=0)

cap = cv2.VideoCapture(0)

def stop():
    cv2.destroyAllWindows()
    window.update()
    #cv2.waitKey(1000)

    #cv2.waitKey(1)
    #cv2.destroyAllWindows()
    #cv2.waitKey(1)

def show_frame():
    
    Button(window, text="Stop Journey", width=15, height=2, command=stop).grid(row=2,column=4)
    window.update()
    while cap.isOpened():
        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        eyes = eyescascade.detectMultiScale(gray,1.1,4)
        numOfeyes=0
        for (x,y,w,h) in eyes:
            cv2.rectangle(img, (x,y), (x+w,y+h),(255,0,0),1)
            numOfeyes+=1
        #cv2.imshow('img',img)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        if numOfeyes == 0:
            if closedcnt >= 2:
                cv2.putText(img,'WAKE UP!',(100,50), font, 4, (255, 255, 255), 2, cv2.LINE_AA)
                print('WAKE UP!')
                winsound.Beep(frequency, duration)
                cnlosedcnt=0
            else:
                closedcnt+=1
        else:
            closedcnt=0
        print(numOfeyes)
        time.sleep(1)

Button(window, text="Start Journey", width=15, height=2, command=show_frame).grid(row=2,column=0)
#show_frame()  #Display 2
window.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




