# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 20:58:54 2017

@author: Sandbox999
"""

import pandas
import glob2

df = pandas.read_csv("C:\\in\\DataAnalysis\\File1.txt")

print(df)
print(type(df))

print(df.mean())

filelist = glob2.glob("C:\\in\\DataAnalysis\\*.txt")

print(filelist)
print(type(filelist))

for file in filelist:
    df = pandas.read_csv(file)
    print(file)
    m = int(df.mean())
    print(m)
    print(type(m))
