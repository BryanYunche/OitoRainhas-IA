import time
from random import randint, choice
from OitoRainhas import OitoRainhas

class HillClibingEstocastico(OitoRainhas):
    def __init__(self):
        super().__init__()  # Inicia a super classe que eu estou herdando
        self.interacoes = 0
        self.tempo = 0.0

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
        max_restarts = 100
        for _ in range(max_restarts):
            self.reiniciaTabuleiro()
            inicio = time.time()
            estadoPai, colisao = self.hillClibingEstocasticos()
            estadoFilho = []

            colisaoPai = colisao
            colisaoFilho = 0
            iteracoes = 1
            max_iter = 1000

            while (colisaoPai >= colisaoFilho) and (estadoPai != estadoFilho) and (iteracoes < max_iter):
                self.setTabuleiro(estadoPai)
                estadoFilho, colisaoFilho = self.hillClibingEstocasticos()
                colisaoPai = colisaoFilho
                estadoPai = estadoFilho
                iteracoes += 1

            fim = time.time()
            tempoTotal = fim - inicio

            if colisaoPai == 0:
                return estadoPai, colisaoPai, iteracoes, tempoTotal

        return estadoPai, colisaoPai, iteracoes, tempoTotal
