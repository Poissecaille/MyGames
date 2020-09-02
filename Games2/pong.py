import pygame, sys, random
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
score_player2 = 0
police = pygame.font.Font("D:/DEVOP/MyGames/Games2/polices/Sketch3D.otf", 25)
score_player1X = window_width * 3 / 4
score_player2X = window_width / 4
score_player1Y = window_height / 4
score_player2Y = window_height / 4
# sounds
music_game = pygame.mixer.Sound("D:/DEVOP/MyGames/Games2/sounds/a-secret-course-super-mario-sunshine.wav")
collision_sound = pygame.mixer.Sound("D:/DEVOP/MyGames/Games2/sounds/pong_noise.wav")
pong_point = pygame.mixer.Sound('D:/DEVOP/MyGames/Games2/sounds/pong_point.wav')
music_game.play(-1)

pygame.display.set_caption('Pong')
icon = pygame.image.load('D:/DEVOP/MyGames/Games2/images/pong.png')

random_direction = random.choice([-1, 1])
start_speedX = 4
start_speedY = 4

difficultyX = 7
difficultyY = 7

difficulty_cursor_lenght = 100
ball_speed_x = start_speedX * random_direction
ball_speed_y = start_speedY * random_direction

ball = pygame.Rect(int(window_width / 2 - 15), int(window_height / 2 - 15), 30, 30)
player1 = pygame.Rect(int(window_width - 20), int(window_height / 2 - 70), 10, difficulty_cursor_lenght)
player2 = pygame.Rect(10, int(window_height / 2 - 70), 10, difficulty_cursor_lenght)
background_color = (0, 0, 0)
white = (255, 255, 255)
player_speed = 0
player_speed_p2 = 0
difficulty_cursor_speed = 10
player1_name = 'Alex'
player2_name = 'Alice'

number_of_collisions = 0

while True:
    display_score_player1 = police.render(str(player1_name) + ':' + str(score_player1), True,
                                          pygame.Color(255, 255, 255))
    display_score_player2 = police.render(str(player2_name) + ':' + str(score_player2), True,
                                          pygame.Color(255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= difficulty_cursor_speed
            if event.key == pygame.K_w:
                player_speed_p2 -= difficulty_cursor_speed
            if event.key == pygame.K_DOWN:
                player_speed += difficulty_cursor_speed
            if event.key == pygame.K_s:
                player_speed_p2 += difficulty_cursor_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_speed_p2 += difficulty_cursor_speed
            if event.key == pygame.K_UP:
                player_speed += difficulty_cursor_speed
            if event.key == pygame.K_DOWN:
                player_speed -= difficulty_cursor_speed
            if event.key == pygame.K_s:
                player_speed_p2 -= difficulty_cursor_speed

    # player_movements
    player1.y += player_speed
    player2.y += player_speed_p2
    if player1.top <= 0:
        player1.top = 0
    if player2.top <= 0:
        player2.top = 0
    if player1.bottom >= window_height:
        player1.bottom = window_height
    if player2.bottom >= window_height:
        player2.bottom = window_height
    # ball movements
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    random_direction = random.choice([-1, 1])

    if ball.top <= 0 or ball.bottom >= window_height:
        ball_speed_y *= -1
    if ball.x < 0:
        score_player1 += 1
        pong_point.play()
        number_of_collisions = 0
        time.sleep(1)
        ball.center = (int(window_width / 2), int(window_height / 2))
        ball_speed_x = start_speedX * random_direction
        ball_speed_y = start_speedY * random_direction
    if ball.x >= window_width:
        score_player2 += 1
        pong_point.play()
        number_of_collisions = 0
        time.sleep(1)
        ball.center = (int(window_width / 2), int(window_height / 2))
        ball_speed_x = start_speedX * random_direction
        ball_speed_y = start_speedY * random_direction
    if ball.colliderect(player1) and ball_speed_x > 0:
        if (ball.right - player1.left) < 20:
            ball_speed_x = difficultyX * random_direction
            ball_speed_y = difficultyY * random_direction
            ball_speed_x *= -1
            collision_sound.play()
            number_of_collisions += 1
            print(number_of_collisions)
            print('ping')
        if (ball.bottom - player1.top) < 20:
            ball_speed_x = difficultyX * random_direction
            ball_speed_y = difficultyY * random_direction
            ball_speed_x *= -1
            ball_speed_y *= -1
            collision_sound.play()
            number_of_collisions += 1
            print(number_of_collisions)
            print('ping')
        if (ball.top - player1.bottom) < 20:
            ball_speed_x = difficultyX * random_direction
            ball_speed_y = difficultyY * random_direction
            ball_speed_x *= -1
            ball_speed_y *= -1
            collision_sound.play()
            number_of_collisions += 1
            print(number_of_collisions)
            print('ping')
    if ball.colliderect(player2) and ball_speed_x < 0:
        if ball.left - player2.right < 20:
            ball_speed_x = difficultyX * random_direction
            ball_speed_y = difficultyY * random_direction
            ball_speed_x *= -1
            collision_sound.play()
            number_of_collisions += 1
            print(number_of_collisions)
            print('pong')
        if (ball.bottom - player2.top) < 20:
            ball_speed_x = difficultyX * random_direction
            ball_speed_y = difficultyY * random_direction
            ball_speed_x *= -1
            ball_speed_y *= -1
            collision_sound.play()
            number_of_collisions += 1
            print(number_of_collisions)
            print('ping')
        if (ball.top - player2.bottom) < 20:
            ball_speed_x = difficultyX * random_direction
            ball_speed_y = difficultyY * random_direction
            ball_speed_x *= -1
            ball_speed_y *= -1
            collision_sound.play()
            number_of_collisions += 1
            print(number_of_collisions)
            print('ping')
    # if number_of_collisions >= 10:
    #     difficultyX += 1
    #     difficultyY += 1
    # if number_of_collisions >= 20:
    #     difficultyX += 1
    #     difficultyY += 1
    window.fill(background_color)
    pygame.draw.rect(window, white, player1)
    pygame.draw.rect(window, white, player2)
    pygame.draw.ellipse(window, white, ball)
    pygame.draw.aaline(window, white, (window_width / 2, window_height), (window_width / 2, 0))
    window.blit(display_score_player1, (int(score_player1X), int(score_player1Y)))
    window.blit(display_score_player2, (int(score_player2X), int(score_player2Y)))

    # update
    clock.tick(60)
    pygame.display.update()
