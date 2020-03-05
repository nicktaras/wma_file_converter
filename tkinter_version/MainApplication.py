import tkinter as tk
from tkinter import StringVar, IntVar, messagebox, OptionMenu, Button, Label, filedialog as fd 
import ftransc
import os
import subprocess
from pathlib import Path
import os
import webbrowser
import sys
import cmd

# Import custom classes
import guiFactory

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # styles
        leftPadding = 20
        backgroundColor = '#3E4149'
        canvasSize = "300x300"

        # Canvas Size
        parent.geometry(canvasSize)
        self.configure(bg='#3E4149')
        parent.title("WMA File Converter - Nick Taras") 

        # Submit Button
        def convertFilesHandler():
            convertFile(fromDirectory.get(), selectedFileType.get())

        # Convert File Util
        # print ("Converting files from: ", _path + ' to ' + _type + " 's.")
        def convertFile(_path, _type):
            for i in Path(_path).glob('**/*'):
                if str(i).endswith('.wma'):
                    outputChildProcess = subprocess.check_output(['ftransc', '-q', 'extreme', '-f', _type, str(i)])
                    if str(outputChildProcess).find("Success") != -1:
                        progressOutputVar.set("File Success: " + str(i))
                        progressOutput.configure(bg = "#105b10")
                        filesConvertedOutputVar.set(filesConvertedOutputVar.get()+1)
                        self.update()
                    else:
                        progressOutputVar.set("File Skipped: " + str(i))
                        progressOutput.configure(bg = "#992a2a")
                        self.update()

        # Open url to GitHub
        def openUrlHandler():
            webbrowser.open("https://github.com/nicktaras/audio_converter")
            
        # Directory
        fromDirectory = StringVar()
        fromDirectory.set('')

        # Supported File types:
        supportedFileTypes = ['mp3', 'ogg']
        selectedFileType = StringVar(self)
        selectedFileType.set(supportedFileTypes[0])

        # Browse File
        # print(fromDirectory.get())
        def fromDirectoryHandler():
            fromDirectory.set(fd.askdirectory())
            directoryTitleVar.set((fromDirectory.get()[:255] + '...') if len(fromDirectory.get()) > 255 else fromDirectory.get())
            self.update_idletasks()

        # import gui           

        w = OptionMenu(self, selectedFileType, *supportedFileTypes)
        w.pack()
        w.place(x = leftPadding, y = 250)
        w.config(bg = "#3E4149")

        # labels

        appTitle = Label(self, text="Windows Media Audio Converter", background="#3E4149", foreground="white",  font="none 14 bold")
        appTitle.pack()
        appTitle.place(x = leftPadding, y = 14)

        appFooter = Label(self, anchor="center", height=2, text="by Nick Taras    |                       ", width=37, background="orange red", foreground="white", borderwidth=2, relief="groove")
        appFooter.pack()
        appFooter.place(x = 0, y = 316)

        progressOutputVar = StringVar()
        progressOutputVar.set('')
        progressOutput = Label(self, wraplength=250, width=32, textvariable=progressOutputVar, foreground="white", justify="left")
        progressOutput.configure(bg = "#234")
        progressOutput.pack()
        progressOutput.place(x = leftPadding, y = 160)

        filesConvertedLabel = Label(self, wraplength=250, text="Files Successfully Converted:", foreground="white", justify="left")
        filesConvertedLabel.configure(bg = backgroundColor)
        filesConvertedLabel.pack()
        filesConvertedLabel.place(x = leftPadding, y = 208)

        filesConvertedOutputVar = IntVar()
        filesConvertedOutputVar.set(0)
        filesConvertedOutput = Label(self, wraplength=250, textvariable=filesConvertedOutputVar, foreground="white", justify="left")
        filesConvertedOutput.configure(bg = backgroundColor)
        filesConvertedOutput.pack()
        filesConvertedOutput.place(x = 210, y = 208)

        directoryTitleVar = StringVar()
        directoryTitleVar.set('')
        directoryTitle = Label(self, wraplength=250, textvariable=directoryTitleVar, background=backgroundColor, foreground="white", justify="left")
        directoryTitle.pack()
        directoryTitle.place(x = leftPadding, y = 90)

        # buttons
        convertBtn = guiFactory.createButton(self, Button, "Convert", convertFilesHandler, "#3E4149", "center", 200, 250)
        linkBtn = guiFactory.createButton(self, Button, "Github", openUrlHandler, "orange red", "center", 175, 320)
        fromDirectoryBtn = guiFactory.createButton(self, Button, "Choose Music Directory", fromDirectoryHandler, "#3E4149", "center", leftPadding, 50)
        
if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
