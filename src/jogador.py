import pygame


class Jogador:

    def __init__(self, personagem):

        imagens = {

            1: "assets/imagens/jogador1.png",
            2: "assets/imagens/jogador2.png"
        }

        self.imagem = pygame.image.load(
            imagens[personagem]
        )

        self.x = 350
        self.y = 500

        self.velocidade = 6

    def desenhar(self, tela):

        tela.blit(
            self.imagem,
            (self.x, self.y)
        )