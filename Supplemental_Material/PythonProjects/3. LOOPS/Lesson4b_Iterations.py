# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 06:47:17 2017

@author: Sandbox999
"""

filelist=[2015, 2016, 2017]
for item in filelist:
    print(item)
    

for item in range(2015, 2030, 2):
    print(item)
    
print() #prints a blank line

for item in range(2015, 2030, 2):
    if item!=2025: #== equals, != not equals
        print(item)