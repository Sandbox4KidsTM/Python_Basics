# http://www.c-sharpcorner.com/blogs/basics-for-displaying-image-in-tkinter-python

#To display image in Python is as simple as that. 
#But, the problem is PhotoImage class only supports GIF and PGM/PPM formats.
 
#The more generalized formats are JPEG/JPG and PNG. 
#To open and display with those formats, we need help of ImageTk and Image classes 
#from PIL(photo imaging Library) package.
#With the help of PIL(photo imaging Library), we can load images in over 30 formats 
#and convert them to image objects, even base64-encoded GIF files from strings!!

import tkinter as tk
#NOTE: PhotoImage only supports GIF Files

window = tk.Tk()

canvas = tk.Canvas(window, width = 300, height = 300)  
canvas.pack()

photo1 = tk.PhotoImage(file = "villager.gif")
canvas.create_image(150, 150, image=photo1) 

window.mainloop()

#The PhotoImage class is part of the Tkinter module, 
#just like all the other Tkinter classes you're calling (Label, StringVar, Button, etc). 
#You haven't loaded PhotoImage into the global namespace, 
#so you can't access it simply with PhotoImage. Try tk.PhotoImage instead.
# self.bg = tk.PhotoImage(file="bgmain.gif")


