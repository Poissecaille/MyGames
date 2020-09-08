import pygame, sys, random, math
import time

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)
BGCOLOR = BLACK

pygame.init()
clock = pygame.time.Clock()
start_countdown = 3
window_width = 1000
window_height = 800
window = pygame.display.set_mode((window_width, window_height))
pygame.font.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()

# score and texts
player1_name = 'Alex'
score_player1 = 0
score_ordi = 0
police = pygame.font.Font("D:/DEVOP/MyGames/Games2/polices/Sketch3D.otf", 25)
score_player1X = window_width * 3 / 4
score_ordiX = window_width / 4
score_player1Y = window_height / 4
score_ordiY = window_height / 4

music_game = pygame.mixer.Sound("D:/DEVOP/MyGames/Games2/sounds/ace_combat.wav")
racket_noise = pygame.mixer.Sound("D:/DEVOP/MyGames/Games2/sounds/shuffle_racket_noise.wav")
racket_noise2 = pygame.mixer.Sound("D:/DEVOP/MyGames/Games2/sounds/shuffle_racket_noise_ordi.wav")
obstacle_noise = pygame.mixer.Sound("D:/DEVOP/MyGames/Games2/sounds/shuffle_obstacle_noise.wav")
goal = pygame.mixer.Sound("D:/DEVOP/MyGames/Games2/sounds/shuffle_puck_goal.wav")
# music_game.play(-1)

pygame.display.set_caption('Shuffle Puck')
icon = pygame.image.load('D:/DEVOP/MyGames/Games2/images/ball.png')
player_cursor = pygame.image.load('D:/DEVOP/MyGames/Games2/images/shuffle_racket.png').convert_alpha()
ordi_cursor = pygame.image.load('D:/DEVOP/MyGames/Games2/images/shuffle_racket2.png').convert_alpha()
ball = pygame.image.load('D:/DEVOP/MyGames/Games2/images/shuffle_ball.png').convert_alpha()
pygame.display.set_icon(icon)
background_color = (0, 0, 0)

# rect_player_cursor = player_cursor.get_rect()
player_cursorX = int(window_width / 2) - 30
player_cursorY = int(window_height / 4 * 3)
ordi_cursorX = int(window_width / 2) - 30
ordi_cursorY = 25
ordi_cursor_speed = 5
rect_player = pygame.draw.rect(window, WHITE, (55, 55, 55, 55), 1)
rect_ordi = pygame.draw.rect(window, WHITE, (55, 55, 55, 55), 1)
ballX_start = int(window_width / 2) - 15
ballY_start = int(window_height / 2) - 15
ballX = ballX_start
ballY = ballY_start
rect_ball = pygame.draw.rect(window, WHITE, (50, 50, 50, 50), 1)

random_direction = random.choice([-1, 1])
start_speedX = 3 * random_direction
start_speedY = 3 * random_direction
ballX_speed = 10
ballY_speed = 10

goalXlow = 353
goalXhigh = 652
goalYordi = 60
goalYplayer = window_height - 60
score_time = True
basic_font = pygame.font.Font('freesansbold.ttf', 32)
################ SETTINGS ####################

# mouse blocking
pygame.mouse.set_visible(False)
collision_correction_for_straight_mov = 16
pygame.mouse.set_pos([int(window_width / 2), int(window_height / 4 * 3)])


# push_fix_ordi = 20
# maskPlayer = pygame.mask.from_surface(player_cursor)
# maskBall = pygame.mask.from_surface(ball)

def collision(rect_, rect_ball):
    if rect_ball.right < rect_.left:
        return False
    if rect_ball.bottom < rect_.top:
        return False
    if rect_ball.left > rect_.right:
        return False
    if rect_ball.top > rect_.bottom:
        return False
    return True


