# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 20:50:27 2017

@author: Sandbox999
"""

"""
Set is a unique collection of unordered items
Sets use curly brackets
"""

fileset={2015, 2016, 2019}
print(fileset)
print(type(fileset))

filelist=[2015, 2015, 2015, 2017, 2017]
print(type(filelist))

filelist=set(filelist)
print(type(filelist))
print(filelist)

""" filelist got converted from list to set after non-unique items were removed with the set() function """

filelist=list(filelist)
print(type(filelist))
print(filelist)