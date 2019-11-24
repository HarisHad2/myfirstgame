import pygame
import random
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First game")

x = 220
y = 480
width = 60
height = 20
vel = 10

enemy_left_size = 30
enemy_left_x = 1
enemy_left_y = random.randrange(1, 251)

enemy_right_size = 30
enemy_right_x = 470
enemy_right_y = random.randrange(1, 251)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

run = True 

clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
   
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel

    win.fill((BLACK))
    if enemy_left_y >= 0 and enemy_left_y < 500:
        enemy_left_y += 15
        enemy_left_x += 8
    else:
        enemy_left_y = random.randrange(1, 251)
        enemy_left_x = 1
    
    if enemy_right_y <= 500 and enemy_right_y < 500:
        enemy_right_y += 15
        enemy_right_x -= 8
    else:
        enemy_right_y = random.randrange(1, 251)
        enemy_right_x = 470


    pygame.draw.rect(win, GREEN, (enemy_right_x, enemy_right_y, enemy_right_size, enemy_right_size))
    pygame.draw.rect(win, RED, (enemy_left_x, enemy_left_y, enemy_left_size, enemy_left_size))
    pygame.draw.rect(win, BLUE, (x, y, width, height))
    pygame.display.update()

    clock.tick(30)

pygame.quit()