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


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="#2E4053", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\developer (2).jpg")
        img_top = img_top.resize((1530, 760), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=42, width=1530, height=760)
        
        # Frame
        main_frame = Frame(f_lbl, bd=2, bg="#1B4F72")
        main_frame.place(x=500, y=150, width=500, height=400)
        
        img_top1 = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\my.jpeg")
        img_top1 = img_top1.resize((200, 200), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl1 = Label(main_frame, image=self.photoimg_top1)
        f_lbl1.place(x=150, y=42, width=200, height=200)
        
        # Developer info
        dev_label = Label(main_frame, text="Hello I'm Nazrana Nahreen", font=("times new roman", 13, "bold"), bg="#1B4F72",fg="white")
        dev_label.place(x=150, y=240)
        
        dev1_label = Label(main_frame, text="As a beginner, I've initiated this project with the ambition of", font=("times new roman", 13, "bold"), bg="#1B4F72",fg="white")
        dev1_label.place(x=20, y=264)
        
        dev2_label = Label(main_frame, text="transforming it into an advanced machine learning-driven ", font=("times new roman", 13, "bold"), bg="#1B4F72",fg="white")
        dev2_label.place(x=20, y=288)
        
        dev3_label = Label(main_frame, text="system suitable for real-world deployment I've taken the", font=("times new roman", 13, "bold"), bg="#1B4F72", fg="white")
        dev3_label.place(x=20, y=312)
        
        dev4_label = Label(main_frame, text=" initiative to embark on this project as a learning experience", font=("times new roman", 13, "bold"), bg="#1B4F72", fg="white")
        dev4_label.place(x=20, y=338)
        
        
    
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
