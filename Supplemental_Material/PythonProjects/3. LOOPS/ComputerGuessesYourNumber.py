# This is a guess the number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

lowerLimit = 1
upperLimit = 20

print('Well, ' + myName + ', you think of a number between 1 and 20.')

while guessesTaken < 6:
     computerGuess = random.randint(lowerLimit, upperLimit)
     print("is it",computerGuess) # There are four spaces in front of print.
     check = input()
     check = int(check)

     guessesTaken = guessesTaken + 1

     if check == 0:
         print('My guess was too LOW.') # There are eight spaces in front of print.
         lowerLimit = computerGuess
        
     if check == 1:
         print('My guess was RIGHT.')
         break
       
     if check == 2:
         print('My guess was too HIGH.')
         upperLimit = computerGuess

if check == 1:
      guessesTaken = str(guessesTaken)
      print('I am awesome, ' + myName + '! I guessed my number in ' + guessesTaken + ' guesses!')

if check != 1:
      print('Am not feeling awesome today. You win!')