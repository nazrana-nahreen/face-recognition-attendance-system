from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import openpyxl 
import re
from datetime import datetime
import tkinter.simpledialog as simpledialog


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="#1B7251", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\help desk.png")
        img_top = img_top.resize((1530, 760), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=42, width=1530, height=760)
        dev_label = Label(f_lbl, text="Email:nahreennazrana@gmail.com", font=("times new roman", 40, "bold"), bg="#1B4F72",fg="white")
        dev_label.place(x=360, y=610)




if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
