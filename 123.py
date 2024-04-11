import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Цвета
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

# Шрифт
font = pygame.font.SysFont(None, 30)

# Класс монетки
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(3, 7)  # Скорость монетки

    def update(self):
        self.rect.y += self.speed

# Генерация монеток с разной вероятностью
def generate_coins():
    coins = pygame.sprite.Group()
    for _ in range(10):  # Генерируем 10 монеток
        coin = Coin()
        coins.add(coin)
    return coins

# Функция отрисовки текста
def draw_text(text, color, x, y):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

# Главный игровой цикл
def main():
    clock = pygame.time.Clock()
    coins = generate_coins()
    player_collected_coins = 0
    enemy_speed_increment_threshold = 5  # Порог для увеличения скорости врага
    enemy_speed_increment = 1  # Увеличение скорости врага
    enemy_speed = 5  # Изначальная скорость врага

    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Обновление монеток
        for coin in coins:
            coin.update()
            screen.blit(coin.image, coin.rect)

        # Отрисовка и обновление текста собранных монеток
        draw_text(f"Collected Coins: {player_collected_coins}", RED, SCREEN_WIDTH - 200, 20)

        # Проверка коллизий с монетками
        collected_coins = pygame.sprite.spritecollide(player, coins, True)
        player_collected_coins += len(collected_coins)

        # Увеличение скорости врага при достижении порога собранных монеток
        if player_collected_coins >= enemy_speed_increment_threshold:
            enemy_speed += enemy_speed_increment
            enemy_speed_increment_threshold += 5

        pygame.display.flip()
        clock.tick(60)

# Запуск игры
if __name__ == "__main__":
    main()
