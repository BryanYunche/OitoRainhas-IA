from OitoRainhas import OitoRainhas

tabuleiro = OitoRainhas()

estado01 = tabuleiro.geraTabuleiro()
colisao = tabuleiro.getColisoes()

print(estado01)
print(colisao)

estado01 = tabuleiro.mudaPosicao(0, 1)
colisao = tabuleiro.getColisoes()

print(estado01)
print(colisao)
