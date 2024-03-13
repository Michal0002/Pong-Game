import random
import pygame
import sys

pygame.init()
width, height = 800, 600

#sounds
collision_sound = pygame.mixer.Sound('sounds/ball_sound.wav')
round_over_sound = pygame.mixer.Sound('sounds/round_over.wav')

def display_message(screen, message):
    font = pygame.font.SysFont("Comic Sans MS", 50)
    text = font.render(message, True, (255, 255, 255))
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)
    pygame.display.update()

def singleplayer():
    global player_position, computer_position, ball_position, ball_direction, start_time, player_won, player_score, computer_score, player_size, computer_size, computer_speed

    #player pallete
    player_size = (width // 10, 20)
    player_speed = 8
    player_position = [width // 2 - player_size[0] // 2, height - 2 * player_size[1]]

    #pc palette
    computer_size = (width // 10, 20)
    computer_position = [width // 2 - computer_size[0] // 2, 0]
    computer_speed = 5
    computer_reaction_time = 500 * 30

    screen = pygame.display.set_mode((width, height))

    ball_size = 20
    ball_speed = 5
    ball_direction = [random.choice([-1, 1]), random.choice([-1, 1])]
    ball_position = [width // 2, height // 2]

    #timer
    elapsed_time = 0
    player_won = False
    start_time = pygame.time.get_ticks()
    timer = pygame.time.Clock()
    game_over = False

    player_score = 0
    computer_score = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        #ball movement with collision with site edges
        ball_position[0] += ball_speed * ball_direction[0]
        ball_position[1] += ball_speed * ball_direction[1]

        if ball_position[0] <= 0 or ball_position[0] >= width - ball_size:
            ball_direction[0] *= -1
        elif ball_position[1] <= 0:
            player_score += 1
            if player_score >= 3:
                round_over_sound.play()
                display_message(screen, "You won the round!")
                pygame.time.delay(3000)
                return True
            else:
                display_message(screen, "You scored!")
                pygame.time.delay(1000)
                reset_position()
        elif ball_position[1] >= height - ball_size:
            computer_score += 1
            if computer_score >= 3:
                round_over_sound.play()
                display_message(screen, "Computer won the round!")
                pygame.time.delay(3000)
                return True
            else:
                display_message(screen, "Computer scored!")
                pygame.time.delay(1000)
                reset_position()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if player_position[0] > 0:
                player_position[0] -= player_speed
        elif keys[pygame.K_RIGHT]:
            if player_position[0] < width - player_size[0]:
                player_position[0] += player_speed

        #computer behavior
        elapsed_time = pygame.time.get_ticks() - start_time
        if not player_won and elapsed_time >= computer_reaction_time:
            computer_speed = 1
            player_won = True
            print("Po 15s: " + str(computer_speed))        
            
        if computer_position[0] + computer_size[0] // 2 < ball_position[0]:
            computer_position[0] += computer_speed
        elif computer_position[0] + computer_size[0] // 2 > ball_position[0]:
            computer_position[0] -= computer_speed

        #collision with palettes
        if (player_position[1] <= ball_position[1] + ball_size and player_position[1] + player_size[1] >= ball_position[1] and player_position[0] <= ball_position[0] <= player_position[0] + player_size[0]):
            ball_direction[1] *= -1
            collision_sound.play()

        elif (computer_position[1] <= ball_position[1] + ball_size and computer_position[1] + computer_size[1] >= ball_position[1] and computer_position[0] <= ball_position[0] <= computer_position[0] + computer_size[0]):
            ball_direction[1] *= -1
            collision_sound.play()

        screen.fill("black")
        elapsed_seconds = elapsed_time / 1000
        font = pygame.font.SysFont("Comic Sans MS", 12)
        timer_text = font.render("Time: {:.2f}s".format(elapsed_seconds), True, (99, 255, 11))
        
        score_text = font.render(f"You: {player_score} - Computer: {computer_score}", True, (255, 255, 255))
        score_text_rect = score_text.get_rect(midbottom=(width // 2, height))
        screen.blit(score_text, score_text_rect)
        screen.blit(timer_text, (width - timer_text.get_width(), height - timer_text.get_height()))
        pygame.draw.ellipse(screen, "white", (ball_position[0], ball_position[1], ball_size, ball_size))
        pygame.draw.rect(screen, "lightblue", (player_position[0], player_position[1], player_size[0], player_size[1]))
        pygame.draw.rect(screen, "white", (computer_position[0], computer_position[1], computer_size[0], computer_size[1]))

        pygame.display.update()
        timer.tick(60)

def reset_position():
    pygame.time.delay(3000)
    global player_position, computer_position, ball_position, ball_direction, start_time, player_won, computer_speed, computer_reaction_time,elapsed_time
    player_position = [width // 2 - player_size[0] // 2, height - 2 * player_size[1]]
    computer_position = [width // 2 - computer_size[0] // 2, 0]
    ball_position = [width // 2, height // 2]
    ball_direction = [random.choice([-1, 1]), random.choice([-1, 1])]
    start_time = pygame.time.get_ticks()
    player_won = False
    elapsed_time = pygame.time.get_ticks() - start_time
    computer_speed = 5
    computer_reaction_time = 500 * 30 
    print("W po resecie: " + str(computer_speed))