from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.geometry('300x100')

def filedialog():
    fileopen = askopenfilename()
    fileread = fileopen
    file = open(fileread)
    mylabel = Label(text = file.read()).pack()
    
    
btn = Button(text = 'open file', width = 50, command = filedialog).pack()

root.mainloop()