import pygame
import sys
import time

pygame.init()

width, height = 500, 500
center=(width//2, height//2)
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Mickey Mouse Clock")


bc_img = pygame.transform.scale(pygame.image.load("C:/Users/User/Downloads/photo_5395711786004639314_x.jpg"), (width, height))


second_hand=pygame.image.load("C:/Users/User/Downloads/mickeyclock-fotor-bg-remover-20250320163245.png")
minute_hand=pygame.image.load("C:/Users/User/Downloads/mickeyclock-fotor-bg-remover-20250320164211.png")

clock = pygame.time.Clock()

run=True
while run:
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    minute_angle = -(minutes / 60) * 360 + 90
    second_angle = -(seconds / 60) * 360 + 90


    screen.blit(bc_img, (0, 0))

    rotated_minute = pygame.transform.rotate(minute_hand, minute_angle)
    minute_rect = rotated_minute.get_rect()
    minute_rect.center = center  
    screen.blit(rotated_minute, minute_rect.topleft)

    
    rotated_second = pygame.transform.rotate(second_hand, second_angle)
    second_rect = rotated_second.get_rect()
    second_rect.center = center
    screen.blit(rotated_second, second_rect.topleft)

    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)  


