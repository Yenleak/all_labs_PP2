import pygame, sys
from pygame.locals import *
import random, time

pygame.init()


FPS = 60
clock = pygame.time.Clock()

# Түстер
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Экран өлшемдері
WIDTH = 400
HEIGHT = 600

#жылдамдық, ұпай, жиналған тиындар саны 
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0

# Шрифттер
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Фон 
background = pygame.image.load("C:/Users/User/Downloads/AnimatedStreet.png")


screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("Car Game by Yenleak")

# Дыбыс
pygame.mixer.init()
pygame.mixer.music.load("C:/Users/User/Desktop/LAB_PP2/labs/lab8/racer/background.wav")
pygame.mixer.music.play(-1)

# Соғысу дыбысы
crash_sound = pygame.mixer.Sound("C:/Users/User/Desktop/LAB_PP2/labs/lab8/racer/crash.wav")

# Монета суреті
coin_image = pygame.image.load("C:/Users/User/Downloads/Coin.jpg")
coin_image = pygame.transform.scale(coin_image, (30, 30))

# Жау 
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/User/Downloads/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)

# Ойыншы
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/User/Downloads/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(5, 0)

# Монета 
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), random.randint(-100, -30))

    def move(self):
        self.rect.move_ip(0, SPEED // 2)
        if self.rect.top > HEIGHT:
            self.respawn()

    def respawn(self):
        self.rect.center = (random.randint(40, WIDTH - 40), random.randint(-100, -30))


P1 = Player()
E1 = Enemy()

coins = pygame.sprite.Group()
for _ in range(3):
    coin = Coin()
    coins.add(coin)

enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(*coins)


INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Фон
    screen.blit(background, (0, 0))

    #ұпайлар
    score_display = font_small.render(f"Score: {SCORE}", True, BLACK)
    screen.blit(score_display, (10, 10))

    coin_display = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    screen.blit(coin_display, (WIDTH - 100, 10))

    
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    P1.move()

    # Егер  соғылса
    if pygame.sprite.spritecollideany(P1, enemies):  
        crash_sound.play()  # Дыбысты ойнату

        screen.fill(RED)  
        screen.blit(game_over, (30, 250))  # "Game Over" жазуы
        pygame.display.update()

        pygame.time.delay(2000) 
        sys.exit()

    # Монеталарды 
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    for _ in collected_coins:
        COINS_COLLECTED += 1
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)  

    pygame.display.update()
    clock.tick(FPS)
