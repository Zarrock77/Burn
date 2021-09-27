import pygame


class J1(pygame.sprite.Sprite):
    """Classe pour le Joueur 1

    On crée une instance J1
    """

    def __init__(self, game):
        """Initialisation de la classe

        On charge les images utilisés pour la vie du Joueur 1:
        lifeJ1_1.png
        lifeJ1_2.png
        lifeJ1_3.png
        On charge le spriteSheet du Joueur 1:
        J1.png
        On crée des sequences des mouvements du joueur 1
        que l'on flip ou non en fonction de sa position

        Parameters
        game
        """
        super().__init__()
        self.game = game
        self.max_health = 3
        self.health = self.max_health

        self.three_hearts = pygame.image.load("data/img/life/lifeJ1_1.png")
        self.two_hearts = pygame.image.load("data/img/life/lifeJ1_2.png")
        self.one_heart = pygame.image.load("data/img/life/lifeJ1_3.png")

        self.spriteSheet = pygame.image.load("data/img/sprites/J1.png")
        self.spriteSheet = self.spriteSheet.convert_alpha()
        self.image = self.spriteSheet.subsurface(pygame.Rect(1, 1, 63, 63))
        self.rect = pygame.Rect(1, 1, 63, 63)
        self.rect.x = 368
        self.rect.y = 344

        self.sequences = [(0, 2, True), (2, 6, True)]
        self.sequence_number = 0
        self.image_number = 0
        self.flip = False

        self.delta_time = 0
        self.speed = 4

    def animation_update(self, time):
        """On met à jour les animations

        On met à jour les animations du joueur 1 tout les
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

        On met la séquence n d'animation du joueur 1

        Parameters
        n : int
            numéro de la séquence
        """
        if self.sequence_number != n:
            self.image_number = 0
            self.sequence_number = n

    def move_right(self):
        """On bouge le joueur 1 vers la droite

        On bouge le rectangle du joueur 1 self.rect avec self.rect.move
        de self.speed vers la droite
        en ne tournant pas l'image et en mettant la séquence 1
        """
        self.rect = self.rect.move(self.speed, 0)
        self.flip = False
        self.set_sequence(1)

    def move_left(self):
        """On bouge le joueur 1 vers la gauche

        On bouge le rectangle du joueur 1 self.rect avec self.rect.move
        de -self.speed vers la gauche
        en tournant l'image et en mettant la séquence 1
        """
        self.rect = self.rect.move(-self.speed, 0)
        self.flip = True
        self.set_sequence(1)

    def damage(self, amount):
        """Le joueur 1 prend des dégats

        Le joueur va prendre amount dégats

        Parameters
        amount : int
            nombre de coeurs en moins
        """
        self.health -= amount
        if self.health <= 0:
            self.game.game_over()

    def life_update(self, screen):
        """La vie du joueur reste en continue affiché

        On update en continue les images représentant la vie du J1 pour
        afficher 1, 2 ou 3 coeurs

        Parameters
        screen : surface
            surface sur laquelle on affiche la vie du J1
        """
        if self.health == 3:
            screen.blit(self.three_hearts, (0, 408))

        elif self.health == 2:
            screen.blit(self.two_hearts, (0, 408))

        elif self.health == 1:
            screen.blit(self.one_heart, (0, 408))
