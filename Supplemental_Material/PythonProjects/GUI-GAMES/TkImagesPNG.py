import tkinter as tk
from PIL import ImageTk, Image
#PIL for png, jpg, etc. formats

root = tk.Tk()  
canvas = tk.Canvas(root, width = 300, height = 300)  
canvas.pack()  

img = ImageTk.PhotoImage(Image.open("RA.png"))  
canvas.create_image(150, 150, image=img)  
root.mainloop()  