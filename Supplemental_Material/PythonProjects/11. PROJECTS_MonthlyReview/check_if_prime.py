# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 09:18:44 2017

@author: Sandbox999
"""
#this is Sandbox's Python Code

#check if prime

n = int(input("enter a number to check if it is prime: "))
a = int(n/2)
#print(a)
factors = 0
i = 2
while i <= a:
    if n % i == 0:
        print(n, "is not a prime")
        factors = factors + 1
        break
    i = i + 1
    
if factors == 0:
    print(n, "is a prime")
