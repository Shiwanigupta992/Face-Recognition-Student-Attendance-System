from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login")

        img3=Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\bg1.jpg")
        img3 = img3.resize((1530, 780), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_lbl=Label(self.root,image=self.photoimg3)
        bg_lbl.place(x=0,y=0,width=1530,height=780) 

        title=Label(bg_lbl,text="FACE RECOGNITION ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="navy blue")
        title.place(x=0,y=0,width=1530,height=45)

        downtitle=Label(self.root,text="Note: Enter valid username and valid password ",font=("times new roman",30,"bold"),bg="white",fg="navy blue")
        downtitle.place(x=0,y=740,width=1600,height=35)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\log.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100) 

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),bg="black",fg="white")
        username.place(x=70,y=155)
    
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #=======Icon Image=======
        img2=Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\log.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
    
        lblimg1=Label(image=self.photoimg2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)

        img4=Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\pp.jpeg")
        img4=img4.resize((25,25),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
    
        lblimg1=Label(image=self.photoimg4,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=395,width=25,height=25)

# login button
        loginbtn=Button(frame,text="Login",borderwidth=3,relief=RIDGE,font=("times new roman",15,"bold"),bd=3,bg="red",fg="white")
        loginbtn.place(x=110,y=300,width=120,height=35)
    
        registerbtn=Button(frame,text="New User Register",borderwidth=0,font=("times new roman",10,"bold"),bd=3,bg="black",fg="white",activebackground="red")
        registerbtn.place(x=15,y=350,width=160)

        #forgetpassword
        registerbtn=Button(frame,text="forgot Password",borderwidth=0,font=("times new roman",10,"bold"),bd=3,bg="black",fg="white", activebackground="red")
        registerbtn.place(x=15,y=380,width=160)

       
    
    
    
    

if __name__ == "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()