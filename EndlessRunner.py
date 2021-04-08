import pygame
import sys
from pygame.locals import *

# #Constants
NAVY = (40, 40, 80)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
# #Set up window
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))  # #TODO: Change to monitor size

pygame.display.set_caption('Hello World')
DISPLAYSURF.fill(NAVY)


class GameObject:
    def __init__(self, color, width, height, xpos, ypos):
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.pos = self.rect.move(xpos, ypos)
        self.ax = 0
        self.ay = 0

    def move(self):
        # #shift position by (ax,ay)
        self.pos = self.pos.move(self.ax, self.ay)

        # #loop the character if it falls off the edge of screen
        if self.pos.right > 400:
            self.pos.left = 0
        if self.pos.left < 0:
            self.pos.right = 400
        if self.pos.top > 300:
            self.pos.bottom = 0
        if self.pos.bottom < 0:
            self.pos.top = 300


def check_collision():
    for x in allObjects:
        if (
                ((player.pos.left <= x.pos.left <= player.pos.right) or
                 (player.pos.left <= x.pos.right <= player.pos.right)) and
                ((player.pos.top <= x.pos.top <= player.pos.bottom) or
                 (player.pos.top <= x.pos.bottom <= player.pos.bottom))
        ):
            x.image.fill(RED)


player = GameObject(WHITE, 10, 10, 200, 150)
not_player = GameObject(BLACK, 10, 10, 20, 20)

allObjects = []

allObjects.append(not_player)

# #Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # #set player acceleration when key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.ax -= 10
            if event.key == pygame.K_RIGHT:
                player.ax += 10
            if event.key == pygame.K_UP:
                player.ay -= 10
            if event.key == pygame.K_DOWN:
                player.ay += 10
        # #reset player acceleration when key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.ax += 10
            if event.key == pygame.K_RIGHT:
                player.ax -= 10
            if event.key == pygame.K_UP:
                player.ay += 10
            if event.key == pygame.K_DOWN:
                player.ay -= 10

    player.move()
    check_collision()

    DISPLAYSURF.fill(NAVY)

    DISPLAYSURF.blit(not_player.image, not_player.pos)
    DISPLAYSURF.blit(player.image, player.pos)
    pygame.display.update()
    pygame.time.delay(50)
