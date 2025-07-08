import time
import statistics
from HillClibingEstacastico import HillClibingEstocastico

solucoes = []
listaTempos = []
listaIteraçoes = []
listaColisoes = []

#Inicio o Tabuleiro
tabuleiroTemp = HillClibingEstocastico()

#Solução já conhecida do Hill Clibing
tabuleiroTemp.setTabuleiro([1, 3, 5, 7, 2, 0, 6, 4])

teste = 50 # DEFINE QUANTAS VEZES EU VOU RODAR O PROGRAMA

# Coloca em Loop algoritmo
for _ in range(teste):
    #Inicio do algortimo em tempo
    timeInicial = time.time()
    tabuleiroAtual = tabuleiroTemp.getTabuleiro()
    colisaoAtual = tabuleiroTemp.getColisoes()
    resultadoAtual =tabuleiroTemp.loopHillClibingEstocasticos()

    #cria arrya com conjunto problema e solução
    solucoes.append([tabuleiroAtual, colisaoAtual, resultadoAtual])

    #Cria lista com iteraçoes feitas
    listaIteraçoes.append(resultadoAtual[2])

    #Cria lista com as coliçoes totais
    listaColisoes.append(resultadoAtual[1])

    #Reincia tabuleiro para a proxima iteração
    tabuleiroTemp.reiniciaTabuleiro()

    #Fim do algortimo em tempo
    timeFinal = time.time()

    #Tempo total
    tempoTotalAtual = timeFinal - timeInicial

    #Cria lista de tempos de execução
    listaTempos.append(tempoTotalAtual)

#Resgata os idices dos melhores valores das colisões
MAX_COLISAO = 28
indicesMelhoresResultadosColisao = []
for i in range(0, MAX_COLISAO):
    for indiceColisao, colisao in enumerate(listaColisoes):
        if i == colisao:
            indicesMelhoresResultadosColisao.append(indiceColisao)

#Monta uma lista ordenada dos melhores resultados
melhoresResultadosGerais = []
for indices in indicesMelhoresResultadosColisao:
    melhoresResultadosGerais.append(solucoes[indices])


#------------------------------------------------------------------------
print("Quantas vezes foi rodado o programa dado um estado inicial: ", teste)
print("Foi escontrado uma solução: ", 0 in listaColisoes)

#Mostra os X melhores resultados
melhoresResultados = 5

print("Os ", melhoresResultados, " melhores resultados:")
for solucao in range(melhoresResultados):
    print("======================================================================")
    print("Tabuleiro Inicial: ", melhoresResultadosGerais[solucao][0])
    print("Colições da lista inicial: ", melhoresResultadosGerais[solucao][1])
    print("Tabuleiro Encontrado: ", melhoresResultadosGerais[solucao][2][0])
    print("Colisões do Tabuleiro Encontrado: ", melhoresResultadosGerais[solucao][2][1])
    print("Iterações necessárias para encontrar o Tabuleiro:", melhoresResultadosGerais[solucao][2][2])






print()
#------------------------------------------------------------------------
#DADOS ITERAÇÕES
print("Média ITERAÇÕES: ", statistics.mean(listaIteraçoes))
print("Desvio Padrão ITERAÇÕES: ",statistics.stdev(listaIteraçoes))

print()
#------------------------------------------------------------------------
#DADOS TEMPO
print("Média TEMPO: ", statistics.mean(listaTempos))
print("Desvio Padrão TEMPO: ",statistics.stdev(listaTempos))

print()
#----------------------------------------------------------------------------
#DADOS COLISÕES
print("Média COLISÕES: ", statistics.mean(listaColisoes))
print("Desvio Padrão COLISÕES: ",statistics.stdev(listaColisoes))