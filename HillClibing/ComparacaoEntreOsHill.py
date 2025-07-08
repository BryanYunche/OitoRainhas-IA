from HillClibing import HillClibing
from HillClibingEstacastico import HillClibingEstocastico
from OitoRainhas import OitoRainhas

tabuleiroPivo = OitoRainhas()

tabuleiroPivo.reiniciaTabuleiro()
print(tabuleiroPivo.tabuleiro)

tabuleiro01 = HillClibingEstocastico()
tabuleiro02 = HillClibing()

tabuleiro01.setTabuleiro(tabuleiroPivo.tabuleiro)
tabuleiro02.setTabuleiro(tabuleiroPivo.tabuleiro)

print("Hill Clibing Estocático: ")
print(tabuleiro01.getTabuleiro(), tabuleiro01.getColisoes())
print()

print(tabuleiro01.loopHillClibingEstocasticos())

print("\nHill Clibing Normal: ")
print(tabuleiro02.getTabuleiro(), tabuleiro02.getColisoes())
print()

print(tabuleiro02.loopHillClibing())


