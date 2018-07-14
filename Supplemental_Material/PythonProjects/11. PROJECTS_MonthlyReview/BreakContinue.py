# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 21:48:15 2017

@author: Sandbox999
"""
#this is Sandbox's Python Code
# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
    
# break is used to exit a for loop or a while loop, 
#whereas continue is used to skip the current block, and return to the "for" or "while" statement.