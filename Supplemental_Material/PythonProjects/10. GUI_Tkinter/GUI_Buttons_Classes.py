import tkinter


class BuckysButtons:
    
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
        self.printButton = Button(frame, text="Print Message", command=self.printMessage, bg="red", fg="white")
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit, bg="red", fg="black")
        self.quitButton.pack(side=LEFT)
        
    def printMessage(self):
        print("wow, this actually worked!")
        
root = Tk()
b = BuckysButtons(root)
root.mainloop()