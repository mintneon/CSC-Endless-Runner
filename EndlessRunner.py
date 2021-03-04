import pygame
import sys
from pygame.locals import *

# #Constants
NAVY = (40, 40, 80)
WHITE = (255, 255, 255)
# #Set up window
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))  # #TODO: Change to monitor size

pygame.display.set_caption('Hello World')
DISPLAYSURF.fill(NAVY)


class GameObject:
    def __init__(self, color, width, height):
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.pos = self.rect.move(200, 150)
        self.ax = 0
        self.ay = 0

    def move(self):
        self.pos = self.pos.move(self.ax, self.ay)
        if self.pos.right > 400:
            self.pos.left = 0
        if self.pos.left < 0:
            self.pos.right = 400
        if self.pos.top > 300:
            self.pos.bottom = 0
        if self.pos.bottom < 0:
            self.pos.top = 300


player = GameObject(WHITE, 10, 10)

# #Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.ax = -10
            if event.key == pygame.K_RIGHT:
                player.ax = 10
            if event.key == pygame.K_UP:
                player.ay = -10
            if event.key == pygame.K_DOWN:
                player.ay = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.ax = 0
            if event.key == pygame.K_RIGHT:
                player.ax = 0
            if event.key == pygame.K_UP:
                player.ay = 0
            if event.key == pygame.K_DOWN:
                player.ay = 0

    player.move()
    DISPLAYSURF.fill(NAVY)
    DISPLAYSURF.blit(player.image, player.pos)
    pygame.display.update()
    pygame.time.delay(50)
