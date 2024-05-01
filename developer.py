from tkinter import*
from tkinter import ttk
from PIL import Image
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2  


class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",30,"bold"),bg="white",fg="navy blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\Shiwani Gupta\OneDrive\Desktop\Attendence system\image\DEV.png")
        img_top=img_top.resize((1530, 720), Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=680)

        img_top1=Image.open(r"C:\Users\Shiwani Gupta\Downloads\PIC S.jpg")
        img_top1=img_top1.resize((200, 200), Image.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        
        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)


    # developer info
        dep_label=Label(main_frame,text="hello my name is shiwani",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        img_top2=Image.open(r"C:\Users\Shiwani Gupta\Downloads\PIC S.jpg")
        img_top2=img_top2.resize((200, 200), Image.LANCZOS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)
        
        f_lbl=Label(main_frame,image=self.photoimg_top2)
        f_lbl.place(x=300,y=230,width=200,height=200)

if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()        

   