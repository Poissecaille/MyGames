from random import randint
import pygame
from pygame.locals import *
import math

# 1) Initialisation de pygame
# 2) Appel des modules nécessaires
# 3) L’affichage
# 4) Boucle infinie
# 5) Fermeture du programme

# Initialise window framerate, window text render and sounds production
pygame.init()
clock = pygame.time.Clock()
framerateX = 50
pygame.mouse.set_visible(False)
# creation of the window
window = pygame.display.set_mode((800, 600))
window_centerX = 180
window_centerY = 250
pygame.font.init()
pygame.mixer.init()

# score and texts
score = 0
police = pygame.font.Font("Games1/polices/MountainBridge.otf", 25)
textX = 600
textY = 20

# sounds
radio = pygame.mixer.Sound("Games1/sounds/the-man-who-sold-the-world-1982.wav")
missile_explosion = pygame.mixer.Sound("Games1/sounds/explosion.wav")
missile_sound = pygame.mixer.Sound("Games1/sounds/missile.wav")
music_ambiance = pygame.mixer.Sound("Games1/sounds/metroid-prime.wav")
flame_noise = pygame.mixer.Sound("Games1/sounds/flame.wav")
music_ambiance.play(-1)

# creation of the background
# background = pygame.image.load("Games1/frames/frame_0_delay-0.03s.png").convert_alpha()
background_animated = ['frame_' + str(i + 1) + '_delay-0.03s.png' for i in range(0, 159)]
pic_width = 800
pic_height = 600
# window.blit(background, (0, 0))
animation_list = []
for i in range(159):
    animation_list.append(pygame.image.load("Games1/frames/" + str(background_animated[i])).convert_alpha())
    # print(animation_list)
#     # print(background_animated[i])
#     window.blit(background_animated[i], (0, 0, pic_width, pic_height))

# legend and images
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('Games1/images/alien.png')
pygame.display.set_icon(icon)
playerIMG = pygame.image.load('Games1/images/spaceship_player.png').convert_alpha()
enemyIMG = pygame.image.load('Games1/images/alien_spaceship.png').convert_alpha()
missileIMG = pygame.image.load('Games1/images/missile-1.png').convert_alpha()
missile_fireIMG = pygame.image.load('Games1/images/fire-missile.png').convert_alpha()
flameshipIMG = pygame.image.load('Games1/images/flame-ship.png').convert_alpha()
explosionIMG = pygame.image.load('Games1/images/explosion.png').convert_alpha()

# control of the player
player_position = playerIMG.get_rect()
player_position.x = 370
player_position.y = 480
player_position_change = 5
x_limit_left = 3
x_limit_right = 694
y_limit_low = 504
y_limit_high = 132
y_enemy_limit_low = 450
y_enemy_limit_high = 50
second_y_enemy_limit_high = 70
# continuous movement
pygame.key.set_repeat(400, 30)

# enemy control
enemy_position_x = randint(x_limit_left, x_limit_right)
enemy_position_y = randint(y_enemy_limit_high, second_y_enemy_limit_high)
enemy_change = 1.5
enemyY_change = 30
number_of_enemies = 10

# ammo
missileX = 370
missileY = 440
missileXchange = 0
missileYchange = 2.0
missile_fired = "ready for fire"

# ammo effect
fireX = missileX
fireY = missileY + 30
fireXchange = 0
fireYchange = 2.0
fire_missile = "nofire"
state_of_target = "missed"
# ship flame effect
flameX = 375
flameY = 520
flame2X = 365
flame2Y = 520
flameXchange = 0
flameYchange = 0.5
flame_ship = "noflame"

# mouse blocking
pygame.event.set_blocked(pygame.MOUSEMOTION)

# difficulty definition

# difficulty_choice = input("select a level difficulty: /1=>very easy,2=>easy,3=>medium,4=>hard,5=>very hard")
# if difficulty_choice == 1:
#     enemy_change = 1
#     number_of_enemies = 6
# if difficulty_choice == 2:
#     number_of_enemies = 10
#     enemy_change = 1
# if difficulty_choice == 3:
#     pass
# if difficulty_choice == 4:
#     number_of_enemies = 15
#     enemy_change = 2
#     enemyY_change = 40
# if difficulty_choice == 5:
#     number_of_enemies = 15
#     enemy_change = 2
#     missileYchange = 1.5
#     enemyY_change = 40
# if difficulty_choice == 6:
#     number_of_enemies = 15
#     enemy_change = 2.5
#     missileYchange = 1.5
#     enemyY_change = 50

