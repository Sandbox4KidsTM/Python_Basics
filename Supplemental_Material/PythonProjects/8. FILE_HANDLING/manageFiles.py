# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 08:05:11 2017

@author: Sandbox999
"""

fileVar=open("C:\\in\\testing20.txt",'w')
fileVar.write("something to write about")
fileVar.close()

fileVar=open("C:\\in\\testing20.txt",'r')
fileContent = fileVar.read()
print(fileContent)

with open("C:\\in\\testing20.txt",'a') as fileVar: #a is a append, w is to write
    fileVar.write("\nwriting using the with method")
    # 'with' is a compact approach to creating, opening & closing files

print()
fileVar=open("C:\\in\\testing20.txt",'r')
fileContent = fileVar.read()
print(fileContent)
fileVar.close()
