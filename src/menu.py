import pygame


class Menu:

    def __init__(self, tela):

        self.tela = tela

        self.fonte = pygame.font.Font(
            None,
            50
        )

        self.opcao = 0

        self.opcoes = [
            "Jogar",
            "Ranking",
            "Sair"
        ]

    def desenhar(self):

        self.tela.fill((0, 0, 0))

        titulo = self.fonte.render(
            "DINAMITE RACHA",
            True,
            (255,255,255)
        )

        self.tela.blit(
            titulo,
            (220,80)
        )

        y = 220

        for indice, texto in enumerate(self.opcoes):

            cor = (255,255,255)

            if indice == self.opcao:
                cor = (255,255,0)

            item = self.fonte.render(
                texto,
                True,
                cor
            )

            self.tela.blit(
                item,
                (300,y)
            )

            y += 70

    def selecionar(self, evento):

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_UP:
                self.opcao -= 1

            if evento.key == pygame.K_DOWN:
                self.opcao += 1

            self.opcao %= len(self.opcoes)

            if evento.key == pygame.K_RETURN:
                return self.opcao

        return None