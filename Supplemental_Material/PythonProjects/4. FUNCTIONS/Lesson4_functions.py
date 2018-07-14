# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 20:25:36 2017

@author: Sandbox999
"""

def currencyConverter(inmoney, rate):
    print(inmoney*rate)
    
currencyConverter(1, 0.9)

def authenticate(password):
    if password=="hey":
        print("you are good to go!")
    else:
        print("you belong here")
        
authenticate("heyyy")


def miles2km(miles):
    print(miles*1.6)
    
miles2km(100)


def areaRect(length, breadth):
    area = length*breadth
    return(area)

print(areaRect(10, 20))

def conCat(firstName, lastName):
    fullName = firstName+" "+lastName
    return(fullName)
print(conCat("John", "Wayne"))
