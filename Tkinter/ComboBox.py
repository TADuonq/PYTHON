from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

def click():
    Label(text = '      You selected fruit is: ' + var.get()).grid(row = 2, column = 1)

root = Tk()
root.title('ComboBox')

var = StringVar(value = "Choose a fruit")
combo = ttk.Combobox(width = 25, textvariable = var, font = 10)
combo['values'] = ('Apple', 'Orange', 'Mango', 'Cashew', 'Papaya', 'Melon')
combo.grid(row = 0, column = 1)

ttk.Label(text = 'Select your favorite fruit').grid(row = 0, column = 0)

btn = ttk.Button(text = 'Click me', command = click)
btn.grid(row = 1, column = 1)

root.mainloop()