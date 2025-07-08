import time
from OitoRainhas import OitoRainhas

class HillClibing(OitoRainhas):
    def __init__(self):
        super().__init__()  # Inicia a super classe que eu estou herdando
        self.interacoes = 0
        self.tempo = 0.0

    def hillClibing(self):
        self.interacoes += 1
        menorColisao = self.colisao
        melhorEstado = self.tabuleiro
        for estado in self.filhos:
            valorColisao = self.calculaColisoes(estado)
            if valorColisao < menorColisao:
                melhorEstado = estado
                menorColisao = valorColisao

        return melhorEstado, menorColisao

    def loopHillClibing(self):

        self.interacoes = 1  # conta a primeira chamada
        estadoPai = self.tabuleiro
        colisaoPai = self.colisao

        while True:
            estadoFilho, colisaoFilho = self.hillClibing()
            self.interacoes += 1

            # Se não houver melhora ou o estado não mudar, para
            if colisaoFilho >= colisaoPai or estadoFilho == estadoPai:
                break

            self.setTabuleiro(estadoFilho)
            estadoPai = estadoFilho
            colisaoPai = colisaoFilho

        return estadoFilho, colisaoFilho, self.interacoes




