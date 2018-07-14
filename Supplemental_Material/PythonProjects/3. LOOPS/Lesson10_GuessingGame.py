# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 21:41:46 2017

@author: Sandbox999
"""
# this is number guessing game
# this is how you do a single-line comment

import random #imports libary

guessesTaken = 0

print("Hello, what's your name?")
myName=input()

number = random.randint(1,10)
print('well, '+myName+ ', I am thinking of a number between 1 and 10')

while guessesTaken<5: #you have 5 attempts to guess the number
    print('Take a guess')
    guess = input()
    guess=int(guess)
    
    guessesTaken = guessesTaken+1
    
    if guess > number:
        print('your number is too high')
    
    if guess < number:
        print('your number is too low')
        
    if guess == number:
        print('good job')
        break
    
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, '+myName+ ', you guessed in '+guessesTaken+ ' attempt(s)!')

