from tkinter import *

root = Tk()

one = Label(root, text="one", bg="red", fg="white")
one.pack()

two = Label(root, text="two", bg="green", fg="black")
two.pack(fill=X) #label fills the parent to the X-value of the parent

three = Label(root, text="three", bg="yellow", fg="brown")
three.pack(side=LEFT, fill=Y) #label fills the parent to the X-value of the parent

root.mainloop()