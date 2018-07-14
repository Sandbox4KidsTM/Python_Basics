# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 22:23:38 2017

@author: Sandbox999
"""
#this is Sandbox's Python Code
#http://www.geeksforgeeks.org/interesting-facts-about-strings-in-python-set-1/

# A python program to show that string
# cannot be changed
 
a = 'Geeks'
print(a)       # output is displayed
#a[2] = 'E'
#print(a)      # causes error

# A python program to show that a string
# can be appended to a string.
 
a = 'Geeks'
print(a) # output is displayed
a = a + 'for'
print(a) # works fine

#string 'Geeks' is immutable. variable a is being reassigned to a+'for'

print('ee' in a) #returns true if substring is found in the string

b = "ApplePie"
print(b.islower())

print(b.join(b))

c = "    apple pie     "
print(c.strip())