import pygame


class Fundo:

    def __init__(self):

        self.fundos = {

            1: "assets/imagens/fase1.png",
            2: "assets/imagens/fase2.png",
            3: "assets/imagens/fase3.png",
            4: "assets/imagens/fase4.png"
        }

    def carregar(self, fase):

        return pygame.image.load(
            self.fundos[fase]
        )