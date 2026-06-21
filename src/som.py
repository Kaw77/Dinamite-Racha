import pygame


class Som:

    def __init__(self):

        pygame.mixer.init()

        self.menu = "assets/sons/menu.mp3"

        self.fases = {

            1: "assets/sons/fase1.mp3",
            2: "assets/sons/fase2.mp3",
            3: "assets/sons/fase3.mp3",
            4: "assets/sons/fase4.mp3"
        }

        self.colisao = pygame.mixer.Sound(
            "assets/sons/colisao.wav"
        )

    def tocar_menu(self):

        pygame.mixer.music.load(
            self.menu
        )

        pygame.mixer.music.play(-1)

    def tocar_fase(self, fase):

        pygame.mixer.music.load(
            self.fases[fase]
        )

        pygame.mixer.music.play(-1)

    def tocar_colisao(self):

        self.colisao.play()