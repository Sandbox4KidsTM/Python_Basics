#racing game
import pygame

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

def car(x,y):
    gameDisplay.blit(carImg, (x,y)) #blit() draws the image at (x,y)
    # note: origin is in the top right hand corner

x = (display_width * 0.45)
y = (display_height * 0.8)

x_change = 0

crashed = False

while not crashed:
    for event in pygame.event.get(): #gets all the events per frame per second
            if event.type == pygame.QUIT:
                crashed = True #break out of the while loop
                
            if event.type == pygame.KEYDOWN: #move left or right
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            
            if event.type == pygame.KEYUP: #no change when key is released
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            
    gameDisplay.fill(white)
    x = x + x_change #new coordinate for x
    car(x,y)
    pygame.display.update() #update the screen
    clock.tick(60) #how fast do you want to want to display in frames per second
    
pygame.quit() #end pygame
quit()
    
           