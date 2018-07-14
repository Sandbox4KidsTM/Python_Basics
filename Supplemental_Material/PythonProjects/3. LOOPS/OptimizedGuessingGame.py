# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 13:47:32 2017

@author: Sandbox999
"""

print("welcome to optimized guessing game")
print("pick a number between 1 and 16")
print("type 0, 1 or 2, depending on whether my guess is less, equal or more than your secret number")

lowerLimit = 1
upperLimit = 16

while 0 < 1:
    cpuGuess = round((lowerLimit + upperLimit)/2)
    print(cpuGuess)
    humanFeedback = int(input())
    
    if humanFeedback == 1:
        print("I got it!")
        break
        
    if humanFeedback == 0:
        print("my guess was too low")
        lowerLimit = cpuGuess
        
    if humanFeedback == 2:
        print("my guess was too high")
        upperLimit = cpuGuess