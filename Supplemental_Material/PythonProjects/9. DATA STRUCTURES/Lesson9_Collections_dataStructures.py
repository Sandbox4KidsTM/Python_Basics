# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 21:03:45 2017

@author: Sandbox999
"""

filelist=list(range(2000,2020, 2)) 
"""2 indicates range here"""
print(filelist)

print(filelist[2])

print(filelist[2:5])
"""note: upperbound is NOT included i.e. upperbound-excluded"""

print(filelist[0:3])

print(filelist[:3])
"""everything up until item #3"""

print(filelist[2:])