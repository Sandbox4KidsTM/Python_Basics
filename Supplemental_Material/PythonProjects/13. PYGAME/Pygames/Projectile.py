import pygame, sys
import time

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Rocket Projectile Animation')

WHITE = (255, 255, 255)
rImg = pygame.image.load('rocket.png')
Rx = 1
Ry = 1

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
y = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]

i = 0
while True: # the main game loop
    DISPLAYSURF.fill(WHITE)
    
    DISPLAYSURF.blit(rImg, (Rx, Ry))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    Rx = x[i]
    Ry = x[i] #Rx^2
    time.sleep(0.3) # wait and let the sound play for 1 second
   
    pygame.display.update()
    fpsClock.tick(FPS)
    i = i + 1
    
pygame.quit() #end pygame
quit()