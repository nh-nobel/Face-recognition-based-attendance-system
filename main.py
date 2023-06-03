from tkinter import* 
from tkinter import ttk 
from PIL import Image, ImageTk 
from students import Student 
import os 
from train import face_train 
from face_recognition import Face_Recognition 


class face_recognition_system:
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition based attendance System") 

        #first image
        img = Image.open(r"G:\nobel\Uni\23\Automatic attendance 1\college_images\images.jfif")
        img = img.resize((500,130), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=500, height=130)

        #second image
        img2 = Image.open(r"G:\nobel\Uni\23\Automatic attendance 1\college_images\nature.jpg")
        img2 = img2.resize((500,130), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=500, height=130)   


        #third image
        img3 = Image.open(r"G:\nobel\Uni\23\Automatic attendance 1\college_images\sunrise.jpg")
        img3 = img3.resize((500,130), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width=500, height=130)


        #background image
        img4 = Image.open(r"G:\nobel\Uni\23\Automatic attendance 1\college_images\class.jfif")
        img4 = img4.resize((1530,710), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4) 

        bg_img=Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)


        #title 
        title_lbl = Label(bg_img, text="AUTOMATIC ATTENDANCE TAKING FROM FACE RECOGNITION.", font=("arial", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #students button 
        img5 = Image.open(r"G:\nobel\Uni\23\Automatic attendance 1\college_images\students_button.png")
        img5 = img5.resize((150, 150), Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5) 

        b1 = Button(bg_img, image=self.photoimg5, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=150, height=150) 

        b1_2 = Button(bg_img, text="STUDENT DETAILS", command=self.student_details, cursor="hand2", font=("arial", 10, "bold"), bg="skyblue", fg="white")
        b1_2.place(x=200, y=250, width=150, height=40) 


        #face detection button 
        img6 = Image.open(r"G:\nobel\Uni\23\Automatic attendance 1\college_images\face_detect.jpg")
        img6 = img6.resize((150, 150), Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6) 

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.face_data)
        b1.place(x=500, y=100, width=150, height=150) 

        b1_2 = Button(bg_img, text="FACE DETECTOR", cursor="hand2", command=self.face_data, font=("arial", 10, "bold"), bg="skyblue", fg="white")
        b1_2.place(x=500, y=250, width=150, height=40)


        #attendance face button 
        img7 = Image.open(r"G:\nobel\Uni\23\Automatic attendance 1\college_images\face_detect.jpg")
        img7 = img7.resize((150, 150), Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7) 

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b1.place(x=800, y=100, width=150, height=150) 

        b1_2 = Button(bg_img, text="ATTENDANCE BUTTON", cursor="hand2", font=("arial", 10, "bold"), bg="skyblue", fg="white")
        b1_2.place(x=800, y=250, width=150, height=40)


        #help face button 
        img8 = Image.open(r"G:\nobel\Uni\23\Automatic attendance 1\college_images\face_detect.jpg")
        img8 = img8.resize((150, 150), Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8) 

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        b1.place(x=1100, y=100, width=150, height=150) 

        b1_2 = Button(bg_img, text="HELP", cursor="hand2", font=("arial", 10, "bold"), bg="skyblue", fg="white")
        b1_2.place(x=1100, y=250, width=150, height=40) 


        #train face button 
        img9 = Image.open(r"G:\nobel\Uni\23\Automatic attendance 1\college_images\face_detect.jpg")
        img9 = img9.resize((150, 150), Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9) 

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.train_data)
        b1.place(x=200, y=350, width=150, height=150) 

        b1_2 = Button(bg_img, text="TRAIN DATA", cursor="hand2", command=self.train_data, font=("arial", 15, "bold"), bg="skyblue", fg="white")
        b1_2.place(x=200, y=500, width=150, height=40)


        #photos face button 
        img10 = Image.open(r"G:\nobel\Uni\23\Automatic attendance 1\college_images\face_detect.jpg")
        img10 = img10.resize((150, 150), Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10) 

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.open_img)
        b1.place(x=500, y=350, width=150, height=150) 

        b1_2 = Button(bg_img, text="PHOTOS", cursor="hand2", command=self.open_img, font=("arial", 15, "bold"), bg="skyblue", fg="white")
        b1_2.place(x=500, y=500, width=150, height=40) 


        #developer face button 
        img11 = Image.open(r"G:\nobel\Uni\23\Automatic attendance 1\college_images\face_detect.jpg")
        img11 = img11.resize((150, 150), Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11) 

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b1.place(x=800, y=350, width=150, height=150) 

        b1_2 = Button(bg_img, text="DEVELOPER", cursor="hand2", font=("arial", 15, "bold"), bg="skyblue", fg="white")
        b1_2.place(x=800, y=500, width=150, height=40)


        #EXIT face button 
        img12 = Image.open(r"G:\nobel\Uni\23\Automatic attendance 1\college_images\face_detect.jpg")
        img12 = img12.resize((150, 150), Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12) 

        b1 = Button(bg_img, image=self.photoimg12, cursor="hand2")
        b1.place(x=1100, y=350, width=150, height=150) 

        b1_2 = Button(bg_img, text="EXIT", cursor="hand2", font=("arial", 15, "bold"), bg="skyblue", fg="white")
        b1_2.place(x=1100, y=500, width=150, height=40) 

    def open_img(self): 
        os.startfile("data") 

        #=================== Functions button ==================== 
    def student_details(self):
        self.new_window=Toplevel(self.root) 
        self.app = Student(self.new_window) 

    def train_data(self):
        self.new_window=Toplevel(self.root) 
        self.app = face_train(self.new_window) 

    def face_data(self):
        self.new_window=Toplevel(self.root) 
        self.app = Face_Recognition(self.new_window) 





if __name__ == "__main__":
    root = Tk()
    obj = face_recognition_system(root)
    root.mainloop() 
