from tkinter import* 
from tkinter import ttk 
from PIL import Image, ImageTk 
from tkinter import messagebox 
import mysql.connector 
from time import strftime 
from datetime import datetime 
import cv2 
import os 
import numpy as np 

class Face_Recognition:
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition based attendance System")  

        #title 
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("arial", 25, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45) 

        #button 
        b1_2 = Button(self.root, text="press here to recognize face!", command=self.face_recog, cursor="hand2", font=("arial", 15, "bold"), bg="skyblue", fg="black")
        b1_2.place(x=400, y=250, width=450, height=40)  


    #==================== attendance ===================== 
    def mark_attendance(self, i, r, n, d): 
        with open("attendence.csv", "r+", newline="\n") as f:
            myDataList = f.readlines() 
            name_list=[] 
            for line in myDataList: 
                entry=line.split((",")) 
                name_list.append(entry[0]) 
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)): 
                now = datetime.now() 
                d1 = now.strftime("%d/%m/%Y") 
                dtString = now.strftime("%H:%M:%S") 
                f.writelines(f"\n {i}, {r}, {n}, {d}, {dtString}, {d1}, Present") 




    #================ Face recognition ============ 
    def face_recog(self): 
        def draw_boundry(img, classifier, scaleFactor, minNeighbors, color, text, clf): 
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors) 

            coord =[] 

            for (x,y,w,h) in features: 
                cv2.rectangle(img,(x,y), (x+w, y+h), (0, 255, 0), 3) 
                id, predict = clf.predict(gray_image[y:y+h, x:x+w]) 
                confidence = int((100*(1-predict/300))) 

                conn = mysql.connector.connect(host="localhost", username="root", password="Top0987!", database="autometic_attendance")
                my_cursor= conn.cursor() 

                my_cursor.execute("select Student_name from student where Student_id = " + str(id)) 
                n=my_cursor.fetchone() 
                n="+".join(n) 

                my_cursor.execute("select Roll_number from student where Student_id = " + str(id)) 
                r=my_cursor.fetchone() 
                r="+".join(r) 

                my_cursor.execute("select Dep from student where Student_id = " + str(id)) 
                d=my_cursor.fetchone() 
                d="+".join(d) 

                my_cursor.execute("select Student_id from student where Student_id = " + str(id)) 
                i=my_cursor.fetchone() 
                i="+".join(i) 


                if confidence>77: 
                    cv2.putText(img, f"Id:{i}", (x,y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Roll:{r}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3) 
                    cv2.putText(img, f"Name:{n}", (x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)  
                    cv2.putText(img, f"Department:{d}", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3) 
                    self.mark_attendance(i,r,n,d) 
                else: 
                    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 3) 
                    cv2.putText(img, "Unknown face!", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3) 

                coord=[x,y,w,h] 

            return coord
         
        def recognize(img, clf, faceCascade):
            coord = draw_boundry(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf) 
            return img 
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
        clf=cv2.face.LBPHFaceRecognizer_create()  
        clf.read("classifier.xml") 

        video_cap =cv2.VideoCapture(0) 

        while True: 
            ret, img = video_cap.read() 
            img = recognize(img, clf, faceCascade) 
            cv2.imshow("Welcome to face recognition! ", img) 

            if cv2.waitKey(1)==13: 
                break
        video_cap.release() 
        video_cap.destroyAllWindows()
        #cv2.destroyAllWindows() 








if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop() 