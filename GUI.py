import GePFAMMFiFoA
import tkinter
from tkinter import *
from tkinter import filedialog

def browse_button():
    global folder_path
    global realPath
    filename = filedialog.askdirectory()
    folder_path = filename
    realPath = folder_path
    return realPath
    print(realPath)

def buttones():
    state = "Yo es startet"
    GePFAMMFiFoA.generate(realPath)
    state="Die kagge is fertig"

root = Tk()
state = StringVar()
realPath =""
folder_path = ""
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Browse", command=(lambda: browse_button()))
button2.config(height=3, width=20)
button2.grid(row=2, column=2)
button3 = Button(text="Generate", command=(lambda: buttones()))
button3.config(height=3, width=20)
button3.grid(row=3, column=3)
labe = Label(master=root, textvariable=state)
labe.grid(row=0, column=1)


mainloop()
