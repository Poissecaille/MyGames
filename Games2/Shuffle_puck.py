import pygame, sys, random, math
import time

pygame.init()
clock = pygame.time.Clock()

window_width = 1000
window_height = 800
window = pygame.display.set_mode((window_width, window_height))
pygame.font.init()
pygame.mixer.init()

# score and texts
score_player1 = 0
score_ordi = 0
police = pygame.font.Font("D:/DEVOP/MyGames/Games2/polices/Sketch3D.otf", 25)
score_player1X = window_width * 3 / 4
score_ordiX = window_width / 4
score_player1Y = window_height / 4
score_ordiY = window_height / 4

music_game = pygame.mixer.Sound("D:/DEVOP/MyGames/Games2/sounds/ace_combat.wav")
racket_noise = pygame.mixer.Sound("D:/DEVOP/MyGames/Games2/sounds/shuffle_racket_noise.wav")
obstacle_noise = pygame.mixer.Sound("D:/DEVOP/MyGames/Games2/sounds/shuffle_obstacle_noise.wav")
goal = pygame.mixer.Sound("D:/DEVOP/MyGames/Games2/sounds/shuffle_puck_goal.wav")
# music_game.play(-1)

pygame.display.set_caption('Shuffle Puck')
icon = pygame.image.load('D:/DEVOP/MyGames/Games2/images/ball.png')
player_cursor = pygame.image.load('D:/DEVOP/MyGames/Games2/images/shuffle_racket.png').convert_alpha()
ordi_cursor = pygame.image.load('D:/DEVOP/MyGames/Games2/images/shuffle_racket2.png')
ball = pygame.image.load('D:/DEVOP/MyGames/Games2/images/shuffle_ball.png')
pygame.display.set_icon(icon)
background_color = (0, 0, 0)
white = (255, 255, 255)

# player_cursor_position=player_cursor.get_rect()
rect_player_cursor=player_cursor.get_rect()
player_cursorX = int(window_width / 2) - 30
player_cursorY = int(window_height / 4 * 3)
ordi_cursorX = int(window_width / 2) - 30
ordi_cursorY = 25
ordi_cursor_speed = 10
random_direction = random.choice([-1, 1])

ballX_start = int(window_width / 2) - 15
ballY_start = int(window_height / 2) - 15
ballX = ballX_start
ballY = ballY_start
# ball_position = ball.get_rect()
# ball_position.x = ballX_start
# ball_position.y = ballY_start
start_speedX = 4 * random_direction
start_speedY = 4 * random_direction
ballX_speed = 5
ballY_speed = 5

goalXlow = 353
goalXhigh = 652
goalYordi = 60
goalYplayer = window_height - 60

collision_upgrade = 15
push_upgrade = 50
impact_distance = 40
# mouse blocking
pygame.mouse.set_visible(True)

while True:
    # physics
    player_distance_from_ball = math.sqrt(
        math.pow(player_cursorX - ballX, 2) + (math.pow(player_cursorY - ballY, 2)))
    ordi_distance_from_ball = math.sqrt(
        math.pow(ordi_cursorX - ballX, 2) + (math.pow(ordi_cursorY - ballY, 2)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            player_cursorX = event.pos[0]
            player_cursorY = event.pos[1]
            print(player_cursorX)
            print(player_cursorY)
            if player_cursorY <= int(window_height / 2):
                player_cursorY = int(window_height / 2)
            if player_cursorY >= window_height - 65:
                player_cursorY = window_height - 65
            if player_cursorX <= 0:
                player_cursorX = 0
            if player_cursorX >= window_width - 65:
                player_cursorX = window_width - 65
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    # ball movements
    ballX += start_speedX
    ballY += start_speedY
    random_direction = random.choice([-1, 1])
    # print(ballX)
    # print(ballY)
    if ballX > goalXlow and ballX < goalXhigh:
        if ballY <= 10 or ballY >= window_height - 10:
            print('goal')
            goal.play()
            ballX = ballX_start
            ballY = ballY_start
    if ballX <= 0:
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

    if ordi_distance_from_ball < impact_distance:
        # bug stick ball
        ballY += push_upgrade
        # ball_acceleration
        start_speedX = ballX_speed
        start_speedY *= -1
        # contact
        racket_noise.play()
        ballX_speed *= random_direction
        random_direction = random.choice([-1, 1])
        ballY_speed *= -1

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

    # if player_distance_from_ball < 40:
    #     # ball_acceleration
    #
    #     # contact
    #
    #     ballX_speed *= random_direction
    #     random_direction = random.choice([-1, 1])
    #     ballY_speed *= random_direction

    # collision improvements
    solX = ballX - player_cursorX
    solY = ballY - player_cursorY
    if player_distance_from_ball < impact_distance:
        racket_noise.play()
        start_speedX = ballX_speed
        start_speedY = ballY_speed
        if solX < -collision_upgrade and solY < 0:
            ballX_speed = -5
            ballY_speed = -5
            ballY -= push_upgrade
            ballX -= push_upgrade
        if solX > collision_upgrade and solY < 0:
            ballX_speed = 5
            ballY_speed = -5
            ballY -= push_upgrade
            ballX += push_upgrade
        if solX < -collision_upgrade and solY > 0:
            ballX_speed = -5
            ballY_speed = 5
            ballY += push_upgrade
            ballX -= push_upgrade
        if solX > collision_upgrade and solY > 0:
            ballX_speed = 5
            ballY_speed = 5
            ballX += push_upgrade
            ballY += push_upgrade
        if solX > -collision_upgrade and solX < collision_upgrade:
            if solY < 0:
                ballX_speed = 0
                ballY_speed = 5
                ballY += push_upgrade
            if solY > 0:
                ballX_speed = 0
                ballY_speed = -5
                ballY -= push_upgrade

    window.fill(background_color)
    pygame.draw.rect(window, white, (int(window_width / 3) + 20, -20, 300, 80), 1)
    pygame.draw.rect(window, white, (int(window_width / 3) + 20, window_height - 60, 300, 80), 1)
    pygame.draw.aaline(window, white, (0, window_height / 2), (window_width, window_height / 2))
    pygame.draw.circle(window, white, [int(window_width / 2), int(window_height / 2)], 80, 1)
    window.blit(ball, (ballX, ballY))
    # window.blit(player_cursor, (player_cursorX - 40, player_cursorY))
    window.blit(rect_player_cursor, (rect_player_cursor.x - 40, rect_player_cursorY))
    window.blit(ordi_cursor, (ordi_cursorX, ordi_cursorY))
    clock.tick(60)
    pygame.display.update()
