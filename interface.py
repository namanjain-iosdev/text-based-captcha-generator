from tkinter import *
from PIL import Image, ImageTk
from func import *
from tkinter import messagebox

def chkauth():
    if str(cap) == str(captcha_var.get()):
        l1.configure(background="green",text="successful")
    else:
        l1.configure(background="red",text="invalid")

def refresh():
    global cap
    global cap_img
    global l2
    global f2
    cap = captcha_gen()
    cap_img = PhotoImage(file="cap_img.png")
    l2=Label(f2, image=cap_img)
    l2.grid(row=0,column=0,pady="5")


def login_screen():
    main_screen = Tk()
    main_screen.config(bg="#ffe6c8")
    main_screen.geometry('800x800')
    main_screen.minsize(400, 300)
    
    main_screen.title("Text Captcha")
    
    global l1
    l1 = Label(main_screen, text="Status", bg="#8c8272",fg="white", font=('Times New Roman', 18))
    l1.pack(fill=X,side=TOP)
    global f1
    f1 = Frame(main_screen, bg="#262669", padx="100", pady="150")
    f1.pack()
    global user_var
    global pass_var
    global captcha_var
    user_var = StringVar(main_screen,value="User Name")
    pass_var = StringVar(main_screen,value="Password")
    captcha_var = StringVar()

    user_entry = Entry(f1, textvariable=user_var)
    user_entry.pack(side=TOP,anchor="nw",pady="5")


    pass_entry = Entry(f1, textvariable=pass_var,show="*")
    pass_entry.pack(side=TOP,anchor="nw",pady="5")

    
    global captcha_entry
    captcha_entry = Entry(f1, textvariable=captcha_var)
    captcha_entry.pack(side=TOP,anchor="nw",pady="5")
    global cap
    global l2
    global cap_img
    global f2
    
    f2=Frame(f1,bg="#262669")
    f2.pack()
    refresh()
    
    f3=Frame(f1,bg="#262669")
    f3.pack(side=TOP)

    submit_pic = PhotoImage(file='go_img.png')
    refresh_pic = PhotoImage(file='refresh_img.png')
    Button(f3, text="Submit", fg="black", command=chkauth,image=submit_pic, padx="0", pady="0").pack(side=LEFT,padx=(0,3))
    Button(f3, text="refresh", fg="black", command=refresh,image=refresh_pic,height="21",width="24", padx="0", pady="5").pack(side=LEFT)
    
        

    main_screen.mainloop()
login_screen()