# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 08:08:25 2017

@author: Sandbox999
"""

str = "hEllo wORld"
print(str)
print(len(str))

#string formatting
print("Hellow %s" %("WORLD"))
print("String is %s %d %1.3f" %("really", 54, 2.46))

#prints character at index 1 of the string

print(str[1])

print(str.upper())
print(str.lower())

#find indext of a character in a string
print('index of letter R in the string is %d' %(str.index('R')))

#Python uses ZERO-BASED INDEXING
# Python is CASE-SENSITIVE
# Python allows METHOD CHAINING

print("index of letter 'r' in the string is %d" %str.lower().index('r'))
#Python cannot find 'r' until the entire string is converted to lower case

#slicing a string
print(str[8])
print(str[2:8]) #note: the upper and lower bounds are NOT included

print(str[2:len(str)-1])

#split a string
name = "Bryan Cairns"
mylist = name.split(" ")
print(mylist[0]+mylist[1])
print(name) #original variable was not modified by the split() function
#print(name.split(name))