import pygame
import time

pygame.init()


DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('BGND & FGND Music')

# Loading background music:
pygame.mixer.music.load('ElectricLight.wav')
soundObj = pygame.mixer.Sound('beep.wav')




while True:
    soundObj.play()
    time.sleep(1) # wait and let the sound play for 1 second
    soundObj.stop()
    
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.stop()

pygame.quit() #end pygame
quit()