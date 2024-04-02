import tkinter as tk
from tkinter import Button, Label
import cv2
import numpy as np
import csv
from datetime import datetime
import face_recognition
from PIL import Image, ImageTk
import mysql.connector

class TAKEATTENDANCE:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TAKE MY ATTENDANCE", font=("times new roman", 35, "bold"), bg="#A52A2A", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_bottom = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\attendance (2).jpg")
        img_bottom = img_bottom.resize((1538, 790), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=45, width=1538, height=790)

        # Establish connection with MySQL database
        self.connection = mysql.connector.connect(
            host="localhost",
            username="root",
            password="nazrana2028@",
            database="face_recognizer",
        )
        self.cursor = self.connection.cursor()

        # Specify student IDs and corresponding image paths
        self.student_data = {
            1: r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\data\user.1.1.jpg",
            2: r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\data\user.2.1.jpg",
            3: r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\data\user.3.1.jpg",
        }

        # Button
        b1_1 = Button(f_lbl, text="I am present", cursor="hand2", command=self.face_recog, font=("times new roman", 30, "bold"), bg="green", fg="white")
        b1_1.place(x=600, y=600, width=300, height=60)

    # Face recognition method
    def face_recog(self):
        known_face_encodings = []
        known_face_names = []

        # Load known faces and their IDs from the specified student data
        for student_id, image_path in self.student_data.items():
            student_image = face_recognition.load_image_file(image_path)
            student_encoding = face_recognition.face_encodings(student_image)[0]
            known_face_encodings.append(student_encoding)
            known_face_names.append(student_id)

   

        # Open the CSV file in append mode
        with open("attendance.csv", "a", newline="") as f:
            lnwriter = csv.writer(f)

            # Write column names if the file is empty
            if f.tell() == 0:
                lnwriter.writerow(["Date", "Time", "Name", "Student ID", "Department", "Passkey", "Semester"])

            # Get the current date
            now = datetime.now()
            current_date = now.strftime("%d-%m-%Y")
            

            video_capture = cv2.VideoCapture(0)
            attendance_recorded = False  # Flag to track whether attendance has been recorded

            while True:
                _, frame = video_capture.read()
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

                # Recognize faces
                face_locations = face_recognition.face_locations(rgb_small_frame)

                for (top, right, bottom, left) in face_locations:
                    face_encoding = face_recognition.face_encodings(rgb_small_frame, [(top, right, bottom, left)])[0]
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distance)

                    if matches[best_match_index] and not attendance_recorded:
                        student_id = known_face_names[best_match_index]

                        # Fetch additional information from the database based on student ID
                        self.cursor.execute("SELECT name, department, passkey,semester FROM student WHERE student_id = %s", (student_id,))
                        student_info = self.cursor.fetchone()

                        if student_info:
                            name, department, passkey,semester = student_info

                            # Log attendance
                            current_time = now.strftime("%H:%M:%S")
                            lnwriter.writerow([current_date, current_time, name, student_id, department, passkey, semester])

                            attendance_recorded = True  # Set the flag to True after recording attendance

                cv2.imshow("Camera", frame)
                key = cv2.waitKey(1)
                if key == ord("q"):
                    break
                elif key == 13:  # Enter key
                    break

            video_capture.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    obj = TAKEATTENDANCE(root)
    root.mainloop()