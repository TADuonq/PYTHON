from tkinter import *
from tkinter import ttk 

def Convert():
    var2 = indicator.get()
    var3= var1.get()
    if var2 == 'China':
        e3.delete(0, END)
        var4 = ((var3 * 6.88), 'Yuan')
        e3.insert(0, var4)
    elif var2 == 'France':
        e3.delete(0, END)
        var4 = ((var3 * 0.81), 'Euro')
        e3.insert(0, var4)
    elif var2 == 'Vietnamese':
        e3.delete(0, END)
        var4 = ((var3 * 22.81), 'VND')
        e3.insert(0, var4)
    elif var2 == 'Japanese':
        e3.delete(0, END)
        var4 = ((var3 * 7.68), 'Man')
        e3.insert(0, var4)
    elif var2 == 'USA':
        e3.delete(0, END)
        var4 = ((var3 * 1), 'Dollar')
        e3.insert(0, var4)
    elif var2 == 'UK':
        e3.delete(0, END)
        var4 = ((var3 * 0.68), 'Euro')
        e3.insert(0, var4)
    else:
        e3.delete(0, END)
        var4 = ('Error: Please, choose a country')
        e3.insert(0, var4)

def Clear():
    e1.delete(0, END)
    e2.delete(0, END)

root = Tk()
root.title('Currency Converter')

var1 = IntVar()
indicator = StringVar(value = 'Choose a country')

Label(text = 'Currency Converter', padx = 10, font = ('arial', 20, 'bold')).grid(row = 0, column = 1)

Label(text = 'Amount ($)', padx = 10, font = ('arial', 20, 'bold')).grid(row = 1, sticky = W)
e1 = Entry(width = 30, font = ('arial', 20, 'bold'), textvariable = var1)
e1.grid(row = 1, column = 1)

Label(text = 'Country', padx = 10, font = ('arial', 20, 'bold')).grid(row = 2, sticky = W)
e2 = ttk.Combobox(width = 20, font = ('arial', 30, 'bold'), textvariable = indicator)
e2['values'] = ('China', 'France', 'Vietnamese', 'Japanese', 'USA', 'UK')
e2.grid(row = 2, column = 1)

Label(text = 'Total', padx = 10, font = ('arial', 20, 'bold')).grid(row = 3, sticky = W)
e3 = Entry(width = 20, font = ('arial', 30, 'bold'))
e3.grid(row = 3, column = 1)

Button(text = 'Convert', font = ('arial', 20, 'bold'), width = 15, command = Convert).grid(row = 4, column = 1, sticky = W)
Button(text = 'Clear', font = ('arial', 20, 'bold'), width = 15, command = Clear).grid(row = 4, column = 1, sticky = E)

root.mainloop()