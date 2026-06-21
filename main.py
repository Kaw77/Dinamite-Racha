import pygame
from pygame import Surface, Rect

# Inicializar o Módulo do PyGame
print("Dinamite Racha - Amando velocidade...")
pygame.init()

# Criação de janela do pygame
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dinamite Racha")

# Carregar imagem e gerar um fundo
surface = pygame.image.load("assets/imagens/dinamite.png")

# Obter o retângulo do fundo
rect = surface.get_rect()

# Desenhar na janela (window)
window.blit(surface, rect)

# Atualizar a janela
pygame.display.update()

# Colocar um relógio no nosso jogo
clock = pygame.time.Clock()

# Carregar musica e deixar ela tocando
pygame.mixer.music.load("assets/sons/menu.mp3")
pygame.mixer.music.play(-1)

#Ajustar o fps do jogo
clock.tick(60)  