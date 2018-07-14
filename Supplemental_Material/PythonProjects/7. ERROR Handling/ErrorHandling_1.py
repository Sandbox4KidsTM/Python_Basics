# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 08:05:17 2017

@author: Sandbox999
"""
#this is Sandbox's Python Code
# error handling

#2 types of errors: syntax errors (parsing errors encountered by interpreter) 
# and exceptions(logical/language errors: nameError, typeError, etc.)


print(a) #variable names are strings are different
#a is an old variable I stored data in long time ago; 
#it has no relevance to current program

print(int('103')+333)

#syntax errors: closing brackets, matching brackets, indenting

#Exceptions: no syntax error, but language usage is incorrect
# e.g. print(1+"2") 
# 1 is a string

#print(1+"2")  #TypeError: unsupported operand type(s) for +: 'int' and 'str'

#print(newVar) #NameError: name 'newVar' is not defined

#print(2/0) #NameError: name 'newVar' is not defined

#myDict = ["a":1, "b":2, "c":3]
#print(mydict) #Syntax Error, Python is not expecting a semi-colon in a list

myList = [John, Jack, Jim]
print(myList) #NameError: name 'John' is not defined