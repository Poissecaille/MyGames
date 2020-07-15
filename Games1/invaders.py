from random import randint

import pygame
from pygame.locals import *

# 1) Initialisation de pygame
# 2) Appel des modules nécessaires
# 3) L’affichage
# 4) Boucle infinie
# 5) Fermeture du programme

# Initialise window
pygame.init()
pygame.mouse.set_visible(False)
# creation of the window
window = pygame.display.set_mode((760, 570))

# creation of the background
background = pygame.image.load("Games1/images/space_image.png")
# window.blit(background, (0, 0))

# legend and images
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('Games1/images/alien.png')
pygame.display.set_icon(icon)

# control of the player
playerIMG = pygame.image.load('Games1/images/spaceship_player.png').convert_alpha()
player_position = playerIMG.get_rect()
player_position.x = 370
player_position.y = 480
x_limit_left = 3
x_limit_right = 694
y_limit_low = 543
y_limit_high = 132
y_enemy_limit_low = y_limit_low / 3
window.blit(playerIMG, player_position)
# continuous movement
pygame.key.set_repeat(400, 30)

# enemy control
enemyIMG = pygame.image.load('Games1/images/alien_spaceship.png').convert_alpha()
enemy_position_x = randint(x_limit_left, x_limit_right)
enemy_position_y = randint(y_limit_high, y_enemy_limit_low)
enemy_change = 1

# rafraichissement de l'écran
window.blit(background, (0, 0))
window.blit(playerIMG, player_position)
window.blit(enemyIMG, (enemy_position_x, enemy_position_y))
pygame.display.update()

# mouse blocking
pygame.event.set_blocked(pygame.MOUSEMOTION)

# Event loop
Continue = True
while Continue:
    # blit 2 params: 1) image to print 2)tuple abscissa and ordered
    window.fill((0, 0, 0))
    window.blit(background, (0, 0))

    # borders and enemy movements
    enemy_position_x += enemy_change
    if enemy_position_x < x_limit_left:
        enemy_position_x = x_limit_left
        enemy_change = 1
    if enemy_position_x > x_limit_right:
        enemy_position_x = x_limit_right
        enemy_change = -1
    if enemy_position_x == x_limit_left or enemy_position_x == x_limit_right:
        enemy_position_y += 3

        # keys
    for event in pygame.event.get():
        if event.type == QUIT:
            Continue = False
        if event.type == pygame.KEYUP:
            print('key released')
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_position = player_position
        if event.type == pygame.KEYDOWN:
            print('key pressed')
            print(player_position.x, player_position.y)
            if event.key == pygame.K_ESCAPE:
                Continue = False
            if event.key == pygame.K_UP:
                player_position = player_position.move(0, -3)
                print("UP")
            if event.key == pygame.K_DOWN:
                print("DOWN")
                player_position = player_position.move(0, 3)
            if event.key == pygame.K_RIGHT:
                print("RIGHT")
                player_position = player_position.move(3, 0)
            if event.key == pygame.K_LEFT:
                print("LEFT")
                player_position = player_position.move(-3, 0)

    # borders and player movements
    if player_position.x < x_limit_left:
        player_position.x = x_limit_right
    if player_position.x > x_limit_right:
        player_position.x = x_limit_left
    if player_position.y < y_limit_high:
        player_position.y = y_limit_high
    # if player_position.y > y_limit_low:
    #     player_position.y = y_limit_low

    window.blit(playerIMG, player_position)
    window.blit(enemyIMG, (enemy_position_x, enemy_position_y))
    # rafraichissement de l'écran
    pygame.display.update()
