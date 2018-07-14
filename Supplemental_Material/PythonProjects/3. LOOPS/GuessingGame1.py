# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 13:08:49 2017

@author: Sandbox999
"""

import random

print(random.randint(1, 100))

print("what's your age?")
age = input()
age = int(age)

if age > 75:
    print("you get free movie tickets")
else:
    print("buy your own tickets")
    
# this is a comment