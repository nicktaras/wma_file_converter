# !/usr/bin/python3
from tkinter import *
from tkinter import filedialog as fd 
from tkinter import messagebox
import ftransc
import os
import subprocess
from pathlib import Path
import os

# styles
leftPadding = 20

# Initialise tkinter
top = Tk()

# Canvas Size
top.geometry("300x300")
top.configure(bg='#3E4149')
top.title("WMA File Converter")  

appTitle = Label(top, text="Windows Media Audio Converter", background="#3E4149", foreground="white")
appTitle.pack()
appTitle.place(x = leftPadding, y = 14)

directoryTitleVar = StringVar()
directoryTitleVar.set('')
directoryTitle = Label(top, wraplength=250, textvariable=directoryTitleVar, background="#3E4149", foreground="white", justify="left")
directoryTitle.pack()
directoryTitle.place(x = leftPadding, y = 90)

# Directory
fromDirectory = ""

# Browse File
def fromDirectoryHandler():
    fromDirectory = fd.askdirectory() 
    info = (fromDirectory[:255] + '...') if len(fromDirectory) > 255 else fromDirectory
    directoryTitleVar.set(info)
    top.update_idletasks()

errmsg = 'Error!'

# Browser Directory Button
fromDirectoryButton = Button(top, text = "Choose Directory", command = fromDirectoryHandler, highlightbackground='#3E4149')
fromDirectoryButton.place(x = leftPadding, y = 50)

# Supported File types:
supportedFileTypes = ['mp3', 'ogg']
selectedFileType = StringVar(top)
selectedFileType.set(supportedFileTypes[0])

w = OptionMenu(top, selectedFileType, *supportedFileTypes)
w.pack()
w.place(x = leftPadding, y = 250)
w.config(bg = "#3E4149")

# Submit Button
def convertFilesHandler():
    convertFile(fromDirectory, selectedFileType.get())

convertFilesButton = Button(top, text = "Convert", command = convertFilesHandler, highlightbackground='orange', foreground="black", compound=CENTER)
convertFilesButton.place(x = 200, y = 250)

# Convert File Util
def convertFile(_path, _type):
    print ("Converting files from: ", _path + ' to ' + _type + " 's.")
    p = Path(_path)
    for i in p.glob('**/*'):
        subprocess.call(['ftransc', '-f', _type, '--directory', str(i)])

top.mainloop()
