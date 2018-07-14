# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 20:12:02 2017

@author: Sandbox999
"""
#this is Sandbox's Python Code
#basics of File Handling

#Notepad can open & edit text files; Python can do the same with code

# Python can handle text and binary files

fileVar=open("C:\\in\\example.txt", 'r') #'r' is a handler to read the file
print(type(fileVar)) # <class '_io.TextIOWrapper'>

contentVar=fileVar.read() #read() method reads the file and copies to contentVar
print(contentVar)
print(type(contentVar)) #type is <class 'str'>

contentVar2=fileVar.read() #read() method reads the file and copies to contentVar
#after reading the first time, the pointer is at the bottom of the file and therefore returns blank
print(contentVar2)
print(type(contentVar2)) #type is <class 'str'>

fileVar.seek(0) #moves the pointer back to the beginning of the file
contentVar3=fileVar.read() #read() method reads the file and copies to contentVar
print(contentVar3)
print(type(contentVar3)) #type is <class 'str'>

fileVar.seek(0) #moves the pointer back to the beginning of the file
contentVar4=fileVar.readlines() #readlines() method reads the file Lines and copies to contentVar4
print(contentVar4)
print(type(contentVar4)) #type is <class 'str'>
contentVar4=[i.rstrip("\n") for i in contentVar4]
print(contentVar4)

fileVar.close() #to close the file #the closed file can be deleted