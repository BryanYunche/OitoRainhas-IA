class OitoRainhas:

    def __initi__(self):
        self.tabuleiro = []
        self.estadosFilho = []
        self.colisao = 0

    def geraTabuleiro(self):
        estado = []
        for i in range(8):
            estado.append(0)
            self.tabuleiro = estado
        self.calculaColisoes()
        return self.tabuleiro

    def calculaColisoes(self):
        colisoes = 0
        for i in range(len(self.tabuleiro)):
            for j in range(i + 1, len(self.tabuleiro)):
                if self.tabuleiro[i] == self.tabuleiro[j]:
                    colisoes += 1
                elif abs(self.tabuleiro[i] - self.tabuleiro[j]) == abs(i - j):
                    colisoes += 1
        self.colisao = colisoes

    def getColisoes(self):
        return self.colisao

    def mudaPosicao(self, coluna, linha):
        if (linha and coluna) in range(8):
            self.tabuleiro[coluna] = linha
            self.calculaColisoes()
            return self.tabuleiro
        else:
            print("Digite um valor entre 0 e 7")

