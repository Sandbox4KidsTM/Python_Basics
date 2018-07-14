#solving single variable equation

#import math

singleVar = input("enter a single variable equation in the form: ax + b = c: ")
print(singleVar)

terms = singleVar.split(" ")
print(terms)

a, rhs = terms[0].split("x")
a = int(a)
print("a is", a)

b = terms[2]
b = int(b)
if terms[1] == '-':
    b = -1*b
print("b is", b)

c = terms[4]
c = int(c)
print("c is", c)

soln = (c - b) / a
print("solution is", soln)