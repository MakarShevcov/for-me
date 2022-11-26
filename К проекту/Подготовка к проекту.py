import math
import pygame as pg
from random import randint
import pygame.display
import numpy as np

WIDTH, HEIGHT = 500, 500
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

texture = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
def array(k):
    b = []
    for i in range(50):
        a = []
        for j in range(50):
            a += [k]
        b += [a]
    return b
def mass():
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
def draw_walls():
    for i in range(len(texture)):
        for j in range(len(texture)):
            if texture[i][j] == 1:
                kub(50*j, 50*i, (150, 150, 150))

def check(x, y):
    zx = int(x//50)
    zy = int(y//50)
    if mass()[zy][zx] == 1:
        return False
    elif mass()[zy][zx] == 0:
        return True

print(mass()[340//50][253//50])
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(screen, (0, 0))
    draw_walls()
    screen.blit(pygame.image.load('11781957.png'), (x, y))
    draw_walls()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and check(x + 41, y) and check(x + 41, y + 40) and x < 460:
        x += speed
    if keys[pygame.K_LEFT] and check(x - 1, y) and check(x - 1, y + 40) and x > 0:
        x -= speed
    if keys[pygame.K_UP] and check(x, y - 1) and check(x + 40, y - 1) and y > 0:
        y -= speed
    if keys[pygame.K_DOWN] and check(x, y + 41) and check(x + 40, y + 41) and y < 458:
        y += speed

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

