# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 19:45:23 2017

@author: Sandbox999
"""
#this is Sandbox's Python Code
# check for duplicate characters

print("enter a string")
myString = input()
i = 0

while i < len(myString):
    j = 0
    while j < len(myString):
        print(myString[j])
        if((myString[i] == myString[j]) and (i != j)):
                print(myString[i]+"is a duplicate char")
        j = j+1
    i = i+1
    
    
