#rename files

import os

os.rename("C:\\in\\example.txt", "C:\\in\\NEWexample.txt")
os.remove("C:\\in\\example20.txt")
os.mkdir("newDirectory") #creates a new directory within the current directory
os.chdir("C:\\in\\BrandNewDirectory") #note this directory should exist before you are able to change to it

os.getcwd() #gets you the Current (Working) Directory
os.rmdir("newDirectory") #removes the directory