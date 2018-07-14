# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 20:05:14 2017

@author: Sandbox999
"""
#this is Sandbox's Python Code

def binary_search(list, item):
    low = 0
    high = len(list)-1
    
    while low <= high:
        mid = (low+ high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid-1
        else:
            low = mid+1
    return None
my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 9))