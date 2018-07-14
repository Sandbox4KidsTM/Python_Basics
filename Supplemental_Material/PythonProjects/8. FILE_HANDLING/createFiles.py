# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 08:26:58 2017

@author: Sandbox999
"""
ids=["B3\n", "B4\n", "B5\n", "B6\n"]

with open("C:\\in\\testing3.txt",'a') as file: #a is a append, w is to write
    i = 0
    while i <= 3:
        file.write(ids[i])
        i = i+1

fileNew = open("C:\\in\\testing3.txt", 'r')
print(fileNew)
fileCont = fileNew.read()
print(fileCont)
