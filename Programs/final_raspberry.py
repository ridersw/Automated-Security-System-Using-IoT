import numpy as np
import cv2
import pickle
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders 

email_user = '********************@gmail.com'
email_send = '*****************@gmail.com'
subject = "Python!"

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Intruder Has Been Detected'
msg.attach(MIMEText(body,'plain'))

face_cascade = cv2.CascadeClassifier('/home/pi/Latest/cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"person_name" : 1}
with open("labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
    for (x, y , w, h) in faces:
        #print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        id_, conf = recognizer.predict(roi_gray)
        if conf >= 75 and conf <= 200:
            print(conf)
            print(id_)
            print(labels[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
            #cv2.putText(frame, conf, (x,y), font, 1, color, stroke, cv2.LINE_AA)
        else:
            #cv2.putText(frame, "Unknown", (x,y), font, 1, color, stroke, cv2.LINE_AA)
            cv2.imwrite('n.jpg',frame);
            filename = 'n.jpg'
            attachment = open(filename,'rb')

            part = MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',"attachment; filename= "+filename)

            msg.attach(part)
            text = msg.as_string()
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(email_user,'********************')

            body = 'Hello From Python'
            server.sendmail(email_user,email_send,text)
            server.quit()
            print("Email Sent Successfully")
        #img_item = "2.png"
        
        #cv2.imwrite(img_item, roi_color)

        color = (255, 0, 0)
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x,y),(end_cord_x, end_cord_y), color, stroke)
        #cv2.putText(frame,conf,(10,500), font, 3, (200,255,155), 13, cv2.LINE_AA)
        
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

