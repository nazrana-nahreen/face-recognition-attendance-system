import tkinter as tk
from tkinter import Button, Label
import cv2
import numpy as np
from datetime import datetime
import face_recognition
from PIL import Image, ImageTk
import mysql.connector

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="#A52A2A", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_bottom = Image.open(r"C:\Users\DELL\Desktop\newFace Recognition, Student Attendance System\images\FACERECOG.jpg")
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
        b1_1 = Button(f_lbl, text="RECOGNIZE ME", cursor="hand2", command=self.face_recog, font=("times new roman", 30, "bold"), bg="#A52A2A", fg="white")
        b1_1.place(x=520, y=600, width=500, height=60)
        # Bind the <Return> event to close the window
        

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

        video_capture = cv2.VideoCapture(0)

        while True:
            _, frame = video_capture.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

            # Recognize faces
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distance)

                if matches[best_match_index]:
                    student_id = known_face_names[best_match_index]

                    # Fetch additional information from the database based on student ID
                    self.cursor.execute("SELECT name, department, passkey FROM student WHERE student_id = %s", (student_id,))
                    student_info = self.cursor.fetchone()

                    if student_info:
                        name, department, passkey = student_info

                        # Construct the formatted text with proper line breaks
                        info_text = f"Name: {name}\nDepartment: {department}\nPasskey: {passkey}"

                        # Draw a rectangle around the detected face
                        cv2.rectangle(frame, (left * 4, top * 4), (right * 4, bottom * 4), (0, 255, 0), 2)

                        # Calculate the position for displaying text below the rectangle
                        text_position = (left * 4, bottom * 4 + 20)

                        # Add the text if a person is present
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        font_scale = 0.8
                        font_color = (255, 255, 255)
                        thickness = 2

                        # Split the info_text into lines and draw each line separately
                        lines = info_text.split('\n')
                        for i, line in enumerate(lines):
                            cv2.putText(frame, line, (text_position[0], text_position[1] + i*30), font, font_scale, font_color, thickness)

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
    obj = FaceRecognition(root)
    root.mainloop()
    
   
