from AlgoritmoGenetico.AlgoritmosGenetico import GeneticAlgorithm, Chromosome
import time
import numpy as np

num_executions = 50
iterations = []
times = []
solutions = set()

for _ in range(num_executions):
    start_time = time.time()
    ga = GeneticAlgorithm()
    generation, best_individual = ga.run()
    end_time = time.time()
    iterations.append(generation)
    times.append(end_time - start_time)
    solutions.add(tuple(best_individual.genes))

mean_iterations = np.mean(iterations)
std_iterations = np.std(iterations)
mean_time = np.mean(times)
std_time = np.std(times)

print("""b) Execute o algoritmo 50 vezes e calcule:
- média e desvio padrão do número mínimo de iterações necessário para parar o algoritmo;
- média e desvio padrão do tempo de execução do algoritmo.""")
print()
print(f"media do numero de iteracoes: {mean_iterations:.2f}")
print(f"desvio padrao do numero de iteracoes: {std_iterations:.2f}")
print(f"media do tempo de execucao: {mean_time:.2f} segundos")
print(f"desvio padrao do tempo de execucao: {std_time:.2f} segundos")
print()
print("c) Cinco melhores soluções distintas encontradas pelo algoritmo:")

solutions_list = [Chromosome(np.array(sol)) for sol in solutions]
solutions_sorted = sorted(solutions_list, key=lambda x: x.fitness())
for i, sol in enumerate(solutions_sorted[:5]):
    print(f"solucao {i + 1}: {sol.decode()}")