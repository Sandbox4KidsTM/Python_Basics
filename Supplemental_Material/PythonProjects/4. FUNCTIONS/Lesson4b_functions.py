# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 07:11:02 2017

@author: Sandbox999
"""

def milesToKm(miles):
    km=miles*1.609344
    return km

print(milesToKm(10))


def milesToKm2(miles):
    global km #making a variable global makes it accessible outside of the function
    km=miles*1.609344
    return km

print(milesToKm2(10))
print(km)