# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 21:04:46 2017

@author: Sandbox999
"""
#this is Sandbox's Python Code

long_string = "   apple    pie1                             "

print(long_string[0:4])

print(long_string[-5:]) #print the last 5 characters

print(long_string[:-5]) #print up to the last 5 characters 

print(long_string[0:4] + " be there")

print("%c is my %s letter and my number %d is %.5f" %('x', "favourite", 1, .15))
#passing parameters using the % placeholder

print(long_string.capitalize()) #first letter of a sentence is upper case, rest is lowercase

print(long_string.find("Floor")) #index value of the start of the string #case sensitive

print(long_string.isalpha())

print(long_string.isalnum())

print(long_string.replace("pie", "fudge"))
print(long_string.strip())

quote_list = long_string[1:5]
print(quote_list)