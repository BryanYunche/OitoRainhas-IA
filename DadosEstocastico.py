import time

from HillClibingEstacastico import HillClibingEstocastico

solucoes = []
listaTempos = []
listaIteraçoes = []
listaColisoes = []

#Inicio o Tabuleiro
tabuleiroTemp = HillClibingEstocastico()

#Solução já conhecida do Hill Clibing
tabuleiroTemp.setTabuleiro([1, 3, 5, 7, 2, 0, 6, 4])

teste = int(input("Numero de teste para fazer: "))

# Coloca em Loop algoritmo
for _ in range(teste):
    #Inicio do algortimo em tempo
    timeInicial = time.time()
    tabuleiroAtual = tabuleiroTemp.getTabuleiro()
    colisaoAtual = tabuleiroTemp.getColisoes()
    resultadoAtual =tabuleiroTemp.loopHillClibingEstocasticos()

    #cria arrya com conjunto problema e solução
    solucoes.append([tabuleiroAtual, colisaoAtual, resultadoAtual])

    #Fim do algortimo em tempo
    timeFinal = time.time()

    #Tempo total
    tempoTotalAtual = timeFinal - timeInicial

    #Cria lista de tempos de execução
    listaTempos.append(tempoTotalAtual)

    #Cria lista com iteraçoes feitas
    listaIteraçoes.append(resultadoAtual[2])

    #Cria lista com as coliçoes totais
    listaColisoes.append(resultadoAtual[1])

    #Reincia tabuleiro para a proxima iteração
    tabuleiroTemp.reiniciaTabuleiro()


#------------------------------------------------------------------------
#Media de iteraçoes
print(listaIteraçoes)

#desvio padrão de iteraçoes

#------------------------------------------------------------------------
#Media de tempo
print(listaTempos)

#desvio padrão de tempo

#----------------------------------------------------------------------------
#Media de Colisoes
print(listaColisoes)