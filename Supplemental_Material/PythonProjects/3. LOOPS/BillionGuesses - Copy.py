# computer will guess any number between 1 and 1 16 in 4 or fewer attempts

# This is a guess the number game.
import random
import time

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

lowerLimit = 1
upperLimit = 1000000

print('Well, ' + myName + ', you think of a number between 1 and 1000000')
print('type "0" if Computer''s Guess is lower than your number')
print('type "2" if Computer''s Guess is higher than your number')
print('type "1" if Computer''s Guess is equal to your number')

print('come on, pick a number and write it down and truthly answer the following questions.')

time.sleep(3)

while guessesTaken < 31:
     computerGuess = round(((lowerLimit+upperLimit)/2)-1)
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


time.sleep(10)
