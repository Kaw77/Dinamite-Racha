def verificar_distancia(self, outro):

    distancia = outro.x - self.x

    if 0 < distancia < 60:
        return False

    return True