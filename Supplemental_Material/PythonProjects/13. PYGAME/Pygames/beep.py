import pygame
import time

pygame.init()

soundObj = pygame.mixer.Sound('beep1.ogg')

beep2 = pygame.mixer.Sound('beep2.ogg')

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

time.sleep(5)

i = 0

while i < 5:
    soundObj.play()
    time.sleep(1.5) # wait and let the sound play for 1 second
    soundObj.stop()
    time.sleep(.5)
    beep2.play()
    time.sleep(1.5)
    beep2.stop()
    i = i + 1

pygame.quit() #end pygame    