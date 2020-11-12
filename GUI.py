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

root = Tk()
realPath =""
folder_path = ""
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Browse", command=(lambda: browse_button()))
button2.config(height=3, width=20)
button2.grid(row=2, column=2)
button3 = Button(text="Generate", command=(lambda: GePFAMMFiFoA.generate(realPath)))
button3.config(height=3, width=20)
button3.grid(row=3, column=3)

mainloop()
