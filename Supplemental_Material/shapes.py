# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 16:49:24 2018

@author: Mitch Labrenz
"""

import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(2)

def draw_house():
    for __i in range(0,4):
        t.forward(60)
        t.left(90)

    t.left(90)
    t.forward(60)
    t.right(90)

    for i in range(0,3):
        t.forward(60)
        t.left(120)

draw_house()
t.penup()
t.goto(-60,0)
t.pendown()
draw_house()

s = turtle.Screen()
s.exitonclick()