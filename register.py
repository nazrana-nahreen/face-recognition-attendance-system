from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
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

            b1 = Button(main_frame, image=self.photoimage1, borderwidth=0, cursor="hand2")  
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
                   

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
