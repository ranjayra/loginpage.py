from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.big = ImageTk.PhotoImage(file=r"D:\jillltt\pexels-photo-7846473.jpeg")
        
        self.bg = Label(self.root, image=self.big)
        self.bg.place(x=0, y=0, relwidth=1, relheight=1)
        
        frame = Frame(self.root, bg="black")
        frame.place(x=510, y=100, width=300, height=450)
        
        img1 = Image.open(r"D:\Pictures\icon-symbol-or-website-admin-social-login-element-concept-3d-rendering-png.webp")
        img1 = img1.resize((100, 100),  Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=600, y=115, width=100, height=100)
        get_str=Label(frame,text="Get_started",font=("time new roman",20 ,"bold"),fg="white",bg="black" )
        get_str.place(x=58,y=120)
        
        
        user_name=lbl=Label(frame,text="user name",font=("time new roman",15 ,"bold"),fg="white",bg="black" )
        user_name.place(x=95,y=160)
        self.txtuser=ttk.Entry(frame,font=("time new roman",15,"bold"))
        self.txtuser.place(x=30,y=200,width=240)
        
        password=lbl=Label(frame,text="password",font=("time new roman",15,"bold"),fg="white",bg="black")
        password.place(x=98,y=240)
        
        self.txtpass=ttk.Entry(frame,font=("time new roman",15,"bold"))
        self.txtpass.place(x=30,y=280,width=240)
        
        img2= Image.open(r"D:\Pictures\icon-symbol-or-website-admin-social-login-element-concept-3d-rendering-png.webp")
        img2 = img2.resize((25, 25),  Image.Resampling.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg1.place(x=580, y=265, width=25, heigh=25)
        
        img3= Image.open(r"D:\Pictures\images.png")
        img3 = img3.resize((25, 25),  Image.Resampling.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg1.place(x=580, y=345, width=25, heigh=25)
        
        #login button
        loginbtn=Button(frame,command=self.login,text="login",font=("time new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=85,y=320,width=100,height=35)
        
        #register button
        registerbtn=Button(frame,text="New enter resister",font=("time new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="black",activebackground="black")
        registerbtn.place(x=20,y=370,width=180,height=30)
        
        #forgate pasword
        registerbtn=Button(frame,text="Forgate password",font=("time new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="black",activebackground="black")
        registerbtn.place(x=20,y=405,width=180,height=30)
        
    def login(self):
        if self.txtuser.get()==""and self.txtpass.get()=="":
            messagebox.showerror("error","all failled required")
        elif self.txtuser.get()=="Ranjay"and self.txtpass.get()=="@12345":
             messagebox.showinfo("succsess","welcome to aapna constitution")
        else:
            messagebox.showerror("invilid user name password")
        
            
     
     
        
        
if __name__ == "__main__":
    root = Tk()
    app = LoginWindow(root)
    root.mainloop()
