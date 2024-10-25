import cv2
import numpy as np
from imutils.video import VideoStream

video = VideoStream(src=0).start()
eye_cascade = cv2.CascadeClassifier(r'Detection\haarcascade_eye.xml') 
face_cascade = cv2.CascadeClassifier(r'Detection\haarcascade_frontalface_default.xml')

while True:
    img = video.read()
    img = cv2.flip(img, 1)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
  
    for (x,y,w,h) in faces: 
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = img[y:y+h, x:x+w] 
  
        eyes = eye_cascade.detectMultiScale(roi_gray)  
  
        for (ex,ey,ew,eh) in eyes: 
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2) 
  
    
    cv2.imshow("detection", img)
    key = cv2.waitKey(1)
    
    if key == ord("q"):
        break
video.stop()
cv2.destroyAllWindows()