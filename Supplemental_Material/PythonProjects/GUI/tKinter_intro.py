import tkinter
myWindow = tkinter.Tk()

def km_to_miles():
    print(e1_value.get())
    t1.insert(END, int(e1_value.get())*0.6)

b1 = Button(myWindow, text='Execute', command=km_to_miles) #button widget
b1.grid(row=0, column=0)

e1_value=StringVar()
e1 = Entry(myWindow,textvariable=e1_value) # (data) entry widget
e1.grid(row=0, column=1)

t1=Text(myWindow, height=1, width=30) #textbox widget
#height and width of the Text widget are in cells
t1.grid(row=0, column=2)

myWindow.mainloop()