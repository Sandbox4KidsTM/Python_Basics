import pygame
import random
import time 

white = (255,255,255)
black = (0,0,0)
pygame.init()
myClock = pygame.time.Clock()

blueButton = pygame.image.load("blueButton.jpg")
yellowButton = pygame.image.load("yellowButton.jpg")
redButton = pygame.image.load("redButton.jpg")
greenButton = pygame.image.load("greenButton.jpg")

wWidth = 1000
wHeight = 800

def main():
    global fpsClock, gameDisplay, basicFont, beep1, beep2, beep3, beep4
    
    pygame.init()
    fpsClock = pygame.time.Clock()
    gameDisplay = pygame.display.set_mode((wWidth, wHeight))
    pygame.display.set_caption('Simon Simulate')
    
    BasicFont = pygame.font.Font('freesansbold.ttf', 16)
    infoSurf = BasicFont.render('Match the pattern by clicking on the button or using the Q, W, A, S keys.', 1, black)
    infoRect = infoSurf.get_rect()
    infoRect.topleft = (10, wHeight - 25)
    
    #load the sournd files
    beep1 = pygame.mixer.Sound('beep1.ogg')
    beep2 = pygame.mixer.Sound('beep2.ogg')
    beep3 = pygame.mixer.Sound('beep3.ogg')
    beep4 = pygame.mixer.Sound('beep4.ogg')
    
    #initialize some varibales for a new game
    pattern = [] #stores the pattern of colors
    currentStep = 0 #the color the player must push next
    score = 0

    crashed = False
    
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            print(event)
        
        for i in range(1, 5):
            randColor = random.randint(1,4)
            if randColor == 1:
                    someButton = redButton
            if randColor == 2:
                    someButton = blueButton
            if randColor == 3:
                    someButton = greenButton
            if randColor == 4:
                    someButton = yellowButton
            
            gameDisplay.fill(white)
            gameDisplay.blit(redButton,(200,50))
            gameDisplay.blit(blueButton,(400,50))
            gameDisplay.blit(yellowButton,(600,50))
            gameDisplay.blit(greenButton,(800,50))
            
            gameDisplay.blit(someButton,(300,300))
        time.sleep(10)
        
        pygame.display.update()
        myClock.tick(1)
        
main()
pygame.quit()
quit()