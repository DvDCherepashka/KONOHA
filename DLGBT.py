import pygame
import sys

W = 800
H = 600
k = 0
collide = False
# Квадрат
rect_size = w, h = 70, 70
rect_pos = ((W - w) // 2, (H - h) // 2)

# Круг
circle_radius = 35
circle_pos = (0, 0)

# цвета
RED = (250, 0, 0, 180)
BLUE = (255, 0, 238, 180)
GREEN = (72, 255, 0, 180)
BG = (0, 255, 255)

pygame.init()
pygame.display.set_caption('♂Dungeon master♂')
pygame.mouse.set_visible(True)
screen = pygame.display.set_mode((W, H))

font = pygame.font.SysFont('Arial', 40, True, False)
run = True
# Создаём поверхность размером в 2 раза больше радиуса круга и тд
surface = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA)
# НА СОЗДАНОЙ ПОВЕРХНОСТИ РИСУЕМ КРУГ А ЦВЕТА
pygame.draw.circle(surface, GREEN, (circle_radius, circle_radius), circle_radius)
# находится рект у поверхности
rect1 = surface.get_rect()


clock = pygame.time.Clock()
FPS = 597
speed_x, speed_y = 1, 1
ball = pygame.image.load('ball.png')
ball_rect = ball.get_rect()

while True:
    clock.tick(FPS)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)
        elif e.type == pygame.MOUSEMOTION:
            circle_pos = e.pos

    screen.fill(BG)

    ball_rect = ball_rect.move(speed_x, speed_y)
    if ball_rect.left < 0 or ball_rect.right > W:
        speed_x = -speed_x
    if ball_rect.top < 0 or ball_rect.bottom > H:
        speed_y = -speed_y

    COLOR = RED if collide else BLUE
    rect1 = pygame.draw.circle(screen, GREEN, circle_pos, circle_radius)
    rect2 = pygame.draw.rect(screen, COLOR, (rect_pos, rect_size))
    screen.blit(font.render('scorse: ' + str(k), True, GREEN), (60, 20))
    screen.blit(surface, rect1)
    if rect1.colliderect(rect2):  # Столкновение
        collide = True
        if COLOR == BLUE:
            k += 1
    else:
        collide = False

    screen.blit(ball, ball_rect)
    pygame.display.update()
