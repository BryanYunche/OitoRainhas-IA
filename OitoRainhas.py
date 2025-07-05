class OitoRainhas:

    def __init__(self):
        self.tabuleiro = [0, 0, 0, 0, 0, 0, 0, 0]
        self.filhos = self.filhosTabuleiro(self.tabuleiro)
        self.colisao = self.calculaColisoes(self.tabuleiro)

    def calculaColisoes(self, tabuleiro):
        colisoes = 0
        for i in range(len(tabuleiro)):
            for j in range(i + 1, len(tabuleiro)):
                if tabuleiro[i] == tabuleiro[j]:
                    colisoes += 1
                elif abs(tabuleiro[i] - tabuleiro[j]) == abs(i - j):
                    colisoes += 1
        return colisoes

    def getColisoes(self):
        return self.colisao

    def getTabuleiro(self):
        return self.tabuleiro

    def getFilhos(self):
        return self.filhos

    #Vai calcular e preencher os valores da classe Oito Rainhas
    def setTabuleiro(self, tabuleiro):
        self.tabuleiro = tabuleiro
        self.colisao = self.calculaColisoes(self.tabuleiro)
        self.filhos = self.filhosTabuleiro(self.tabuleiro)

    #Aqui vai gerar os filhos do tabuleiro com variações de +1 e -1
    def filhosTabuleiro(self, lista):
        filhos = []

        for i in range(len(lista)):
            if lista[i] > 0:
                novo = lista.copy()
                novo[i] -= 1
                filhos.append(novo)
            if lista[i] < 7:
                novo = lista.copy()
                novo[i] += 1
                filhos.append(novo)

        return filhos





