import pygame
import random
pygame.init()

# Skärmen
win_WIDTH = 500
win_HEIGHT = 500

win = pygame.display.set_mode((win_WIDTH, win_HEIGHT))
pygame.display.set_caption("First game")

# Variabler till min gubbe
player_pos = [220, 480]
width = 20
height = 15
vel = 2

# Variabler till fienderna
enemy_left_size = 15
enemy_left_pos = [1, random.randrange(1, 251)]
enemy_left_list = [enemy_left_pos]

enemy_right_size = 15
enemy_right_pos = [485, random.randrange(1, 251)]
enemy_right_list = [enemy_right_pos]

speed_down = 1
speed_left = 1
speed_right = 1

# Färger
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


run = True 

clock = pygame.time.Clock()

def enemy_left_count(enemy_left_list):
    if len(enemy_left_list) < 5:
        xl_pos = 1
        yl_pos = random.randrange(1,251)        
        enemy_left_list.append([xl_pos, yl_pos])


def draw_left_enemies(enemy_left_list):
    for enemy_left_pos in enemy_left_list:
        pygame.draw.rect(win, RED, (enemy_left_pos[0], enemy_left_pos[1], enemy_left_size, enemy_left_size))

#def enemy_left_movement(enemy_left_list):
    




def collision_left(player_pos, enemy_left_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_l_x = enemy_left_pos[0]
    e_l_y = enemy_left_pos[1]

    if (e_l_x >= p_x and e_l_x < (p_x + width)) or (p_x >= e_l_x and p_x < (e_l_x + enemy_left_size)):
        if (e_l_y >= p_y and e_l_y < (p_y + width)) or (p_y >= e_l_y and p_y < (e_l_y + enemy_left_size)):
            return True
    return False

def collision_right(player_pos, enemy_right_pos):

    p_x = player_pos[0]
    p_y = player_pos[1]

    e_r_x = enemy_right_pos[0]
    e_r_y = enemy_right_pos[1]

    if (e_r_x >= p_x and e_r_x < (p_x + width)) or (p_x >= e_r_x and p_x < (e_r_x + enemy_right_size)):
        if (e_r_y >= p_y and e_r_y < (p_y + width)) or (p_y >= e_r_y and p_y < (e_r_y + enemy_right_size)):
            return True
    return False
    
    
    

# Spel loopet
while run:
    pygame.time.delay(1)

    # Stänga fönstret
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Kontroller
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_pos[0] > vel:
        player_pos[0] -= vel
   
    if keys[pygame.K_RIGHT] and player_pos[0] < 500 - width - vel:
        player_pos[0] += vel

    win.fill((BLACK))
    # Fienders rörelse
    if enemy_left_pos[1] >= 0 and enemy_left_pos[1] < 500:
        enemy_left_pos[1] += speed_down
        enemy_left_pos[0] += speed_right
    else:
        enemy_left_pos[1] = random.randrange(1, 251)
        enemy_left_pos[0] = 1
    
    if enemy_right_pos[1] <= 500 and enemy_right_pos[1] < 500:
        enemy_right_pos[1] += speed_down
        enemy_right_pos[0] -= speed_left
    else:
        enemy_right_pos[1] = random.randrange(1, 251)
        enemy_right_pos[0] = 485

    if collision_left(player_pos, enemy_left_pos):
        run = False
        break

    if collision_right(player_pos, enemy_right_pos):
        run = False
        break

    enemy_left_count(enemy_left_list)
    draw_left_enemies(enemy_left_list)    

    pygame.draw.rect(win, GREEN, (enemy_right_pos[0], enemy_right_pos[1], enemy_right_size, enemy_right_size))
    #pygame.draw.rect(win, RED, (enemy_left_pos[0], enemy_left_pos[1], enemy_left_size, enemy_left_size))
    pygame.draw.rect(win, BLUE, (player_pos[0], player_pos[1], width, height))
    pygame.display.update()

    clock.tick(120)

pygame.quit()