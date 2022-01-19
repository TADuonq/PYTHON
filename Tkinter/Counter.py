from tkinter import *

counter = 0
def digit_counter(mylabel1):
    counter = 0
    def digit():
        global counter
        counter += 1
        mylabel1.config(text = str(counter))
        mylabel1.after(10, digit)
    digit()

root = Tk()
root.title('Digit Counter')
mylabel1 = Label(fg = 'red', font = 100)
mylabel1.pack()
digit_counter(mylabel1)
btn = Button(text = 'Terminate', width = 50, command = root.destroy)
btn.pack()


root.mainloop()