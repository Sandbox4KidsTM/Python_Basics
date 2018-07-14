# race game that messages player when they crash into boundaries
# racing game with boundaries

import pygame, sys
import time
import random

pygame.init() #start pygame

display_width = 800
display_height = 600

black = (0,0,0) #RGB (red, green, blue)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A racing game')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')
car_width = 74

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0,0))

def things(thingX, thingY, thingW, thingH, color): #falling things/blocks for the car to avoid
    pygame.draw.circle(gameDisplay, color, [thingX, thingY], 50) #draw a box

def car(x,y):
    gameDisplay.blit(carImg, (x,y)) #blit() draws the image at (x,y)
    # note: origin is in the top right hand corner

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    textFont = pygame.font.Font('freesansbold.ttf', 60) #font type and font size
    TextSurf, TextRect = text_objects(text, textFont) #text_objects() function needs to be defined
    # this is like insert-text in word: there is an encasing rectangle contained in the surface
    TextRect.center = ((display_width/2), (display_height/2)) #middle of the screen
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update() #update the screen

    time.sleep(2) #wait for 2 seconds beore the game resets/restarts
    game_loop() #to reset the game

def crash():
    message_display('You CRASHED!!!') #message_display() is a function that needs to be defined

def game_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    #things(thingX, thingY, thingW, thingH, color)
    thing_startX = random.randrange(0, display_width) #where the thing starts to fall
    thing_startY = -600 #600 pixels off the screen
    thing_width = 100
    thing_height = 100 #a rectangle of 100x100 pixles
    thing_speed = 7

    dodged = 0
    gameExit = False #crashed is changed to gameExit
    
    key_l = pygame.K_a
    key_r = pygame.K_d

    while not gameExit:
        for event in pygame.event.get(): #gets all the events per frame per second
                if event.type == pygame.QUIT:
                    #gameExit = True #break out of the while loop
                    pygame.quit() #end pygame
                    quit()

                if event.type == pygame.KEYDOWN: #move left or right
                    if event.key == key_l:
                        x_change = -5
                    if event.key == key_r:
                        x_change = 5

                if event.type == pygame.KEYUP: #no change when key is released
                    if event.key == key_l or event.key == key_r:
                        x_change = 0

        gameDisplay.fill(white)
        #things(thingX, thingY, thingW, thingH, color)
        things(thing_startX, thing_startY, thing_width, thing_height, black)
        thing_startY = thing_startY + thing_speed
        
        x = x + x_change #new coordinate for x
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0: #boundary
            crash() #gameExit = True is replaced with crash() function

        if thing_startY > display_height:
            thing_startY = 0 - thing_height
            thing_startX = random.randrange(0, display_width) #where the thing restarts to fall
            dodged += 1    

        #check if the things collided into the car
        if y < (thing_startY + thing_height):
            print('thingY crossed-over the car')
            if ((x > thing_startX) and (x < (thing_startX + thing_width))
                or ((x + car_width > thing_startX) and ((x + car_width) < thing_startX + thing_width))):
                    print('thingX crossed-over the car' )
                    crash()    

        pygame.display.update() #update the screen
        clock.tick(60) #how fast do you want to want to display in frames per second

game_loop()
pygame.quit() #end pygame
sys.quit() #end Python Program Execution

