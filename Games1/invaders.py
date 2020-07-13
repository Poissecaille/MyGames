import pygame
from pygame.locals import *

# 1) Initialisation de pygame
# 2) Appel des modules nécessaires
# 3) L’affichage
# 4) Boucle infinie
# 5) Fermeture du programme

# Initialise window
pygame.init()

# creation of the window
window = pygame.display.set_mode((760, 570))

# creation of the background
background = pygame.image.load("Games1/images/space_image.png")
window.blit(background, (0, 0))

# legend and images
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('Games1/images/alien.png')
pygame.display.set_icon(icon)

# control of the player
playerIMG = pygame.image.load('Games1/images/spaceship.png').convert_alpha()
player_position = playerIMG.get_rect()
player_position.x = 370
player_position.y = 480
x_limit_left = 3
x_limit_right = 733
y_limit_low = 543
y_limit_high = 132
window.blit(playerIMG, player_position)
# continuous movement
pygame.key.set_repeat(400, 30)

# rafraichissement de l'écran
pygame.display.flip()

# Event loop
Continue = True
while Continue:

    # blit 2 params: 1) image to print 2)tuple abscissa and ordered
    for event in pygame.event.get():
        # print(player_position.x, player_position.y)

        if event.type == QUIT:
            Continue = False
        if event.type == pygame.KEYDOWN:
            print('key pressed')
            print(player_position.x, player_position.y)
            if player_position.x < x_limit_left:
                player_position.x = x_limit_right
            if player_position.x > x_limit_right:
                player_position.x = x_limit_left
            if player_position.y < y_limit_high:
                player_position.y = y_limit_high
            if player_position.y > y_limit_low:
                player_position.y = y_limit_low

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
        if event.type == pygame.KEYUP:
            print('released key')
    window.blit(background, (0, 0))
    window.blit(playerIMG, player_position)
    # rafraichissement de l'écran
    pygame.display.flip()
