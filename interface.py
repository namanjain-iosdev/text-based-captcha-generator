from tkinter import *
from PIL import Image, ImageTk
from func import *
from tkinter import messagebox

def chkauth():
    if str(cap) == str(captcha_var.get()):
        l1.configure(background="green",text="successful")
    else:
        l1.configure(background="red",text="invalid")



def login_screen():
    main_screen = Tk()
    main_screen.config(bg="#ffe6c8")
    main_screen.geometry('1080x1080')
    main_screen.minsize(400, 300)
    main_screen.title("Text Captcha")
    #main_screen.wm_iconbitmap("1.icn")
    global l1
    l1 = Label(main_screen, text="Status", bg="#8c8272",fg="white", font=('Times New Roman', 18))
    l1.pack(fill=X,side=TOP)

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

    
    
    captcha_entry = Entry(f1, textvariable=captcha_var)
    captcha_entry.pack(side=TOP,pady="5")
    global cap
    cap = captcha_gen()
    cap_img = PhotoImage(file="cap_img.png")
    Label(f1, image=cap_img).pack(pady="5")
    submit_pic = PhotoImage(file='go_img.png')
    Button(f1, text="Submit", fg="black", command=chkauth,image=submit_pic, padx="0", pady="0").pack(side=BOTTOM)
    
        

    main_screen.mainloop()
