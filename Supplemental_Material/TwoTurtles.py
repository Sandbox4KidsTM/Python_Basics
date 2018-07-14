# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 13:39:24 2018

@author: Mitch Labrenz
"""

from turtle import *

def moveUp():
    t1.setheading(90)
    t1.forward(10)
def moveRight():
    t1.setheading(0)
    t1.forward(10)
def moveLeft():
    t1.setheading(180)
    t1.forward(10)
def moveDown():
    t1.setheading(270)
    t1.forward(10)

def moveUp2():
    t2.setheading(90)
    t2.forward(10)
def moveRight2():
    t2.setheading(0)
    t2.forward(10)
def moveLeft2():
    t2.setheading(180)
    t2.forward(10)
def moveDown2():
    t2.setheading(270)
    t2.forward(10)

t1 = Turtle()
t2 = Turtle()
t2.color("Blue")
t2.pu()
t2.forward(50)
t2.pd()

window = Screen()
window.onkey(moveUp, "w")
window.onkey(moveUp2, "Up")
window.onkey(moveDown2, "Down")
window.onkey(moveRight2, "Right")
window.onkey(moveDown, "s")
window.onkey(moveLeft, "a")
window.onkey(moveLeft2,"Left")
window.onkey(moveRight, "d")
window.listen()


done()