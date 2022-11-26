import math
import pygame as pg
from random import randint
import pygame.display
import numpy as np

WIDTH, HEIGHT = 600, 600
FONE_COLOR = (155, 155, 155)
FPS = 30
pg.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))

x = 100
y = 50
speed = 0.5
class Kub:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
    def draw_Kub(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

def kub(x, y, color):
    Kub(x, y, 50, color).draw_Kub()

texture1 = [[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
           [1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0],
           [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
           [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
           [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0],
           [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
           [0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

texture2= [[1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1],
           [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
           [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1],
           [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
           [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0],
           [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
           [0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def array(k):
    b = []
    for i in range(50):
        a = []
        for j in range(50):
            a += [k]
        b += [a]
    return b
def mass(texture):
    mass = []
    for i in range(len(texture)):
        mas = []
        for j in range(len(texture)):
            if texture[i][j] == 1:
                mas += [1]
            if texture[i][j] == 0:
                mas += [0]
        mass += [mas]
    return mass
def draw_walls(texture):
    for i in range(len(texture)):
        for j in range(len(texture)):
            if texture[i][j] == 1:
                kub(50*j, 50*i, (150, 150, 150))

def check(x, y, texture):
    zx = int(x//50)
    zy = int(y//50)
    if mass(texture)[zy][zx] == 1:
        return False
    elif mass(texture)[zy][zx] == 0:
        return True

Exit = pygame.image.load('exit_door_180.png')
Exx = 0
Exy = HEIGHT - 50
texture = texture1
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(screen, (0, 0))
    screen.blit(pygame.image.load('11781957.png'), (x, y))
    draw_walls(texture)
    screen.blit(Exit, (Exx, Exy))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and check(x + 41, y, texture) and check(x + 41, y + 40, texture) and x < 558:
        x += speed
    if keys[pygame.K_LEFT] and check(x - 1, y, texture) and check(x - 1, y + 40, texture) and x > 0:
        x -= speed
    if keys[pygame.K_UP] and check(x, y - 1, texture) and check(x + 40, y - 1, texture) and y > 0:
        y -= speed
    if keys[pygame.K_DOWN] and check(x, y + 41, texture) and check(x + 40, y + 41, texture) and y < 558:
        y += speed

    #pygame.display.update()

    if x <= 15 and y >= WIDTH - 50:
        Exit = pygame.image.load('exit_door.png')
        Exx = WIDTH - 30
        Exy = 0
        texture = texture2
        x = 100
        y = 50

    if x >= WIDTH - 70 and y <= 50:
        Exit = pygame.image.load('exit_door_180.png')
        Exx = 0
        Exy = HEIGHT - 50
        texture = texture1
        x = 100
        y = 50

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

pygame.quit()
