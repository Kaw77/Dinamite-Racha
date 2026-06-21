def mover(self, lista_adversarios):

    pode_andar = True

    for outro in lista_adversarios:

        if outro != self:

            if not self.verificar_distancia(outro):
                pode_andar = False

    if pode_andar:
        self.x += self.velocidade
        
def trocar_pista(self):

    import random

    nova_pista = random.randint(0,3)

    self.y = PISTAS[nova_pista]      