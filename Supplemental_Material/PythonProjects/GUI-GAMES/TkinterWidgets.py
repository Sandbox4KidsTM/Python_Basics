from tkinter import *

window = Tk()

l1 = Label(window, text="Label One", bg="red", fg="white")
l1.pack()

l2 = Label(window, text="Label Two", bg="green", fg="black")
l2.pack(fill=X)

l3 = Label(window, text="Label Three", bg="pink", fg="blue")
l3.pack(side=RIGHT, fill=Y)

window.mainloop()