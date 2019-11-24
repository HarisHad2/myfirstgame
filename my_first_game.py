import pygame
import random
pygame.init()

# Skärmen
win_WIDTH = 500
WIN_HEIGHT = 500

win = pygame.display.set_mode((win_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("First game")

# Variabler till min gubbe
x = 220
y = 480
width = 20
height = 20
vel = 10

# Variabler till fienderna
enemy_left_size = 15
enemy_left_x = 1
enemy_left_y = random.randrange(1, 251)

enemy_right_size = 15
enemy_right_x = 485
enemy_right_y = random.randrange(1, 251)

speed_down = 15
speed_left = 15
speed_right = 15

# Färger
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


run = True 

clock = pygame.time.Clock()

# Spel loopet
while run:
    pygame.time.delay(100)

    # Stänga fönstret
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Kontroller
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
   
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel

    win.fill((BLACK))
    # Fienders rörelse
    if enemy_left_y >= 0 and enemy_left_y < 500:
        enemy_left_y += speed_down
        enemy_left_x += speed_right
    else:
        enemy_left_y = random.randrange(1, 251)
        enemy_left_x = 1
    
    if enemy_right_y <= 500 and enemy_right_y < 500:
        enemy_right_y += speed_down
        enemy_right_x -= speed_left
    else:
        enemy_right_y = random.randrange(1, 251)
        enemy_right_x = 485

    pygame.draw.rect(win, GREEN, (enemy_right_x, enemy_right_y, enemy_right_size, enemy_right_size))
    pygame.draw.rect(win, RED, (enemy_left_x, enemy_left_y, enemy_left_size, enemy_left_size))
    pygame.draw.rect(win, BLUE, (x, y, width, height))
    pygame.display.update()

    clock.tick(30)

pygame.quit()
