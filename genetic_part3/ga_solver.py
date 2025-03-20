# -*- coding: utf-8 -*-
"""
Package to solve a Genetic algorithm problem
DO NOT MODIFY THIS FILE. You need to adapt the file "your_problem.py"
"""
import random
from abc import ABC, abstractmethod


class Individual:
    """Represents an Individual for a genetic algorithm"""

    def __init__(self, chromosome: list, fitness: float):
        """Initializes an Individual for a genetic algorithm

        Args:
            chromosome (list[]): a list representing the individual's chromosome
            fitness (float): the individual's fitness (the higher the value, the better the fitness)
        """
        self.chromosome = chromosome
        self.fitness = fitness

    def __lt__(self, other):
        """Implementation of the less_than comparator operator"""
        return self.fitness < other.fitness

    def __repr__(self):
        """Representation of the object for print calls"""
        return f'Indiv({self.fitness:.1f},{self.chromosome})'


class GAProblem(ABC):
    """Defines a Genetic algorithm problem to be solved by ga_solver"""

    def __init__(self):
        pass  # REPLACE WITH YOUR CODE

    @abstractmethod
    def create_chromosome(self):
        """Function that creates a random chromosome as a list."""
        pass  # REPLACE WITH YOUR CODE

    @abstractmethod
    def fitness(self, chromosome):
        """Takes a chromosome and returns its fitness as a numerical value.
        The better the chromosome is, the higher the fitness should be"""
        pass  # REPLACE WITH YOUR CODE

    @abstractmethod
    def cross_population(self, parent1: list, parent2: list):
        """Takes two chromosomes to cross them and create a new chromosome."""
        pass  # REPLACE WITH YOUR CODE

    @abstractmethod
    def mutation(self, chromosome):
        """Takes one chromosome and returns it after a mutation"""
        pass  # REPLACE WITH YOUR CODE


class GASolver:
    def __init__(self, problem: GAProblem, selection_rate=0.5, mutation_rate=0.1,
                 pop_size=200, max_nb_of_generations=100, treshold_fitness=None):
        """Initializes an instance of a ga_solver for a given GAProblem

        Args:
            problem (GAProblem): GAProblem to be solved by this ga_solver
            selection_rate (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
            mutation_rate (float, optional): Mutation rate between 0 and 1.0. Defaults to 0.1.
            pop_size (int, optional): Size of the population, at least 2. Defaults to 200.
            max_nb_of_generations (int, optional): Maximum number of generations. Defaults to 100.
            treshold_fitness (int, optional): Threshold fitness to reach before stopping. Defaults to None.
        """
        self._problem = problem
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._pop_size = pop_size
        self._max_number_of_generations = max_nb_of_generations
        self._treshold_fitness = treshold_fitness
        self._population = []

    def reset_population(self):
        """Initialize the population with pop_size random Individuals"""
        for _ in range(self._pop_size):
            new_chromosome = self._problem.create_chromosome()
            fitness = self._problem.fitness(new_chromosome)
            self._population.append(Individual(new_chromosome, fitness))

    def evolve_for_one_generation(self):
        """Apply the process for one generation:
            - Sort the population (Descending order)
            - Selection: Remove x% of the population (less adapted)
            - Reproduction: Recreate the same quantity by crossing the surviving ones
            - Mutation: Mutate individuals with a probability equal to mutation_rate
        """
        population_size = len(self._population)
        self._population.sort(key=lambda ind: ind.fitness, reverse=True)
        del self._population[int(len(self._population) * (1 - self._selection_rate)):]

        number_of_birth_needed = population_size - len(self._population)
        for _ in range(number_of_birth_needed):
            parent1, parent2 = random.sample(self._population, 2)
            new_chromosome = self._problem.cross_population(parent1.chromosome, parent2.chromosome)
            if random.random() < self._mutation_rate:
                new_chromosome = self._problem.mutation(new_chromosome)
            fitness = self._problem.fitness(new_chromosome)
            self._population.append(Individual(new_chromosome, fitness))

    def show_generation_summary(self):
        """Print some debug information on the current state of the population"""
        self._population.sort(key=lambda ind: ind.fitness, reverse=True)
        print(f"Best chromosome fitness: {self._population[0].fitness}")
        median_index = len(self._population) // 2
        print(f"Median chromosome fitness: {self._population[median_index].fitness}")

    def get_best_individual(self):
        """Return the best Individual of the population"""
        return max(self._population, key=lambda ind: ind.fitness)

    def evolve_until(self):
        """Launch the evolve_for_one_generation function until one condition is met:
            - Max number of generations is reached
            - The fitness of the best Individual is greater than or equal to threshold_fitness
        """
        nb_of_generations = 0
        while nb_of_generations < self._max_number_of_generations:
            self.evolve_for_one_generation()
            if self._treshold_fitness is not None and self.get_best_individual().fitness >= self._treshold_fitness:
                break
            nb_of_generations += 1
        best = self.get_best_individual()
        print(f"Best individual: {best.chromosome} with a fitness of {best.fitness}")