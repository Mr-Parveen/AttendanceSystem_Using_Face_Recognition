from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import cv2
from PIL import Image,ImageTk

import captureWin
import attendance

root = Tk()
root.title("Attendance System")
root.geometry("550x300")  # width x height
root.minsize(550, 300)
root.maxsize(550, 300)

# ================= frame =========================
Manage_frame = Frame(root, bd=5, relief=RIDGE, bg="white")
Manage_frame.place(x=5, y=48, width=350, height=245)

Manage_frame2 = Frame(root, bd=5, relief=RIDGE, bg="white")
Manage_frame2.place(x=357, y=48, width=185, height=245)

# ================= title =========================
title = Label(root, text="Welcome To Attendance System", bd=5,
              relief=GROOVE, font=("poppins", 20, "bold"), bg="red", fg="white")
title.pack(side=TOP, fill=X)

# ============================================ Exit ===================================================================================
def exit():
    choice = messagebox.askyesno(message='Do you want to exit?')
    if choice == True:
        root.destroy()
    else:
        pass

# ============================================ About ===================================================================================
def About():  # This is a constructor
    root = Tk()
    root.title("About")
    root.geometry("400x100")
    root.resizable(False, False)

    # =================== Lable ================================
    intro_lab = Label(root, text="Welcome To Attendance System")
    intro_lab.place(x=40, y=15)
    intro_lab = Label(root, text="Contact : parveen@example.com")
    intro_lab.place(x=40, y=35)
    intro_lab = Label(root, text="Developed By : Parveen Biswas")
    intro_lab.place(x=40, y=55)

    # =================== Button ===============================
    OK_Exit = Button(root, text="(OK)", command=lambda: root.destroy(), font=(
        "poppins", 10), width=7, bd=2)
    OK_Exit.place(x=290, y=30)

    root.mainloop()

