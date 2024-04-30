import sys
import time
import pygame
import random
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Racer")
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.fill(WHITE)
fps = pygame.time.Clock()
FPS = 60
font = pygame.font.Font(None, 36)
coins_collected = 0


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C://Users//ASUS TUF Gaming F15//Downloads//coin_2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()  # Удаляем монету, если она вышла за пределы экрана


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C://Users//ASUS TUF Gaming F15//Downloads//blue1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C://Users//ASUS TUF Gaming F15//Downloads//red1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
coins = pygame.sprite.Group()
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
CREATE_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_COIN, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 1
        if event.type == CREATE_COIN:
            new_coin = Coin()
            if not pygame.sprite.spritecollideany(new_coin, enemies):
                coins.add(new_coin)
                all_sprites.add(new_coin)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    display.fill(WHITE)

    for entity in all_sprites:
        display.blit(entity.image, entity.rect)
        if isinstance(entity, Player):
            entity.update()
        else:
            entity.move()
    # Обработка столкновений с монетками
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)  # True удалит монетку при столкновении
    if collected_coins:
        coins_collected += len(collected_coins)

    # Отрисовка количества монеток
    text = font.render(f"Coins: {coins_collected}", True, BLACK)
    display.blit(text, (SCREEN_WIDTH - 150, 10))
    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        display.fill(RED)
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(1)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    fps.tick(FPS)
