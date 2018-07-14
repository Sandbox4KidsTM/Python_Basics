#https://likegeeks.com/python-gui-examples-tkinter-tutorial/#Create-your-first-GUI-application

from tkinter import *
 
window = Tk()
window.geometry('350x200')
 
window.title("Welcome to LikeGeeks app")
 
lbl = Label(window, text="Hello", font=("Arial Bold", 50))
 
lbl.grid(column=2, row=2)
 
window.mainloop()