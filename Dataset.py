import cv2
import numpy as np
import os
import pickle

video = cv2.VideoCapture(0)  #0 for webcam
facedetect = cv2.CascadeClassifier("/Users/vysubs28/Python Projects/FaceRecognitionProject/haarcascade_frontalface_default.xml")

face_data = []

i = 0 

name = input("Enter your name:")

while True:
    ret,frame=video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
    
    for (x,y,w,h) in faces:
        crop_img = frame[y:y+h,x:x+w,:]
        resize_img = cv2.resize(crop_img,(50,50))
        if len(face_data) <= 100 and i % 10 == 0:
            face_data.append(resize_img)
            cv2.putText(frame,str(len(face_data)),org=(50,50),fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=(255, 255, 255), thickness=1)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),1)
            
    cv2.imshow("frame",frame)
        
    if len(face_data)==50:
        break
        
    i+=1
    k=cv2.waitKey(1)
    if k == ord('q'):
        break
        
video.release()
cv2.destroyAllWindows

#save faces in pickle file

face_data = np.array(face_data)
face_data = face_data.reshape(50,-1)

if not os.path.exists('data'):
    os.makedirs('data')

if 'names.pkl' not in os.listdir('data/'):
    names = [name]*50
    with open('data/names.pkl','wb') as f:
        pickle.dump(names,f)
else:
    with open('data/names.pkl','rb') as f:
        names=pickle.load(f)
        names=names+[name]*50
        
    with open('data/names.pkl','wb') as f:
        pickle.dump(names,f)
        
if 'face_data.pkl' not in os.listdir('data/'):
    with open('data/face_data.pkl','wb') as f:
        pickle.dump(face_data,f)
else:
    with open('data/face_data.pkl','rb') as f:
        faces = pickle.load(f)
    faces = np.append(faces,face_data,axis = 0)
    with open('data/face_data.pkl','wb') as f:
        pickle.dump(faces,f)