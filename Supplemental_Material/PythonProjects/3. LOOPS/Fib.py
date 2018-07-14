# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 12:15:14 2017

@author: Sandbox999
"""
print("Fibonacci number series")
print("how many items in the series do you want to print?")
num = int(input()) #10

prevNum = 1
print(prevNum)
currNum = 1
print(currNum)

while num > 0:

    nextNum = prevNum+currNum
    print(nextNum) #2, 3, 5, 8, 13, ...
    num = num - 1
    prevNum = currNum #1
    currNum = nextNum #2
    
