import turtle as t
import random #

t.shape("turtle")
t.speed(1) #speed of the turtle
t.clear() #clear the screen

t.penup()
t.setpos(random.randint(-200, 200),random.randint(-200,200))
t.pendown()

sides = random.randint(3,12)

for count in range(sides): #sides, instead of hardcoding
    t.forward(20)
    t.left(360/sides) #external angle
    t.write(count+1) #print the count on the window

t.exitonclick() #close window when you click on X