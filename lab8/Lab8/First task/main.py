# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initialzing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
SINIY = (0, 0, 255)
KRASNIY = (255, 0, 0)
ZELEN = (0, 255, 0)
CHERNIY = (0, 0, 0)
BELIY = (255, 255, 255)

# Other Variables for use in the program
SCREEN_SHIRINA = 400
SCREEN_VISOTA = 600
SPEED = 5
SCORE = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, CHERNIY)

backgr = pygame.image.load("AnimatedStreet.png")

# Create a white screen
DISPLAY = pygame.display.set_mode((400, 600))
DISPLAY.fill(BELIY)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_SHIRINA - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_SHIRINA - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        press_keys = pygame.key.get_pressed()
        # if pressed_keys[K_UP]:
        # self.rect.move_ip(0, -5)
        # if pressed_keys[K_DOWN]:
        # self.rect.move_ip(0,5)

        if self.rect.left > 0:
            if press_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_SHIRINA:
            if press_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


a = pygame.image.load("coin.png")
coin = pygame.transform.scale_by(a, 0.2)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_SHIRINA - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_SHIRINA - 40), 0)


# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()
C2 = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C2)

coin1 = pygame.sprite.Group()
coin1.add(C1)
coin2 = pygame.sprite.Group()
coin2.add(C2)

sumcoins = 0

# Adding a new User event
INCSPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INCSPEED, 1000)

# Game Loop
while True:

    # Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == INCSPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAY.blit(backgr, (0, 0))
    scores = font_small.render(str(SCORE), True, CHERNIY)
    DISPLAY.blit(scores, (10, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAY.blit(entity.image, entity.rect)
        entity.move()

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        DISPLAY.fill(KRASNIY)
        DISPLAY.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    if pygame.sprite.spritecollideany(P1, coin1):
        C1.rect.center = (random.randint(40, SCREEN_SHIRINA - 40), 0)
        sumcoins += 1
    if pygame.sprite.spritecollideany(P1, coin2):
        C2.rect.center = (random.randint(40, SCREEN_SHIRINA - 40), 0)
        sumcoins += 1

    show_sum = font_small.render(str(sumcoins), True, CHERNIY)
    DISPLAY.blit(show_sum, (SCREEN_SHIRINA-25, 10))

    pygame.display.update()
    FramePerSec.tick(FPS)