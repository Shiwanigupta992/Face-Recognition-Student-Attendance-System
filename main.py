from tkinter import*
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image
from PIL import Image,ImageTk
from student import STUDENT
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from helpdesk import Help

class Face_Recognition_System:
    
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        img=Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\bg3.jpg")
        img = img.resize((800, 130), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=130)

        img1=Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\f29.jpg")
        img1 = img1.resize((730, 130), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=730,height=130)
         
        
        
        
        # BAGROUND IMAGE:
        img3=Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\bg1.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimge3=ImageTk.PhotoImage(img3)
        
        bg_lbl=Label(self.root,image=self.photoimge3)
        bg_lbl.place(x=0,y=130,width=1530,height=710) 
        
        
        title_lbl=Label(bg_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="white",fg="navy blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        # STUDENT BUTTON  ------
        
        img4=Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\student-icon-10.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimge4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_lbl,image=self.photoimge4,command=self.student_details,cursor="hand2")
        b1.place(x=280,y=100,width=220,height=220)
        
        b1_1=Button(bg_lbl,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="navy blue")
        b1_1.place(x=280,y=300,width=220,height=40)
        
        # DETECT FACE BUTTON  ------
        
        img5=Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\face d.jpeg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimge5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_lbl,image=self.photoimge5,cursor="hand2",command=self.face_data)
        b1.place(x=530,y=100,width=220,height=220)
        
        b1_1=Button(bg_lbl,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="white",fg="navy blue")
        b1_1.place(x=530,y=300,width=220,height=40)
        
        
        #Attendance Face Button-----
        
        img6=Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\attendence.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimge6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_lbl,image=self.photoimge6,cursor="hand2", command=self.attendance_data)
        b1.place(x=780,y=100,width=220,height=220)
        
        b1_1=Button(bg_lbl,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="white",fg="navy blue")
        b1_1.place(x=780,y=300,width=220,height=40)
        
        #help face button---------
        img7=Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\help.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimge7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_lbl,image=self.photoimge7,cursor="hand2",command=self.help_desk)
        b1.place(x=1030,y=100,width=220,height=220)
        
        b1_1=Button(bg_lbl,text="Help Desk",cursor="hand2",command=self.help_desk,font=("times new roman",15,"bold"),bg="white",fg="navy blue")
        b1_1.place(x=1030,y=300,width=220,height=40)
        
        
        # Train face button------
        
        img8=Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\train data.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimge8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_lbl,image=self.photoimge8,cursor="hand2",command=self.train_data)
        b1.place(x=280,y=360,width=220,height=220)
        
        b1_1=Button(bg_lbl,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="white",fg="navy blue")
        b1_1.place(x=280,y=560,width=220,height=40)
        
        # Photos button----
        
        img9=Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\photos.jpg")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimge9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_lbl,image=self.photoimge9,cursor="hand2",command=self.open_img)
        b1.place(x=530,y=360,width=220,height=220)
        
        b1_1=Button(bg_lbl,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="navy blue")
        b1_1.place(x=530,y=560,width=220,height=40)
        
        # Developer button-------
        
        img10=Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\Women-in-Tech.jpg")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimge10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_lbl,image=self.photoimge10,cursor="hand2",command=self.develop_data)
        b1.place(x=780,y=360,width=220,height=220)
        
        b1_1=Button(bg_lbl,text="Developer",cursor="hand2",command=self.develop_data,font=("times new roman",15,"bold"),bg="white",fg="navy blue")
        b1_1.place(x=780,y=560,width=220,height=40)
        
        # Exit button-----
        
        img11=Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\exit-icon.jpg")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimge11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_lbl,image=self.photoimge11,cursor="hand2", command=self.iExit)
        b1.place(x=1030,y=360,width=220,height=220)
        
        b1_1=Button(bg_lbl,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="white",fg="navy blue")
        b1_1.place(x=1030,y=560,width=220,height=40)


    def open_img(self):
          os.startfile("data")

    def iExit(self):
         self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
         if self.iExit>0:
              self.root.destroy()
         else: 
               return     
          
        #......................function button........
    def student_details(self):
            self.new_window = Toplevel(self.root)
            self.app = STUDENT(self.new_window)

    def train_data(self):
            self.new_window = Toplevel(self.root)
            self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
    
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def develop_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_desk(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    


    

if __name__ == "__main__":
       root=Tk()
       obj=Face_Recognition_System(root)
       root.mainloop()
    
