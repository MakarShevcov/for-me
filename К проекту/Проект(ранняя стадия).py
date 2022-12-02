#чтобы стрелять, нажмите мышкой в нужном направлении; чтобы ходить, нажимайте A,W,S,D; чтобы стрелять вторыми снарядами, нажимайте Left,Up,Down,Right; 

import math
import pygame as pg
import pygame.display

WIDTH, HEIGHT = 600, 600
FPS = 60
pg.init()
f_score = pg.font.Font(None, 36)
screen = pg.display.set_mode((WIDTH, HEIGHT))
x = 0
y = HEIGHT - 90
speed = 0.2
nps = []
bullets = []
sbullets = []
stalin_bullets = []
running = True
final = False
level = 1
size = 50
weapon = 1
stalin_shoot = 1
texX = [[], [], []]
texY = [[], [], []]
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
    """
    рисует стены
    """
    for i in range(len(texture)):
        for j in range(len(texture)):
            if texture[i][j] == 1:
                if (x - 5 - size*j) ** 2 + (y -5 - size*i) ** 2 <= 8100:
                    screen.blit(pygame.image.load('iRR_GK-U1lma2Y5UBqXL5ux9UR4KR4BJ0Z2hHVIm0-bBrfN5Lr4Owz4utX7za9UnyEm124OFwNk5TtjyY-qB0lhN.jpg'), (size*j, size*i))

