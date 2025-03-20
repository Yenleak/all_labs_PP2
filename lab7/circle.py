import pygame, os

pygame.init()

WIDTH, HEIGHT = 800, 600
window = (WIDTH, HEIGHT)
pygame.display.set_caption("Circle")
screen = pygame.display.set_mode((WIDTH, HEIGHT))


bg = pygame.Color('white')


ball_color = pygame.Color('red')
ball_position = [600, 400]
ball_radius = 25
ball_speed = 20

clock = pygame.time.Clock()  


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: 
        ball_position[1] = max(ball_position[1] - ball_speed, ball_radius)
    if keys[pygame.K_DOWN]:
        ball_position[1] = min(ball_position[1] + ball_speed, window[1] - ball_radius)
    if keys[pygame.K_LEFT]:  
        ball_position[0] = max(ball_position[0] - ball_speed, ball_radius)
    if keys[pygame.K_RIGHT]:
        ball_position[0] = min(ball_position[0] + ball_speed, window[0] - ball_radius)

    screen.fill(bg)
    pygame.draw.circle(screen, ball_color, ball_position, ball_radius)
    pygame.display.flip()
    
    clock.tick(24)  
