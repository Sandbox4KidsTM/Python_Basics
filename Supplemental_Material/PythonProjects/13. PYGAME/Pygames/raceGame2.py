# racing game with boundaries

import pygame

pygame.init() #start pygame

#variables for game window dimension
display_width = 800 
display_height = 600

black = (0,0,0) #RGB (red, green, blue) #absense of colors is black
white = (255, 255, 255) #all colors mixed give white
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height)) #game window
pygame.display.set_caption('A racing game')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png') #load the image in the background
car_width = 74

def car(x,y):
    gameDisplay.blit(carImg, (x,y)) #blit() function draws image carImg at (x,y)
    # note: origin is in the top right hand corner of the screen
    #display in the foreground

def game_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.8)
    
    x_change = 0
    
    gameExit = False #crashed is changed to gameExit
    
    while not gameExit:
        for event in pygame.event.get(): #gets all the events per frame per second
                if event.type == pygame.QUIT:
                    gameExit = True #break out of the while loop
                    
                if event.type == pygame.KEYDOWN: #move left or right
                    if event.key == pygame.K_LEFT:
                        x_change = -5
                    if event.key == pygame.K_RIGHT:
                        x_change = 5
                
                if event.type == pygame.KEYUP: #no change when key is released
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0
                
        gameDisplay.fill(white) #background color of game window
        x = x + x_change #new coordinate for x
        car(x,y)
        # note: nothing is actually moving on the computer
        # image is being redrawn a little to left or right, giving the impression that it is moving
        
        if x > display_width - car_width or x < 0: #boundary
            gameExit = True
        
        pygame.display.update() #update the screen
        clock.tick(60) #how fast do you want to want to display in frames per second
    
game_loop()    
pygame.quit() #end pygame
quit()
    
           