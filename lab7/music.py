import pygame
import os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

music_path = r"C:\Users\User\Music" 
music_files = [f for f in os.listdir(music_path) if f.endswith(".mp3")]

if not music_files:
    print(" Музыка табылған жоқ!")
    exit()

index = 0
pygame.mixer.music.load(os.path.join(music_path, music_files[index]))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

bg_image = pygame.image.load("C:/Users/User/Downloads/bc_bts.jpg") 
play_img = pygame.image.load(r"C:\Users\User\Downloads\play.png") 
pause_img = pygame.image.load(r"C:\Users\User\Downloads\pause.png") 
next_img = pygame.image.load(r"C:\Users\User\Downloads\next.png")  
prev_img = pygame.image.load(r"C:\Users\User\Downloads\back.png")

bg_image=pygame.transform.scale(bg_image,(WIDTH,HEIGHT))
play_img = pygame.transform.scale(play_img, (60, 60))
pause_img = pygame.transform.scale(pause_img, (60, 60))
next_img = pygame.transform.scale(next_img, (60, 60))
prev_img = pygame.transform.scale(prev_img, (60, 60))

playing = False

run = True
while run:
    screen.fill(WHITE) 
    screen.blit(bg_image, (0, 0))  

    music_text = font.render(music_files[index], True, BLACK)
    screen.blit(music_text, (200, 50))

    screen.blit(prev_img, (150, 500))
    screen.blit(play_img if not playing else pause_img, (350, 500))
    screen.blit(next_img, (550, 500))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                playing = not playing 
            
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                playing = False

            elif event.key == pygame.K_RIGHT:
                index = (index + 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_path, music_files[index]))
                pygame.mixer.music.play()
                playing = True

            elif event.key == pygame.K_LEFT:
                index = (index - 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_path, music_files[index]))
                pygame.mixer.music.play()
                playing = True

    pygame.display.update()
    clock.tick(30)

pygame.quit()
