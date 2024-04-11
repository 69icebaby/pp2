import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Определение констант
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Функция отрисовки змейки
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

# Функция отрисовки еды
def draw_food(food_position):
    pygame.draw.rect(screen, GREEN, (food_position[0], food_position[1], GRID_SIZE, GRID_SIZE))

# Основной игровой цикл
def main():
    clock = pygame.time.Clock()
    snake = [(WIDTH // 2, HEIGHT // 2)]  # Начальное положение змейки
    food_position = (random.randint(0, (WIDTH-GRID_SIZE)//GRID_SIZE) * GRID_SIZE,
                     random.randint(0, (HEIGHT-GRID_SIZE)//GRID_SIZE) * GRID_SIZE)  # Положение еды

    while True:
        screen.fill(WHITE)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Движение змейки
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            snake[0] = (snake[0][0] - GRID_SIZE, snake[0][1])
        elif keys[pygame.K_RIGHT]:
            snake[0] = (snake[0][0] + GRID_SIZE, snake[0][1])
        elif keys[pygame.K_UP]:
            snake[0] = (snake[0][0], snake[0][1] - GRID_SIZE)
        elif keys[pygame.K_DOWN]:
            snake[0] = (snake[0][0], snake[0][1] + GRID_SIZE)

        # Отрисовка змейки и еды
        draw_snake(snake)
        draw_food(food_position)

        pygame.display.update()
        clock.tick(10)  # Скорость движения змейки (10 кадров в секунду)

if __name__ == "__main__":
    main()
