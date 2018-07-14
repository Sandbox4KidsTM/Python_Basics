# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 21:30:12 2017

@author: Sandbox999
"""
#this is Sandbox's Python Code
#write to a file from a list
#write iteratively

#NOTE: write() method takes only string datatypes, so convert integers to strings before writing

numbers = [1,2,3,4,5,6,7,8,9]

fileVar = open("C:\\out\\example_write.txt", 'w') #(creates and) opens a file in write mode
i = 0
while i < len(numbers): #alternatively: for i in numbers:
    fileVar.write(str(numbers[i])) #writes content to the file
    fileVar.write("\n") #newline character is added
    i = i+1
    
fileVar.close()

fileVar = open("C:\\out\\example_write.txt", 'r')
print(fileVar.read()) #print the contents of the fileVar
fileVar.close()