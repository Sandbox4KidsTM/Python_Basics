# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 09:08:30 2017

@author: Sandbox999
"""
#this is Sandbox's Python Code
#user defined functions a.k.a. custom functions
# min_to_hrs() is a custom function
# print() and input() are built-in functions


minutesInput=int(input("enter the minutes you want to convert to hours: "))


def min_to_hrs(minutes):
    hours = minutes/60
    return hours

print(min_to_hrs(minutesInput))

