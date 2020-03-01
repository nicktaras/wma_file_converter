# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("300x300")

def selectUploadFileHander():
   msg = messagebox.showinfo( "Hello Python", "Hello World")

selectUploadButton = Button(top, text = "Hello", command = selectUploadFileHander)
selectUploadButton.place(x = 50,y = 50)
top.mainloop()

