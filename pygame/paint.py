import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

current_color = BLACK
current_tool = "square"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_color = RED
            elif event.key == pygame.K_b:
                current_color = BLUE
            elif event.key == pygame.K_w:
                current_color = WHITE
            elif event.key == pygame.K_k:
                current_color = BLACK
            elif event.key == pygame.K_s:
                current_tool = "square"
            elif event.key == pygame.K_c:
                current_tool = "circle"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if current_tool == "square":
                    pygame.draw.rect(window, current_color, pygame.Rect(event.pos[0], event.pos[1], 20, 20))
                elif current_tool == "circle":
                    pygame.draw.circle(window, current_color, event.pos, 10)

    window.fill(WHITE)

    pygame.display.flip()

