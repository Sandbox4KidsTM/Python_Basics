# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:17:18 2017

@author: Sandbox999
"""
#this is Sandbox's Python Code
# functions: reuse and write more readable code

import random
import sys
import os

def addNumber(fNum, lNum):
    sumNum = fNum * lNum
    return sumNum

#print(sumNum) #sumNum is a local variable and is not accessible to the code outside the function definition
print(addNumber(1,9))