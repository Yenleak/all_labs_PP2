import pygame, sys
from pygame.locals import * #клавиш пернелерін тікелей қолдануға мүмкіндік береді (QUIT, K_LEFT, K_RIGHT т.б)
import random

pygame.init()

# Бастапқы тұрақты мәндер
FPS = 60
WIDTH, HEIGHT = 400, 600
SPEED = 5  # Бастапқы жылдамдық
SCORE = 0
COINS_COLLECTED = 0
N = 5  # N тиын жинағанда жаудың жылдамдығы артады

#Түстер
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Шрифттер
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

#Фон мен суреттер
background = pygame.image.load("C:/Users/User/Downloads/AnimatedStreet.png")
player_image = pygame.image.load("C:/Users/User/Downloads/Player.png")
enemy_image = pygame.image.load("C:/Users/User/Downloads/Enemy.png")
coin_image = pygame.image.load("C:/Users/User/Downloads/Coin.jpg")
coin_image = pygame.transform.scale(coin_image, (30, 30))

#экран
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game by Yenleak")

# Класстар
class Enemy(pygame.sprite.Sprite): # жаудың класы
    def __init__(self):
        super().__init__()
        self.image = enemy_image #жау суреті
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0) #кездейсоқ орында пайда болуы

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > HEIGHT:
            SCORE += 1
            self.rect.top = 0 # қайтадан басынан бастап келуі
            self.rect.center = (random.randint(40, WIDTH - 40), 0) #кездейсоқ орында пайда болуы

class Player(pygame.sprite.Sprite): # ойыншы класы
    def __init__(self):
        super().__init__()
        self.image = player_image # ойыншының суреті
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520) #ойыншының бастапқы координатасы

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0) #солға қарай қозғалу
        if pressed_keys[K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(5, 0) #оңға қарай қозғалу

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_image #Монета суреті
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), random.randint(-100, -30)) #
        self.weight = random.randint(1, 5)  # Тиынның салмағы

    def move(self): # Монетаны төмен қарай қозғалуы
        self.rect.move_ip(0, SPEED // 2)
        if self.rect.top > HEIGHT:
            self.respawn()

    def respawn(self): #Монетаны қайта орналастыру
        self.rect.center = (random.randint(40, WIDTH - 40), random.randint(-100, -30))
        self.weight = random.randint(1, 5)  # Жаңа салмақ беру

#Объектілер
P1 = Player()
E1 = Enemy()
coins = pygame.sprite.Group()
for _ in range(3):
    coins.add(Coin())

enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, *coins)

#Жылдамдық арттыру
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Ойын циклі
clock = pygame.time.Clock()
run= True
while run:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))

    # Ұпайлар
    score_display = font_small.render(f"Score: {SCORE}", True, BLACK)
    screen.blit(score_display, (10, 10))
    coin_display = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    screen.blit(coin_display, (WIDTH - 100, 10))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    P1.move()

    # Егер соғылса:
    if pygame.sprite.spritecollideany(P1, enemies):
        screen.fill(RED)
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        pygame.time.delay(2000)
        sys.exit()

    # Тиын жинау:
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collected_coins:
        COINS_COLLECTED += coin.weight  # Тиынның салмағын қосу
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

        # Егер N тиын жиналса, жаудың жылдамдығы артады
        if COINS_COLLECTED % N == 0:
            SPEED += 1

    pygame.display.update()
    clock.tick(FPS)
