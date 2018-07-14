# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 20:37:28 2017

@author: Sandbox999
"""

"""
lists are one of the popular data structures in Python
they store an ordered/indexed list of items that you can access
lists are MODIFIABLE
"""

filelist = [2015, 2016, 2017]
print(type(filelist))

print(filelist)
print(filelist[2])

filelist.append(2018)
print(filelist)

print(filelist[1]-2000)
