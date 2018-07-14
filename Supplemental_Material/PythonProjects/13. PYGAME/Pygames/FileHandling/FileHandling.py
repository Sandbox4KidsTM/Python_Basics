# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 16:07:28 2018

@author: Mitch Labrenz
"""

# Recursion and File Handling
file = open("input.txt", 'r')

out = open("output.txt", 'w')

# firstLine= file.readline()
# secondline = file.readline()
# print(firstline)
# print(secondline)
# file.readline()

fibonacci = []

for line in file:
    line = line.rstrip('\n')
    if line.isnumeric():
        fibonacci.append(int(line))
        
print(fibonacci)

lucas_number = [2,1]
for i in range(0,7):
    secondLast = lucas_number[i]
    last = lucas_number[i+1]
    lucas_number.append(last + secondLast)
    
print(lucas_number)

for element in lucas_number:
    out.write(str(element)+"\n")