import pygame
from random import randint


class Fireball(pygame.sprite.Sprite):
    """Classe pour la boule de feu

    On crée une instance Fireball
    """

    def __init__(self, game):
        """Initialisation de la classe

        On charge le spriteSheet d'une boule de feu :
        fire_ball.png
        On lui donne une position x et y aléatoires
        dans la fenêtre en utlisant randint
        On définit une séquence de mouvement quand
        la boule de feu va tomber, une vitesse ainsi que ses dégats
        """
        super().__init__()
        self.game = game

        self.spriteSheet = pygame.image.load("data/img/sprites/fire_ball.png")
        self.spriteSheet = self.spriteSheet.convert_alpha()
        self.image = self.spriteSheet.subsurface(pygame.Rect(1, 1, 63, 63))
        self.rect = pygame.Rect(1, 1, 63, 63)
        self.rect.x = randint(0, 737)
        self.rect.y = 0 - randint(0, 100)

        self.sequences = [(0, 6, True)]
        self.sequence_number = 0
        self.image_number = 0
        self.flip = False

        self.delta_time = 0
        self.speed = 6

        self.attack = 1

    def animation_update(self, time):
        """On met à jour les animations

        On met à jour les animations de la boule de feu toutes les
        time secondes

        Parameters
        time : int
            temps entre chaque rafraichissement
        """
        self.delta_time += time

        if self.delta_time >= 200:
            self.delta_time = 0

            n = self.sequences[self.sequence_number][0] + self.image_number
            rectangle = ((n % 10 * 64) + 1, (n // 10 * 64) + 1, 63, 63)
            self.image = self.spriteSheet.subsurface(pygame.Rect(rectangle))

            if self.flip:
                self.image = pygame.transform.flip(self.image, True, False)

            self.image_number += 1

            if self.image_number == self.sequences[self.sequence_number][1]:
                if self.sequences[self.sequence_number][2]:
                    self.image_number = 0
                else:
                    self.image_number -= 1

    def set_sequence(self, n):
        """On met la séquence d'animation

        On met la séquence n d'animation de la boule de feu

        Parameters
        n : int
            numéro de la séquence
        """
        if self.sequence_number != n:
            self.image_number = 0
            self.sequence_number = n

    def fall(self):
        """La boule de feu tombe

        Si la boule de feu rentre en contact avec le joueur
        celle-ci se déplace instantanément a une position aléatoire
        dans la fenêtre, on utilise donc la fonction
        check_collision venant de la classe Game
        """
        if not self.game.check_collision(self, self.game.all_players):
            self.rect = self.rect.move(0, self.speed)
            self.set_sequence(0)
            if self.rect.y > 346:
                self.rect.y = 0 - randint(0, 100)
                self.rect.x = randint(0, 737)
        else:
            self.rect.x = randint(0, 737)
            self.rect.y = 0 - randint(0, 100)
            self.game.J1.damage(self.attack)
