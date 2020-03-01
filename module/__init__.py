# !/usr/bin/python3
from tkinter import *
from tkinter import filedialog as fd 
from tkinter import messagebox
import os

top = Tk()
top.geometry("300x300")

# Browse file
def callback():
    name= fd.askopenfilename() 
    print(name)
    
errmsg = 'Error!'

selectUploadButton = Button(top, text = "Hello", command = callback)
selectUploadButton.place(x = 50,y = 50)

# Submit Button
def selectUploadFileHander():
   msg = messagebox.showinfo( "Hello Python", variable.get())

selectUploadButton = Button(top, text = "Hello", command = selectUploadFileHander)
selectUploadButton.place(x = 50,y = 150)

# Select File Type
# Supported File types:
OPTIONS = ['mp3', 'ogg']
variable = StringVar(top)
variable.set(OPTIONS[0])

w = OptionMenu(top, variable, *OPTIONS)
w.pack()

top.mainloop()


