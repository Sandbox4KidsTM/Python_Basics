# https://www.raywenderlich.com/24252/beginning-game-programming-for-teens-with-python
# 1 - Import library
import pygame
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))

keys = [False, False, False, False] #track state of 4 keys: W, A, S, D, whether pressed or not
playerpos=[100,100] #track position of player 'bunny'

# 3 - Load images
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    #grass image is not large enough to fill the screen, hence you tile it.
    for x in range(int(width/grass.get_width())+1):
        for y in range(int(height/grass.get_height())+1):
                screen.blit(grass,(x*100,y*100))
        screen.blit(castle,(0,30)) #post 4 castles at diff positions on screen
        screen.blit(castle,(0,135))
        screen.blit(castle,(0,240))
        screen.blit(castle,(0,345 ))
    
     screen.blit(player, playerpos) #player 'bunny' position on the screen
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0) 