import pygame
import os

class Jogador:

    def __init__(self, imagem, x, y):

        caminho = os.path.join(os.getcwd(), imagem)

        if os.path.exists(caminho):
            self.imagem = pygame.image.load(caminho).convert_alpha()
            self.imagem = pygame.transform.scale(
                self.imagem,
                (64, 64)
            )
        else:
            print("Imagem não encontrada:", caminho)
            self.imagem = pygame.Surface((64, 64))
            self.imagem.fill((255, 0, 0))

        self.x = x
        self.y = y
        self.velocidade = 5

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))

    def obter_rect(self):
        return self.imagem.get_rect(topleft=(self.x, self.y))