from tkinter import *

window = Tk()

b1 = Button(window, text = "SubmIt", background = "red")
b1.grid(row=0, column=1)

e1 = Entry(window)
e1.grid(row=0, column=0)

t1 = Text(window, height = 2, width = 2)
t1.grid(row=0, column=2)

window.mainloop()