goal_status = "no_goal"
while True:
    random_direction = random.choice([-1, 1])
    window.fill(background_color)
    time_in_miliseconds = pygame.time.get_ticks()
    time_in_seconds = time_in_miliseconds // 1000
    time_in_minutes = time_in_seconds // 60
    countdown = start_countdown + score_time - time_in_seconds
    display_countdown = police.render('cooldown:' + str(countdown), True, pygame.Color(255, 255, 255))
    display_timer = police.render('time:' + str(time_in_minutes) + '.' + str(time_in_seconds), True,
                                  pygame.Color(255, 255, 255))
    display_score_player1 = police.render(str(player1_name) + ':' + str(score_player1), True,
                                          pygame.Color(255, 255, 255))
    display_score_ordi = police.render('ordi:' + str(score_ordi), True,
                                       pygame.Color(255, 255, 255))
    if countdown >= 0:
        start_speedX = 0
        start_speedY = 0
        if countdown <= 3:
            window.blit(display_countdown, (int(window_width / 2 - 60), int(window_height / 3)))
    print(countdown)
    # ball movements
    ballX += start_speedX
    ballY += start_speedY
    # physics
    # player_distance_from_ball = math.sqrt(
    #     math.pow(player_cursorX - ballX, 2) + (math.pow(player_cursorY - ballY, 2)))
    # ordi_distance_from_ball = math.sqrt(
    #     math.pow(ordi_cursorX - ballX, 2) + (math.pow(ordi_cursorY - ballY, 2)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION and event.pos[1] > window_height / 2:
            player_cursorX = event.pos[0]
            player_cursorY = event.pos[1]
            rect_player.center = pygame.mouse.get_pos()
            # print(player_cursorX)
            # print(player_cursorY)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # print(ballX)
    # print(ballY)
    if ballX > goalXlow and ballX < goalXhigh:
        if ballY <= 10:
            goal.play()
            score_player1 += 1
            ballX = ballX_start
            ballY = ballY_start
            goal_status = "goal"
            score_time = pygame.time.get_ticks() // 1000
            start_speedX = start_speedX * random_direction
            start_speedY = start_speedY * random_direction
        if ballY >= window_height - 10:
            goal.play()
            score_ordi += 1
            ballX = ballX_start
            ballY = ballY_start
            goal_status = "goal"
            score_time = pygame.time.get_ticks() // 1000
            start_speedX = start_speedX * random_direction
            start_speedY = start_speedY * random_direction

    if ballX < 0:
        ballX = 0
        start_speedX *= -1
        obstacle_noise.play()
    if ballX >= window_width:
        ballX = window_width
        start_speedX *= -1
        obstacle_noise.play()
    if ballY <= 0:
        ballY = 0
        start_speedY *= -1
        obstacle_noise.play()
    if ballY >= window_height:
        ballY = window_height
        start_speedY *= -1
        obstacle_noise.play()

    if collision(rect_player, rect_ball) == True:
        start_speedX = ballX_speed
        start_speedY = ballY_speed
        racket_noise.play()
        if rect_ball.x < rect_player.x - collision_correction_for_straight_mov and rect_ball.y < rect_player.y:
            start_speedY *= -1
            start_speedX *= -1
        if rect_ball.x > rect_player.x - collision_correction_for_straight_mov and rect_ball.x < rect_player.x + collision_correction_for_straight_mov and rect_ball.y < rect_player.y:
            start_speedX *= 0
            start_speedY *= -1
        if rect_ball.x > rect_player.x + collision_correction_for_straight_mov and rect_ball.y < rect_player.y:
            start_speedX *= 1
            start_speedY *= -1

        if rect_ball.x < rect_player.x - collision_correction_for_straight_mov and rect_ball.y > rect_player.y:
            start_speedY *= 1
            start_speedX *= -1
        if rect_ball.x > rect_player.x + collision_correction_for_straight_mov and rect_ball.x < rect_player.x + collision_correction_for_straight_mov and rect_ball.y > rect_player.y:
            start_speedX *= 0
            start_speedY *= 1
        if rect_ball.x > rect_player.x + collision_correction_for_straight_mov and rect_ball.y > rect_player.y:
            start_speedX *= 1
            start_speedY *= 1

        if rect_ball.x > rect_player.x and rect_ball.y > rect_player.y - collision_correction_for_straight_mov and rect_ball.y < rect_player.y + collision_correction_for_straight_mov:
            start_speedY *= 0
            start_speedX *= 1
        if rect_ball.x < rect_player.x and rect_ball.y > rect_player.y - collision_correction_for_straight_mov and rect_ball.y < rect_player.y + collision_correction_for_straight_mov:
            start_speedY *= 0
            start_speedX *= 1
        if rect_ball.y > rect_player.y and rect_ball.x > rect_player.x - collision_correction_for_straight_mov and rect_ball.x < rect_player.x + collision_correction_for_straight_mov:
            start_speedY *= 1
            start_speedX *= 0

    if collision(rect_ordi, rect_ball):
        start_speedX = ballX_speed
        start_speedY = ballY_speed
        ordi_cursorX = int(window_width / 2)
        racket_noise2.play()
        if rect_ball.x < rect_ordi.x - collision_correction_for_straight_mov and rect_ball.y > rect_ordi.y:
            start_speedY *= 1
            start_speedX *= -1
            # rect_ball.x -= push_fix_ordi
            # rect_ball.y += push_fix_ordi
        if rect_ball.x > rect_ordi.x - collision_correction_for_straight_mov and rect_ball.x < rect_ordi.x + collision_correction_for_straight_mov and rect_ball.y > rect_player.y:
            start_speedX *= 0
            start_speedY *= 1
            # rect_ball.y += push_fix_ordi
        if rect_ball.x > rect_ordi.x + collision_correction_for_straight_mov and rect_ball.y > rect_ordi.y:
            start_speedX *= 1
            start_speedY *= 1
            # rect_ball.x += push_fix_ordi
            # rect_ball.y += push_fix_ordi

        if rect_ball.x < rect_ordi.x - collision_correction_for_straight_mov and rect_ball.y < rect_ordi.y:
            start_speedY *= -1
            start_speedX *= -1
            # rect_ball.x -= push_fix_ordi
            # rect_ball.y -= push_fix_ordi
        if rect_ball.x > rect_ordi.x + collision_correction_for_straight_mov and rect_ball.x < rect_ordi.x + collision_correction_for_straight_mov and rect_ball.y < rect_ordi.y:
            start_speedX *= 0
            start_speedY *= -1
            # rect_ball.y -= push_fix_ordi

        if rect_ball.x > rect_ordi.x + collision_correction_for_straight_mov and rect_ball.y < rect_ordi.y:
            start_speedX *= -1
            start_speedY *= -1
            # rect_ball.x -= push_fix_ordi
            # rect_ball.y -= push_fix_ordi

        #############################################################################
        # if rect_ball.x > rect_ordi.x and rect_ball.y > rect_ordi.y - collision_correction_for_straight_mov and rect_ball.y < rect_ordi.y + collision_correction_for_straight_mov:
        #     start_speedY *= 0
        #     start_speedX *= 1
        #     racket_noise2.play()
        # if rect_ball.x < rect_ordi.x and rect_ball.y > rect_ordi.y - collision_correction_for_straight_mov and rect_ball.y < rect_ordi.y + collision_correction_for_straight_mov:
        #     start_speedY *= 0
        #     start_speedX *= 1
        #     racket_noise2.play()
        # if rect_ball.y > rect_ordi.y and rect_ball.x > rect_ordi.x - collision_correction_for_straight_mov and rect_ball.x < rect_ordi.x + collision_correction_for_straight_mov:
        #     start_speedY *= 1
        #     start_speedX *= 0
        #     racket_noise2.play()
        #############################################################################

        # if rect_ball.x < rect_player.x and rect_ball.y < rect_player.y - 30:
        #     racket_noise.play()
        #     start_speedX *= -1
        #     start_speedY *= -1
        # if rect_ball.x < rect_player.x and rect_ball.y > rect_player.y - 30 and rect_ball.y < rect_player.y - 10:
        #     racket_noise.play()
        #     start_speedY *= 0
        #     start_speedX *= -1
        # if rect_ball.x < rect_player.x and rect_ball.y > rect_player.y - 10:
        #     racket_noise.play()
        #     start_speedY *= -1
        #     start_speedX *= -1
        # if rect_ball.x > rect_player.x and rect_ball.y > rect_player.y:
        #     start_speedY *= 0
        #     start_speedX *= 1

    # masking for non-geometric forms
    # if maskPlayer.overlap(maskBall, (rect_ball.left - rect_player.left, rect_ball.top - rect_player.top)) != None:
    #     print("collision")
    #     racket_noise.play()
    #     start_speedX = ballX_speed
    #     start_speedY = ballY_speed
    #     start_speedY *= -1

    # if ordi_distance_from_ball < impact_distance:
    #     # bug stick ball
    #     ballY += push_upgrade
    #     # ball_acceleration
    #     start_speedX = ballX_speed
    #     start_speedY *= -1
    #     # contact
    #     racket_noise.play()
    #     ballX_speed *= random_direction
    #     random_direction = random.choice([-1, 1])
    #     ballY_speed *= -1

    if ballX > ordi_cursorX:
        ordi_cursorX += ordi_cursor_speed
    if ballX < ordi_cursorX:
        ordi_cursorX -= ordi_cursor_speed
    if ballY < ordi_cursorY:
        ordi_cursorY -= ordi_cursor_speed
    if ballY > ordi_cursorY:
        ordi_cursorY += ordi_cursor_speed
    if ordi_cursorX < goalXlow:
        ordi_cursorX = goalXlow
    if ordi_cursorX > goalXhigh:
        ordi_cursorX = goalXhigh
    if ordi_cursorY > goalYordi:
        ordi_cursorY = goalYordi

    if player_cursorY <= int(window_height / 2):
        player_cursorY = int(window_height / 2)
    if player_cursorY >= window_height - 65:
        player_cursorY = window_height - 65
    if player_cursorX < 0:
        player_cursorX = 0
    if player_cursorX >= window_width - 65:
        player_cursorX = window_width - 65

    # if player_distance_from_ball < 40:
    #     # ball_acceleration
    #
    #     # contact
    #
    #     ballX_speed *= random_direction
    #     random_direction = random.choice([-1, 1])
    #     ballY_speed *= random_direction

    # collision improvements
    # solX = ballX - player_cursorX
    # solY = ballY - player_cursorY
    # if player_distance_from_ball < impact_distance:
    #     racket_noise.play()
    #     start_speedX = ballX_speed
    #     start_speedY = ballY_speed
    # if solX < -collision_upgrade and solY < 0:
    #     ballX_speed = -5
    #     ballY_speed = -5
    #     ballY -= push_upgrade
    #     ballX -= push_upgrade
    # if solX > collision_upgrade and solY < 0:
    #     ballX_speed = 5
    #     ballY_speed = -5
    #     ballY -= push_upgrade
    #     ballX += push_upgrade
    # if solX < -collision_upgrade and solY > 0:
    #     ballX_speed = -5
    #     ballY_speed = 5
    #     ballY += push_upgrade
    #     ballX -= push_upgrade
    # if solX > collision_upgrade and solY > 0:
    #     ballX_speed = 5
    #     ballY_speed = 5
    #     ballX += push_upgrade
    #     ballY += push_upgrade
    # if solX > -collision_upgrade and solX < collision_upgrade:
    #     if solY < 0:
    #         ballX_speed = 0
    #         ballY_speed = 5
    #         ballY += push_upgrade
    #     if solY > 0:
    #         ballX_speed = 0
    #         ballY_speed = -5
    #         ballY -= push_upgrade

    pygame.draw.rect(window, WHITE, (int(window_width / 3) + 20, -20, 300, 80), 1)
    pygame.draw.rect(window, WHITE, (int(window_width / 3) + 20, window_height - 60, 300, 80), 1)
    pygame.draw.aaline(window, WHITE, (0, window_height / 2), (window_width, window_height / 2))
    pygame.draw.circle(window, WHITE, [int(window_width / 2), int(window_height / 2)], 80, 1)
    rect_ball.center = (ballX + 15, ballY + 15)
    rect_ordi.center = (ordi_cursorX + 35, ordi_cursorY + 30)
    pygame.draw.rect(window, BLACK, rect_player, 1)
    pygame.draw.rect(window, BLACK, rect_ball, 1)
    pygame.draw.rect(window, BLACK, rect_ordi, 1)
    window.blit(ordi_cursor, (ordi_cursorX, ordi_cursorY))
    window.blit(ball, (ballX, ballY))
    window.blit(player_cursor, (player_cursorX - 35, player_cursorY - 30))
    window.blit(display_score_player1, (int(score_player1X), int(score_player1Y)))
    window.blit(display_score_ordi, (int(score_ordiX), int(score_ordiY)))
    window.blit(display_timer, (30, 30))
    # update
    clock.tick(60)
    pygame.display.update()
