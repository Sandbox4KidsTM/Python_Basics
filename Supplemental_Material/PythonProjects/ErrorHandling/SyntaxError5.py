# -*- coding: utf-8 -*-

def factorial(a):
   fac = 1
   while a >= 0:
       fac = fac * a
       a = a - 1
   return fac

print(factorial(10)) #NameError: name 'factorial' is not defined
# function should be defined before it is used


