import tkinter

root = Tk()

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root) #blank single line of textbox i.e. data entry field
entry_2 = Entry(root) #blank single line of textbox i.e. data entry field

label_1.grid(row=0, column=0, sticky=E) #right-align using sticky = E (i.e. East)
label_2.grid(row=1, column=0, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="keep me logged in")
c.grid(columnspan=2) #spans two columns

root.mainloop()