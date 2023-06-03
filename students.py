from tkinter import* 
from tkinter import ttk 
from PIL import Image, ImageTk 
from tkinter import messagebox 
import mysql.connector 
import cv2 
import os 
import numpy as np 

class Student:
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition based attendance System") 

        #============= variables =============== 
        self.var_dep = StringVar() 
        self.var_course = StringVar() 
        self.var_year = StringVar() 
        self.var_semesetr = StringVar() 
        self.var_std_id = StringVar() 
        self.var_std_name = StringVar() 
        self.var_division = StringVar() 
        self.var_roll_num = StringVar() 
        self.var_gender = StringVar() 
        self.var_dob = StringVar() 
        self.var_email = StringVar()
        self.var_phone = StringVar() 
        self.var_address = StringVar() 
        self.var_teacher_name =StringVar() 
        #self.var_radio1 = StringVar()
        #self.var_radio2 = StringVar()

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
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("arial", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45) 

        main_frame=Frame(bg_img, bd=2)
        main_frame.place(x=5, y=55, width=1350, height=510)

        #left frame 
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="STUDENT DETAILS", font=("aial", 12, "bold"))
        Left_frame.place(x=10, y=10, width=650, height=485) 

        img_left = Image.open(r"G:\nobel\Uni\23\Automatic attendance 1\college_images\sunrise.jpg")
        img_left = img_left.resize((500,130), Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=640, height=130) 

        #current courses 
        current_course_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="CURRENT COURSE INFORMATION", font=("aial", 12, "bold"))
        current_course_frame.place(x=15, y=135, width=640, height=105) 

        #department 
        dep_label = Label(current_course_frame, text="DEPARTMENT", font=("aial", 11, "bold"))
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep ,font=("aial", 11, "bold"), state="readonly")
        dep_combo["values"]=("Select department", "ECE", "BBA", "Law", "Math")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)


        #courses
        course_label = Label(current_course_frame, text="COURSES", font=("aial", 11, "bold"))
        course_label.grid(row=0, column=2, padx=10)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("aial", 11, "bold"), state="readonly")
        course_combo["values"]=("Select course", "CSE115", "CSE215", "CSE225", "MAT120")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W) 


        #year 
        year_label = Label(current_course_frame, text="Year", font=("aial", 11, "bold"))
        year_label.grid(row=1, column=0, padx=10)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("aial", 11, "bold"), state="readonly")
        year_combo["values"]=("Select Year", "2023", "2024", "2025", "2026")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W) 


        #semester 
        semester_label = Label(current_course_frame, text="Semester", font=("aial", 11, "bold"))
        semester_label.grid(row=1, column=2, padx=10)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semesetr, font=("aial", 11, "bold"), state="readonly")
        semester_combo["values"]=("Select Semester", "Spring22", "Fall22", "Spring23", "Fall23")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W) 

        #class student information 
        class_student_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="CURRENT COURSE INFORMATION", font=("aial", 12, "bold"))
        class_student_frame.place(x=15, y=250, width=640, height=240) 

        #student id 
        student_id_label = Label(class_student_frame, text="STUDENT ID: ", font=("aial", 10, "bold"))
        student_id_label.grid(row=0, column=0, padx=10, sticky=W) 

        student_id_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=("aial", 10, "bold"))
        student_id_entry.grid(row=0, column=1, padx=10, sticky=W)

        #student name 
        student_name_label = Label(class_student_frame, text="STUDENT name: ", font=("aial", 10, "bold"))
        student_name_label.grid(row=0, column=2, padx=10, sticky=W) 

        student_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20, font=("aial", 10, "bold"))
        student_name_entry.grid(row=0, column=3, padx=10, sticky=W)

        ## class di vision 
        class_division_label = Label(class_student_frame, text="CLASS DIVISION: ", font=("aial", 10, "bold"))
        class_division_label.grid(row=1, column=0, padx=10, sticky=W) 

        #class_division_entry = ttk.Entry(class_student_frame, textvariable=self.var_division, width=20, font=("aial", 10, "bold"))
        #class_division_entry.grid(row=1, column=1, padx=10, sticky=W) 
        division_combo = ttk.Combobox(class_student_frame, textvariable=self.var_division, font=("aial", 10, "bold"), state="readonly")
        division_combo["values"]=("Select division","A", "B", "C", "D", "E", "F", "G", "H")
        division_combo.current(0)
        division_combo.grid(row=1, column=1, padx=10, sticky=W) 

        #roll number 
        roll_number_label = Label(class_student_frame, text="ROLL NUMBER: ", font=("aial", 10, "bold"))
        roll_number_label.grid(row=1, column=2, padx=10, sticky=W) 

        roll_number_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll_num, width=20, font=("aial", 10, "bold"))
        roll_number_entry.grid(row=1, column=3, padx=10, sticky=W)

        #gender 
        gender_label = Label(class_student_frame, text="GENDER: ", font=("aial", 10, "bold"))
        gender_label.grid(row=2, column=0, padx=10, sticky=W) 

        #gender_entry = ttk.Entry(class_student_frame, textvariable=self.var_gender, width=20, font=("aial", 10, "bold"))
        #gender_entry.grid(row=2, column=1, padx=10, sticky=W) 
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("aial", 10, "bold"), state="readonly")
        gender_combo["values"]=("Select gender","Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, sticky=W) 

        #darte of birth
        dob_label = Label(class_student_frame, text="DATE OF BIRTH: ", font=("aial", 10, "bold"))
        dob_label.grid(row=2, column=2, padx=10, sticky=W) 

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=("aial", 10, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, sticky=W) 

        #email ///////////////
        email_label = Label(class_student_frame, text="EMAIL: ", font=("aial", 10, "bold"))
        email_label.grid(row=3, column=0, padx=10, sticky=W) 

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("aial", 10, "bold"))
        email_entry.grid(row=3, column=1, padx=10, sticky=W)

        #phone number 
        phone_number_label = Label(class_student_frame, text="PHONE NUMBER: ", font=("aial", 10, "bold"))
        phone_number_label.grid(row=3, column=2, padx=10, sticky=W) 

        phone_number_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=("aial", 10, "bold"))
        phone_number_entry.grid(row=3, column=3, padx=10, sticky=W) 

        #address/////////
        address_label = Label(class_student_frame, text="Address: ", font=("aial", 10, "bold"))
        address_label.grid(row=4, column=0, padx=10, sticky=W) 

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=("aial", 10, "bold"))
        address_entry.grid(row=4, column=1, padx=10, sticky=W)

        #teacher name 
        teacher_name_label = Label(class_student_frame, text="Teacher's name: ", font=("aial", 10, "bold"))
        teacher_name_label.grid(row=4, column=2, padx=10, sticky=W) 

        teacher_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher_name, width=20, font=("aial", 10, "bold"))
        teacher_name_entry.grid(row=4, column=3, padx=10, sticky=W) 

        #radio buttons 
        self.var_radio1 = StringVar()
        rdobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take photo sample", value="Yes") 
        rdobtn1.grid(row=6, column=0)

        rdobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No photo sample", value="No") 
        rdobtn2.grid(row=6, column=1) 

        #button frame 
        btnfrm = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btnfrm.place(x=0, y=130, width=635, height=85) 

        save_btn = Button(btnfrm, text="Save", command=self.add_data, width=18, font=("aial", 10, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btnfrm, text="Update", command=self.update_data, width=18, font=("aial", 10, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btnfrm, text="Delete", command=self.delete_data, width=18, font=("aial", 10, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btnfrm, text="Reset", command=self.reset_data, width=18, font=("aial", 10, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        take_a_photo_btn = Button(btnfrm, text="Take photo sample", command=self.generate_dataset, width=18, font=("aial", 10, "bold"), bg="blue", fg="white")
        take_a_photo_btn.grid(row=1, column=0)

        update_photo_sample_btn = Button(btnfrm, text="Update photo sample", width=18, font=("aial", 10, "bold"), bg="blue", fg="white")
        update_photo_sample_btn.grid(row=1, column=1)




        #right frame 
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, font=("aial", 12, "bold"))
        Left_frame.place(x=680, y=10, width=650, height=485) 

        # img_right = Image.open(r"G:\nobel\Uni\23\Automatic attendance 1\college_images\sunrise.jpg")
        # img_right = img_right.resize((500,130), Image.ANTIALIAS)
        # self.photoimg_right=ImageTk.PhotoImage(img_right)

        # f_lbl=Label(Left_frame, image=self.photoimg_right)
        # f_lbl.place(x=5, y=0, width=640, height=130)

        #=========== Search System ================
        search_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="SYSTEM SEARCH", font=("aial", 12, "bold")) 
        search_frame.place(x=5, y=5, width=635, height=70) 

        search_label = Label(search_frame, text="Search by: ", font=("aial", 10, "bold"), bg="skyblue", fg="black")
        search_label.grid(row=0, column=0, padx=10, sticky=W) 

        search_combo = ttk.Combobox(search_frame, font=("aial", 11, "bold"), state="readonly")
        search_combo["values"]=("Select", "ID", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W) 

        search_btn = Button(search_frame, text="Search", width=18, font=("aial", 10, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=2)

        search_btn = Button(search_frame, text="Show All", width=18, font=("aial", 10, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3) 


        #================= Table frame ================ 
        table_frame = Frame(Left_frame, bd=2, relief=RIDGE) 
        table_frame.place(x=5, y=80, width=635, height=250) 

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient= VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll_num", "gender", "dob", "email", "phone", "address", "teacher", "photo")) 

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y) 
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course") 
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="ID")
        self.student_table.heading("name", text="Name") 
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll_num", text="Roll number")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="Date of Birth")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo")

        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH, expand=1) 
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data() 

    #=================== function declaration ===============
    def add_data(self): 
        if self.var_dep.get()=="Select department" or self.var_std_name.get()=="" or self.var_std_id.get()=="": 
            messagebox.showerror("Error", "All feild are required.", parent=self.root) 
        else: 
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Top0987!", database="autometic_attendance")
                my_cursor= conn.cursor() 
                my_cursor.execute("insert into student values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                                                                                                                                self.var_dep.get(), 
                                                                                                                                self.var_course.get(), 
                                                                                                                                self.var_year.get(), 
                                                                                                                                self.var_semesetr.get(), 
                                                                                                                                self.var_std_id.get(), 
                                                                                                                                self.var_std_name.get(), 
                                                                                                                                self.var_division.get(), 
                                                                                                                                self.var_roll_num.get(), 
                                                                                                                                self.var_gender.get(), 
                                                                                                                                self.var_dob.get(), 
                                                                                                                                self.var_email.get(),
                                                                                                                                self.var_phone.get(), 
                                                                                                                                self.var_address.get(), 
                                                                                                                                self.var_teacher_name.get(), 
                                                                                                                                self.var_radio1.get() 
                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("Success", "Student details hase been added successfully.", parent=self.root) 

            except Exception as es: 
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root) 

    #========================== fetch data ========================== 
    def fetch_data(self): 
        conn = mysql.connector.connect(host="localhost", username="root", password="Top0987!", database="autometic_attendance") 
        my_cursor= conn.cursor() 
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data: 
                self.student_table.insert("", END, values=i)
            conn.commit() 
        conn.close() 

    #========================= get cursor========================== 
    def get_cursor(self, event=""): 
        cursor_focus = self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0]) 
        self.var_course.set(data[1]) 
        self.var_year.set(data[2]) 
        self.var_semesetr.set(data[3]) 
        self.var_std_id.set(data[4]) 
        self.var_std_name.set(data[5]) 
        self.var_division.set(data[6]) 
        self.var_roll_num.set(data[7]) 
        self.var_gender.set(data[8]) 
        self.var_dob.set(data[9]) 
        self.var_email.set(data[10])
        self.var_phone.set(data[11]) 
        self.var_address.set(data[12]) 
        self.var_teacher_name.set(data[13]) 
        self.var_radio1.set(data[14]) 
    
    #============== update function ===================== 
    def update_data(self): 
        if self.var_dep.get()=="Select department" or self.var_std_name.get()=="" or self.var_std_id.get()=="": 
            messagebox.showerror("Error", "All feild are required.", parent=self.root) 
        else: 
            try: 
                Update=messagebox.askyesno("Update", "Do you want to update this student details.", parent=self.root)
                if Update>0: 
                    conn = mysql.connector.connect(host="localhost", username="root", password="Top0987!", database="autometic_attendance")
                    my_cursor= conn.cursor() 
                    my_cursor.execute("update student set Dep=%s, Course=%s, Year=%s, Semester=%s, Student_name=%s, Division=%s, Roll_number=%s, Student_gender=%s, Date_of_birth=%s, email=%s, Phone=%s, Address=%s, Teacher_name=%s, Photosample=%s where Student_id=%s", (
                                                                                                                                                                                                                                                                                self.var_dep.get(), 
                                                                                                                                                                                                                                                                                self.var_course.get(), 
                                                                                                                                                                                                                                                                                self.var_year.get(), 
                                                                                                                                                                                                                                                                                self.var_semesetr.get(), 
                                                                                                                                                                                                                                                                                self.var_std_name.get(), 
                                                                                                                                                                                                                                                                                self.var_division.get(), 
                                                                                                                                                                                                                                                                                self.var_roll_num.get(), 
                                                                                                                                                                                                                                                                                self.var_gender.get(), 
                                                                                                                                                                                                                                                                                self.var_dob.get(), 
                                                                                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                                                                                self.var_phone.get(), 
                                                                                                                                                                                                                                                                                self.var_address.get(), 
                                                                                                                                                                                                                                                                                self.var_teacher_name.get(), 
                                                                                                                                                                                                                                                                                self.var_radio1.get(), 
                                                                                                                                                                                                                                                                                self.var_std_id.get()
                                                                                                                                                                                                                                                                            ))
                else: 
                    if not Update: 
                        return
                messagebox.showinfo("Success", "Student details successfully updated.", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close() 
            except Exception as es: 
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root) 

    
    #====================== delete data ========================= 
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error", "Student ID must be required.", parent=self.root)
        else: 
            try:
                delete=messagebox.askyesno("Student delete page", "Do you want to delete this student's data?", parent=self.root)
                if delete>0: 
                    conn = mysql.connector.connect(host="localhost", username="root", password="Top0987!", database="autometic_attendance")
                    my_cursor= conn.cursor() 
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else: 
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("Delete", "Successfully deleted student details.", parent=self.root)
            except Exception as es: 
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root) 

    #========================= reset function ======================= 
    def reset_data(self):
        self.var_dep.set("Select department") 
        self.var_course.set("Select course") 
        self.var_year.set("Select Year") 
        self.var_semesetr.set("Select Semester") 
        self.var_std_id.set("") 
        self.var_std_name.set("") 
        self.var_division.set("Select division") 
        self.var_roll_num.set("") 
        self.var_gender.set("Select gender") 
        self.var_dob.set("") 
        self.var_email.set("")
        self.var_phone.set("") 
        self.var_address.set("") 
        self.var_teacher_name.set("") 
        self.var_radio1.set("") 

    #======================= generate dataset / take photo samples ================ 
    def generate_dataset(self):
        if self.var_dep.get()=="Select department" or self.var_std_name.get()=="" or self.var_std_id.get()=="": 
            messagebox.showerror("Error", "All feild are required.", parent=self.root) 
        else: 
            try: 
                conn = mysql.connector.connect(host="localhost", username="root", password="Top0987!", database="autometic_attendance")
                my_cursor= conn.cursor()
                my_cursor.execute("select * from student")
                my_result=my_cursor.fetchall()
                id=0 
                for x in my_result: 
                    id+=1 
                my_cursor.execute("update student set Dep=%s, Course=%s, Year=%s, Semester=%s, Student_name=%s, Division=%s, Roll_number=%s, Student_gender=%s, Date_of_birth=%s, email=%s, Phone=%s, Address=%s, Teacher_name=%s, Photosample=%s where Student_id=%s", (
                                                                                                                                                                                                                                                                                self.var_dep.get(), 
                                                                                                                                                                                                                                                                                self.var_course.get(), 
                                                                                                                                                                                                                                                                                self.var_year.get(), 
                                                                                                                                                                                                                                                                                self.var_semesetr.get(), 
                                                                                                                                                                                                                                                                                self.var_std_name.get(), 
                                                                                                                                                                                                                                                                                self.var_division.get(), 
                                                                                                                                                                                                                                                                                self.var_roll_num.get(), 
                                                                                                                                                                                                                                                                                self.var_gender.get(), 
                                                                                                                                                                                                                                                                                self.var_dob.get(), 
                                                                                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                                                                                self.var_phone.get(), 
                                                                                                                                                                                                                                                                                self.var_address.get(), 
                                                                                                                                                                                                                                                                                self.var_teacher_name.get(), 
                                                                                                                                                                                                                                                                                self.var_radio1.get(), 
                                                                                                                                                                                                                                                                                self.var_std_id.get()==id+1 
                                                                                                                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data() 
                conn.close()
                #========================= Load pre defined data on face frontals opencv ============ 
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 

                def face_cropped(img): 
                    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x,y,w,h) in faces: 
                        face_cropped=img[y:y+h, x:x+w]
                        return face_cropped 
                cap=cv2.VideoCapture(0)
                img_id=0
                while True: 
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None: 
                        img_id += 1 
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY) 
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100: 
                        break 
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating datasets completed.") 
            except Exception as es: 
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root) 

                    












if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop() 
