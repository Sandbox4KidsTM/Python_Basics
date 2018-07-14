from tkinter import *

window = Tk()

canvas = Canvas(window, width=200, height=100)
canvas.pack()

blueLine = canvas.create_line(0,0,200,50, fill="blue")
redLine = canvas.create_line(0,100,200,50, fill="red")

greenBox = canvas.create_rectangle(25, 25, 130, 160, fill="green")

#canvas.delete(redLine)

#canvas.delete(ALL)


window.mainloop()