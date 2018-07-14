#random insult generator using Arrays of Strings

import random
import tkinter

column1 = ["artless", "bawdy"]
column2 = ["base-court", "bat-folwing", "chocolate-fudge"]
column3 = ["apple-john", "baggage", "banana", "pineapple"]

def pickInsult():
    insultLabel.configure(text=("Thou " + random.choice(column1) + (" ") 
                        + random.choice(column2) + (" ") 
                        + random.choice(column3)))
    
root = tkinter.Tk()
root.title("Shakespearean insult generator")
root.geometry("600x100")

insultLabel = tkinter.Label(root, text="", font=("Ariel", 20))
insultLabel.pack()

insultButton = tkinter.Button(text="Please insult me!", command=pickInsult)
insultButton.pack()

root.mainloop()