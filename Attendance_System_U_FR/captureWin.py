from tkinter import *
from tkinter import messagebox
import cv2
from PIL import Image,ImageTk
from numpy import char
      
def UploadPhoto():
    root = Tk()
    root.title("Upload Photo")
    root.geometry("660x580")
    root.resizable(False,False)

    def exit():
        choice = messagebox.askyesno(message='Do you want to exit?')
        if choice == True:
            root.destroy()
        else:
            pass
    
    def captPhoto():
        name = txt_enter.get()
        image = Image.fromarray(img1)
        imageN = str(name)+".jpeg"
        image.save(imageN)

    

    # ========================== Frame ===============================================
    capt_frame = Label(root, bd = 3, relief= RIDGE, bg="white")
    capt_frame.place(x=4,y=5,width=650,height=489)

    txt_frame = Frame(root, bd = 3, relief= RIDGE, bg="#c4c4c4")
    txt_frame.place(x=6,y=490,width=645,height=80)

    # =========================== detail =============================================
    name_lab = Label(txt_frame, text="Name :", font=("poppins",10, 'bold'), bg="#c4c4c4")
    name_lab.place(x=5, y=10)

    txt_enter = Entry(txt_frame, font=("poppins",10, 'bold'), bd=2)
    txt_enter.place(x=5, y=40)

    tk_Photo = Button(txt_frame, command = captPhoto, text="Upload Photo", width=12, font=("poppins",8, 'bold'))
    tk_Photo.place(x=500, y=10)

    Exit_win = Button(txt_frame, text="Exit", width=12, command=exit, font=("poppins",8, 'bold'))
    Exit_win.place(x=500, y=40)
    # ============================= Camera ===============================================

    cam = cv2.VideoCapture(0)
    

    while True:
        img = cam.read()[1]
        img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(Image.fromarray(img1))
        capt_frame['image'] = img
        root.update()

    

if __name__ == '__main__':
    UploadPhoto()