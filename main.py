import pygame
from pygame import Surface, Rect

# Inicializar o Módulo do PyGame
print("Dinamite Racha - Amando velocidade...")
pygame.init()

# Criação de janela do pygame
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dinamite Racha")
print("Dinamite Racha - Dizendo: - Tchau...Tchau!")

print("Prontos ou não, lá vamos nós...")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

# Carregar imagem e gerar um fundo
surface = pygame.image.load("assets/imagens/dinamite.png")
#importar a imagem para a fase 1, fase 2, fase 3 e fase 4
surface_fase1 = pygame.image.load("assets/imagens/fase1.png")
surface_fase2 = pygame.image.load("assets/imagens/fase2.png")
surface_fase3 = pygame.image.load("assets/imagens/fase3.png")
surface_fase4 = pygame.image.load("assets/imagens/fase4.png")
importar a explosão para colisão
explosion_image = pygame.image.load("assets/imagens/explosao.png")

# Obter o retângulo do fundo
rect = surface.get_rect()

# Desenhar na janela (window)
window.blit(surface, rect, fase1=True, fase2=True, fase3=True, fase4=True)

# Atualizar a janela
pygame.display.update()

# Colocar um relógio no nosso jogo
clock = pygame.time.Clock()

# Carregar musica e deixar ela tocando
pygame.mixer.music.load("assets/sons/menu.mp3")
pygame.mixer.music.play(-1)
# Carregar o som da explosão
explosion_sound = pygame.mixer.Sound("assets/sons/colisao.wav")
#importar sons para a fase 1, fase 2, fase 3 e fase 4
fase1_sound = pygame.mixer.Sound("assets/sons/fase1.mp3")
fase2_sound = pygame.mixer.Sound("assets/sons/fase2.mp3")
fase3_sound = pygame.mixer.Sound("assets/sons/fase3.mp3")
fase4_sound = pygame.mixer.Sound("assets/sons/fase4.mp3")
#Tocar o som da fase 1
fase1_sound.play()
fase2_sound.play()
fase3_sound.play()
fase4_sound.play()


#Ajustar o fps do jogo
clock.tick(60)  