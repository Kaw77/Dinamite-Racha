# adversario.py

import pygame
import random


class Adversario:

    def __init__(
        self,
        imagem,
        pista,
        velocidade
    ):

        self.sprite = pygame.image.load(
            imagem
        )

        self.x = random.randint(
            50,
            750
        )

        self.y = pista

        self.velocidade = velocidade

    def mover(self):

        self.x += self.velocidade

        if self.x > 800:

            self.x = -50

    def desenhar(self, tela):

        tela.blit(
            self.sprite,
            (self.x,self.y))