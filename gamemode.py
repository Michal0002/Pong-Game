import random
import pygame
import sys
import time 

pygame.init()
width, height = 800, 600

def singleplayer():
    screen = pygame.display.set_mode((width, height))

    ball_size = 20
    ball_speed = 5
    ball_direction = [random.choice([-1,1]), random.choice([-1,1])]
    ball_position = [width // 2, height //2] 

    #player pallete
    player_size = (width// 10, 20)
    player_speed = 8
    player_position = [width // 2 - player_size[0] // 2, height - 2 * player_size[1]]

    #pc pallete
    computer_size = (width // 10, 20)
    computer_speed = 8
    computer_position = [width // 2 - computer_size[0] // 2, 0]

    timer = pygame.time.Clock()
    game_over = False
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        ball_position[0] += ball_speed * ball_direction[0]
        ball_position[1] += ball_speed * ball_direction[1]

        if ball_position[0] <= 0 or ball_position[0] >= width - ball_size:
            ball_direction[0] *= -1
        if ball_position[1] <= 0 or ball_position[1] >= height - ball_size:
            ball_direction[1] *= -1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_position[0] > 0:
            player_position[0] -= player_speed
        if keys[pygame.K_RIGHT] and player_position[0] < width - player_size[0]:
            player_position[0] += player_speed
        
        if computer_position[0] + computer_size[0] // 2 < ball_position[0]:
            computer_position[0] += computer_speed
        elif computer_position[0] + computer_size[0] // 2 > ball_position[0]:
            computer_position[0] -= computer_speed

        screen.fill("black")
        pygame.draw.ellipse(screen, "white", (ball_position[0], ball_position[1], ball_size, ball_size))
        pygame.draw.rect(screen, "lightblue", (player_position[0], player_position[1], player_size[0], player_size[1]))
        pygame.draw.rect(screen, "white", (computer_position[0], computer_position[1], computer_size[0], computer_size[1]))

        pygame.display.update()
        timer.tick(60)  

