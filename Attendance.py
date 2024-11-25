import cv2
import numpy as np
import os
import csv
import time
import pickle
from sklearn.neighbors import KNeighborsClassifier
from datetime import datetime

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier("/Users/vysubs28/Python Projects/FaceRecognitionProject/haarcascade_frontalface_default.xml")

# Load data
with open('data/names.pkl', 'rb') as w:
    LABELS = pickle.load(w)

with open('data/faces_data.pkl', 'rb') as f:
    FACES = pickle.load(f)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

infobackground = cv2.imread("/Users/vysubs28/Python Projects/FaceRecognitionProject/Chi.jpg")
if infobackground is None:
    print("Error: Background image not found. Check the file path.")
    exit()

COL_NAMES = ['Name', 'Time']

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w, :]
        resized_img = cv2.resize(crop_img, dsize=(50, 50)).flatten().reshape(1, -1)
        output = knn.predict(resized_img)
        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")
        exists = os.path.isfile("Attendance/Attendance_" + date + ".csv")

        # Draw rectangles and text
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(frame, text=str(output[0]), org=(x, y - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(50, 50, 255), thickness=2)
        attendance = [str(output[0]), str(timestamp)]

        if exists:
            with open("Attendance/Attendance_" + date + ".csv", "a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(attendance)
        else:
            with open("Attendance/Attendance_" + date + ".csv", "a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                writer.writerow(attendance)

    # Update background
    try:
        infobackground[162:162+frame.shape[0], 55:55+frame.shape[1]] = frame
    except ValueError:
        print("Error: Frame dimensions do not match background.")
        break

    cv2.imshow("frame", infobackground)

    # Break conditions
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
