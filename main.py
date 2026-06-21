import pygame
from src.jogador import Jogador

pygame.init()

LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Dinamite Racha")

fundo = pygame.image.load(
    "assets/imagens/dinamite.png"
)

fundo = pygame.transform.scale(
    fundo,
    (LARGURA, ALTURA)
)

# Jogador começa na pista 1
jogador = Jogador(
    "assets/imagens/jogadores/jogador1.png",
    80,
    350
)

clock = pygame.time.Clock()

rodando = True

while rodando:

    clock.tick(60)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()

    jogador.mover(teclas)

    tela.blit(fundo, (0, 0))

    jogador.desenhar(tela)

    pygame.display.flip()

pygame.quit()