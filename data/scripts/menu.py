import pygame


class Menu:
    """Classe pour le menu

    On crée une instance Menu
    """

    def __init__(self, screen):
        """Initialisation de la classe

        On charge les images utilisés dans le menu:
        title.png
        play.png
        rules.png
        quit.png
        Puis on les place dans la fenêtre

        Parameters
        screen
        """
        self.screen = screen

        self.title = pygame.image.load("data/img/menu/title.png")
        self.title_rect = self.title.get_rect()
        self.title_rect.x = (800 // 2) - (130 // 2)
        self.title_rect.y = (450 // 8)

        self.play_button = pygame.image.load("data/img/menu/play.png")
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = (800 // 2) - (91 // 2)
        self.play_button_rect.y = self.title_rect.y + 150

        self.rules_button = pygame.image.load("data/img/menu/rules.png")
        self.rules_button_rect = self.rules_button.get_rect()
        self.rules_button_rect.x = (800 // 2) - (129 // 2)
        self.rules_button_rect.y = self.play_button_rect.y + 50

        self.quit_button = pygame.image.load("data/img/menu/quit.png")
        self.quit_button_rect = self.quit_button.get_rect()
        self.quit_button_rect.x = (800 // 2) - (134 // 2)
        self.quit_button_rect.y = self.rules_button_rect.y + 50

        self.solo_button = pygame.image.load('data/img/menu/solo.png')
        self.solo_button_rect = self.solo_button.get_rect()
        self.solo_button_rect.x = 150
        self.solo_button_rect.y = 350

        self.one_vs_one_button = pygame.image.load('data/img/menu/1vs1.png')
        self.one_vs_one_button_rect = self.one_vs_one_button.get_rect()
        self.one_vs_one_button_rect.x = 550
        self.one_vs_one_button_rect.y = 350

    def blit_title_button(self):
        """ On blit le titre

        On blit sur l'écran self.title aux coordonées self.title_rect
        """
        self.screen.blit(self.title, self.title_rect)

    def blit_play_button(self):
        """On blit le bouton play

        On blit sur l'écran self.play_button
        aux coordonées self.play_button_rect
        """
        self.screen.blit(self.play_button, self.play_button_rect)

    def blit_rules_button(self):
        """On blit le bouton règles

        On blit sur l'écran self.rules_button
        aux coordonées self.rules_button_rect
        """
        self.screen.blit(self.rules_button, self.rules_button_rect)

    def blit_quit_button(self):
        """On blit le bouton quitter

        On blit sur l'écran self.quit_button
        aux coordonées self.quit_button_rect
        """
        self.screen.blit(self.quit_button, self.quit_button_rect)

    def blit_menu(self):
        """On execute toutes les fonctions blit du menu

        On blit le titre, le bouton play, le bouton règles et le bouton quitter
        """
        self.blit_title_button()
        self.blit_play_button()
        self.blit_rules_button()
        self.blit_quit_button()
