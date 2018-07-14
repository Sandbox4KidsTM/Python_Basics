# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 20:06:03 2017

@author: Sandbox999
"""
#this is Sandbox's Python Code
#reverse a string without using a library method

print("enter your string")
myS = input()

i = len(myS)

while i > 0:
    print(myS[i-1])
    i = i-1
    