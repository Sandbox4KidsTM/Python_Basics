# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 22:44:56 2017

@author: Sandbox999
"""

import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True: # main game loop
    for event in pygame.event.get():
         if event.type == QUIT:
             pygame.quit()
             sys.exit()
    pygame.display.update()