from random import randint


class OitoRainhas:

    def __initi__(self):
        self.tabuleiro = []
        self.colisao = 0

    def geraTabuleiro(self):
        estado = []
        for i in range(8):
            estado.append(randint(0, 7))
        return estado
