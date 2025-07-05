from OitoRainhas import OitoRainhas
import time

class HillClibing(OitoRainhas):
    def __init__(self):
        self.interacoes = 0
        self.tempo = 0.0

    def hillClibing(self):
        menorColisao = self.calculaColisoes(self.filhos[0])
        melhorEstado = self.tabuleiro
        for estado in self.filhos:
            valorColisao = self.calculaColisoes(estado)
            if valorColisao < menorColisao:
                melhorEstado = estado
