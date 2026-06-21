import pygame
import os

class Jogador:

    LARGURA_NAVE = 56
    ALTURA_NAVE = 56

    def __init__(self, imagem, x, y):

        caminho = os.path.join(os.getcwd(), imagem)

        if os.path.exists(caminho):
            self.imagem = pygame.image.load(caminho).convert_alpha()

            self.imagem = pygame.transform.scale(
                self.imagem,
                (self.LARGURA_NAVE, self.ALTURA_NAVE)
            )
        else:
            self.imagem = pygame.Surface(
                (self.LARGURA_NAVE, self.ALTURA_NAVE)
            )
            self.imagem.fill((255, 0, 0))

        self.x = x
        self.y = y

        self.velocidade = 5

    def centralizar_na_pista(self, topo_pista, altura_pista):

        self.y = topo_pista + (
            altura_pista - self.ALTURA_NAVE
        ) // 2

    def desenhar(self, tela):

        tela.blit(
            self.imagem,
            (self.x, self.y)
        )

    def obter_rect(self):

        return self.imagem.get_rect(
            topleft=(self.x, self.y)
        )
        
    def mover(self, teclas):

        if teclas[pygame.K_LEFT]:
           self.x -= self.velocidade

        if teclas[pygame.K_RIGHT]:
           self.x += self.velocidade

        if teclas[pygame.K_UP]:
           self.y -= self.velocidade

        if teclas[pygame.K_DOWN]:
           self.y += self.velocidade

    # Limites da tela

        if self.x < 0:
           self.x = 0

        if self.x > 800 - self.imagem.get_width():
           self.x = 800 - self.imagem.get_width()

        if self.y < 0:
           self.y = 0

        if self.y > 600 - self.imagem.get_height():
           self.y = 600 - self.imagem.get_height()