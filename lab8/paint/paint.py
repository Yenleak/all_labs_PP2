import pygame

pygame.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Paint Game by Yenleak")
clock = pygame.time.Clock()


game_over = False
prev, cur = None, None
drawing_mode = "free"  # "free", "rect", "circle", "eraser"
color = RED  #алғашқы түс–қызыл
start_pos = None  # Тікбұрыш\шеңбер

screen.fill(WHITE) 

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
            start_pos = prev  
        
       
        if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
            if prev and drawing_mode == "free":
                pygame.draw.line(screen, color, prev, cur, 3)
                prev = cur
        
     
        if event.type == pygame.MOUSEBUTTONUP:
            if drawing_mode == "rect":  # Тікбұрыш 
                end_pos = pygame.mouse.get_pos()
                rect_width = end_pos[0] - start_pos[0]
                rect_height = end_pos[1] - start_pos[1]
                pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], rect_width, rect_height), 2)

            elif drawing_mode == "circle":  # Шеңбер
                end_pos = pygame.mouse.get_pos()
                radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, color, start_pos, radius, 2)

            prev = None 
        
        # клавиш арқылы басқару
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Қызыл
                color = RED
            elif event.key == pygame.K_g:  # Жасыл
                color = GREEN
            elif event.key == pygame.K_b:  # Көк
                color = BLUE
            elif event.key == pygame.K_e:  # Өшіргіш (ақ)
                color = WHITE
            elif event.key == pygame.K_f:  # Еркін сызу
                drawing_mode = "free"
            elif event.key == pygame.K_t:  # Тікбұрыш 
                drawing_mode = "rect"
            elif event.key == pygame.K_c:  # Шеңбер 
                drawing_mode = "circle"

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
