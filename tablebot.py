import cv2
import os
import pyttsx3
import datetime
import time

engine=pyttsx3.init('espeak')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

         
def speak(text):
    engine.say(text)
    engine.runAndWait()
cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frames = video_capture.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
          
            hour=datetime.datetime.now().hour
            if hour>=0 and hour<12:
              speak("Hello,Good Morning welcome to the special team")
              print("Hello,Good Morning welcome to the special team")
            elif hour>=12 and hour<18:
                speak("Hello,Good Afternoon welcome to the special team")
                print("Hello,Good Afternoon welcome to the special team")
            else:
                speak("Hello,Good Evening welcome to the special team")
                print("Hello,Good Evening welcome to the special team")
            
            cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frames);
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
       
       break
video_capture.release()
cv2.destroyAllWindows()
