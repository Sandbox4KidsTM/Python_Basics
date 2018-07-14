# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 06:32:11 2017

@author: Sandbox999
"""
#this is Sandbox's Python Code
#String Manipulation Techniques...



def left(string, numberOfCharacters):
    return string[:numberOfCharacters]

def right(string, numberOfCharacters):
    return string[-numberOfCharacters:]

def mid(string, start, numberOfCharacters):
    return string[start:start+numberOfCharacters]

def length(string):
    return len(string)
    
def locate(stringToFind, string):
    return string.find(stringToFind)

#Main Program Starts Here    
print("##### String Manipulation Techniques #####")
myString = "Hello World"
print("Our String is: \"Hello World\"")

print("\nLENGTH:")
print(len(myString))

print("\nThe left 2 characters are:")
print(left(myString,2))

print("\nThe right 5 characters are:")
print(right(myString,5))

print("\nExtracting 5 characters from the 4th character:")
print(mid(myString,3,5))

print("\nSearching for the position of word \"World\" in our string:")
print(locate("World", myString))

print("\nSearching for the position of word \"Universe\" in our string:")
print(locate("Universe", myString))