# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 14:08:16 2018

@author: Mitch Labrenz
"""

from turtle import *
from random import randint

speed(0)
bgcolor('black')

def one():
    x = 1
    
    while x < 400:
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        
        colormode(255)
        pencolor(r,g,b)
        forward(50+x)
        right(600.911)
        x = x+1
        
def two():
    colors = ["blue", "purple", "red", "white","orange", "green"]
    for x in range(300):
        color(colors[x%6])
        fd(x)
        left(59)
    
two()
exitonclick()