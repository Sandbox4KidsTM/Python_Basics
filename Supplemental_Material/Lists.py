# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 15:30:22 2018

@author: Mitch Labrenz
"""

# Lists 
my_data = [1,3,5,7,9,11,13,23]

def mean(array):
    return sum(array) / len(array)

# List has to be sorted
def median(array):
        if len(array) % 2 == 1:
            midpoint = int(len(array) / 2)
            return array[midpoint]
        else:
            midpoint = int(len(array) / 2) - 1
            return mean(array[midpoint:midpoint+2])
        
# Dictionary
def mode(array):
    nums = {}
    for el in array:
        if not el in nums:
            nums[el] = array.count(el)
    modes, count = [],0
    for key, value in nums.items():
        if value > count:
            modes = [key]
            count = value
        elif value == count:
            modes.append(key)
    return modes

print("Mean:", mean(my_data))
print("Median:", median(my_data))
print("Modes:", mode(my_data))