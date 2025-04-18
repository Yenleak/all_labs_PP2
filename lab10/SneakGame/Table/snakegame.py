import pygame
import random
import sys
from database import getcreate_user, save_score

#ойыншының логинін алу
username = input("Enter your username: ")
user_id = getcreate_user(username)


pygame.init()

#screen
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game by Yenleak")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

# Түстер
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# snake body and first position
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
change_to = snake_direction
speed = 15

# food class (random food, random food weight )
class Food:
    def __init__(self):
        self.position = self.generate_food()
        self.weight = random.randint(1, 5)  # Weight food(1-5)
        self.spawn_time = pygame.time.get_ticks()  #time food

    def generate_food(self):
        while True:
            pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
            if pos not in snake_body:
                return pos

    def is_expired(self): #Food disappears after 5 seconds
        return pygame.time.get_ticks() - self.spawn_time > 5000

    def respawn(self):#new food
        self.position = self.generate_food()
        self.weight = random.randint(1, 5)
        self.spawn_time = pygame.time.get_ticks()

food = Food()
game_score = 0
level = 1
level_threshold = 3

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
        # keyboard control
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"

    # snake movement
    snake_direction = change_to
    if snake_direction == "UP" and snake_pos[1]>50: #50 пиксельге жоғары шықпайды
        snake_pos[1] -= 10
    elif snake_direction == "DOWN":
        snake_pos[1] += 10
    elif snake_direction == "LEFT":
        snake_pos[0] -= 10
    elif snake_direction == "RIGHT":
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))

    # if snake eat food:
    if snake_pos == food.position:
        game_score += food.weight  # add points based on the weight of the food
        food.respawn()  # new food
    else:
        snake_body.pop()

    if food.is_expired():
        food.respawn()

    # if it goes out of bounds or touches itself
    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        run = False

    for block in snake_body[1:]:
        if snake_pos == block:
            run = False

    # the speed increases as the level increases
    if game_score % level_threshold == 0 and game_score != 0:
        level = game_score // level_threshold + 1
        speed = 15 + (level - 1) * 3


    screen.fill(BLACK)
    for p in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(p[0], p[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food.position[0], food.position[1], 10, 10))

    # score and level
    score_text = font.render(f"Score: {game_score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (20, 20))
    screen.blit(level_text, (20, 50))

    pygame.display.update()
    clock.tick(speed)

# end game, "Game Over"
game_over_text = font.render("GAME OVER", True, WHITE)
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (WIDTH / 2, HEIGHT / 2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(3000)

save_score(user_id, game_score, level)


pygame.quit()

