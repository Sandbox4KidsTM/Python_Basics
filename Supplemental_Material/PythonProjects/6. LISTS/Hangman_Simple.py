#hangman simple game built ground up

import time

name = input("what's your name?")
print("Hello, " + name + " let's play Hangman")
print("")

time.sleep(1)
print("start guessing...")
time.sleep(1)

word = "secret"
guesses = ''
turns = 10

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char,)
        else:
            print('_')
            failed = failed+1
    
    if failed == 0:
        print("you won")
        break
    
    myGuess = input("guess a character:")
    guesses = guesses + myGuess
    
    if myGuess not in word:
        turns = turns - 1
        print("wrong")
        print("You have ", turns, "turns remaining")
    
    if turns == 0:
        print("you lose")
    