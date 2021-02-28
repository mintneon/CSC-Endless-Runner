import pygame, sys
from pygame.locals import *

#Constants
NAVY = (40, 40, 80)

#Set up window
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300)) #TODO: Change to monitor size
pygame.display.set_caption('Hello World')
DISPLAYSURF.fill(NAVY)

#Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
