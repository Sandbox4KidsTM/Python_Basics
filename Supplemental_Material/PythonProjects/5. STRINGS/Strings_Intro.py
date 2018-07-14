# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 22:44:21 2017

@author: Sandbox999
"""
#this is Sandbox's Python Code
greeting = "Hello, there!"
print(greeting)
print(type(greeting))
print(greeting[1])
print(type(greeting[1])) #NOTE: a string is made up of strings

#indexing: left to right: 0 to len()-1
#indexing: right to left: -1 to -(len())

#strings have methods associated with it

c = "Here"
print(c)

print(c.replace('e', 'x', 1))

print(c.upper())

print(c.lower())

c = input("type a string:")
print(c[len(c)-1]) #print last character of a string