# ============================================ Student detail ===================================================================================
def student():       # This is a constructor
    root = Tk()
    root.title("Student Details")
    root.geometry("1100x650+0+0")      # height x width x X-axis x Y-axis
    root.minsize(1100, 650)
    root.maxsize(1100, 650)

    title = Label(root, text="Student Details", bd=5, relief=GROOVE, font=(
        "times new roman", 25, "bold"), bg="#c4c4c4", fg="red")
    title.pack(side=TOP, fill=X)

    # ================== Frame ==================================

    Manage_frame = Frame(root, bd=5, relief=RIDGE, bg="#d3ceb6")
    Manage_frame.place(x=250, y=50, width=600, height=190)

    Manage_frame2 = Frame(root, bd=5, relief=RIDGE, bg="#d3ceb6")
    Manage_frame2.place(x=25, y=50, width=220, height=190)

    Manage_frame3 = Frame(root, bd=5, relief=RIDGE, bg="#d3ceb6")
    Manage_frame3.place(x=855, y=50, width=216, height=190)

    Detail_frame = Frame(root, bd=5, relief=RIDGE, bg="#d3ceb6")
    Detail_frame.place(x=1, y=245, width=1095, height=400)

    # ================== dialog Box =====================================

    roll_lbl = Label(Manage_frame, text="Roll no.", font=(
        "times new roman", 15, "bold"), bg="#d3ceb6")
    roll_lbl.place(x=15, y=15)
    roll_txt = Entry(Manage_frame, font=(
        "times new roman", 10, "bold"), bd=5, relief=GROOVE)
    roll_txt.place(x=95, y=15)

    name_lbl = Label(Manage_frame, text="Name", font=(
        "times new roman", 15, "bold"), bg="#d3ceb6")
    name_lbl.place(x=15, y=55)
    name_txt = Entry(Manage_frame, font=(
        "times new roman", 10, "bold"), bd=5, relief=GROOVE)
    name_txt.place(x=95, y=55)

    brh_lbl = Label(Manage_frame, text="Branch", font=(
        "times new roman", 15, "bold"), bg="#d3ceb6")
    brh_lbl.place(x=15, y=95)
    brh_txt = Entry(Manage_frame, font=(
        "times new roman", 10, "bold"), bd=5, relief=GROOVE)
    brh_txt.place(x=95, y=95)

    strm_lbl = Label(Manage_frame, text="Stream", font=(
        "times new roman", 15, "bold"), bg="#d3ceb6")
    strm_lbl.place(x=15, y=135)
    strm_txt = Entry(Manage_frame, font=(
        "times new roman", 10, "bold"), bd=5, relief=GROOVE)
    strm_txt.place(x=95, y=135)

    sem_lbl = Label(Manage_frame, text="Semester", font=(
        "times new roman", 15, "bold"), bg="#d3ceb6")
    sem_lbl.place(x=300, y=15)
    # combobox for options which is readable only
    sem_txt = ttk.Combobox(Manage_frame, font=(
        "times new roman", 10, "bold"), state='readonly')
    sem_txt['values'] = ("1st", "2nd", "3rd", "4th",
                         "5th", "6th", "7th", "8th")
    sem_txt.place(x=400, y=19)

    eml_lbl = Label(Manage_frame, text="Email", font=(
        "times new roman", 15, "bold"), bg="#d3ceb6")
    eml_lbl.place(x=300, y=55)
    eml_txt = Entry(Manage_frame, font=(
        "times new roman", 10, "bold"), bd=5, relief=GROOVE)
    eml_txt.place(x=400, y=55)

    phn_lbl = Label(Manage_frame, text="Phone no.", font=(
        "times new roman", 15, "bold"), bg="#d3ceb6")
    phn_lbl.place(x=300, y=95)
    phn_txt = Entry(Manage_frame, font=(
        "times new roman", 10, "bold"), bd=5, relief=GROOVE)
    phn_txt.place(x=400, y=95)

    # ======================= Button ==================================================

    uplod_btn = Button(Manage_frame2, text="Upload photo", width=18, font=(
        "poppins", 10, 'bold'), fg="#333331", height=1)
    uplod_btn.place(x=10, y=145)

    add_btn = Button(Manage_frame3, text="Add", width=18, font=(
        "poppins", 10, 'bold'), fg="#333331", height=1)
    add_btn.place(x=10, y=5)

    updt_btn = Button(Manage_frame3, text="Update", width=18, font=(
        "poppins", 10, 'bold'), fg="#333331", height=1)
    updt_btn.place(x=10, y=40)

    dlt_btn = Button(Manage_frame3, text="Delete", width=18, font=(
        "poppins", 10, 'bold'), fg="#333331", height=1)
    dlt_btn.place(x=10, y=75)

    abt_btn = Button(Manage_frame3, text="About", command=About, width=18, font=(
        "poppins", 10, 'bold'), fg="#333331", height=1)
    abt_btn.place(x=10, y=110)

    ext_btn = Button(Manage_frame3, text="Exit", command=lambda: root.destroy(), width=18, font=(
        "poppins", 10, 'bold'), fg="#333331", height=1)
    ext_btn.place(x=10, y=145)

    # ======================= Search Dialog Box ========================================

    srh_lbl = Label(Detail_frame, text="Search By",
                    font=("poppins", 12, "bold"), bg="#d3ceb6")
    srh_lbl.place(x=60, y=12)
    # combobox for options which is readable only
    srh_bx = ttk.Combobox(Detail_frame, font=(
        "times new roman", 10, "bold"), state='readonly')
    srh_bx['values'] = ("Roll no.", "Name", "Phone no.", "Email")
    srh_bx.place(x=160, y=10, width=100, height=27)

    srh_txt = Entry(Detail_frame, font=(
        "times new roman", 10, "bold"), relief=GROOVE)
    srh_txt.place(x=275, y=10, width=180, height=29)

    srh_btn = Button(Detail_frame, text="Search", font=(
        "poppins", 8, 'bold'), fg="#333331")
    srh_btn.place(x=465, y=10, width=80)

    sho_btn = Button(Detail_frame, text="Show all",
                     font=("poppins", 8, 'bold'), fg="#333331")
    sho_btn.place(x=550, y=10, width=80)

    # ======================= Table Frame ===============================================

    tbl_frame = Frame(Detail_frame, bd=3, relief=RIDGE, bg="white")
    tbl_frame.place(x=1, y=45, width=1083, height=345)

    srol_x = Scrollbar(tbl_frame, orient=HORIZONTAL)
    srol_y = Scrollbar(tbl_frame, orient=VERTICAL)

    std_tbl = ttk.Treeview(tbl_frame, column=("roll", "name", "branch", "stream", "semester",
                           "email", "phone"), xscrollcommand=srol_x.set, yscrollcommand=srol_y.set)

    srol_x.pack(side=BOTTOM, fill=X)
    srol_y.pack(side=RIGHT, fill=Y)

    srol_x.config(command=std_tbl.xview)
    srol_y.config(command=std_tbl.yview)

    root.mainloop()

# ================= Button ========================
tk_Att_btn = Button(Manage_frame2, text="Take Attendance", command= attendance.Attendance, width=14, font=(
        "poppins", 10, 'bold'), fg="#333331", height=1)
tk_Att_btn.place(x=10, y=20)

up_Pt_btn = Button(Manage_frame2, text="Upload Photo", command=captureWin.UploadPhoto, width=14, font=(
        "poppins", 10, 'bold'), fg="#333331", height=1)
up_Pt_btn.place(x=10, y=60)

st_Dt_btn = Button(Manage_frame2, text="Student Details", command=student, width=14, font=(
        "poppins", 10, 'bold'), fg="#333331", height=1)
st_Dt_btn.place(x=10, y=100)

abt_btn = Button(Manage_frame2, text="About", command=About, width=14, font=(
        "poppins", 10, 'bold'), fg="#333331", height=1)
abt_btn.place(x=10, y=140)

ext_btn = Button(Manage_frame2, text="Exit", command=exit, width=14, font=(
        "poppins", 10, 'bold'), fg="#333331", height=1)
ext_btn.place(x=10, y=180)

root.mainloop()
