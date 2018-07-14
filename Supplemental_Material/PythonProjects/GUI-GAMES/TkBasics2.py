import tkinter as tk

window = tk.Tk()

d1 = tk.Label(window, text = "Kg")
d1.grid(row=0, column=0, padx=100, pady=5)

def kg2other(): #multiple actions on multiple fields using 1 button command functioncall
    grams = float(e1_value.get())*1000
    t1.delete("1.0", END) #clears current text
    t1.insert(END,grams)

    ounces = float(e1_value.get())*35.274
    t2.delete("1.0", END)
    t2.insert(END,ounces)

    pounds = float(e1_value.get())*2.2
    t3.delete("1.0", END)
    t3.insert(END,pounds)

e1_value = StringVar()

e1 = tk.Entry(window, textvariable = e1_value)
e1.grid(row=0, column=1, padx=100, pady=5)

b1 = tk.Button(window, text = "Convert", command=kg2other)
b1.grid(row=0, column=2, padx=100, pady=5)

t1 = tk.Text(window, height=2, width=30)
t1.grid(row=1, column=0)

t2 = tk.Text(window, height=2, width=30)
t2.grid(row=1, column=1)

t3 = tk.Text(window, height=2, width=30)
t3.grid(row=1, column=2)

window.mainloop()


