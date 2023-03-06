import numpy as np
import cv2
import pickle

face_cascade = cv2.CascadeClassifier('cascades//data//haarcascade_frontalface_alt2.xml')
#use this cascade to detect the face 
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")
#get labels for the values, reverse of what is done in faces_train.py 
labels = {"person_name": 1}
with open("labels.pickle", 'rb') as f:
    org_labels = pickle.load(f)
    labels = {v:k for k,v in org_labels.items()}

cap = cv2.VideoCapture(0)

while(True):
    ret , frame = cap.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY) #convert the frame to gray
    #find face using this gray frame 
    faces = face_cascade.detectMultiScale(gray , scaleFactor=1.5 , minNeighbors = 5 )
    for( x,y,w,h) in faces:
        #print(x,y,w,h)
        roi_gray =  gray[y:y+h , x:x+w]  #region Of Interest
        roi_color =  frame[y:y+h , x:x+w]

        #recognize
        id_, conf = recognizer.predict(roi_gray) #confidence
        if conf>=45 and conf<=85:
            print(id_)
            print(conf)
            print(labels[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255,255,255)
            stroke = 2
            cv2.putText(frame , name , (x,y), font , 1,color,stroke, cv2.LINE_AA) 

        img_item = "my-image.png"
        cv2.imwrite(img_item , roi_gray)

        color = (255 , 0, 0) #BGR
        stroke = 4
        end_cord_x = x + w 
        end_cord_y = y + h
        cv2.rectangle(frame , (x,y) ,(end_cord_x,end_cord_y), color , stroke)

    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()