from tkinter import *
import tkinter.messagebox

root = Tk()

def btnf1():
    txt1 = txt.get()
    Label(root, text = txt1, fg = 'blue', bg = 'red', font = 12).pack()

def btnf2():
    Label(text = 'Open button in Python', fg = 'blue', bg = 'yellow', font = 12).pack()

def gui():
    gu = Tk()
    gu.title("New Project")
    gu.mainloop()
    
def save():
    Label(root, text = 'Project Saved', fg = 'black', bg = 'green', font = 12).pack()
    
def mbox():
    tkinter.messagebox.showinfo('Save', 'Do you want to open this file ?')

def delete():
    de = tkinter.messagebox.askquestion('Delete', 'Want to close this file ?')
    if de == 'yes':
        root.destroy()
        
txt = StringVar()

root.title('First GUI')
root.geometry('500x500+100+200')

mylabel1 = Label(text = 'First Text', fg = 'blue', bg = 'yellow', font = 12).pack()
mylabel2 = Label( text = 'Second Text', fg = 'red', bg = 'green', font = 12).pack()
Btn1 = Button( text = 'Submit', fg = 'black', bg = 'purple', command = btnf1, font = 12).pack()
mytext = Entry(textvariable = txt).pack()
Btn2 = Button(text = 'Open', fg = 'white', bg = 'blue', command = btnf2, font = 12).pack()

Chooser = Menu()
itemone = Menu()
itemone.add_command(label = 'New Project', command = gui)
itemone.add_separator()
itemone.add_command(label = 'Save', command = save)
itemone.add_command(label = 'Open', command = mbox)
itemone.add_checkbutton(label = 'program')
itemone.add_separator()
itemone.add_radiobutton(label = 'male')
itemone.add_command(label = 'Close', command = delete)

itemtwo = Menu()
itemtwo.add_command(label = 'Copy')
itemtwo.add_command(label = 'Cut')
itemtwo.add_separator()
itemtwo.add_command(label = 'Paste')
itemtwo.add_command(label = 'Detele', command = delete)

itemthree = Menu()
itemthree.add_command(label = 'A')
itemthree.add_command(label = 'B')
itemthree.add_command(label = 'C')
itemthree.add_command(label = 'D')

itemfour = Menu()
itemfour.add_command(label = 'E')
itemfour.add_command(label = 'F')
itemfour.add_command(label = 'G')
itemfour.add_command(label = 'H')

itemfive = Menu()
itemfive.add_command(label = 'I')
itemfive.add_command(label = 'K')
itemfive.add_command(label = 'L')
itemfive.add_command(label = 'M')

itemsix = Menu()
itemsix.add_command(label = 'N')
itemsix.add_command(label = 'O')
itemsix.add_command(label = 'Q')
itemsix.add_command(label = 'P')

itemseven = Menu()
itemseven.add_command(label = 'T')
itemseven.add_command(label = 'V')
itemseven.add_command(label = 'U')
itemseven.add_command(label = 'Z')

Chooser.add_cascade(label = 'File', menu = itemone)
Chooser.add_cascade(label = 'Edit', menu = itemtwo)
Chooser.add_cascade(label = 'Naavigate', menu = itemthree)
Chooser.add_cascade(label = 'Code', menu = itemfour)
Chooser.add_cascade(label = 'Run', menu = itemfive)
Chooser.add_cascade(label = 'Tools', menu = itemsix)
Chooser.add_cascade(label = 'Help', menu = itemseven)

root.config(menu = Chooser)



root.mainloop()
