# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 22:53:59 2017

@author: Sandbox999
"""
#this is Sandbox's Python Code

# https://www.datacamp.com/community/tutorials/loops-python-tutorial

# Initialize the first five rows
n = 5

# Start the loop to print the first five rows
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')

# Start the loop to print the remaining rows in decreasing order of stars
for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')