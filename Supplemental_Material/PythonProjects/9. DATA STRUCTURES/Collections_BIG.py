# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 06:51:02 2017

@author: Sandbox999
"""

"""
Lists and Tuples are SEQUENCES i.e. ordered list of items
"""

#LISTS are modifiable i.e. mutable
filelist=[2015,2016,2017]

filelist.append(2018)

for item in filelist:
    print(item)
    
a = filelist[1]-2000
print(a)

#TUPLES are not modifiable i.e. immutable

filetuple=(2015,2016, 2017, 2015, 2015, 2017)

for item in filetuple:
    print(item)
    
print(filetuple.count(2015))

print(filetuple.index(2016))

"""
SETS & DICTIONARIES are COLLECTIONS i.e. UNordered list of items of unqiue items
"""

fileset={2015, 2017, 2017, 2016}
print(fileset)

filelist=[2015, 2016, 2016]
print(filelist)
filelist = set(filelist)
print(filelist) #converted to set, to remove duplicate items
filelist = list(filelist)
print(filelist) #converted back to sets

filedict={"last year":2016, "this year":2017, "next year":2018}
#keys & values
print(filedict["this year"])


