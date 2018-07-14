import turtle as t
import random 

t.clear() 
t.shape("turtle")

for x in range(100):
    t.penup()
    t.setpos(random.randint(-300, 300),random.randint(-300,300))
    t.pendown()
    t.color('red')
    t.stamp()