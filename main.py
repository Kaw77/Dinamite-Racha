'''import pygame

# Inicialização
pygame.init()
pygame.mixer.init()

# Janela
LARGURA = 800
ALTURA = 600

window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Dinamite Racha")

# Relógio
clock = pygame.time.Clock()

# Fundo do menu
fundo_menu = pygame.image.load(
    "assets/imagens/dinamite.png"
)

# Fundos das fases
fase1 = pygame.image.load(
    "assets/imagens/fase1.png"
)

fase2 = pygame.image.load(
    "assets/imagens/fase2.png"
)

fase3 = pygame.image.load(
    "assets/imagens/fase3.png"
)

fase4 = pygame.image.load(
    "assets/imagens/fase4.png"
)

# Som de colisão
explosion_sound = pygame.mixer.Sound(
    "assets/sons/colisao.wav"
)

# Música do menu
pygame.mixer.music.load(
    "assets/sons/menu.mp3"
)

pygame.mixer.music.play(-1)

# Fundo atual
fundo_atual = fundo_menu

rodando = True

while rodando:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                fundo_atual = fase1

            elif event.key == pygame.K_2:
                fundo_atual = fase2

            elif event.key == pygame.K_3:
                fundo_atual = fase3

            elif event.key == pygame.K_4:
                fundo_atual = fase4

    # Desenha fundo
    window.blit(fundo_atual, (0, 0))

    pygame.display.update()

    clock.tick(60)

pygame.quit()'''
#teste
import pygame

pygame.init()

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dinamite Racha")

rodando = True

while rodando:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((0, 0, 0))

    pygame.display.flip()

pygame.quit()