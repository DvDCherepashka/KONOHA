import pygame
import sys

W = 800
H = 600
collide = False
# Квадрат
rect_size = w, h = 70, 70
rect_pos = ((W - w) // 2, (H - h) // 2)

# Круг
circle_radius = 35
circle_pos = (0, 0)

# цвета
RED = (250, 0, 0)
BLUE = (255, 0, 238)
GREEN = (72, 255, 0)
BG = (0, 255, 255)

pygame.init()
pygame.display.set_caption('♂Dungeon master♂')
pygame.mouse.set_visible(True)
screen = pygame.display.set_mode((W, H))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)
        elif e.type == pygame.MOUSEMOTION:
            circle_pos = e.pos

    screen.fill(BG)

    rect1 = pygame.draw.circle(screen, GREEN, circle_pos, circle_radius)
    rect2 = pygame.draw.rect(screen, RED if collide is True else BLUE, (rect_pos, rect_size))

    if rect1.colliderect(rect2): # Столкновение
      
        collide = True
    else:
        collide = False

    pygame.display.update()
