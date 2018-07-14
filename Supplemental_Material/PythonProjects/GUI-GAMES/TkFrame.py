from tkinter import *

window = Tk()

topFrame = Frame(window) #Frame is an invisible rectangle/container
topFrame.pack()

bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)

b1 = Button(topFrame, text = "Button 1", fg = "red")
b2 = Button(topFrame, text = "Button 2", fg = "blue") 
b3 = Button(topFrame, text = "Button 3", fg = "green")
b4 = Button(bottomFrame, text = "Button 1", fg = "purple")

b1.pack(side=LEFT) #places it as far left as possible
b2.pack(side=LEFT)
b3.pack(side=LEFT)
b4.pack(side=BOTTOM)


window.mainloop()

