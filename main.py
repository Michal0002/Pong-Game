import pygame
import sys
import gamemode

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

pygame.init()

font = pygame.font.SysFont('Arial', 36)
font_color = (192, 192, 192)

def draw_text(text, x, y):
    text_surface = font.render(text, True, font_color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def main_menu():
    while True:
        screen.fill('black')
        draw_text("Pong Game", width //2 , height // 3)
        draw_text("1. Singleplayer game", width // 2, height // 2)
        draw_text("2. Multiplayer mode", width // 2, height // 2 + 50)
        draw_text("3. Exit", width // 2, height // 2 + 100)
        pygame.display.flip()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    gamemode.singleplayer()
                elif event.key == pygame.K_2:
                    main_menu()
                elif event.key == pygame.K_3 or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

main_menu()