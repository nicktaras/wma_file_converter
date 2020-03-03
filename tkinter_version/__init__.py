# !/usr/bin/python3
from tkinter import *
from tkinter import filedialog as fd 
from tkinter import messagebox
import ftransc
import os
import subprocess
from pathlib import Path
import os
import webbrowser

# styles
leftPadding = 20
backgroundColor = '#3E4149'
canvasSize = "300x300"

# Initialise tkinter
top = Tk()

# Canvas Size
top.geometry("300x350")
top.configure(bg='#3E4149')
top.title("WMA File Converter - Nick Taras")  

appTitle = Label(top, text="Windows Media Audio Converter", background="#3E4149", foreground="white",  font="none 14 bold")
appTitle.pack()
appTitle.place(x = leftPadding, y = 14)

# fromDirectoryButton = Button(top, text = "Choose Directory", command = fromDirectoryHandler, highlightbackground='#3E4149')
appFooter = Label(top, anchor="center", height=2, text="by Nick Taras    |                       ", width=37, background="orange red", foreground="white", borderwidth=2, relief="groove")
appFooter.pack()
appFooter.place(x = 0, y = 316)

def openUrlHandler():
    webbrowser.open("https://github.com/nicktaras/audio_converter")
    
# Browser Directory Button
gitButton = Button(top, text = "Github", bg="green", fg="red", background='red', command = openUrlHandler, highlightbackground='orange red')
gitButton.place(x = 175, y = 320)

directoryTitleVar = StringVar()
directoryTitleVar.set('')
directoryTitle = Label(top, wraplength=250, textvariable=directoryTitleVar, background=backgroundColor, foreground="white", justify="left")
directoryTitle.pack()
directoryTitle.place(x = leftPadding, y = 90)

# Directory
fromDirectory = StringVar()
fromDirectory.set('')

# Browse File
# print(fromDirectory.get())
def fromDirectoryHandler():
    fromDirectory.set(fd.askdirectory())
    directoryTitleVar.set((fromDirectory.get()[:255] + '...') if len(fromDirectory.get()) > 255 else fromDirectory.get())
    top.update_idletasks()

# Browser Directory Button
fromDirectoryButton = Button(top, text = "Choose Music Directory", command = fromDirectoryHandler, highlightbackground='#3E4149')
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
    convertFile(fromDirectory.get(), selectedFileType.get())

convertFilesButton = Button(top, text = "Convert", command = convertFilesHandler, highlightbackground='#3E4149', foreground="black", compound=CENTER)
convertFilesButton.place(x = 200, y = 250)

# Convert File Util
# print ("Converting files from: ", _path + ' to ' + _type + " 's.")
def convertFile(_path, _type):
    for i in Path(_path).glob('**/*'):
        if str(i).endswith('.wma'):
            subprocess.call(['ftransc', '-q', 'extreme', '-f', _type, str(i)])

top.mainloop()
