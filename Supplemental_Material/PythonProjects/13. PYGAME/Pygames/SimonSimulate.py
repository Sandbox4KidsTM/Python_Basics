import random, sys, time, pygame

FPS = 30
wWidth = 640
wHeight = 480
flashSpeed = 500 #milliseconds
flashDelay = 200
buttonSize = 200
buttonGapSize = 20
timeout = 4 #seconds before game over if no button is pushed

#color
white = (255,255,255)
red = (155,0,0)
brightRed = (255,0,0)
bgColor = (0,0,0)
darkGray = (40, 40, 40)

xMargin = int((wWidth - (2*buttonSize)/2))
yMargin = int((wHeight - (2*buttonSize)/2))

redRect = pygame.Rect(xMargin, yMargin + buttonSize + buttonGapSize, buttonSize, buttonSize)

def main():
    global fpsClock, displaySurf, basicFont, beep1, beep2, beep3, beep4
    
    pygame.init()
    fpsClock = pygame.time.Clock()
    displaySurf = pygame.display.set_mode((wWidth, wHeight))
    pygame.display.set_caption('Simon Simulate')
    
    BasicFont = pygame.font.Font('freesansbold.ttf', 16)
    infoSurf = BasicFont.render('Match the pattern by clicking on the button or using the Q, W, A, S keys.', 1, darkGray)
    infoRect = infoSurf.get.rect()
    infoRect.topleft = (10, wHeight - 25)
    
    #load the sournd files
    beep1 = pygame.mixer.Sound('beep1,ogg')
    beep2 = pygame.mixer.Sound('beep2,ogg')
    beep3 = pygame.mixer.Sound('beep3,ogg')
    beep4 = pygame.mixer.Sound('beep4,ogg')
    
    #initialize some varibales for a new game
    pattern = [] #stores the pattern of colors
    currentStep = 0 #the color the player must push next
    score = 0
    
    
    
    
    
    
    
    
    