def check(x, y, texture):
    """
    проверяет, лежит ли точка внутри стены
    """
    zx = int(x//size)
    zy = int(y//size)
    if texture[zy][zx] == 1:
        return False
    elif texture[zy][zx] == 0:
        return True

class Gun:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.f2_power = 1
        self.f2_on = 0
        self.f1_on = 0
        self.an = 1
        self.color = (150, 150, 150)
        self.x = x
        self.y = y
    def fire1(self):
        """
        так стреляют nps
        """
        new_ball = snaryad(self.x + 25, self.y + 25, (255, 10, 10), 10)
        self.an = math.atan2((y - new_ball.y), (x - new_ball.x))
        new_ball.vx = 20/FPS * math.cos(self.an)
        new_ball.vy = 20/FPS * math.sin(self.an)
        stalin_bullets.append(new_ball)
        new_ball.draw(screen)

    def fire2_start(self):
        self.f2_on = 1

    def fire2_end(self, event):
        """
        так стреляю я
        """
        new_ball = snaryad(self.x + 20, self.y + 20, (10, 10, 50), 5)
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = 20/FPS * math.cos(self.an)
        new_ball.vy = 20/FPS * math.sin(self.an)
        bullets.append(new_ball)
        self.f2_on = 0
        self.f2_power = 5



class snaryad:
    def __init__(self, x, y, color, r):
        self.x = x
        self.y = y
        self.radius = r
        self.color = color
        self.vx = 20/FPS
        self.vy = 20/FPS
    def draw(self, screen):
        """
        рисует снаряд
        """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    def hit(self, obj):
        """
        проверяет, попал ли снаряд в некий объект
        """
        return (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (self.radius + obj.radius)**2
    def flight1(self):
        """
        задаёт передвижение снарядов, отскакивающих от стен
        """
        if (check(self.x + self.vx, self.y, texture) and check(self.x - self.vx, self.y, texture)) and (check(self.x, self.y + self.vy, texture) and check(self.x, self.y - self.vy, texture)):
            self.x += self.vx
            self.y += self.vy
        if not (check(self.x + self.vx, self.y, texture) and check(self.x - self.vx, self.y, texture)) and (check(self.x, self.y + self.vy, texture) and check(self.x, self.y - self.vy, texture)):
            self.vx *= -0.9
            self.y += self.vy
            self.x += self.vx
        if (check(self.x + self.vx, self.y, texture) and check(self.x - self.vx, self.y, texture)) and not (check(self.x, self.y + self.vy, texture) and check(self.x, self.y - self.vy, texture)):
            self.vy *= -0.9
            self.x += self.vx
            self.y += self.vy
        if self.x <= 5 or self.x >= 595:
            self.x -= self.vx
            self.vx *= -1
        if self.y <= 5 or self.y >= 595:
            self.y -= self.vy
            self.vy *= -1

    def flight2(self, level):
        """
        задаёт передвижение снарядов, взрывающих стены
        """
        if (check(self.x + self.vx, self.y, texture) and check(self.x - self.vx, self.y, texture)) and (check(self.x, self.y + self.vy, texture) and check(self.x, self.y - self.vy, texture)):
            self.x += self.vx
            self.y += self.vy
        if not check(self.x + self.vx, self.y, texture):
            zx = int((self.x + self.vx) // 50)
            zy = int(self.y // 50)
            texX[level - 1] += [zx]
            texY[level - 1] += [zy]
            texture[zy][zx] = 0
            sbullets.remove(self)
        if not check(self.x - self.vx, self.y, texture):
            zx = int((self.x - self.vx) // 50)
            zy = int(self.y // 50)
            texX[level - 1] += [zx]
            texY[level - 1] += [zy]
            texture[zy][zx] = 0
            sbullets.remove(self)
        if not check(self.x, self.y + self.vy, texture):
            zx = int(self.x // 50)
            zy = int((self.y + self.vy) // 50)
            texX[level - 1] += [zx]
            texY[level - 1] += [zy]
            texture[zy][zx] = 0
            sbullets.remove(self)
        if not check(self.x, self.y - self.vy, texture):
            zx = int(self.x // 50)
            zy = int((self.y - self.vy) // 50)
            texX[level - 1] += [zx]
            texY[level - 1] += [zy]
            texture[zy][zx] = 0
            sbullets.remove(self)
        if self.x <= 5 or self.x >= 595:
            sbullets.remove(self)
        if self.y <= 5 or self.y >= 595:
            sbullets.remove(self)


class NPS:
    def __init__(self, x, y, v, level, pic, size):
        self.x = x
        self.y = y
        self.v = v
        self.level = level
        self.pic = pic
        self.size = size
        self.rest = False
        self.x0 = x
        self.y0 = y
        self.X = [self.x0]
        self.Y = [self.y0]
    def traectory1(self, xmin, xmax):
        """
        задаёт первую траекторию движения нпс в спокойном состоянии
        """
        if not self.rest:
            self.x += self.v
            if self.x <= xmin or self.x >= xmax:
                self.v *= -1
    def draw(self, screen, level0):
        """
        прорисовывает нпс
        """
        if level == level0:
            screen.blit(pygame.image.load(self.pic), (self.x, self.y))
    def hit(self, obj):
        """
        проверяет, пересёкся ли нпс с другим обьектом (например, пулей)
        """
        return (self.x + self.size/2 - obj.x) ** 2 + (self.y + self.size/2 - obj.y) ** 2 <= (self.size/2)**2

    def nps_motion(self):
        """
        задаёт движение нпс с отклонением от стен
        """
        if (check(self.x + self.size + self.v, self.y, texture) and check(self.x + self.size + self.v, self.y + self.size, texture)) and (
                check(self.x - self.v, self.y, texture) and check(self.x - self.v, self.y + self.size, texture)):
            if (self.vx)**2 >= (self.v/4)**2:
                self.x += self.vx
            else:
                self.vx = self.v/4
                self.x += self.vx
        elif not(check(self.x + self.size + self.v, self.y, texture) and check(self.x + self.size + self.v, self.y + self.size, texture)) and (
                check(self.x - self.v, self.y, texture) and check(self.x - self.v, self.y + self.size, texture)):
            self.x -= self.v
        elif (check(self.x + self.size + self.v, self.y, texture) and check(self.x + self.size + self.v, self.y + self.size, texture)) and not(
                check(self.x - self.v, self.y, texture) and check(self.x - self.v, self.y + self.size, texture)):
            self.x += self.v
        if (check(self.x + self.size, self.y - self.v, texture) and check(self.x, self.y - self.v, texture)) and (
                check(self.x + self.size, self.y + self.size + self.v, texture) and check(self.x, self.y + self.size + self.v, texture)):
            if (self.vy)**2 >= (self.v / 4)**2:
                self.y += self.vy
            else:
                a = self.vy / (self.vy **2)**0.5
                self.vy = a * self.v / 4
                self.y += self.vy
        elif not(check(self.x + self.size, self.y - self.v, texture) and check(self.x, self.y - self.v, texture)) and (
                check(self.x + self.size, self.y + self.size + self.v, texture) and check(self.x, self.y + self.size + self.v, texture)):
            self.y += self.v
        elif (check(self.x + self.size, self.y - self.v, texture) and check(self.x, self.y - self.v, texture)) and not(
                check(self.x + self.size, self.y + self.size + self.v, texture) and check(self.x, self.y + self.size + self.v, texture)):
            self.y -= self.v
        if self.x <= 5 or self.x >= 595:
            self.vx *= 0
        if self.y <= 5 or self.y >= 595:
            self.vy *= 0
        self.Y += [self.y]   #сохраняем все ходы в массив, чтобы потом обратно идти
        self.X += [self.x]

    def monster_attack(self, x, y):
        """
        задаёт движение нпс при атаке
        """
        self.an = math.atan2((y - self.y), (x - self.x))
        self.vx = self.v * math.cos(self.an)
        self.vy = self.v * math.sin(self.an)
        self.nps_motion()
    def monster_come_back(self, l):
        """
        задаёт возвращение нпс обратно после прекращения атаки по обратному маршруту
        """
        if l > -1:
            self.x = self.X[l]
            self.y = self.Y[l]
        self.X.remove(self.X[l])
        self.Y.remove(self.Y[l])
    def contact(self):
        """
        проверяет, пересёкся ли персонаж с нпс (для персонажа я отдельного класса не сделал, потому что зачем?)
        """
        return ((self.x + self.size/2) - (x + 20)) ** 2 + ((self.y + self.size/2) - (y + 20)) ** 2 <= (self.size/2 + 20)**2




def buttons_shooting(keys, x, y):
    """
    стрельба с помощью клавиатуры
    """
    if keys[pygame.K_LEFT]:
        bullet1 = snaryad(round(x + 20), round(y + 20), (255, 0, 0), 10)
        bullet1.vx *= -1
        bullet1.vy *= 0
        sbullets.append(bullet1)
    if keys[pygame.K_RIGHT]:
        bullet2 = snaryad(round(x + 20), round(y + 20), (255, 0, 0), 10)
        bullet2.vx *= 1
        bullet2.vy *= 0
        sbullets.append(bullet2)
    if keys[pygame.K_DOWN]:
        bullet3 = snaryad(round(x + 20), round(y + 20), (255, 0, 0), 10)
        bullet3.vx *= 0
        bullet3.vy *= 1
        sbullets.append(bullet3)
    if keys[pygame.K_UP]:
        bullet4 = snaryad(round(x + 20), round(y + 20), (255, 0, 0), 10)
        bullet4.vx *= 0
        bullet4.vy *= -1
        sbullets.append(bullet4)


def walking(keys, x, y, speed):
    """
    перемещение персонажа
    """
    if keys[pygame.K_d] and check(x + 41, y, texture) and check(x + 41, y + 40, texture) and x < 558:
        x += speed
    if keys[pygame.K_a] and check(x - 1, y, texture) and check(x - 1, y + 40, texture) and x > 0:
        x -= speed
    if keys[pygame.K_w] and check(x, y - 1, texture) and check(x + 40, y - 1, texture) and y > 0:
        y -= speed
    if keys[pygame.K_s] and check(x, y + 41, texture) and check(x + 40, y + 41, texture) and y < 558:
        y += speed
    return [x, y]

def shtryh(x, y):
    """
    создаёт штриховку на заднем фоне
    """
    for i in range(60):
        for j in range(12):
            if ((x) - j*50) ** 2 + ((y) - i*20) ** 2 <= 14400:
                color = (0, 0, 0)
                pygame.draw.rect(screen, color, (j * 50, i * 20, 50, 20), 1)

Exit = pygame.image.load('exit_door_180.png')
Exx = 0
Exy = 147
texture = texture1
attack = False
gun = Gun(screen, x, y)
t = 0
score = 100
score2 = 0
ghost = NPS(248, 149, 10/FPS, 1, 'Ghost.jpg', 50)
stalin =NPS(450, 150, 0, 1, 'Stalin.jpg', 50)
nps_gun = Gun(screen, stalin.x, stalin.y)
nps += [ghost, stalin]
l = 1
while True:
    if running:
        screen.fill((0, 0, 0))
        screen.blit(screen, (0, 0))
        pygame.draw.circle(screen, (10, 10, 10), (x + 20, y + 20), 100)
        pygame.draw.circle(screen, (20, 20, 20), (x + 20, y + 20), 90)       #рисуем освещение вокруг
        pygame.draw.circle(screen, (30, 30, 30), (x + 20, y + 20), 80)
        pygame.draw.circle(screen, (40, 40, 40), (x + 20, y + 20), 70)
        shtryh(x, y)
        screen.blit(pygame.image.load('11781957.png'), (x, y))
        draw_walls(texture)
        gun.x = x
        gun.y = y
        if ghost in nps:
            np = ghost
            if level == np.level: #условие, чтобы призрак появлялся только на определённом уровне
                if (np.x - x) ** 2 + (np.y - y) ** 2 <= 14400: #условие видимости призрака
                    np.draw(screen, 1)
                if (np.x - x) ** 2 + (np.y - y) ** 2 <= 10000: #условие атаки
                    np.monster_attack(x, y)
                    l = len(np.X)
                elif l > 2:               #условие прекащения атаки
                    np.monster_come_back(l-1)
                    l -= 1
                else:         #движение в покое
                    np.traectory1(50, 260)
                if np.contact():   #условие, чтобы мы умирали при пересечении с призраком
                    np.X = []
                    np.Y = []
                    l = 1
                    running = False
                    final = True
                for bullet in bullets:          #убийство призрака
                    if np.hit(bullet):
                        np.X = [np.x0]
                        np.Y = [np.y0]
                        l = 1
                        nps.remove(np)
        if stalin in nps:
            np = stalin
            if level == np.level:
                if (np.x - x) ** 2 + (np.y - y) ** 2 <= 14400:
                    np.draw(screen, 1)
                if np.contact():
                    weapon = 2    #получили новое оружие
                    score2 += 3
                    nps.remove(np) #при контакте мы его убираем
                    stalin_shoot = 0 #чтобы не стрелял после исчезновения
            if stalin_shoot:     #он будет в нас стрелять при приближении
                if ((x + 20) - (stalin.x + stalin.size / 2)) ** 2 + ((y + 20) - (stalin.y + stalin.size / 2)) ** 2 <= 10000:
                    if pg.time.get_ticks() > (t + 3000): #стреляет раз в 3 секунды
                        t = pg.time.get_ticks()
                        nps_gun.fire1()
        for new_ball in stalin_bullets:
            if (new_ball.x - (x + 20)) ** 2 + (new_ball.y - (y + 20)) ** 2 <= 400: #мы погибаем при попадании его пули
                running = False
                final = True
        if (x + 20 - Exx) ** 2 + (y + 20 - Exy) ** 2 <= 14400:
            screen.blit(Exit, (Exx, Exy))
        screen.blit(f_score.render("Патронов: " + str(score), True, (200, 0, 0)), (0, 0))
        keys = pygame.key.get_pressed()
        if weapon == 2:
            screen.blit(f_score.render("Огн. шаров: " + str(score2), True, (200, 0, 0)), (0, 20))
            if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                if score2 > 0:
                    if pg.time.get_ticks() > (t + 400) and score > 0:
                        t = pg.time.get_ticks()
                        buttons_shooting(keys, x, y)
                        score2 -= 1      #чтобы у нового оружия было ограничение на патроны
        walk = walking(keys, x, y, speed)
        x = walk[0]
        y = walk[1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            elif event.type == pygame.MOUSEBUTTONDOWN: #стреляем при нажатии мышкой
                if score > 0:
                    gun.fire2_start()
                    gun.fire2_end(event)
                    score -= 1
        for bullet in bullets:
            if (x + 20 - bullet.x) ** 2 + (y + 20 - bullet.y) ** 2 <= 8100:
                bullet.draw(screen)
            bullet.flight1()
            if pg.time.get_ticks() > (t + 1500):    #полёт и частота выстрелов обычных снарядов
                t = pg.time.get_ticks()
                bullets.pop(bullets.index(bullet))
        for new_ball in stalin_bullets:
            if (x + 20 - new_ball.x) ** 2 + (y + 20 - new_ball.y) ** 2 <= 8100:
                new_ball.draw(screen)
            new_ball.flight1()
            if pg.time.get_ticks() > (t + 1500):    #полёт и частота выстрелов снарядов, выпущенных нпс
                t = pg.time.get_ticks()
                stalin_bullets.pop(stalin_bullets.index(new_ball))
        for sbullet in sbullets:
            sbullet.draw(screen)            #полёт снарядов, взрывающих стены
            sbullet.flight2(level)



        if x <= 15 and 197 >= y >= 147 and level == 1:  #Переход из 1 уровня в 2
            bullets = [] #убираем все летающие снаряды
            Exit = pygame.image.load('exit_door.png')
            Exx = WIDTH - 30          #ставим выход в нужное место и нужную картинку на него
            Exy = -3
            texture = texture2          #задаём текстуру уровня
            x = 100
            y = 50          #координаты нашего появления
            level = 2
            #ниже аналогично
        if x >= WIDTH - 70 and y <= 50 and level == 2:
            bullets = []
            Exit = pygame.image.load('exit_door_180.png')
            Exx = WIDTH/2 - 50
            Exy = HEIGHT/2 + 50
            texture = texture3                   #Переход из 2 уровня в 3
            x = 50
            y = 50
            level = 3

        if WIDTH/2 - 20 >= x >= WIDTH/2 - 50 and  HEIGHT/2 + 100 >= y >= HEIGHT/2 + 50 and level == 3:
            bullets = []
            Exit = pygame.image.load('exit_door_180.png')
            Exx = 0
            Exy = 150
            texture = texture1                  #Переход из 3 уровня в 1
            x = 0
            y = HEIGHT - 90
            level = 1
            nusha = NPS(50, 150, 3 / FPS, 1, 'Ghost.jpg', 50)
            nps += [nusha, stalin]
            for np in nps:
                np.X = [np.x0]
                np.Y = [np.y0]


    if final:
        screen.fill((0, 0, 0))
        f1 = pygame.font.Font(None, 60)
        f2 = pygame.font.Font(None, 62)
        text1 = f1.render("Вы умерли ", True,
                          (255, 0, 0))                          #экран смерти
        text2 = f1.render("Перезапустить", True,
                          (255, 0, 0))
        screen.blit(text1, (180, 200))
        pygame.draw.rect(screen, (250, 250, 0), (150, 500, 305, 45))
        screen.blit(text2, (150, 500))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pygame.quit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 150 <= event.pos[0] <= 455 and 500 <= event.pos[1] <= 545:   #возрождение при перезапуске
                    final = False
                    texture = texture1
                    for l in range(0, 3):  #чтобы всё, что мы при старой жизни разбомбили,вернулось назад
                        for i in range(0, len(texX[l])):
                            texture[texY[l][i]][texX[l][i]] = 1
                    score = 100
                    score2 = 3
                    level = 1
                    weapon = 1
                    x = 0
                    y = HEIGHT - 90               #возвращаем все параметры к исходным
                    nps += [ghost, stalin]
                    l = 1
                    for np in nps:
                        np.X = [np.x0]
                        np.Y = [np.y0]
    running = True
    pygame.display.update()
