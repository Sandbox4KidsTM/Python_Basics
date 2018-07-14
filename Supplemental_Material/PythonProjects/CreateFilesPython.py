# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 07:49:48 2017

@author: Sandbox999
"""

# create a file called testing.txt in the folder C:\in
file=open("C:\\in\\testing.txt", 'w') #w is for write
file.write("such a nice file that I am")
file.close()

file=open("C:\\in\\testing.txt", 'r')
content=file.read() 
#content is an object that stored the data read from the file testing.txt
print(content)
file.close()


file=open("C:\\in\\testing.txt",'a')
file.write("\ncute file I AM")
file.close()
file=open("C:\\in\\testing.txt", 'r')
content=file.read() 
#content is an object that stored the data read from the file testing.txt
print(content)
file.close()
