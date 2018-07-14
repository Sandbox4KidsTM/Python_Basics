from tkinter import *

window = Tk()

l1 = Label(window, text="login")
l1.grid(row=0, column=0, sticky=E) #E for East

e1 = Entry(window)
e1.grid(row=0, column=1)

l2 = Label(window, text="password")
l2.grid(row=1, column=0, sticky=E)

e2 = Entry(window)
e2.grid(row=1, column=1)

window.mainloop()