# Solucionador do Problema das Oito Rainhas

Este repositório contém implementações em Python para resolver o problema das Oito Rainhas, cujo objetivo é posicionar oito rainhas em um tabuleiro de xadrez 8x8 de forma que nenhuma rainha ameace outra, ou seja, sem que compartilhem a mesma linha, coluna ou diagonal. As estratégias implementadas incluem um Algoritmo Genético e duas variantes do algoritmo Hill Climbing (padrão e estocástico). Abaixo, descrevemos cada arquivo, sua função, as classes utilizadas e como elas foram aplicadas em cada estratégia.

## Estrutura do Repositório

### 1. OitoRainhas.py
Este arquivo define a classe base `OitoRainhas`, que modela o problema das Oito Rainhas e fornece funcionalidades essenciais para as demais estratégias.

- **Classe `OitoRainhas`**:
  - **Propósito**: Representa o tabuleiro e gerencia o estado do problema.
  - **Atributos**:
    - `tabuleiro`: Lista de 8 inteiros representando as posições das rainhas (0 a 7) em cada linha.
    - `colisao`: Número de colisões (ataques entre rainhas) no tabuleiro atual.
    - `filhos`: Lista de tabuleiros vizinhos gerados a partir do estado atual.
  - **Métodos Principais**:
    - `reiniciaTabuleiro()`: Gera um novo tabuleiro aleatório com posições de rainhas entre 0 e 7.
    - `calculaColisoes(tabuleiro)`: Calcula o número de colisões (ataques na mesma coluna ou diagonal).
    - `filhosTabuleiro(lista)`: Gera vizinhos do tabuleiro atual, alterando a posição de uma rainha em ±1.
    - `setTabuleiro(tabuleiro)`: Atualiza o tabuleiro, recalcula colisões e gera novos vizinhos.
    - `getTabuleiro()`, `getColisoes()`, `getFilhos()`: Retornam o tabuleiro, número de colisões e vizinhos, respectivamente.
  - **Uso**: Serve como base para as classes `HillClibing` e `HillClibingEstocastico`, fornecendo a lógica central do problema.

### 2. AlgoritmosGenetico.py
Este arquivo implementa um Algoritmo Genético para resolver o problema, utilizando três classes principais.

- **Classe `Chromosome`**:
  - **Propósito**: Representa uma solução candidata (um tabuleiro) codificada como um cromossomo binário.
  - **Atributos**:
    - `genes`: Array NumPy de bits (0 ou 1) com tamanho 24 (8 rainhas × 3 bits por posição).
    - `NUM_LINES = 8`: Número de rainhas/linhas.
    - `BITS_PER_POSITION = 3`: Bits por rainha para codificar posições de 0 a 7.
  - **Métodos**:
    - `__init__(genes)`: Inicializa um cromossomo com genes aleatórios ou fornecidos.
    - `decode()`: Converte os genes binários em uma lista de posições (0 a 7) para as rainhas.
    - `fitness()`: Calcula o número de colisões (menor é melhor; 0 indica solução válida).
  - **Uso**: Cada cromossomo representa um tabuleiro, e sua função de fitness avalia a qualidade da solução.

- **Classe `Population`**:
  - **Propósito**: Gerencia uma população de cromossomos (indivíduos).
  - **Atributos**:
    - `size`: Tamanho da população.
    - `individuals`: Lista de objetos `Chromosome`.
  - **Métodos**:
    - `__init__(size)`: Cria uma população com cromossomos aleatórios.
    - `get_fitness_scores()`: Retorna a lista de valores de fitness dos indivíduos.
    - `select_parents()`: Seleciona pais com base em probabilidades inversamente proporcionais ao fitness (seleção por roleta).
    - `crossover(parents, crossover_rate)`: Realiza cruzamento de ponto único entre pares de pais com probabilidade `crossover_rate`.
    - `mutate(mutation_rate)`: Aplica mutação (inversão de bits) com probabilidade `mutation_rate`.
  - **Uso**: Gerencia a evolução da população, criando novas gerações por meio de seleção, cruzamento e mutação.

- **Classe `GeneticAlgorithm`**:
  - **Propósito**: Coordena a execução do algoritmo genético.
  - **Atributos**:
    - `population_size`, `max_generations`, `crossover_rate`, `mutation_rate`: Parâmetros configuráveis.
    - `population`: Instância da classe `Population`.
  - **Métodos**:
    - `__init__()`: Inicializa o algoritmo com parâmetros padrão (população de 20, 1000 gerações, taxas de cruzamento 0.8 e mutação 0.03).
    - `elitist_selection(offspring)`: Combina os melhores indivíduos da população atual e da prole (elitismo).
    - `run()`: Executa o algoritmo até encontrar uma solução (fitness = 0) ou atingir o número máximo de gerações.
  - **Uso**: Controla o fluxo do algoritmo genético, iterando gerações e retornando a melhor solução encontrada.

### 3. TesteGenetico.py
Este arquivo testa o Algoritmo Genético, executando-o 50 vezes e analisando os resultados.

- **Funcionalidade**:
  - Executa o `GeneticAlgorithm` 50 vezes, medindo o número de gerações, tempo de execução e soluções distintas.
  - Calcula a média e o desvio padrão do número de iterações e do tempo de execução.
  - Exibe as cinco melhores soluções distintas (baseadas no fitness).
- **Uso das Classes**:
  - `GeneticAlgorithm`: Instanciado para cada execução, utilizando `run()` para obter a melhor solução.
  - `Chromosome`: Usado para decodificar e exibir as soluções finais em formato de tabuleiro.
- **Saída**:
  - Média e desvio padrão das iterações e tempos.
  - Lista das cinco melhores soluções (posições das rainhas).

