# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 16:51:09 2018

@author: Mitch Labrenz
"""

heights = open("class_heights")

class_h = {}
# class_h["key"] = "value"

# print('a:b'.split(':')) 

for line in heights:
    key, value = line.split(' = ')
    key = key.lower()
    value = float(value.rstrip('\n'))
    class_h[key] = value
    
sum_h = 0
tallest = ""
t_h = 0
shortest = ""
s_h = 20

for name, height in class_h.items():
    sum_h += height
    if height > t_h:
        tallest = name
        t_h = height
    if height < s_h:
        shortest = name
        s_h = height

average_height = sum_h / len(class_h)
print("Tallest: ", tallest.capitalize())
print("Average Height: ", average_height)
print("Shortest: ", shortest.capitalize())        