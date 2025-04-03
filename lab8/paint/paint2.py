import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Simple Paint by Yenleak")
    clock = pygame.time.Clock()

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GRAY = (200, 200, 200)

    class Button:
        def __init__(self, x, y, width, height, text, color, action):
            self.rect = pygame.Rect(x, y, width, height)
            self.text = text
            self.color = color
            self.action = action  # Function to execute when clicked

        def draw(self, screen):
            pygame.draw.rect(screen, self.color, self.rect)
            font = pygame.font.Font(None, 30)
            text_surface = font.render(self.text, True, WHITE)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

        def check_click(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.action()

    drawing = False
    brush_color = BLUE  # Default color
    circle_mode = False  # Toggle between free draw and circle mode

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
        screen.fill(BLACK)  # Фонды қайтадан қара түске бояйды

    def exit_app():
        pygame.quit()
        sys.exit()

    def toggle_circle_mode():
        global circle_mode
        circle_mode = not circle_mode

    buttons = [
        Button(10, 10, 60, 30, "Black", BLACK, set_color_black),
        Button(80, 10, 60, 30, "Red", RED, set_color_red),
        Button(150, 10, 60, 30, "Green", GREEN, set_color_green),
        Button(220, 10, 60, 30, "Blue", BLUE, set_color_blue),
        Button(290, 10, 80, 30, "Clear", GRAY, clear_screen),
        Button(380, 10, 80, 30, "Exit", GRAY, exit_app),
        Button(470, 10, 80, 30, "Circle", BLUE, toggle_circle_mode)
    ]

    points = []
    radius = 10

    while True:
        screen.fill(BLACK)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            
            if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
                points.append(event.pos)
                points = points[-256:]

            for button in buttons:
                button.check_click(event)  

        for button in buttons:
            button.draw(screen)

        for i in range(len(points) - 1):
            pygame.draw.line(screen, brush_color, points[i], points[i + 1], radius)

        pygame.display.flip()
        clock.tick(60)

main()
