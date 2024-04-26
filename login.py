from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import messagebox
from main import Face_Recognition_System
import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
from student import Admin
from train import Train
from takeattendance import TAKEATTENDANCE
from recognition import FaceRecognition
from developer import Developer
from help import Help
from studentpanel import Student
import os
from tkinter import messagebox
from tkinter.simpledialog import askstring



def main():
    win=Tk()
    app=LoginWindow(win)
    win.mainloop()

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        

        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Load the background image
        try:
            bg_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\bg.jpg")
            bg_img = bg_img.resize((screen_width, screen_height), Image.LANCZOS)
            self.bg_photoimg = ImageTk.PhotoImage(bg_img)
        
            # Create a Label to display the background image
            bg_lbl = Label(self.root, image=self.bg_photoimg)
            bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)  # Position the Label to cover the entire window
            
            main_frame = Frame(self.root, bd=0, bg="white")  # Changed from Frame(frame, ...) to Frame(self.root, ...)
            main_frame.place(x=600, y=150, width=340, height=400)
            
            img_top1 = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\loginicon.png")
            self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

            f_lbl1 = Label(main_frame, image=self.photoimg_top1)
            f_lbl1.place(x=120, y=10, width=90, height=100)

            # Create a Label for "Log In" text
            get_str = Label(main_frame, text="Log In", font=("times new roman", 20, "bold"), fg="blue", bg="white")
            get_str.place(x=123, y=120)  # Adjusted coordinates
            
            
            # Label for Username
            username_lbl = Label(main_frame, text="Username", font=("times new roman", 15, "bold"), fg="blue", bg="white")
            username_lbl.place(x=70, y=155)

            # Entry widget for Username
            self.txtuser = ttk.Entry(main_frame, font=("times new roman", 15, "bold"))
            self.txtuser.place(x=48, y=180, width=270)

            # Label for Password
            password_lbl = Label(main_frame, text="Password", font=("times new roman", 15, "bold"), fg="blue", bg="white")
            password_lbl.place(x=70, y=225)

            # Entry widget for Password
            self.txtpass = ttk.Entry(main_frame, font=("times new roman", 15, "bold"))
            self.txtpass.place(x=40, y=250, width=270)

            # Icon Image for Username
            img2 = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\usernameicon.png")
            img2 = img2.resize((25, 25), Image.LANCZOS)
            self.photoimage2 = ImageTk.PhotoImage(img2)

            # Label to display the icon image for Username
            lbling2 = Label(main_frame, image=self.photoimage2, bg="white", borderwidth=8)
            lbling2.place(x=40, y=150, width=25, height=25)
            
            # Icon Image for Password
            img3 = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\passwordicon.png")
            img3 = img3.resize((25, 25), Image.LANCZOS)
            self.photoimage3 = ImageTk.PhotoImage(img3)

            # Label to display the icon image for Password
            lbling3 = Label(main_frame, image=self.photoimage3, bg="white", borderwidth=8)
            lbling3.place(x=40, y=220, width=25, height=25)
            
            #=======login button==============
            # Create a Login Button
            loginbtn = Button(main_frame, text="Login", font=("times new roman", 15, "bold"), borderwidth=8, bd=3, relief="ridge", fg="white", bg="navy", command=self.login)
            loginbtn.place(x=110, y=300, width=120, height=35)
            
            # Register Button
            registerbtn = Button(main_frame, text="New User Register", font=("times new roman", 10, "bold"),command=self.register_window, fg="navy", bg="white")
            registerbtn.place(x=20, y=350, width=130)

            # Forget Password Button
            forgetpassbtn = Button(main_frame, text="Forget Password", font=("times new roman", 10, "bold"),command=self.forgot_password_window, fg="navy", bg="white")
            forgetpassbtn.place(x=180, y=350, width=130)
           
           
            iiuc_logo_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\iiuclogo.png")
            iiuc_logo_img = iiuc_logo_img.resize((100, 100), Image.LANCZOS)
            self.iiuc_logo_photoimg = ImageTk.PhotoImage(iiuc_logo_img)

            # Create a label to display the IIUC logo
            iiuc_logo_label = Label(self.root, image=self.iiuc_logo_photoimg, bg="skyblue")
            iiuc_logo_label.place(x=395, y=20)  # Adjust the coordinates as needed

            register_lbl = Label(self.root, text="INTERNATIONAL ISLAMIC UNIVERSITY CHITTAGONG", font=("times new roman", 20, "bold"), fg="darkgreen", bg="skyblue")
            register_lbl.place(x=500, y=50)

        except Exception as e:
            print("Error loading image:", e)
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="nazrana2028@",
                    database="face_recognizer",
                )
            my_cursor = conn.cursor()  
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                    ))  
            
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid username or password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only admin")
                if open_main:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return  
            conn.commit()
            self.clear()
            conn.close()

    def clear(self):
        # Clear the entry fields
        self.txtuser.delete(0, 'end')
        self.txtpass.delete(0, 'end') 
    #================reset password window=======================================
    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select security Question", parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please enter the answer", parent=self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter the new password", parent=self.root2)
        else:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="nazrana2028@",
                database="face_recognizer",
            )
            my_cursor = conn.cursor() 
            query = "SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s"
            values = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get())
            my_cursor.execute(query, values)
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please enter correct Answer", parent=self.root2)
            else:
                update_query = "UPDATE register SET password=%s WHERE email=%s"
                update_values = (self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(update_query, update_values)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your password has been reset, please login with the new password", parent=self.root2)

        
        
        
           
    #===============forget password window============================    
    def forgot_password_window(self):
        if self.txtuser.get()=="":
           messagebox.showerror("Error", "Plaese enter the Email address to reset password")
        else:
            conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="nazrana2028@",
                    database="face_recognizer",
                )
            my_cursor = conn.cursor()   
            query=("select* from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()
           
            if row==None:
                messagebox.showerror("My Error", "Plaese enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+178") 
                # Label for "Forget Password"
                lbl_forget_password = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), fg="red", bg="white")
                lbl_forget_password.place(x=0, y=10, relwidth=1)

                # Label for Security Question
                security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
                security_Q.place(x=50, y=80)

                # Combobox for Security Question
                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your favourite food name", "Your Pet Name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)  # Setting default value to "Select"

                # Label for Security Answer
                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
                security_A.place(x=50, y=150)

                # Entry widget for Security Answer
                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_security.place(x=50, y=180, width=250)
                
                # Label for New Password
                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
                new_password.place(x=50, y=220)

                # Entry widget for New Password
                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_newpass.place(x=50, y=250, width=258)

                # Reset Button
                btn_reset = Button(self.root2, text="Reset", font=("times new roman", 15, "bold"),command=self.reset_pass, fg="white", bg="green")
                btn_reset.place(x=120, y=290)

                        
                        
            
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.login_window = LoginWindow
        self.root.geometry("1550x800+0+0")
       

        
        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        
         
        #=============variables==================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_check= IntVar()
        

        # Load the background image
        try:
            bg_img = Image.open(r"C:/Users/DELL/Desktop/newFace Recognition, Student Attendance System/images/bg.jpg")
            bg_img = bg_img.resize((screen_width, screen_height), Image.LANCZOS)
            self.bg_photoimg = ImageTk.PhotoImage(bg_img)
        
            # Create a Label to display the background image
            bg_lbl = Label(self.root, image=self.bg_photoimg)
            bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)  # Position the Label to cover the entire window
            
            # Main frame
            main_frame = Frame(self.root, bd=0, bg="white") 
            main_frame.place(x=480, y=130, width=650, height=500)
            
            register_lbl = Label(main_frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkgreen", bg="white")
            register_lbl.place(x=210, y=20)
            
            # First Name
            fname_lbl = Label(main_frame, text="First Name", font=("times new roman", 15, "bold"), bg="white") 
            fname_lbl.place(x=50, y=100)
            self.txt_fname = ttk.Entry(main_frame, font=("times new roman", 15), textvariable=self.var_fname) 
            self.txt_fname.place(x=50, y=130, width=250)

            # Last Name
            lname_lbl = Label(main_frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black") 
            lname_lbl.place(x=370, y=100)
            self.txt_lname = ttk.Entry(main_frame, font=("times new roman", 15), textvariable=self.var_lname) 
            self.txt_lname.place(x=370, y=130, width=250)

            # Contact Number
            contact_lbl = Label(main_frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="black") 
            contact_lbl.place(x=50, y=180)
            self.txt_contact = ttk.Entry(main_frame, font=("times new roman", 15), textvariable=self.var_contact) 
            self.txt_contact.place(x=50, y=205, width=250)

            # Email
            email_lbl = Label(main_frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black") 
            email_lbl.place(x=370, y=180)
            self.txt_email = ttk.Entry(main_frame, font=("times new roman", 15), textvariable=self.var_email) 
            self.txt_email.place(x=370, y=205, width=250)

            # Security Question
            securityQ_lbl = Label(main_frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black") 
            securityQ_lbl.place(x=50, y=240)
            self.combo_securityQ = ttk.Combobox(main_frame, font=("times new roman", 15), textvariable=self.var_securityQ, state="readonly")
            self.combo_securityQ["values"] = ("Select", "Your Birth Place", "Your favourite food name", "Your Pet Name")
            self.combo_securityQ.current(0)
            self.combo_securityQ.place(x=50, y=270, width=250)

            # Security Answer
            securityA_lbl = Label(main_frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black") 
            securityA_lbl.place(x=370, y=240)
            self.txt_security = ttk.Entry(main_frame, font=("times new roman", 15), textvariable=self.var_securityA) 
            self.txt_security.place(x=370, y=270, width=250)

            # Password
            pswd_lbl = Label(main_frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black") 
            pswd_lbl.place(x=50, y=310)
            self.txt_pswd = ttk.Entry(main_frame, font=("times new roman", 15), show="*", textvariable=self.var_pass) 
            self.txt_pswd.place(x=50, y=340, width=258)

            # Confirm Password
            confirmPswd_lbl = Label(main_frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black") 
            confirmPswd_lbl.place(x=370, y=310)
            self.txt_confirmPswd = ttk.Entry(main_frame, font=("times new roman", 15), show="*", textvariable=self.var_confpass) 
            self.txt_confirmPswd.place(x=370, y=340, width=258)
            
            # Check Button
            checkbtn = Checkbutton(main_frame, text="I Agree The Terms & Conditions", font=("times new roman", 15, "bold"), variable=self.var_check,onvalue=1, offvalue=0, bg="white")
            checkbtn.place(x=50, y=380)

            
            # Buttons
            img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\registernowbtn (1).png")  
            img = img.resize((200, 50), Image.LANCZOS)
            self.photoimage = ImageTk.PhotoImage(img)

            bi = Button(main_frame, image=self.photoimage,command=self.register_data, borderwidth=0, cursor="hand2")  
            bi.place(x=110, y=420, width=200)

            img1 = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\loginbtn.png")  
            img1 = img1.resize((150, 50), Image.LANCZOS)
            self.photoimage1 = ImageTk.PhotoImage(img1)

            b1 = Button(main_frame, image=self.photoimage1, borderwidth=0, cursor="hand2",command=self.return_login)  
            b1.place(x=330, y=420, width=150)  
            
            
             # Create a label to display the IIUC logo
            iiuc_logo_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\iiuclogo.png")
            iiuc_logo_img = iiuc_logo_img.resize((100, 100), Image.LANCZOS)
            self.iiuc_logo_photoimg = ImageTk.PhotoImage(iiuc_logo_img)
            iiuc_logo_label = Label(self.root, image=self.iiuc_logo_photoimg, bg="skyblue")
            iiuc_logo_label.place(x=395, y=20)  # Adjust the coordinates as needed

            iiuc_lbl = Label(self.root, text="INTERNATIONAL ISLAMIC UNIVERSITY CHITTAGONG", font=("times new roman", 20, "bold"), fg="darkgreen", bg="skyblue")
            iiuc_lbl.place(x=500, y=50)
            
            

        except Exception as e:
            print("Error loading image:", e)
     
    # ==========Function declaration========================
        # Handle login button click event
   
            
            
            
    def register_data(self):
        if not (self.var_fname.get() and self.var_email.get() and self.var_securityQ.get() != "Select"):
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password and Confirm Password must be the same")
        elif not self.var_check.get():
            messagebox.showerror("Error", "Please agree to our terms and conditions")
        else:
            conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="nazrana2028@",
                    database="face_recognizer",
                )
            my_cursor = conn.cursor()  
            query = ("select * FROM register WHERE email = %s")
            value=(self.var_email.get(),)
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()
            if row!=None:
                 messagebox.showerror("Error", "User already exists, please try another email")
            else:
                
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", ( 
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()  
                                                                                      ))
            conn.commit()
            
            messagebox.showinfo("Success", "Register Successfully") 
            conn.close()
    def return_login(self):
        self.root.destroy()
            
     
  
            

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.admin_password = "admin123"  # Define the admin password

        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        try:
            # Load the background image
            bg_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\bg.jpg")
            bg_img = bg_img.resize((screen_width, screen_height), Image.LANCZOS)
            self.bg_photoimg = ImageTk.PhotoImage(bg_img)
            
            # Create a Label to display the background image
            bg_lbl = Label(self.root, image=self.bg_photoimg)
            bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)  # Position the Label to cover the entire window

            # Load the logo image and resize it
            logo_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\iiuclogo.png")
            logo_img = logo_img.resize((100, 100), Image.LANCZOS)
            self.logo_photoimg = ImageTk.PhotoImage(logo_img)
            
            # Create a Label to display the logo
            logo_lbl = Label(self.root, image=self.logo_photoimg, bg="white")
            logo_lbl.place(x=0, y=45)  # Position the logo over the title label

            # Create a Label for the title
            title_lbl = Label(self.root, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 18, "bold"), bg="#8FBC8F", fg="navy")
            title_lbl.place(x=0, y=0, width=screen_width, height=45)

            # Load the student image
            student_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\Student Panel (8).jpg")
            student_img = student_img.resize((220, 220), Image.LANCZOS)
            self.student_photoimg = ImageTk.PhotoImage(student_img)

            # Create and place the student button
            b1 = Button(self.root, image=self.student_photoimg, command=self.check_admin_password, cursor='hand2')
            b1.place(x=200, y=380, width=220, height=220)

            b1_1 = Button(self.root, text="ADMIN PANEL", command=self.check_admin_password, cursor='hand2', font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
            b1_1.place(x=200, y=560, width=220, height=40)

            # Load the face scan image
            facescan_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\facescan (2).jpg")
            facescan_img = facescan_img.resize((220, 220), Image.LANCZOS)
            self.facescan_photoimg = ImageTk.PhotoImage(facescan_img)

            # Create and place the face scan button
            b2 = Button(self.root, image=self.facescan_photoimg, cursor='hand2',command=self.face_data)
            b2.place(x=500, y=100, width=220, height=220)

            b2_1 = Button(self.root, text="RECOGNIZE ME", cursor='hand2',command=self.face_data ,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
            b2_1.place(x=500, y=310, width=220, height=40)

            # Load the attendance face image
            attendance_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\Student Panel (3).jpg")
            attendance_img = attendance_img.resize((220, 220), Image.LANCZOS)
            self.attendance_photoimg = ImageTk.PhotoImage(attendance_img)

            # Create and place the attendance face button
            b3 = Button(self.root, image=self.attendance_photoimg, cursor='hand2')
            b3.place(x=800, y=100, width=220, height=220)

            b3_1 = Button(self.root, text=" TAKE MY ATTENDANCE", cursor='hand2',command=self.attendance_data, font=("times new roman", 13, "bold"), bg="darkblue", fg="white")
            b3_1.place(x=800, y=310, width=220, height=40)
              
              
            # Load the help image
            help_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\Student Panel (4).jpg")
            help_img = help_img.resize((220, 220), Image.LANCZOS)
            self.help_photoimg = ImageTk.PhotoImage(help_img)

            # Create and place the help button
            b4 = Button(self.root, image=self.help_photoimg, cursor='hand2',command=self.help_data)
            b4.place(x=1100, y=100, width=220, height=220)

            b4_1 = Button(self.root, text="HELP", cursor='hand2',command=self.help_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
            b4_1.place(x=1100, y=310, width=220, height=40)


            

              ################  # Load the photos image
            photos_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\Student Panel (12).jpg")
            photos_img = photos_img.resize((220, 220), Image.LANCZOS)
            self.photos_photoimg = ImageTk.PhotoImage(photos_img)

            # Create and place the photos button
            b6 = Button(self.root, image=self.photos_photoimg, cursor='hand2',command=self.check_admin_password_photos)
            b6.place(x=500, y=380, width=220, height=220)

            b6_1 = Button(self.root, text="STUDENT PHOTOS", cursor='hand2',command=self.check_admin_password_photos, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
            b6_1.place(x=500, y=560, width=220, height=40)
            
              ################  # Load the developer image
            dev_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\Student Panel (9).jpg")
            dev_img = dev_img.resize((220, 220), Image.LANCZOS)
            self.dev_photoimg = ImageTk.PhotoImage(dev_img)

            # Create and place the developer button
            b7 = Button(self.root, image=self.dev_photoimg, cursor='hand2')
            b7.place(x=800, y=380, width=220, height=220)

            b7_1 = Button(self.root, text="DEVELOPER", cursor='hand2',command=self.developer_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
            b7_1.place(x=800, y=560, width=220, height=40)
            
            #############student panel####
            
            studentpanel_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\Student Panel.jpg")
            studentpanel_img = studentpanel_img.resize((220, 220), Image.LANCZOS)
            self.studentpanel_photoimg = ImageTk.PhotoImage(studentpanel_img)

            # Create and place the studentpanel button
            b9 = Button(self.root, image=self.studentpanel_photoimg, cursor='hand2')
            b9.place(x=200, y=100, width=220, height=220)

            b9_1 = Button(self.root, text="STUDENT PANEL", cursor='hand2',command=self.studentpanel, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
            b9_1.place(x=200, y=300, width=220, height=40)
            

             ################  # Load the exit image
            exit_img = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\Student Panel (10).jpg")
            exit_img = exit_img.resize((220, 220), Image.LANCZOS)
            self.exit_photoimg = ImageTk.PhotoImage(exit_img)

            # Create and place the help button
            b8 = Button(self.root, image=self.exit_photoimg, cursor='hand2',command=self.iExit)
            b8.place(x=1100, y=380, width=220, height=220)

            b8_1 = Button(self.root, text="EXIT", cursor='hand2',command=self.iExit, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
            b8_1.place(x=1100, y=560, width=220, height=40)
        except Exception as e:
            print("Error:", e)    
    def open_img(self):
        os.startfile(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\data")      
    def iExit(self):
        self.iExit= messagebox.askyesno ("Face Recognition", "Are you sure exit this project",parent=self.root)
        if self.iExit:
           self.root.destroy()
        else:
            return      
        
        
        
    def check_admin_password(self):
        password = askstring("Password", "Enter admin password:")
        if password == self.admin_password:
            self.student_details()
        else:
            messagebox.showerror("Error", "Incorrect password!")

    def check_admin_password_photos(self):
        password = askstring("Password", "Enter admin password:")
        if password == self.admin_password:
            self.open_img()
        else:
            messagebox.showerror("Error", "Incorrect password!")

    #=========function buttons===================
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Admin(self.new_window)     
    def train_data (self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)  
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=FaceRecognition(self.new_window)    
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=TAKEATTENDANCE(self.new_window)    
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)    
    
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)        
    def studentpanel(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)  
           
           
           
           
           
           
           
            







     
   
                  
            
                       

if __name__ == "__main__":
    main()
