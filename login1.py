from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import tkinter
import tkinter.messagebox
from PIL import Image
from student import STUDENT
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from helpdesk import Help


def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()
    

class Login_window:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        # Load the background image

        img3 = Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\bg1.jpg")
        img3 = img3.resize((1530, 750), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_lbl=Label(self.root,image=self.photoimg3)
        bg_lbl.place(x=0,y=0,width=1530,height=750) 
        
        title=Label(bg_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="white",fg="navy blue")
        title.place(x=0,y=0,width=1530,height=45)
        #self.bg = ImageTk.PhotoImage(file=r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\DEV.png")
    
       # lbl_bg = Label(self.root, image=self.bg)
        #lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

#======project button(description)=======
        downtitle=Label(self.root,text="Note: Enter valid username and valid password ",font=("times new roman",30,"bold"),bg="white",fg="navy blue")
        downtitle.place(x=0,y=740,width=1600,height=35)
        
        # Load and resize another image
        img1 = Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\log.png")
        img1 = img1.resize((100,100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)
        
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)
        
        
        # label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
      
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)
        
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        
        #=======icon images========
       
        img2 = Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\log.png")
        img2 = img2.resize((25,25), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=650, y=323, width=25, height=25)
        
        
        img3 = Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\pp.jpeg")
        img3 = img3.resize((25,25), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=650, y=395, width=25, height=25)
        
        #loginButton
        
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        #registerButton
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)
        
        #forgetpassbtn
        forgetpassbtn=Button(frame,text="Forget password",font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetpassbtn.place(x=10,y=390,width=160)
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
            
    def login(self):    
        if self.txtuser.get()=="" or self.txtpass.get()== "":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="Nikita" and self.txtpass.get()=="N2034":
            messagebox.showinfo("Success","welcome to my page")
        else:
           conn=mysql.connector.connect(host="localhost",user="root",password="Shiwani@123",database="mydata") 
           cur=conn.cursor()
           cur.execute("select * from register where email=%s and password=%s",(
                
                                                                             self.txtuser.get(),
                                                                             self.txtpass.get()
                                                                                     ))
        row= cur.fetchone()
        
        #print (row)
        
        if row==None:
                messagebox.showerror("Error","Invalid Username & password")
        else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.new_window)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                     if not open_main:
                          return
        conn.commit()
        conn.close()
        
                    
    #=======  Register page     
            
            
class Register:
    def __init__ (self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        #==============varibles============
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        
        #=========bg image=============
        img3 = Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\bg1.jpg")
        img3 = img3.resize((1530, 750), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_lbl=Label(self.root,image=self.photoimg3)
        bg_lbl.place(x=0,y=0,width=1530,height=750) 
        
        title=Label(bg_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="white",fg="navy blue")
        title.place(x=0,y=0,width=1530,height=45)
    
        
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        #======project button(description)=======
        downtitle=Label(self.root,text="Note: Enter your correct information ",font=("times new roman",30,"bold"),bg="white",fg="navy blue")
        downtitle.place(x=0,y=740,width=1600,height=35)
        
        
        #=========left image=========
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\R_image.jpeg")
        
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)
        
       #========main frame=============
        frame = Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("timews new romen",20,"bold"),fg="darkgreen")
        register_lbl.place(x=20,y=20)
        
        #========lable and entry=======
        
        #=========row1=================
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)
        
        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)
        
        #=========row2=================
        
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)
        
        #===============row3==================
        
        security_Q=Label(frame,text=" Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        
        
        security_A=Label(frame,text=" Select Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)
        
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)
        
        
        #===========row4===========
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)
        
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)
        
        #===========checkbutton============
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Term & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)
        
        #==========buttons=================
        img=Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\register button.jpeg")
        img=img.resize((180,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self. register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=60,y=420,width=180)
        
        img1=Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\login button.jpeg")
        img1=img1.resize((180,50),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=380,y=420,width=180)
        
        
        #============function declaration===========
        
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Shiwani@123",database="mydata") 
            cur=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            cur.execute(query,value)  # Corrected method call
            row=cur.fetchone()  # Corrected variable name
            if row!=None:
                messagebox.showerror("Error","User already exists, please try another email")
            else:
                cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                     self.var_fname.get(),
                                                                                     self.var_lname.get(),
                                                                                     self.var_contact.get(),
                                                                                     self.var_email.get(),
                                                                                     self.var_securityQ.get(),
                                                                                     self.var_securityA.get(),
                                                                                     self.var_pass.get()
                                                                                
                                                                                  ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Registered Successfully")    
      #====main page========           
                
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
  main()