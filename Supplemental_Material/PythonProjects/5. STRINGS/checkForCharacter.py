# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 20:00:41 2017

@author: Sandbox999
"""
#this is Sandbox's Python Code
print("enter a string")
myS=input()
print("enter a character you want to check")
myC = input()

i = 0
while i < len(myS):
    if myC[0] == myS[i]:
        print("character exists in string")
    i = i+1
