from random import randint
import pygame
from pygame.locals import *
import math

# 1) Initialisation de pygame
# 2) Appel des modules nécessaires
# 3) L’affichage
# 4) Boucle infinie
# 5) Fermeture du programme

# Initialise window
pygame.init()
pygame.mouse.set_visible(False)
# # creation of the window
window = pygame.display.set_mode((760, 570))

# sounds
radio = pygame.mixer.Sound("Games1/sounds/the-man-who-sold-the-world-1982.wav")
missile_sound = pygame.mixer.Sound("Games1/sounds/missile.wav")
music_ambiance = pygame.mixer.Sound("Games1/sounds/metroid-prime.wav")
music_ambiance.play(-1)
# creation of the background
background = pygame.image.load("Games1/frames/frame_0_delay-0.03s.png")
# background_animated = ['frame_' + str(i + 1) + '_delay-0.03s.png' for i in range(0, 159)]
# print(background_animated)

pic_width = 800
pic_height = 600
window.blit(background, (0, 0))
# for i in range(159):
#     background_animated[i] = pygame.image.load("Games1/frames/" + str(background_animated[i])).convert_alpha()
# print(background_animated[i])
# print(background_animated[i].get_rect())

# window.blit(background_animated[i], (0, 0, pic_width, pic_height))

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
y_limit_low = 504
y_limit_high = 132
y_enemy_limit_low = y_limit_low / 3
# continuous movement
pygame.key.set_repeat(400, 30)

# enemy control
enemyIMG = pygame.image.load('Games1/images/alien_spaceship.png').convert_alpha()
enemy_position_x = randint(x_limit_left, x_limit_right)
enemy_position_y = randint(y_limit_high, y_enemy_limit_low)
enemy_change = 0.3

# ammo
missileIMG = pygame.image.load('Games1/images/missile-1.png').convert_alpha()
missileX = 370
missileY = 440
missileXchange = 0
missileYchange = 0.5
fire_missile = "ok"

# rafraichissement de l'écran
# window.blit(background, (0, 0))
# window.blit(sprite_group, (0, 0))
window.blit(playerIMG, player_position)
window.blit(enemyIMG, (enemy_position_x, enemy_position_y))
# window.blit(missileIMG, (missileX, missileY))
pygame.display.update()

# mouse blocking
pygame.event.set_blocked(pygame.MOUSEMOTION)

# Event loop
Music = True
Continue = True
while Continue:
    # blit 2 params: 1) image to print 2)tuple abscissa and ordered
    window.fill((0, 0, 0))

    enemy_position_x += enemy_change
    if enemy_position_x < x_limit_left:
        enemy_position_x = x_limit_left
        enemy_change = 0.3
    if enemy_position_x > x_limit_right:
        enemy_position_x = x_limit_right
        enemy_change = -0.3
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
            if event.key == pygame.K_SPACE:
                if fire_missile == "ok":
                    fire_missile = "launched"
                    missile_sound.play()
                    missileX = player_position.x
                    window.blit(missileIMG, (player_position.x, player_position.y - 40))
                    print("FIRE!!!!")

            if event.key == pygame.K_ESCAPE:
                Continue = False
            if event.key == pygame.K_TAB and Music == True:
                Music = False
                music_ambiance.stop()
                radio.play()
            if event.key == pygame.K_LSHIFT and Music == False:
                Music = True
                radio.stop()
                music_ambiance.play(-1)
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

    # missile movements

    if missileY <= 0:
        missileY = player_position.y - 40
        fire_missile = "ok"

    if fire_missile == "launched":
        fire_missile = "launched"
        missileY -= missileYchange

    # missile physics
    distance_from_enemy = math.sqrt(
        math.pow(enemy_position_x - missileX, 2) + (math.pow(enemy_position_y - missileY, 2)))
    if distance_from_enemy < 27:
        state_of_target = "Hit"
        print("HIT!!!!")
    else:
        state_of_target = "Missed"

    if state_of_target == "hit":
        missileY = missileY - 40
        fire_missile = "ok"

    # borders and player movements
    if player_position.x < x_limit_left:
        player_position.x = x_limit_right
    if player_position.x > x_limit_right:
        player_position.x = x_limit_left
    if player_position.y < y_limit_high:
        player_position.y = y_limit_high
    if player_position.y > y_limit_low:
        player_position.y = y_limit_low

    # for i in range(159):background
    #     window.blit(_animated[i], ((0, 0, i * pic_width, i * pic_height)))
    window.blit(background, (0, 0))
    window.blit(playerIMG, player_position)
    window.blit(enemyIMG, (enemy_position_x, enemy_position_y))
    if fire_missile == "launched":
        window.blit(missileIMG, (missileX, missileY - 40))

    # rafraichissement de l'écran
    pygame.display.update()