# many enemies control
ManyenemyIMG = []
ManyenemyX = []
ManyenemyY = []
ManyenemyX_change = []
ManyenemyY_change = []

for e in range(number_of_enemies):
    ManyenemyIMG.append(enemyIMG)
    ManyenemyX.append(randint(x_limit_left, x_limit_right))
    ManyenemyY.append(randint(y_enemy_limit_high, second_y_enemy_limit_high))
    ManyenemyX_change.append(enemy_change)
    ManyenemyY_change.append(enemyY_change)
    # print(ManyenemyY)
    # print(ManyenemyX)

# Event loop
Music = True
Continue = True
Continue_after_endgame = True
counter = 0
while Continue:
    window.fill((0, 0, 0))
    for i in range(159):
        # counter += 1
        # print(counter)
        # if counter > 160:
        #     counter = 0
        pygame.display.update()
        window.blit(animation_list[i], (0, 0, pic_width, pic_height))
        # rending score/FPS actualisation
        score_text = police.render("Votre Score:" + str(score), True, pygame.Color('#FFFFFF'))
        framerate = police.render("FPS:" + str(int(clock.get_fps())), True, pygame.Color('#FFFFFF'))
        clock.tick(80)
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
                    if missile_fired == "ready for fire":
                        missile_fired = "launched"
                        fire_missile = "fire"
                        missile_sound.play()
                        missileX = player_position.x
                        fireX = player_position.x
                        missileY = player_position.y - 60
                        fireY = missileY + 66
                        window.blit(missileIMG, (player_position.x, missileY + 40))
                        window.blit(missile_fireIMG, (player_position.x, fireY + 20))
                        print("FIRE!!!!")
                if event.key == pygame.K_ESCAPE:
                    Continue = False
                if event.key == pygame.K_TAB and Music == True:
                    Music = False
                    music_ambiance.stop()
                    radio.play(-1)
                if event.key == pygame.K_LSHIFT and Music == False:
                    Music = True
                    radio.stop()
                    music_ambiance.play(-1)
                if event.key == pygame.K_UP:
                    flame_ship = "flame"
                    flameX = player_position.x - 10
                    flame2X = player_position.x + 10
                    flameY = player_position.y + 30
                    flame2Y = player_position.y + 30
                    player_position = player_position.move(0, -player_position_change)
                    print("UP")
                    window.blit(flameshipIMG, (player_position.x - 10, flameY + 30))
                    window.blit(flameshipIMG, (player_position.x + 10, flame2Y + 30))
                    pygame.time.delay(1)
                if event.key == pygame.K_DOWN:
                    print("DOWN")
                    player_position = player_position.move(0, player_position_change)
                if event.key == pygame.K_RIGHT:
                    print("RIGHT")
                    player_position = player_position.move(player_position_change, 0)
                if event.key == pygame.K_LEFT:
                    print("LEFT")
                    player_position = player_position.move(-player_position_change, 0)

        # enemy movements
        # enemy_position_x += enemy_change
        # if enemy_position_x <= x_limit_left:
        #     enemy_position_x = x_limit_left
        #     enemy_change += 0.5
        # if enemy_position_x >= x_limit_right:
        #     enemy_position_x = x_limit_right
        #     enemy_change = -0.5
        # if enemy_position_x == x_limit_left or enemy_position_x == x_limit_right:
        #     enemy_position_y += 10
        # if enemy_position_y >= y_enemy_limit_low:
        #     enemy_position_y = y_enemy_limit_low

        # missile movements
        if missileY <= 0 or missile_fired == "ready for fire":
            missileY = player_position.y - 20
            missile_fired = "ready for fire"

        if missile_fired == "launched":
            # missile_fired = "launched"
            missileY -= missileYchange

        # fire of the missile movements
        if fireY <= 30:
            fireY = player_position.y - 20
            fire_missile = "nofire"

        if fire_missile == "fire":
            fire_missile = "fire"
            fireY -= fireYchange

        # flame behind the ship movements
        if flameY > player_position.y + 40 and flame2Y > player_position.y + 40:
            flameY = player_position.y + 20
            flame2Y = player_position.y + 20
            flame_ship = "noflame"

        if flame_ship == "flame":
            flame_ship = "flame"
            flameY += flameYchange
            flame2Y += flameYchange
            flame_noise.play(1)

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
        # window.blit(background, (0, 0))
        window.blit(playerIMG, player_position)
        # window.blit(enemyIMG, (enemy_position_x, enemy_position_y))
        window.blit(score_text, (textX, textY))
        window.blit(framerate, (framerateX, textY))

        # if distance_from_enemy < 30 and state_of_target == "missed":
        #     state_of_target = "hit"
        #     print("HIT!!!!")
        #     window.blit(explosionIMG, (enemy_position_x, enemy_position_y))
        #     missile_explosion.play()
        #     pygame.display.flip()
        #     pygame.time.delay(1000)
        #     enemy_position_x = randint(x_limit_left, x_limit_right)
        #     enemy_position_y = randint(y_enemy_limit_high, y_enemy_limit_high + 10)
        #     score += 1
        # else:
        #     state_of_target = "Missed"
        #
        if missile_fired == "launched" and state_of_target != "hit":
            state_of_target = "missed"
            window.blit(missileIMG, (missileX, missileY - 20))
            window.blit(missile_fireIMG, (fireX, fireY - 20))
        if flame_ship == "flame":
            window.blit(flameshipIMG, (flameX - 10, flameY + 40))
            window.blit(flameshipIMG, (flame2X + 10, flame2Y + 40))
            # pygame.time.delay(1)
        for e in range(number_of_enemies):
            ManyenemyX[e] += ManyenemyX_change[e]
            # missile physics
            distance_from_enemy = math.sqrt(
                math.pow(ManyenemyX[e] - missileX, 2) + (math.pow(ManyenemyY[e] - missileY, 2)))
            distance_enemy_from_ship = math.sqrt(
                math.pow(ManyenemyX[e] - player_position.x, 2) + (math.pow(ManyenemyY[e] - player_position.y, 2)))
            # print(ManyenemyY)
            # print(ManyenemyX)
            if score >= 50:
                victory = police.render("VICTORY", True, pygame.Color('#FFFFFF'))
                text_rect = victory.get_rect(center=(pic_width / 2, pic_height / 2))
                pygame.display.flip()
                window.blit(victory, (text_rect))
                while Continue_after_endgame == True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            print("PRESS ESCAPE TO QUIT")
                            if event.key == pygame.K_ESCAPE:
                                pygame.quit()
                    pygame.display.update()
            if distance_enemy_from_ship < 50:
                game_over = police.render("Aliens killed you GAME OVER", True, pygame.Color('#FFFFFF'))
                text_rect = game_over.get_rect(center=(pic_width / 2, pic_height / 2))
                pygame.display.flip()
                window.blit(game_over, (text_rect))
                while Continue_after_endgame == True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            print("PRESS ESCAPE TO QUIT")
                            if event.key == pygame.K_ESCAPE:
                                pygame.quit()
                    pygame.display.update()

            if state_of_target == "hit":
                missileY = missileY - 20
                missile_fired = "ready for fire"
            if ManyenemyX[e] <= 0:
                ManyenemyX_change[e] = enemy_change
                ManyenemyY[e] += ManyenemyY_change[e]
            if ManyenemyX[e] >= x_limit_right:
                ManyenemyX_change[e] = -enemy_change
                ManyenemyY[e] += ManyenemyY_change[e]
            window.blit(ManyenemyIMG[e], (ManyenemyX[e], ManyenemyY[e]))
            if distance_from_enemy < 30 and state_of_target == "missed":
                state_of_target = "hit"
                window.blit(explosionIMG, (ManyenemyX[e], ManyenemyY[e]))
                missile_explosion.play()
                print("HIT!")
                pygame.display.flip()
                pygame.time.delay(100)
                ManyenemyX[e] = randint(x_limit_left, x_limit_right)
                ManyenemyY[e] = randint(y_enemy_limit_high, second_y_enemy_limit_high)
                score += 1
            else:
                state_of_target = "missed"
        # rafraichissement de l'écran
        # pygame.display.update()
pygame.quit()
