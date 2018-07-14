# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 08:29:00 2017

@author: Sandbox999
"""
#this is Sandbox's Python Code
#this program divides a number by another and returns the result

myDividend = int(input("type a dividend, please:"))
myDivisor = int(input("type a divisor, please:"))

try:
    myQuotient = myDividend / myDivisor
except ZeroDivisionError:
    print("you tried to divide by zero")
    myQuotient = 0
    
print(int(myQuotient))
print("end of program")    
