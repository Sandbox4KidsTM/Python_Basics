#using Tkinter for GUI
#Tkinter is built-in library, so you don't have to install it separately
#just import the Tkinter library

import tkinter as tk
# Tkinter program is made up of 2 things: Window & Widgets

def km2miles():
    #print(e1_value.get()) #get() method returns a string #print() prints to console
    miles=float(e1_value.get())/1.6
    t1.insert(END,miles)

window = tk.Tk() #creates an empty window

b1 = tk.Button(window, text = "ExecuteMe", command=km2miles) #creates a button inside the window
b1.grid(row=0, column=0) #places a button

e1_value=StringVar()

e1 = tk.Entry(window, textvariable=e1_value) #creates an Entry widget (single line data entry) in the window
e1.grid(row=0, column=1)

# b1.pack() #pack method places the widgets as tightly as possible
# b1.grid() #grid method gives you more control over where to place the widgets

t1 = tk.Text(window, height=1, width=100) #creates an Entry in the window
t1.grid(row=0, column=3)

# to see a full list of functions from Tkinter library, on the iPython Console:
    # type: Button?

window.mainloop() #keeps the window open forever, otherwise it closes immediately