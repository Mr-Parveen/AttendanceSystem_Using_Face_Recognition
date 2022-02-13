from tkinter import *

# fr modules

import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import csv 



window = Tk()
window.title("Welcome To Attendance System Using Face_recognition")
window.geometry("500x200")
window.minsize(500, 200)
window.maxsize(500, 200)

fronthead_label = Label(window, text="Attendance System", bg="#c4c4c4", height=1, width=25,
                       relief="solid", cursor="", fg="red", font=("Castelli", 18, "bold"))
fronthead_label.pack()

# this is the registration form of Attendance system using face_recognition
def registration_form():
    global window
    window = Tk()
    window.title("Attendance System Registration")
    window.geometry("520x600")
    window.maxsize(520, 600)
    window.minsize(520, 600)

    # HeadTitle
    head_label = Label(window, text="Attendance System Form", bg="#c4c4c4", height=1, width=25,
                       relief="solid", cursor="", fg="red", font=("Castelli", 18, "bold"))
    head_label.pack()

    # form fill
    name_lable = Label(window, text=" Name       :", font=("Castelli", 14, "bold"))
    name_lable.pack()
    name_lable.place(relx=0.3, rely=0.15, anchor='se')

    roll_lable = Label(window, text=" Roll no     :", font=("Castelli", 14, "bold"))
    roll_lable.pack()
    roll_lable.place(relx=0.3, rely=0.25, anchor='se')

    branch_lable = Label(window, text=" Branch     :", font=("Castelli", 14, "bold"))
    branch_lable.pack()
    branch_lable.place(relx=0.3, rely=0.35, anchor='se')

    sem_lable = Label(window, text=" Semester :", font=("Castelli", 14, "bold"))
    sem_lable.pack()
    sem_lable.place(relx=0.3, rely=0.45, anchor='se')

    # enter text block
    name_inputtxt = Text(window, height=1.5, width=35)
    name_inputtxt.pack()
    name_inputtxt.place(relx=0.38, rely=0.1, anchor='nw')

    roll_inputtxt = Text(window, height=1.5, width=35)
    roll_inputtxt.pack()
    roll_inputtxt.place(relx=0.38, rely=0.2, anchor='nw')

    branch_inputtxt = Text(window, height=1.5, width=35)
    branch_inputtxt.pack()
    branch_inputtxt.place(relx=0.38, rely=0.3, anchor='nw')

    sem_inputtxt = Text(window, height=1.5, width=35)
    sem_inputtxt.pack()
    sem_inputtxt.place(relx=0.38, rely=0.4, anchor='nw')

    # capture image button
    def error():
        messagebox.showerror("Update", "The RegistrationForm Update will Come Soon")

    capture_printButton = Button(window, text="Capture Student Image", font=("Castelli", 12, 'bold'), fg="grey", height = 1, width = 20)
    capture_printButton.pack()
    capture_printButton.place(relx=0.52, rely=0.55, anchor='center')

    save_printButton = Button(window, text="Save Details", command = error, font=("Castelli", 12, 'bold'), fg="grey", height = 1, width = 20)
    save_printButton.pack()
    save_printButton.place(relx=0.52, rely=0.62, anchor='center')

    # total no students are registered


    totalS_lable = Label(window, text="Total No of Students  :", font=("Castelli", 10, "bold"))
    totalS_lable.pack()
    totalS_lable.place(relx=0.52, rely=0.7, anchor='se')

    dev_lable = Label(window, text="Developed By Parveen Biswas | Contact @mrparveen08 | Version 1.0.1", font=("Castelli", 8))
    dev_lable.pack()
    dev_lable.place(relx=0.5, rely=0.95, anchor='center')



# this is the facerecognition module

def findEncodings(images):
    encodeList = []


    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendance(name):
    with open('attendance.csv', 'r+') as f:
        myDataList = f.readlines()


        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString}')


def main():
    path = '/home/mrparveen/Desktop/PythonPractice/Traning_images'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)

    for cl in myList:
        curImag = cv2.imread(f'{path}/{cl}')
        images.append(curImag)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    encodeListKnown = findEncodings(images)
    print("Encoding Complete")

    cap = cv2.VideoCapture(0)


    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()

                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name,(x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (240, 255, 240), 2)
                markAttendance(name)

            cv2.imshow("Webcam", img)
            cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('0'):
            break


def close():
   window.quit()

# Buttons
atten_lable = Button(window, text="Take Attendance", command = main, font=("Castelli", 12, 'bold'), fg="grey", height = 1, width = 15)
atten_lable.pack()
atten_lable.place(relx=0.5, rely=0.28, anchor='center')

regis_lable = Button(window, text="Registration", command = registration_form, font=("Castelli", 12, 'bold'), fg="grey", height = 1, width = 15)
regis_lable.pack()
regis_lable.place(relx=0.5, rely=0.45, anchor='center')

Exitregis_lable = Button(window, text="Exit", command = close, font=("Castelli", 12, 'bold'), fg="grey", height = 1, width = 15)
Exitregis_lable.pack()
Exitregis_lable.place(relx=0.5, rely=0.62, anchor='center')

dev_lable = Label(window, text="Developed By Parveen Biswas | Contact @mrparveen08 | Version 1.0.1", font=("Castelli", 8))
dev_lable.pack()
dev_lable.place(relx=0.5, rely=0.9, anchor='center')

window.mainloop()
