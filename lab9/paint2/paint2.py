import pygame
import sys
import math

pygame.init()

#screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint game by Yenleak")

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

#paint area
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)  # Фонды ақ түспен бояймыз

#class for buttons
class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action  #if button is pressed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 25)
        text_surface = font.render(self.text, True, WHITE)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.action()


drawing = False
brush_color = BLACK  #first color
shape_mode = None  #form type
start_pos = None  #first pos

#functions for buttons
def set_color_black():
    global brush_color
    brush_color = BLACK

def set_color_red():
    global brush_color
    brush_color = RED

def set_color_green():
    global brush_color
    brush_color = GREEN

def set_color_blue():
    global brush_color
    brush_color = BLUE

def clear_screen():
    canvas.fill(WHITE)  #clear screen

def exit_app():
    pygame.quit()
    sys.exit()

def set_shape_square():
    global shape_mode
    shape_mode = "square"

def set_shape_triangle():
    global shape_mode
    shape_mode = "triangle"

def set_shape_equilateral_triangle():
    global shape_mode
    shape_mode = "equilateral_triangle"

def set_shape_rhombus():
    global shape_mode
    shape_mode = "rhombus"

#list of buttons
buttons = [
    Button(10, 10, 60, 30, "Black", BLACK, set_color_black),
    Button(80, 10, 60, 30, "Red", RED, set_color_red),
    Button(150, 10, 60, 30, "Green", GREEN, set_color_green),
    Button(220, 10, 60, 30, "Blue", BLUE, set_color_blue),
    Button(290, 10, 80, 30, "Clear", GRAY, clear_screen),
    Button(380, 10, 80, 30, "Exit", GRAY, exit_app),
    Button(470, 10, 80, 30, "Square", GRAY, set_shape_square),
    Button(560, 10, 80, 30, "Triangle", GRAY, set_shape_triangle),
    Button(650, 10, 80, 30, "Eq. Tri", GRAY, set_shape_equilateral_triangle),
    Button(740, 10, 80, 30, "Rhombus", GRAY, set_shape_rhombus)
]

#main loop
while True:
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0)) #save first paint

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  #left button
                start_pos = pygame.mouse.get_pos()
                drawing = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                end_pos = pygame.mouse.get_pos()
                if shape_mode == "square":
                    width = abs(end_pos[0] - start_pos[0])
                    pygame.draw.rect(canvas, brush_color, (*start_pos, width, width), 2)
                elif shape_mode == "triangle":
                    pygame.draw.polygon(canvas, brush_color, [start_pos, (end_pos[0], start_pos[1]), end_pos], 2)
                elif shape_mode == "equilateral_triangle":
                    height = abs(end_pos[1] - start_pos[1])
                    pygame.draw.polygon(canvas, brush_color, [start_pos, (start_pos[0] - height // 2, end_pos[1]), (start_pos[0] + height // 2, end_pos[1])], 2)
                elif shape_mode == "rhombus":
                    width = abs(end_pos[0] - start_pos[0])
                    pygame.draw.polygon(canvas, brush_color, [(start_pos[0], start_pos[1] - width // 2), (start_pos[0] - width // 2, start_pos[1]), (start_pos[0], start_pos[1] + width // 2), (start_pos[0] + width // 2, start_pos[1])], 2)
                
                drawing = False  #finished paint
                start_pos = None

        for button in buttons:
            button.check_click(event)

    #putting buttons on the screen
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, 50))  # Басқару панелі
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()
