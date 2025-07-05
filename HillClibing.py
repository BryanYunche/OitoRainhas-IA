import time

from OitoRainhas import OitoRainhas
from teste import inicio


class HillClibing(OitoRainhas):
    def __init__(self):
        super().__init__()  # Inicia a super classe que eu estou herdando
        self.interacoes = 0
        self.tempo = 0.0

    def hillClibing(self):
        menorColisao = self.colisao
        melhorEstado = self.tabuleiro
        for estado in self.filhos:
            valorColisao = self.calculaColisoes(estado)
            if valorColisao <= menorColisao:
                melhorEstado = estado
                menorColisao = valorColisao

        return melhorEstado, menorColisao

    def loopHillClibing(self):
        inicio = time.time()
        estadoPai, colisao = self.hillClibing()

        colisaoPai = colisao
        colisaoFilho = 0

        #Iteraçao já começa com 1 pois já foi utilizado o hill clibing
        iteracoes = 1

        while colisaoPai > colisaoFilho:

            self.setTabuleiro(estadoPai)
            estadoFilho, colisaoFilho = self.hillClibing()

            colisaoPai = colisaoFilho
            estadoPai = estadoFilho
            iteracoes = iteracoes + 1

        fim = time.time()
        tempoTotal = fim - inicio
        return estadoPai, colisaoPai, iteracoes, tempoTotal




