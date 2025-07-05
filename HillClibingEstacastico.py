import time
from random import randint, choice
from OitoRainhas import OitoRainhas

class HillClibingEstocastico(OitoRainhas):
    def __init__(self):
        super().__init__()  # Inicia a super classe que eu estou herdando
        self.interacoes = 0
        self.tempo = 0.0
        self.interacoes = 0

    def hillClibingEstocasticos(self):
        menorColisao = self.colisao
        melhorEstado = self.tabuleiro
        melhoresEstados = []
        for estado in self.filhos:
            valorColisao = self.calculaColisoes(estado)
            if valorColisao < menorColisao:
                melhorEstado = estado
                menorColisao = valorColisao
                #melhoresEstados.append([melhorEstado, menorColisao])
                melhoresEstados = [[melhorEstado, menorColisao]]
            elif valorColisao == menorColisao:
                melhoresEstados.append([melhorEstado, menorColisao])

        if melhoresEstados:
            melhorEstado, menorColisao = choice(melhoresEstados)
            return melhorEstado, menorColisao
        else:
            return self.tabuleiro, self.colisao

    def loopHillClibingEstocasticos(self):
        self.interacoes = 0
        max_iter = 500

        estadoPai, colisaoPai = self.hillClibingEstocasticos()
        self.interacoes += 1

        while self.interacoes < max_iter:
            self.setTabuleiro(estadoPai)
            estadoFilho, colisaoFilho = self.hillClibingEstocasticos()
            self.interacoes += 1

            if colisaoFilho >= colisaoPai or estadoFilho == estadoPai or colisaoFilho == 0:
                break

            estadoPai = estadoFilho
            colisaoPai = colisaoFilho

        return estadoFilho, colisaoFilho, self.interacoes
