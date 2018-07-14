#http://inventwithpython.com/pygame/chapter2.html
# download this image from http://invpy.com/cat.png
# download beep file from here download this image from http://www.bigsoundbank.com/sound-0342-censor-beep.html

# objective: move the cat across the 4 edges of the screen; it keeps going round and round;
import pygame, sys, time

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((350, 300), 0, 32)
pygame.display.set_caption('Animation')

soundObj = pygame.mixer.Sound('beep.wav')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'
i = True
DISPLAYSURF.fill(WHITE)


while True: # the main game loop

    if direction == 'right':
        catx += 5
        if catx >= 220:
            if i:
                direction = 'down'
            else:
                direction = 'up'
        i = not i
    elif direction == 'down':
        caty += 5
        catx -= 5
        if caty >= 220:
            direction = 'right'
    elif direction == 'left':
        catx -= 5
        if catx <= 10:
            direction = 'down'
    elif direction == 'up':
        caty -= 5
        catx -= 5
        if caty <= 10:
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #soundObj.play()
    time.sleep(0.1) # wait and let the sound play for 1 second
    #soundObj.stop()
    
    pygame.display.update()
    fpsClock.tick(FPS)
    
pygame.quit() #end pygame
sys.quit()