from tkinter import *

root = Tk()

def printName():
    print("hello, my name is Bucky")

button_1 = Button(root, text="Print my name", command=printName, bg="red", fg="white") 
# command binds the function printName() to the button_1

button_1.pack()

root.mainloop()