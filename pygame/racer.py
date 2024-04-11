import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

player_car_img = pygame.image.load("player_car.png")
enemy_car_img = pygame.image.load("enemy_car.png")

class Car:
    def __init__(self, x, y, speed, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image

    def move(self):
        self.y += self.speed

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

class Road:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, (0, 0, self.width, self.height))

road = Road(WIDTH, HEIGHT, BLACK)

player_car = Car(WIDTH // 2 - player_car_img.get_width() // 2, HEIGHT - player_car_img.get_height() - 50, 0, player_car_img)
enemy_car = Car(random.randint(0, WIDTH - enemy_car_img.get_width()), -100, 5, enemy_car_img)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_car.x > 0:
        player_car.x -= 5
    if keys[pygame.K_RIGHT] and player_car.x < WIDTH - player_car_img.get_width():
        player_car.x += 5

    enemy_car.move()
    if enemy_car.y > HEIGHT:
        enemy_car = Car(random.randint(0, WIDTH - enemy_car_img.get_width()), -100, 5, enemy_car_img)

    road.draw(window)
    player_car.draw(window)
    enemy_car.draw(window)

    pygame.display.update()
