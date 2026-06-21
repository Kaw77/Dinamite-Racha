# jogador.py

import pygame


class Jogador:

    def __init__(self,imagem, x, y):

        self.sprite = pygame.image.load(imagem)

        self.x = x
        self.y = y

        self.velocidade = 6

    def mover(self):

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_w]:
            self.y -= self.velocidade

        if teclas[pygame.K_s]:
            self.y += self.velocidade

        if teclas[pygame.K_a]:
            self.x -= self.velocidade

        if teclas[pygame.K_d]:
            self.x += self.velocidade

    def desenhar(self, tela):

        tela.blit(
            self.sprite,
            (self.x, self.y)
        )