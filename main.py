import pygame
import sys
import gamemode

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Pong Game")

pygame.init()

font = pygame.font.SysFont('Comic Sans MS', 36)
font_color = (192, 192, 192)
highlight_color = (255, 255, 0)  # Kolor podświetlenia
selected_option = 1  # Początkowo pierwsza opcja jest wybrana

def init_sounds():
    select_sound = pygame.mixer.Sound('sounds/selection.wav')
    choose_sound = pygame.mixer.Sound('sounds/after_choose.wav')
    return select_sound, choose_sound

def draw_text(text, x, y, highlighted=False):
    color = highlight_color if highlighted else font_color
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def main_menu():
    select_sound, choose_sound = init_sounds()
    global selected_option
    while True:
        screen.fill('black')
        draw_text("Pong Game", width // 2, height // 3)
        draw_text("1. Singleplayer game", width // 2, height // 2, selected_option == 1)
        draw_text("2. Multiplayer mode", width // 2, height // 2 + 50, selected_option == 2)
        draw_text("3. Exit", width // 2, height // 2 + 100, selected_option == 3)
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
                elif event.key == pygame.K_UP:
                    select_sound.play()
                    selected_option = max(1, selected_option - 1)
                elif event.key == pygame.K_DOWN:
                    select_sound.play()
                    selected_option = min(3, selected_option + 1)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 1:
                        choose_sound.play()
                        gamemode.singleplayer()
                    elif selected_option == 2:
                        choose_sound.play()
                        main_menu()
                    elif selected_option == 3:
                        choose_sound.play()
                        pygame.quit()
                        sys.exit()

main_menu()
