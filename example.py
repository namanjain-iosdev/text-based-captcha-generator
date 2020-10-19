#this file is made for practice purpose only
from tkinter import *
import tkinter as tk

root = Tk()
root.geometry("500x500")
cap_img = PhotoImage(file="cap_img.png")
Label(root,image = cap_img,height="300",width="300",bg="red").pack()

root.mainloop()
