# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 20:58:28 2017

@author: Sandbox999
"""

"""Dictionaries are data stuctures
you can define your own indices
index/key (e.g. "this year") and value (e.g. "next year") pairs are stored in dictionaries
"""

filedict={"last year":2016, "this year":2017, "next year":2018}
print(filedict["next year"])
print(filedict[1]) 
"""this gives an error:KeyError: 1"""