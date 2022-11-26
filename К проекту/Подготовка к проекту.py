import math
import pygame as pg
from random import randint
import pygame.display
import numpy as np

WIDTH, HEIGHT = 600, 600
FONE_COLOR = (155, 155, 155)
FPS = 60
pg.init()
f_score = pg.font.Font(None, 36)
screen = pg.display.set_mode((WIDTH, HEIGHT))
isJump = False
Jump = 5
x = 0
y = HEIGHT - 90
speed = 0.2
class Kub:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
    def draw_Kub(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

class snaryad:
    def __init__(self, x, y, radius, color, vx, vy):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vx = vx
        self.vy = vy
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    def hit(self, obj):
        return (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (self.radius + obj.radius)**2

class NPS:
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.v = v
    def traectory1(self, xmin, xmax):
        self.x += self.v
        if self.x <= xmin or self.x >= xmax:
            self.v *= -1
    def draw(self, screen, level0):
        if level == level0:
            screen.blit(pygame.image.load('userpic.png'), (self.x, self.y))
    def hit(self, obj):
        return (self.x + 20 - obj.x) ** 2 + (self.y + 20 - obj.y) ** 2 <= 400



def kub(x, y, color):
    Kub(x, y, 50, color).draw_Kub()

texture1 = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
           [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
           [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
           [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
           [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
           [0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
           [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]

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
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]]

texture3= [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
           [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
           [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
           [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
           [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
           [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
           [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
           [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

def draw_walls(texture):
    for i in range(len(texture)):
        for j in range(len(texture)):
            if texture[i][j] == 1:
                kub(50*j, 50*i, (150, 150, 150))

def check(x, y, texture):
    zx = int(x//50)
    zy = int(y//50)
    if texture[zy][zx] == 1:
        return False
    elif texture[zy][zx] == 0:
        return True

nps = []
bullets = []
bullets2 = []
level = 1
Exit = pygame.image.load('exit_door_180.png')
Exx = 0
Exy = 147
texture = texture1
running = True
t = 0
score = 100
nusha = NPS(50, 160, 3/FPS)
nps += [nusha]
while running:
    screen.fill((0, 0, 0))
    screen.blit(screen, (0, 0))
    screen.blit(pygame.image.load('11781957.png'), (x, y))
    draw_walls(texture)
    for nusha in nps:
        nusha.draw(screen, 1)
        nusha.traectory1(50, 260)
        for bullet in bullets:
            if nusha.hit(bullet):
                nps.remove(nusha)
    screen.blit(Exit, (Exx, Exy))
    screen.blit(f_score.render("Патронов: " + str(score), True, (200, 0, 0)), (0, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]:
        if pg.time.get_ticks() > (t + 400) and score > 0:
            t = pg.time.get_ticks()
            if keys[pygame.K_a]:
                bullet1 = snaryad(round(x + 25), round(y + 25), 5, 'red', -30/FPS, 0)
                bullets.append(bullet1)
                score -= 1
            if keys[pygame.K_d]:
                bullet2 = snaryad(round(x + 25), round(y + 25), 5, 'red', 30/FPS, 0)
                bullets.append(bullet2)
                score -= 1
            if keys[pygame.K_s]:
                bullet3 = snaryad(round(x + 25), round(y + 25), 5, 'red', 0, 30/FPS)
                bullets.append(bullet3)
                score -= 1
            if keys[pygame.K_w]:
                bullet4 = snaryad(round(x + 25), round(y + 25), 5, 'red', 0, -30/FPS)
                bullets.append(bullet4)
                score -= 1
    for bullet in bullets:
        bullet.draw(screen)
    for bullet in  bullets:
        if 0 < bullet.x < 600 and check(bullet.x, bullet.y, texture):
            bullet.x += bullet.vx
            bullet.y += bullet.vy
        else:
            bullets.pop(bullets.index(bullet))
    if keys[pygame.K_RIGHT] and check(x + 41, y, texture) and check(x + 41, y + 40, texture) and x < 558:
        x += speed
    if keys[pygame.K_LEFT] and check(x - 1, y, texture) and check(x - 1, y + 40, texture) and x > 0:
        x -= speed
    if keys[pygame.K_UP] and check(x, y - 1, texture) and check(x + 40, y - 1, texture) and y > 0:
        y -= speed
    if keys[pygame.K_DOWN] and check(x, y + 41, texture) and check(x + 40, y + 41, texture) and y < 558:
        y += speed
    if keys[pygame.K_SPACE] and y > 50:
        isJump = True
        while isJump:
            if Jump >= 0:
                if pg.time.get_ticks() > (t + 1):
                    t = pg.time.get_ticks()
                    y -= (Jump ** 2)
                    Jump -= 1
            elif 0 > Jump >= -5:
                if pg.time.get_ticks() > (t + 1):
                    t = pg.time.get_ticks()
                    y += (Jump ** 2)
                    Jump -= 1
            else:
                Jump = 5
                isJump = False




    if x <= 15 and 197 >= y >= 147 and level == 1:
        Exit = pygame.image.load('exit_door.png')
        Exx = WIDTH - 30
        Exy = -3
        texture = texture2
        x = 100
        y = 50
        level = 2

    if x >= WIDTH - 70 and y <= 50 and level == 2:
        Exit = pygame.image.load('exit_door_180.png')
        Exx = WIDTH/2 - 50
        Exy = HEIGHT/2 + 50
        texture = texture3
        x = 50
        y = 50
        level = 3

    if WIDTH/2 - 20 >= x >= WIDTH/2 - 50 and  HEIGHT/2 + 100 >= y >= HEIGHT/2 + 50 and level == 3:
        Exit = pygame.image.load('exit_door_180.png')
        Exx = 0
        Exy = 150
        texture = texture1
        x = 100
        y = 50
        level = 1
        nusha = NPS(50, 160, 3 / FPS)
        nps += [nusha]

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

pygame.quit()
