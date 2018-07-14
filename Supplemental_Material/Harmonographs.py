# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 14:41:58 2018

@author: Mitch Labrenz
"""

import pygame, sys, random as r
from pygame.locals import *
from math import pi, sin, cos, exp

width, height = 1920,1080
dd=0.99995
dt=0.02
speed=100
hui=57*2
hue,sat,val,aaa=0,100,100,0
sd=0.001
mx=4

def check_event():
    global save
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()
def scale(length):
    while True:
        a1,a2=r.randint(-mx,mx),r.randint(-mx,mx)
        max1 = abs(a1)+abs(a2)
        if max1 > 0: break
    return a1,a2, (length/(2*max1))
steps=0
pygame.init()
pygame.event.set_allowed([QUIT,KEYDOWN])
screen = pygame.display.set_mode((width,height),DOUBLEBUF)
screen.set_alpha(None)
fg=pygame.Color(0,0,0,0)
save=False

while True:
    ax1,ax2,xscale=scale(width)
    ay1,ay2,yscale=scale(height)
    fx1,fx2 = r.randint(1,mx) + r.gauss(0,sd), r.randint(1,mx) + r.gauss(0,sd)
    fy1,fy2 = r.randint(1,mx) + r.gauss(0,sd), r.randint(1,mx) + r.gauss(0,sd)
    px1, px2 = r.uniform(0,2*pi), r.uniform(0,2*pi)
    py1, py2 = r.uniform(0,2*pi), r.uniform(0, 2*pi)
    
    dec = 1.0
    t = 0.0
    first = True
    while dec>0.015:
        x = xscale * dec * (ax1 * sin(t * fx1 + px1) + ax2*sin(t * fx2 + px2)) + width/2
        y = yscale * dec * (ay1 * sin(t * fy1 + py1) + ay2 * sin(t * fy2 + py2)) + height/2
        dec *=dd
        if not first:
            fg.hsva=(hue,sat,val,aaa)
            hue = (hue + dt*hui) % 360
            pygame.draw.aaline(screen,fg, (x,y), (prev_x, prev_y),1)
        else:
            first = False
        prev_x = x
        prev_y = y
        if steps%speed==0: pygame.display.update()
        steps+=1
        t+=dt
        check_event()
    
    screen.fill((0,0,0))