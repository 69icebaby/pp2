import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

def check_collision(snake):
    head_x, head_y = snake[0]
    return head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT

def main():
    clock = pygame.time.Clock()
    snake = [(WIDTH // 2, HEIGHT // 2)] * 4 
    direction = "RIGHT"  

    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    direction = "RIGHT"
                elif event.key == pygame.K_UP:
                    direction = "UP"
                elif event.key == pygame.K_DOWN:
                    direction = "DOWN"

        head_x, head_y = snake[0]
        if direction == "RIGHT":
            head_x += GRID_SIZE
        elif direction == "LEFT":
            head_x -= GRID_SIZE
        elif direction == "UP":
            head_y -= GRID_SIZE
        elif direction == "DOWN":
            head_y += GRID_SIZE

        new_head = (head_x, head_y)

        if check_collision(snake):
            pygame.quit()
            sys.exit()

        snake.insert(0, new_head)

        if len(snake) > 4:
            del snake[-1]

        draw_snake(snake)

        pygame.display.update()
        clock.tick(10)  

if __name__ == "__main__":
    main()
