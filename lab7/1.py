import pygame
import sys
from datetime import datetime
import math

pygame.init()
WIDTH, HEIGHT = 849, 833
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Часы")
clock_img = pygame.image.load("mickeyclock.jpeg")

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    now_time = datetime.now()
    h, m = now_time.hour, now_time.minute
    screen.blit(clock_img, (0, 0))

    a_h = (h % 12 + m / 60) * 360 / 12
    a_m = m * 360 / 60

    h_l = 80
    m_l = 110
    h_x = 200 + h_l * math.cos(math.radians(90 - a_h))
    h_y = 200 - h_l * math.sin(math.radians(90 - a_h))
    m_x = 200 + m_l * math.cos(math.radians(90 - a_m))
    m_y = 200 - m_l * math.sin(math.radians(90 - a_m))

    pygame.draw.line(screen, (0, 0, 0), (424, 416), (h_x, h_y), 8)
    pygame.draw.line(screen, (255, 0, 0), (424, 416), (m_x, m_y), 4)

    pygame.display.flip()