from tkinter import *

root =Tk()

def clickLeft(event):
    print("LEFT is clicked")
    
def clickMiddle(event):
    print("MIDDEL is clicked")
    
def clickRight(event):
    print("RIGTH is clicked")

button_1 = Button(root, text= "BIG RED BUTTON", bg="red", fg="white")
button_1.bind("<Button-1>", clickLeft) #calls clickLeft method when left-clicked i.e. Button-1
button_1.bind("<Button-3>", clickRight) #calls clickRight method when right-clicked i.e. Button or Button-3
button_1.bind("<Button-2>", clickMiddle) #calls clickMiddle method when middle-clicked i.e. Button-2

button_1.pack()

root.mainloop()
