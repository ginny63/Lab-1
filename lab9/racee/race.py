import pygame as pg
import random, time, sys
from pygame.locals import *

pg.init()

font = pg.font.SysFont("Areal", 60)
fontsm = pg.font.SysFont("Verdana", True, 20)


sc = pg.display.set_mode((1000, 1000))
W, H = 1000, 1000
pg.display.set_caption("Nit for pace")
clock = pg.time.Clock()

road = pg.image.load("C:/Users/kairb/Pictures/lab9/ro.png")
shark1 = pg.image.load("C:/Users/kairb/Pictures/lab9/sha.png")
rocket1 = pg.image.load("C:/Users/kairb/Pictures/lab9/roc.png")
bomb1 = pg.image.load("C:/Users/kairb/Pictures/lab9/bo.png")


speed = 3
gameov = font.render("Game Over", True, (0, 0, 0))
score = 100
money = 0
index = 0
x = 20
y = 20

class cherry(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("C:/Users/kairb/Pictures/lab9/che.png")
        self.rect = self.image.get_rect()
        self.speed = 10
    def move(self):
        global money
        self.rect.move_ip(0, 3)
        if self.rect.top > 1100:
            self.rect.bottom = 0
            self.rect.center = (random.randint(40, W-40), 200)
    def draw(self):
        sc.blit(self.image, self.rect)

class coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("C:/Users/kairb/Pictures/lab9/co.png")
        self.rect = self.image.get_rect()
        self.speed = 7
    def move(self):
        global money
        self.rect.move_ip(0, self.speed)
        if self.rect.top > 1000:
            self.rect.bottom = 0
            self.rect.center = (random.randint(40, W-40), 200)
    def draw(self):
        sc.blit(self.image, self.rect)
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("C:/Users/kairb/Pictures/lab9/bo.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W-40), 220)

    def move(self):
        global score
        global index
        # if self.rect.top < 100:
        #     x = 30
        #     y = 30
        # elif self.rect.top < 220:
        #     x = 35
        #     y = 35
        # elif self.rect.top < 240:
        #     x = 40
        #     y = 40
        # elif self.rect.top < 260:
        #     x = 50
        #     y = 50
        # elif self.rect.top < 280:
        #     x = 65
        #     y = 65
        #
        # elif self.rect.top < 10000:
        #     x = 100
        #     y = 100

        self.image = pg.transform.scale(self.image, (100, 100))
        self.rect.move_ip(0, speed)
        if self.rect.top > 1000:
            index += 1
            score += 100 * index*0.1
            self.rect.bottom = 0
            x = 20
            y = 20
            self.rect.center = (random.randint(40, W-40), 200)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Shark(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("C:/Users/kairb/Pictures/lab9/sha.png")
        self.rect = self.image.get_rect()
        self.rect.center = (500, 700)

    def move(self):
        pressed_keys = pg.key.get_pressed()
        if self.rect.top > 5:
            if pressed_keys[pg.K_UP]:
                self.rect.move_ip(0, -15)
        if self.rect.bottom < 1200:
            if pressed_keys[pg.K_DOWN]:
                self.rect.move_ip(0, 15)
        if self.rect.left > 0:
            if pressed_keys[pg.K_LEFT]:
                self.rect.move_ip(-15, 0)
        if self.rect.right < 1000:
            if pressed_keys[pg.K_RIGHT]:
                self.rect.move_ip(15, 0)

rocket = Enemy()
shark = Shark()
coin = coin()
cherry = cherry()

cherrys = pg.sprite.Group()
cherrys.add(cherry)

coins = pg.sprite.Group()
coins.add(coin)

rockets = pg.sprite.Group()
rockets.add(rocket)

group = pg.sprite.Group()
group.add(rocket, shark, coin, cherry)

speed_incr = pg.USEREVENT + 1
pg.time.set_timer(speed_incr, 2000)

pg.mixer.music.load("C:/Users/kairb/Music/back.mp3")
pg.mixer.music.play()


run = True
while True:

    for event in pg.event.get():
        if event.type == speed_incr:
            speed += money/20
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    sc.blit(road, (0, 0))
    scores = font.render(str(int(score)), True, (0, 0, 0))
    sc.blit(scores, (20, 20))
    monCnt = font.render(str(money), True, (255, 200, 50))

    sc.blit(monCnt, (800, 10))

    for entity in group:
        sc.blit(entity.image, entity.rect)
        entity.move()

    if pg.sprite.spritecollideany(shark, coins):
        money += 1
        coin.rect.top = 1000

    if pg.sprite.spritecollideany(shark, cherrys):
        money += 2
        cherry.rect.top = 1000

    for rocket in rockets:
        if shark.rect.collidepoint(rocket.rect.center):
            pg.mixer.music.pause()
       
            time.sleep(0.5)

            sc.fill((9, 1, 1))

            pg.display.update()
            for entity in group:
                entity.kill()
            #time.sleep(2)
            pg.quit()
            sys.exit()

    pg.display.update()
    clock.tick(60)