import pygame
from data.scripts.game import Game
from data.scripts.menu import Menu


def main():
    pygame.init()

    pygame.display.set_caption("Burn")
    screen = pygame.display.set_mode((800, 450))
    background = pygame.image.load("data/img/background/background.png")

    clock = pygame.time.Clock()

    frame_rate = 60
    frame_count = 0

    menu = Menu(screen)
    game = Game(screen)

    running = True

    while running:

        screen.blit(background, (0, 0))

        if game.is_playing:
            game.update()
            game.total_seconds = frame_count // frame_rate
            frame_count += 1
        else:
            menu.blit_menu()
            frame_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True

            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if menu.play_button_rect.collidepoint(event.pos):
                    pygame.time.wait(500)
                    game.start()

                elif menu.rules_button_rect.collidepoint(event.pos):
                    pass

                elif menu.quit_button_rect.collidepoint(event.pos):
                    running = False

        clock.tick(frame_rate)

        pygame.display.flip()

    pygame.quit()


main()
