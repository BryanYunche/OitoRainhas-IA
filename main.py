from HillClibing import HillClibing
from HillClibingEstacastico import HillClibingEstocastico
#tabuleiro = HillClibing()
#tabuleiro.setTabuleiro([1, 2, 5, 2, 2, 7, 0, 4])

#print(tabuleiro.getTabuleiro())
#print(tabuleiro.getColisoes())

#print(tabuleiro.loopHillClibing())



tabuleiro = HillClibingEstocastico()
tabuleiro.reiniciaTabuleiro()

print(tabuleiro.getTabuleiro())
print(tabuleiro.getColisoes())

print(tabuleiro.loopHillClibingEstocasticos())

