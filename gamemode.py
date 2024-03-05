import random
import pygame
import sys

pygame.init()
width, height = 800, 600

def singleplayer():
    screen = pygame.display.set_mode((width, height))

    ball_size = 20
    ball_speed = 5
    ball_direction = [random.choice([-1,1]), random.choice([-1,1])]
    ball_position = [width // 2, height //2] 
    
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

        screen.fill("black")
        pygame.draw.ellipse(screen, "white", (ball_position[0], ball_position[1], ball_size, ball_size))

        pygame.display.update()
        timer.tick(60)  

