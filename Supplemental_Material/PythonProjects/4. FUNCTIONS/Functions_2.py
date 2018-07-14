# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 09:35:20 2017

@author: Sandbox999
"""
#this is Sandbox's Python Code
# more details on functions

#functions with more than one variables

def min_to_hrs(minutes, seconds=60): #60 is the argument's default value
#NOTE: non-default argument cannot follow a default argument value
    hours = (minutes/60) + (seconds/3600)
    return hours

print(min_to_hrs(480,720))

#print(min_to_hrs(480))
#if you skip entering an argument, it throws an error
#TypeError: min_to_hrs() missing 1 required positional argument: 'seconds'