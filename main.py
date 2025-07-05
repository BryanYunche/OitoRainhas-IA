from OitoRainhas import OitoRainhas

tabuleiro = OitoRainhas()

print(tabuleiro.getTabuleiro())
print(tabuleiro.getColisoes())

tabuleiro.setTabuleiro([0, 7, 4, 5, 1, 3, 2, 6])
print(tabuleiro.getTabuleiro())
print(tabuleiro.getColisoes())
print(tabuleiro.getFilhos())