### 4. HillClibing.py
Este arquivo implementa o algoritmo Hill Climbing padrão, que busca melhorar iterativamente o tabuleiro.

- **Classe `HillClibing`**:
  - **Propósito**: Implementa o algoritmo Hill Climbing, herdando de `OitoRainhas`.
  - **Atributos**:
    - `interacoes`: Contador de iterações.
    - `tempo`: Tempo de execução (não usado diretamente neste arquivo).
  - **Métodos**:
    - `__init__()`: Inicializa a superclasse `OitoRainhas` e define `interacoes`.
    - `hillClibing()`: Avalia os vizinhos do tabuleiro atual e retorna o melhor estado (menor número de colisões).
    - `loopHillClibing()`: Itera até que não haja melhora ou o número de colisões seja zero, retornando o estado final, colisões e número de iterações.
  - **Uso**: Explora deterministicamente os vizinhos, escolhendo sempre o que reduz mais as colisões, até atingir um mínimo local ou uma solução válida.

### 5. HillClibingEstocastico.py
Este arquivo implementa uma variante estocástica do Hill Climbing, introduzindo aleatoriedade na escolha dos vizinhos.

- **Classe `HillClibingEstocastico`**:
  - **Propósito**: Implementa o Hill Climbing estocástico, herdando de `OitoRainhas`.
  - **Atributos**:
    - `interacoes`: Contador de iterações.
    - `tempo`: Tempo de execução (não usado diretamente neste arquivo).
  - **Métodos**:
    - `__init__()`: Inicializa a superclasse `OitoRainhas` e define `interacoes`.
    - `hillClibingEstocasticos()`: Avalia os vizinhos, seleciona aleatoriamente entre os estados com menor ou igual número de colisões.
    - `loopHillClibingEstocasticos()`: Itera até atingir um máximo de 500 iterações, um mínimo local ou uma solução válida (colisões = 0).
  - **Uso**: A aleatoriedade na escolha dos vizinhos ajuda a escapar de mínimos locais, aumentando a chance de encontrar uma solução global.

### 6. DadosEstocastico.py
Este arquivo avalia o desempenho do Hill Climbing estocástico em 50 execuções, usando um tabuleiro inicial fixo.

- **Funcionalidade**:
  - Executa o `loopHillClibingEstocasticos` 50 vezes a partir do tabuleiro inicial `[1, 3, 5, 7, 2, 0, 6, 4]`.
  - Coleta estatísticas sobre iterações, tempo de execução e colisões.
  - Exibe os cinco melhores resultados, incluindo tabuleiro inicial, final, colisões e iterações.
- **Uso das Classes**:
  - `HillClibingEstocastico`: Instanciado para executar o algoritmo e coletar resultados.
  - `OitoRainhas`: Fornece métodos para manipulação do tabuleiro e cálculo de colisões.
- **Saída**:
  - Confirmação se uma solução válida foi encontrada (colisões = 0).
  - Média e desvio padrão de iterações, tempos e colisões.
  - Detalhes dos cinco melhores resultados.

### 7. ComparacaoEntreOsHill.py
Este arquivo compara as duas variantes do Hill Climbing (padrão e estocástico) em um mesmo tabuleiro inicial.

- **Funcionalidade**:
  - Gera um tabuleiro inicial aleatório com `OitoRainhas`.
  - Executa `HillClibing` e `HillClibingEstocastico` no mesmo tabuleiro, exibindo os resultados (tabuleiro final, colisões e iterações).
- **Uso das Classes**:
  - `OitoRainhas`: Gera o tabuleiro inicial.
  - `HillClibing` e `HillClibingEstocastico`: Executam suas respectivas estratégias e retornam os resultados.
- **Saída**:
  - Tabuleiro inicial e resultados (tabuleiro final, colisões) para cada algoritmo.

## Como Executar

1. **Requisitos**:
   - Python 3.x.
   - Bibliotecas: `numpy` e `statistics` (instale com `pip install numpy`).
2. **Comandos**:
   - Para o Algoritmo Genético: `python TesteGenetico.py`.
   - Para o Hill Climbing estocástico: `python DadosEstocastico.py`.
   - Para comparar Hill Climbing padrão e estocástico: `python ComparacaoEntreOsHill.py`.
3. **Personalização**:
   - Ajuste parâmetros como `population_size`, `max_generations`, `crossover_rate`, e `mutation_rate` em `AlgoritmosGenetico.py`.
   - Modifique o número máximo de iterações (`max_iter`) em `HillClibingEstocastico.py`.
   - Altere o número de execuções (`teste`) em `TesteGenetico.py` ou `DadosEstocastico.py`.

## Observações

- **Algoritmo Genético**:
  - Usa codificação binária (3 bits por rainha) para representar posições.
  - A função de fitness é o número de colisões (objetivo: 0).
  - Elitismo preserva os melhores indivíduos entre gerações.
- **Hill Climbing Padrão**:
  - Explora deterministicamente os vizinhos, escolhendo o melhor.
  - Pode ficar preso em mínimos locais.
- **Hill Climbing Estocástico**:
  - Introduz aleatoriedade na escolha de vizinhos, aumentando a chance de escapar de mínimos locais.
  - Limita-se a 500 iterações para evitar loops infinitos.
- **Resultados**:
  - O Algoritmo Genético é mais robusto, mas pode ser mais lento devido à exploração de múltiplas soluções.
  - O Hill Climbing estocástico é mais rápido e pode encontrar soluções válidas com maior probabilidade que o padrão, mas depende da inicialização.
  - A comparação direta em `ComparacaoEntreOsHill.py` destaca diferenças na eficácia e velocidade entre as variantes do Hill Climbing.