import turtle as t

t.speed(1)
t.clear()

for count in range(6):
    t.forward(100)
    t.left(60)
    t.write(count+1) #print the count on the window

t.exitonclick() #close window when you click on X