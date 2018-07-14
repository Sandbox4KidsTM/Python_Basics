# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 07:24:19 2017

@author: Sandbox999
"""
#this is Sandbox's Python Code
# this checks if a string is a palindrome i.e. reads same forwards & backwards

myS = input("please enter your string:")
newS=""

i = len(myS)
j = 0

while (i > 0):
    newS=newS+myS[i-1] 
    # creates a new string with each iteration, and stores the reference to that new string in newS
    #newS[0]=myS[i] gives an error: 'str' object does not support item assignment
    i = i-1
    j=j+1

print("the reserve of the string is:",newS)

if newS == myS:
    print("this is a palindrome")
else:
    print("sorry, not a palindrome")
