# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 11:24:15 2022

@author: agademer & tdrumond

Template for exercise 1
(genetic algorithm module specification)
"""
import mastermind as mm
import random


MATCH = mm.MastermindMatch(secret_size=4)


class Individual:
    """Represents an Individual for a genetic algorithm"""

    def __init__(self, chromosome: list, fitness: float):
        """Initializes an Individual for a genetic algorithm 

        Args:
            chromosome (list[]): a list representing the individual's chromosome
            fitness (float): the individual's fitness (the higher, the better the fitness)
        """
        self.chromosome = chromosome
        self.fitness = fitness

    def __lt__(self, other):
        """Implementation of the less_than comparator operator"""
        return self.fitness < other.fitness

    def __repr__(self):
        """Representation of the object for print calls"""
        return f'Indiv({self.fitness:.1f},{self.chromosome})'



class GASolver:
    def __init__(self, selection_rate=0.5, mutation_rate=0.1):
        """Initializes an instance of a ga_solver for a given GAProblem

        Args:
            selection_rate (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
            mutation_rate (float, optional): mutation_rate between 0 and 1.0. Defaults to 0.1.
        """
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._population = []

    def reset_population(self, pop_size=50):
        """ Initialize the population with pop_size random Individuals """
        for i in range(pop_size): 
            chromosome = MATCH.generate_random_guess()
            fitness = MATCH.rate_guess(chromosome)
            new_individual = Individual(chromosome, fitness)
            self._population.append(new_individual)

        pass  # REPLACE WITH YOUR CODE

    def evolve_for_one_generation(self):
        """ Apply the process for one generation : 
            -	Sort the population (Descending order)
            -	Selection: Remove x% of population (less adapted)
            -   Reproduction: Recreate the same quantity by crossing the 
                surviving ones 
            -	Mutation: For each new Individual, mutate with probability 
                mutation_rate i.e., mutate it if a random value is below   
                mutation_rate
        """
        size_required = len(self._population)
        self._population.sort(key=lambda ind: ind.fitness, reverse = True)
        del self._population[int(len(self._population)*(1-self._selection_rate)):]  #selection rate stand for the people remaining so in order
        # to delete we use 1-selection_rate

        number_of_birth_needed = size_required-len(self._population) #we want to create as much inidividuals as the ones deleted
        
        for baby in range(number_of_birth_needed):
            parent1 = self._population[baby] 
            parent2 = self._population[baby+1] # elitist behaviour: we make reproduce only the best individuals #KIFFEUR 
            crossing_point = random.randrange(0, len(parent1.chromosome))
            new_chromosome = parent1.chromosome[0:crossing_point] + parent2.chromosome[crossing_point:] #we concatenate the chromosomes of each parent


            #MUTATION
            number = random.random()
            if number < self._mutation_rate:
                valid_colors = mm.get_possible_colors()
                new_gene = random.choice(valid_colors) #we randomly chose a new mutation color
                gene_mutated = random.randrange(0, len(new_chromosome)) #we randomly select the gene mutated
                new_chromosome[gene_mutated] = new_gene #we apply the color to the new gene selected
            fitness=MATCH.rate_guess(new_chromosome)
            new_individual = Individual(new_chromosome, fitness) #we create a new individual
            self._population.append(new_individual)

        pass  # REPLACE WITH YOUR CODE

    def show_generation_summary(self):
        """ Print some debug information on the current state of the population """
        pass  # REPLACE WITH YOUR CODE

    def get_best_individual(self):
        """ Return the best Individual of the population """
        return max(self._population, key= lambda ind: ind.fitness)
        pass  # REPLACE WITH YOUR CODE

    def evolve_until(self, max_nb_of_generations=500, threshold_fitness=None):
        """ Launch the evolve_for_one_generation function until one of the two condition is achieved : 
            - Max nb of generation is achieved
            - The fitness of the best Individual is greater than or equal to
              threshold_fitness
        """
        nb_of_generations = 0
        while nb_of_generations < max_nb_of_generations and self.get_best_individual().fitness < threshold_fitness:
            self.evolve_for_one_generation()

        pass  # REPLACE WITH YOUR CODE

#we run a game
solver = GASolver()
solver.reset_population()
solver.evolve_until(threshold_fitness=MATCH.max_score())
best = solver.get_best_individual()
print(f"Best guess {best.chromosome}")
print(f"Problem solved? {MATCH.is_correct(best.chromosome)}")
