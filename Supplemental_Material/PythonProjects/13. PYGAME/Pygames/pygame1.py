#sentdex YouTube Video Tutorial Series
#first pygame with basic window
import pygame #import pygame module

pygame.init() #start pygame #pygame is an instance, hence need to instantiate it
gameDisplay = pygame.display.set_mode((800, 600)) #resolution of the game window
#set_mode() expects a tuple, not 2 parameters, hence (800,600) is a tuple
pygame.display.set_caption('A racing game') #title of the game window
clock = pygame.time.Clock() #clock for game

crashed = False

while not crashed:
    for event in pygame.event.get(): #gets all the events per frame per second
            if event.type == pygame.QUIT:
                crashed = True #break out of the while loop
    
            print(event) #print all the events in the console
    
    pygame.display.update() #update the screen #udpates just the current window
    # alternate is pygame.display.flip() #updates the entire surface (all windows)
    clock.tick(60) #how fast do you want to want to display in frames per second
    
pygame.quit() #end pygame
quit()
    
            
    