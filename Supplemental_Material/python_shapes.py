# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:52:33 2018

@author: Mitch Labrenz
"""

import turtle
import math
import time

turtle.speed(0)
def drawPolygon(size, sides):
    for i in range(0,sides):
        turtle.forward(size)
        turtle.left(360/sides)
        
def drawCircleInPolygon(size,sides):
    drawPolygon(size,sides)
    turtle.forward(size/2.0)
    turtle.circle(size / (2*abs(math.tan(math.radians(180/sides)))))
    turtle.backward(size/2.0)

def drawPattern(size,sides):
    for i in range(0,12):
        drawCircleInPolygon(size,sides)
        turtle.right(30)
        turtle.forward(size/math.tan(math.radians(180/sides)))
        
def drawPattern2(size):
    turtle.backward(300)
    for i in range(0,10):
        drawCircleInPolygon(size,3)
        turtle.forward(size)

def drawGrid():
    turtle.back(500)
    for i in range(0,100):
        for k in range(0,100):
            drawPolygon(10,4)
            turtle.forward(10)
        turtle.back(1000)
        turtle.left(90)
        turtle.forward(10)
        turtle.right(90)
        
def drawGrid2(size, width,height):
    turtle.pu()
    turtle.back(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.pd()
    for i in range(0,int(height * 2/size)):
        turtle.forward(width * 2)
        if i % 2 == 0:
            turtle.left(90)
            turtle.forward(size)
            turtle.left(90)
        else:
            turtle.right(90)
            turtle.forward(size)
            turtle.right(90)
    turtle.forward(width*2)
    turtle.right(90)
    for i in range(0,int(width*2/size)):
        turtle.forward(height*2)
        if i % 2 == 1:
            turtle.left(90)
            turtle.forward(size)
            turtle.left(90)
        else:
            turtle.right(90)
            turtle.forward(size)
            turtle.right(90)
    turtle.forward(height*2)
        
            
        
    

def moveUp():
    turtle.setheading(90)
    turtle.forward(10)
def moveRight():
    turtle.setheading(0)
    turtle.forward(10)
def moveLeft():
    turtle.setheading(180)
    turtle.forward(10)
def moveDown():
    turtle.setheading(270)
    turtle.forward(10)
def turtleToggle():
    if turtle.isdown():
        turtle.pu()
    else:
        turtle.pd()
def Green():
    turtle.color("#00FF00")
def Red():
    turtle.color("Red")
def Blue():
    turtle.color("Blue")
def move():
    turtle.forward(5)
    time.sleep(0.05)
def run():
    global Running 
    Running = not Running

Running = True
window = turtle.Screen()
window.onkey(moveUp, "w")
window.onkey(Green, "g")
window.onkey(Blue, "b")
window.onkey(Red, "r")
window.onkey(moveDown, "s")
window.onkey(moveLeft, "a")
window.onkey(run,"t")
window.onkey(moveRight, "d")
window.onkey(turtleToggle,"space")
window.listen()
#while True:
#    if Running:
#        move()
#    else:
#        break
#turtle.backward(500)
drawGrid2(10,1000,540)
turtle.home()
#drawPattern2(70)
turtle.done()