import numpy as np
import time
from typing import List, Tuple


class Chromosome:
    NUM_LINES = 8
    BITS_PER_POSITION = 3

    def __init__(self, genes: np.ndarray = None):
        if genes is None:
            self.genes = np.random.randint(0, 2, size=(self.NUM_LINES * self.BITS_PER_POSITION))
        else:
            self.genes = genes

    def decode(self) -> List[int]:
        return [int(''.join(self.genes[i * 3:(i + 1) * 3].astype(str)), 2) for i in range(self.NUM_LINES)]

    def fitness(self) -> int:
        positions = self.decode()
        collisions = 0
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                if positions[i] == positions[j]:  # Same column collision
                    collisions += 1
                if abs(positions[i] - positions[j]) == abs(i - j):  # Diagonal collision
                    collisions += 1
        return collisions


class Population:
    def __init__(self, size: int):
        self.size = size
        self.individuals: List[Chromosome] = [Chromosome() for _ in range(size)]

    def get_fitness_scores(self) -> List[int]:
        return [individual.fitness() for individual in self.individuals]

    def select_parents(self) -> List[Chromosome]:
        fitness_scores = np.array(self.get_fitness_scores())
        probabilities = 1.0 / (1.0 + fitness_scores)
        probabilities /= probabilities.sum()
        selected_indices = np.random.choice(len(self.individuals), size=self.size, p=probabilities)
        return [self.individuals[i] for i in selected_indices]

    def crossover(self, parents: List[Chromosome], crossover_rate: float) -> List[Chromosome]:
        offspring = []
        for i in range(0, len(parents), 2):
            if i + 1 < len(parents):
                if np.random.random() < crossover_rate:
                    cut_point = np.random.randint(1, Chromosome.NUM_LINES * Chromosome.BITS_PER_POSITION)
                    child1 = np.concatenate((parents[i].genes[:cut_point], parents[i + 1].genes[cut_point:]))
                    child2 = np.concatenate((parents[i + 1].genes[:cut_point], parents[i].genes[cut_point:]))
                    offspring.extend([Chromosome(child1), Chromosome(child2)])
                else:
                    offspring.extend([Chromosome(parents[i].genes.copy()), Chromosome(parents[i + 1].genes.copy())])
        return offspring

    def mutate(self, mutation_rate: float) -> None:
        for individual in self.individuals:
            if np.random.random() < mutation_rate:
                idx = np.random.randint(0, Chromosome.NUM_LINES * Chromosome.BITS_PER_POSITION)
                individual.genes[idx] = 1 - individual.genes[idx]

class GeneticAlgorithm:
    def __init__(self, population_size: int = 20, max_generations: int = 1000,
                 crossover_rate: float = 0.80, mutation_rate: float = 0.03):
        self.population_size = population_size
        self.max_generations = max_generations
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.population = Population(population_size)

    def elitist_selection(self, offspring: List[Chromosome]) -> None:
        current_fitness = list(zip(self.population.get_fitness_scores(), self.population.individuals))
        offspring_fitness = list(zip([ind.fitness() for ind in offspring], offspring))
        current_fitness.sort(key=lambda x: x[0])
        offspring_fitness.sort(key=lambda x: x[0])
        survivors = [Chromosome(c.genes.copy()) for _, c in current_fitness[:self.population_size // 2]]
        new_individuals = survivors + [Chromosome(c.genes.copy()) for _, c in offspring_fitness[:self.population_size // 2]]
        self.population.individuals = new_individuals

    def run(self) -> Tuple[int, Chromosome]:
        generation = 0
        while generation < self.max_generations:
            fitness_scores = self.population.get_fitness_scores()
            if min(fitness_scores) == 0:
                break
            parents = self.population.select_parents()
            offspring = self.population.crossover(parents, self.crossover_rate)
            offspring_population = Population(self.population_size)
            offspring_population.individuals = offspring
            offspring_population.mutate(self.mutation_rate)
            self.elitist_selection(offspring)
            generation += 1
        best_index = np.argmin(self.population.get_fitness_scores())
        return generation, self.population.individuals[best_index]
