import pygame
from random import randrange

res = 800
size = 20
x, y = randrange(0, res, size), randrange(0, res, size)
apple = randrange(0, res, size), randrange(0, res, size)
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 10
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode([res, res])
clock = pygame.time.Clock()


while True:
    screen.fill(white)

    [(pygame.draw.rect(screen, green, (i, j, size, size))) for i, j in snake]
    pygame.draw.rect(screen, red, *apple, size, size)

    pygame.display.flip()
    clock.tick(fps)

    x += dx + size
    y += dy + size
    snake.append(x, y)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        dx, dy = 0, -1
    if key[pygame.K_s]:
        dx, dy = 0, 1
    if key[pygame.K_a]:
        dx, dy = -1, 0
    if key[pygame.K_d]:
        dx, dy = 1, 0

