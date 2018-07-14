# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 09:30:45 2017

@author: Sandbox999
"""
#this is Sandbox's Python Code
# print prime numbers up to a given upper limit

def checkPrime(n):
    factors = 0
    i = 2
    while i < n:
        if n % i == 0:
            factors = factors + 1
            break
        i = i + 1
    if factors == 0:
        return(n)

m = int(input("enter until what number you want primes listed: "))
j = 2
while j <= m:
    if checkPrime(j) != None:
        print(checkPrime(j))
    j = j + 1