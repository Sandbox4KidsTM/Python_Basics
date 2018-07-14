# randomly adds or multiplies
import random

def addT(x,y):
    d = x+y
    return(d)

def mulT(x,y):
    return(x*y)

a = int(input("enter first num: "))
b = int(input("enter second num: "))

c = 0
r = random.randint(0,1) #toss on a coin
if r == 0:
    c = addT(a,b) #function call
else:
    c = mulT(a,b)

print(c)