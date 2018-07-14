from tkinter import *

root = Tk()

def printName(event): #event is the parameter for printName function
    print("hello, my name is Bucky")

button_1 = Button(root, text="Print my name", bg="red", fg="white") 
button_1.bind("<Button-1>", printName) #Buton-1 means Left Button
#bind function takes 2 parameters: event and function to call

button_1.pack()

root.mainloop()