from tkinter import *

def dele():
    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
    

root = Tk()
# root.geometry('200x100')
root.title('Data Entry Blocks')
Label(text  = 'First Name').grid(row = 0)
Label(text  = 'Last Name').grid(row = 1)
Label(text  = 'Occupation').grid(row = 2)
Label(text  = 'Email').grid(row = 3)

en1 = Entry()
en1.grid(row = 0, column = 1)
en1.insert(0, 'Duong')
en2 = Entry()
en2.grid(row = 1, column = 1)
en2.insert(0, 'Truong')
en3 = Entry()
en3.grid(row = 2, column = 1)
en3.insert(0, 'Developer')
en4 = Entry()
en4.grid(row = 3, column = 1)
en4.insert(0, 'duongmanucian1999@gmail.com')

btn = Button(text = 'Delete', command = dele).grid(row = 4, column = 1)

root.mainloop()