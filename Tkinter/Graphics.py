from tkinter import *

root = Tk()
root.title('Graphics')

canvas = Canvas(width=300, height=150)
canvas.pack()

reddraw = canvas.create_line(0, 0, 300, 50, fill='red')
bluedraw = canvas.create_line(0, 150, 300, 50, fill = 'blue')
yellowdraw = canvas.create_rectangle(25, 25, 130, 70, fill='yellow')

canvas.delete()

root.mainloop()
