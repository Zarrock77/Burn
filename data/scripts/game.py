import pygame
from data.scripts.player import J1
from data.scripts.fireball import Fireball
from data.scripts.menu import Menu


class Game:
    """Classe pour le jeu

    On crée une instance Game
    """

    def __init__(self, screen):
        """Initialisation de la class

        On crée des sprites group pour les joueurs et les boules de feu
        ainsi qu'un dictionnaire self.pressed servant
        à la de gestion des touches

        Parameters
        screen
        """
        self.screen = screen

        self.menu = Menu(self.screen)

        self.is_playing = False

        self.all_players = pygame.sprite.Group()
        self.J1 = J1(self)
        self.all_players.add(self.J1)

        self.all_fire_ball = pygame.sprite.Group()

        self.total_seconds = 0
        self.score = 0
        self.font = pygame.font.Font("data/font/ARCADE.TTF", 25)

        self.pressed = {}

    def start(self):
        """On lance le jeu

        On lance le jeu en définissant la booléen self.is_playing sur True
        et l'on fait un appel à la fonction self.spawn_fire_ball() dix fois
        """
        self.is_playing = True
        for fire in range(10):
            self.spawn_fire_ball()

    def game_over(self):
        """Le joueur est mort le jeu se termine

        On réinitialise le groupe de sprite des boules de feu
        ainsi que les points de vie du joueur et sa position sur l'écran
        La booléen self.is_playing est alors False
        """
        self.all_fire_ball = pygame.sprite.Group()
        self.J1.health = self.J1.max_health
        self.is_playing = False
        self.J1.rect.x = 368

    def spawn_fire_ball(self):
        """On crée des boules de feu

        On fait appel à la class Fireball
        et l'on ajoute cette boule de feu
        au groupe de sprites self.all_fire_ball
        """
        fire_ball = Fireball(self)
        self.all_fire_ball.add(fire_ball)

    def update(self):
        """On met à jour toutes les animations du jeu

        On met à jour en continue le score du joueur 1
        On blit le joueur 1, self.J1.image, sur l'écran
        aux coordonnées self.J1.rect
        On update ensuite toutes les boules de feu
        Puis en fonction de la touche sur laquelle le joueur
        appuie le self.J1.image bouge à droite, à gauche ou reste sur place
        On update bien en continue toutes les animations
        """
        minutes = self.total_seconds // 60
        seconds = self.total_seconds % 60

        output_string = "{0:02}:{1:02}".format(minutes, seconds)
        self.score = self.font.render(output_string, True, (0, 0, 0))
        self.screen.blit(self.score, (350, 0))

        self.screen.blit(self.J1.image, self.J1.rect)

        for fire_ball in self.all_fire_ball:
            fire_ball.fall()
            fire_ball.animation_update(15)

        var = self.J1.rect.x + self.J1.rect.width < self.screen.get_width()
        if self.pressed.get(pygame.K_RIGHT) and var:
            self.J1.move_right()

        elif self.pressed.get(pygame.K_LEFT) and self.J1.rect.x > 0:
            self.J1.move_left()

        else:
            self.J1.set_sequence(0)

        self.all_fire_ball.draw(self.screen)
        self.J1.animation_update(15)
        self.J1.life_update(self.screen)

    @staticmethod
    def check_collision(sprite, group):
        """On vérifie s'il y a une collision

        On utilise pygame.sprite.spritecollide
        pour return la bouléen True ou False
        Parameters
        sprite
        group
        """
        pygame_scm = pygame.sprite.collide_mask
        return pygame.sprite.spritecollide(sprite, group, False, pygame_scm)
