#random insults generator using IF-ELIF Statements and Function

import random

def insultMe():
        insult = random.randint(1,3)
        if      insult == 1:
                print("gogo")
        elif    insult == 2:
                print("bobo")  
        elif    insult == 3:
                print("nono")
        
state = True
while state == True:
    insultMe()
    check = input("what's the magic word?")
    if (check == "quit"):
        state = False
    else:
        state = True