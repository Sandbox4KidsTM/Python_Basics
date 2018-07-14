# solving a quadratic equation simply
import math

quad = input("enter a standard quadratic equation, enter 1 if coefficient is 1: 1x^2 - 5x + 6 = 0\n")
print(quad)

terms = quad.split(" ")
print(terms)

a, rhs = terms[0].split("x^2")
a = int(a)
print("a is", a)

b, rhs = terms[2].split("x")
b = int(b)
if terms[1] == '-':
    b = -1*b
print("b is", b)

c = terms[4]
c = int(c)
print("c is", c)

sol1 = (-1*b + math.sqrt(b*b - 4*a*c))/(2*a)
print("solution 1 is", sol1)

sol2 = (-1*b - math.sqrt(b*b - 4*a*c))/(2*a)
print("solution 2 is", sol2)