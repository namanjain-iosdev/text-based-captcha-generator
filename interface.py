from tkinter import *
from PIL import Image, ImageTk
from func import *
from tkinter import messagebox


def chkauth():
    if str(cap) == str(captcha_var.get()):
        messagebox.showinfo("Information", "you entered right captcha!")
    else:
        messagebox.showwarning("Warning", "wrong captcha!!!")


def retry():
    cap = captcha_gen()
    chkauth()


main_screen = Tk()
main_screen.config(bg="#ffe6c8")
main_screen.geometry('700x600')
main_screen.minsize(400, 300)

l1 = Label(main_screen, text="Text Captcha", bg="#8c8272",height="0",width="700",
           fg="white", font=('Times New Roman', 18))
l1.pack(fill=Y)
f1 = Frame(main_screen, bg="#262729", padx="100", pady="150")
captcha_var = StringVar()
captcha_entry = Entry(f1, textvariable=captcha_var)
captcha_entry.grid(row=0, column=1)
global cap
cap = captcha_gen()
cap_img = PhotoImage(file="cap_img.png")
Label(f1, image=cap_img).grid(row=0, column=3)


submit_pic = PhotoImage(file='go_img.png')

Button(f1, text="Submit", fg="black", command=chkauth,
       image=submit_pic, padx="0", pady="0").grid(row=1, column=1)

f1.pack()
main_screen.mainloop()
