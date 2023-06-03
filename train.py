from tkinter import* 
from tkinter import ttk 
from PIL import Image, ImageTk 
from tkinter import messagebox 
import mysql.connector 
import cv2 
import os 
import numpy as np 

class face_train:
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition based attendance System") 

        #title 
        title_lbl = Label(self.root, text="DATASET TRAINING", font=("arial", 25, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45) 

        #button 
        b1_2 = Button(self.root, text="press here to start training", command=self.train_classifier, cursor="hand2", font=("arial", 15, "bold"), bg="skyblue", fg="black")
        b1_2.place(x=400, y=250, width=450, height=40)  


    def train_classifier(self): 
        data_dir = ("data") 
        path = [ os.path.join(data_dir, file) for file in os.listdir(data_dir)] 

        faces = []
        ids = [] 

        for image in path:
            img=Image.open(image).convert('L')      #Gray scale image 
            imageNp = np.array(img, 'uint8') 
            id=int(os.path.split(image)[1].split('.')[1]) 

            faces.append(imageNp) 
            ids.append(id)
             
            cv2.imshow("Training", imageNp) 
            cv2.waitKey(1)==13 
        ids=np.array(ids) 

        #============= Training classifier and sasve ==================== 
        clf = cv2.face.LBPHFaceRecognizer_create() 
        # clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids) 
        clf.write("classifier.xml") 
        cv2.destroyAllWindows() 
        messagebox.showinfo("Results", "dataset training completed!!!")


if __name__ == "__main__":
    root = Tk()
    obj = face_train(root)
    root.mainloop() 