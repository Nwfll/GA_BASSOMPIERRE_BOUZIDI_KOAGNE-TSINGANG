# -*- coding: utf-8 -*-
"""
Example of implementation of the GA Solver package to solve the Traveling Salesperson Problem.
"""
from ga_solver import GAProblem
import cities
import random

class TSProblem(GAProblem):
    """Implementation of GAProblem for the traveling salesperson problem"""
        
    def create_chromosome(self):
        """ Function that creates a random chromosome as a list."""
        chromosome = cities.default_road(city_dict) 
        random.shuffle(chromosome) 
        return chromosome

    def fitness(
            self, chromosome):
        """Takes a chromosome and returns its fitness as a numerical value.
        The better the chromosome is, the higher the fitness should be"""
        return - cities.road_length(city_dict, chromosome)

    def cross_population(
            self, parent1: list,
            parent2: list):
        """Takes two chromosomes to cross them and create a new chromosome."""
        crossing_point = len(parent1)//2
        new_chromosome = parent1[0:crossing_point] 
        #we add all the cities from the parent 2 which are not already in the children's itinerary
        for city in parent2[crossing_point:]:
            if (city in new_chromosome) == False :
                new_chromosome.append(city)
            #and if some cities were not added, we add them from the list of all possible cities
        possible_cities = cities.default_road(city_dict) 
        for city in possible_cities:
            if (city in new_chromosome) == False :
                new_chromosome.append(city)
        return new_chromosome

    def mutation(
            self, chromosome: list):
        """Takes one chromosome and returns it after a mutation"""
        gene_mutated1 = random.randrange(0, len(chromosome)) 
        gene_mutated2 = random.randrange(0, len(chromosome))
        #we use a temporary variable to swap them
        temp_gene = chromosome[gene_mutated1]
        chromosome[gene_mutated1]=chromosome[gene_mutated2]
        chromosome[gene_mutated2]=temp_gene
        return chromosome

if __name__ == '__main__':

    from ga_solver import GASolver

    city_dict = cities.load_cities("cities.txt")
    problem = TSProblem()
    solver = GASolver(problem)
    solver.reset_population()
    solver.evolve_until()