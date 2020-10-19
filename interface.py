from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.config(bg="#ffe6c8")
root.geometry('900x900')
root.minsize(400,300)
page = Frame(root,bg="#ffe6c8").pack(fill=BOTH)
f1=Frame(page,bg="#262729",height="700",width="700").pack(side=TOP)
Frame(f1,bg="#ffe6c8",height="100",width="700").pack(side=TOP)
cap_img = PhotoImage(file="cap_img.png")
Label(f1,image = cap_img).pack()
root.mainloop()