from tkinter import *

def calculate():
    var3 = var1.get()
    var4 = var2.get()
    var5 = var3 * var4
    e3.insert(0, var5)
    
def delete():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)

root = Tk()
root.title('Area of a Rectangle')

var1 = IntVar()
var2 = IntVar()

Label(text = 'Area of a Rectangle', padx = 10, font = ('arial', 30, 'bold')).grid(row = 0, column = 1)

Label(text = 'Heigt', padx = 10, font = ('arial', 30, 'bold')).grid(row = 1, sticky = W)
e1 = Entry(width = 30, font = ('arial', 30, 'bold'), textvariable = var1)
e1.grid(row = 1, column = 1)

Label(text = 'Length', padx = 10, font = ('arial', 30, 'bold')).grid(row = 2, sticky = W)
e2 = Entry(width = 30, font = ('arial', 30, 'bold'), textvariable = var2)
e2.grid(row = 2, column = 1)

Label(text = 'Length', padx = 10, font = ('arial', 30, 'bold')).grid(row = 3, sticky = W)
e3 = Entry(width = 30, font = ('arial', 30, 'bold'))
e3.grid(row = 3, column = 1)

Button(text = 'Calculate', font = ('arial', 30, 'bold'), width = 15, command = calculate).grid(row = 4, column = 1, sticky = W)
Button(text = 'Clear', font = ('arial', 30, 'bold'), width = 15, command = delete).grid(row = 4, column = 1, sticky = E)

root.mainloop()