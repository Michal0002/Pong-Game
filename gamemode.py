import random
import pygame

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)

def singleplayer():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    ball_size = 20
    ball_speed = 5
    ball_direction = [random.choice([-1, 1]), random.choice([-1, 1])]
    ball_position = [WIDTH // 2, HEIGHT // 2]

    # Player palette
    player_size = (WIDTH // 10, 20)
    player_speed = 8
    player_position = [WIDTH // 2 - player_size[0] // 2, HEIGHT - 2 * player_size[1]]

    # Computer palette
    computer_size = (WIDTH // 10, 20)
    computer_speed = 8
    computer_position = [WIDTH // 2 - computer_size[0] // 2, 0]

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        ball_position[0] += ball_speed * ball_direction[0]
        ball_position[1] += ball_speed * ball_direction[1]

        if ball_position[0] <= 0 or ball_position[0] >= WIDTH - ball_size or \
           ball_position[1] <= 0 or ball_position[1] >= HEIGHT - ball_size:
            ball_direction[0] *= -1
            ball_direction[1] *= -1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_position[0] > 0:
            player_position[0] -= player_speed
        elif keys[pygame.K_RIGHT] and player_position[0] < WIDTH - player_size[0]:
            player_position[0] += player_speed
        
        if computer_position[0] + computer_size[0] // 2 < ball_position[0]:
            computer_position[0] += computer_speed
        elif computer_position[0] + computer_size[0] // 2 > ball_position[0]:
            computer_position[0] -= computer_speed

        screen.fill(BLACK)
        pygame.draw.ellipse(screen, WHITE, (ball_position[0], ball_position[1], ball_size, ball_size))
        pygame.draw.rect(screen, LIGHT_BLUE, (player_position[0], player_position[1], player_size[0], player_size[1]))
        pygame.draw.rect(screen, WHITE, (computer_position[0], computer_position[1], computer_size[0], computer_size[1]))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

singleplayer()
