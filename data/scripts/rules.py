import pygame


class Rule:

    def __init__(self, screen):
        self.screen = screen

        self.first_rules = pygame.image.load('data/img/rules/first_rules.png')

        self.second_rules = pygame.image.load('data/img/rules/second_rules.png')
