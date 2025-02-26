# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 11:24:15 2022

@author: agademer & tdrumond

Template for exercise 1
(genetic algorithm module specification)
"""
import cities 
import random

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
    def __init__(self, selection_rate=0.5, mutation_rate=0.7):
        """Initializes an instance of a ga_solver for a given GAProblem

        Args:
            selection_rate (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
            mutation_rate (float, optional): mutation_rate between 0 and 1.0. Defaults to 0.1.
        """
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._population = []

    def reset_population(self, pop_size=200):
        """ Initialize the population with pop_size random Individuals """
        for i in range(pop_size): 
            chromosome = cities.default_road(city_dict) 
            random.shuffle(chromosome) 
            fitness = - cities.road_length(city_dict, chromosome) 
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
            parent1, parent2 = random.sample(self._population, 2)  
            #we add the first half of the first parent
            crossing_point = len(parent1.chromosome)//2
            new_chromosome = parent1.chromosome[0:crossing_point] 
            #we add all the cities from the parent 2 which are not already in the children's itinerary
            for city in parent2.chromosome[crossing_point:]:
                if (city in new_chromosome) == False :
                    new_chromosome.append(city)
            #and if some cities were not added, we add them from the list of all possible cities
            possible_cities = cities.default_road(city_dict) 
            for city in possible_cities:
 
                if (city in new_chromosome) == False :
                    new_chromosome.append(city)
            #MUTATION
            number = random.random()
            if number < self._mutation_rate:
                #we randomly select two genes mutated which will be swapped
                gene_mutated1 = random.randrange(0, len(new_chromosome)) 
                gene_mutated2 = random.randrange(0, len(new_chromosome))
               
                #we use a temporary variable to swap them
                temp_gene = new_chromosome[gene_mutated1] 
                new_chromosome[gene_mutated1]=new_chromosome[gene_mutated2]
                new_chromosome[gene_mutated2]=temp_gene

            fitness = - cities.road_length(city_dict, new_chromosome) 
            new_individual = Individual(new_chromosome, fitness) #we create the new individual
            self._population.append(new_individual)
        pass  # REPLACE WITH YOUR CODE

    def show_generation_summary(self):
        """ Print some debug information on the current state of the population """
        self._population.sort(key=lambda ind: ind.fitness, reverse = True)
        print(f"Best chromosome length : {cities.road_length(city_dict, self._population[0].chromosome)}")
        print(f"Median chromosome length : {cities.road_length(city_dict, self._population[len(self._population)//2].chromosome)}")
        total_road = 0

        for road in range(len(self._population)):
            total_road+=cities.road_length(city_dict,self._population[road].chromosome)
        print(f"Mean chromosome length : {total_road/len(self._population)}")
        
        pass  # REPLACE WITH YOUR CODE

    def get_best_individual(self):
        """ Return the best Individual of the population """
        return max(self._population, key= lambda ind: ind.fitness)
        pass  # REPLACE WITH YOUR CODE

    def evolve_until(self, max_nb_of_generations=100, threshold_fitness=None):
        """ Launch the evolve_for_one_generation function until one of the two condition is achieved : 
            - Max nb of generation is achieved
            - The fitness of the best Individual is greater than or equal to
              threshold_fitness
        """
        nb_of_generations = 0
        while nb_of_generations < max_nb_of_generations :# and self.get_best_individual().fitness < threshold_fitness:
            self.evolve_for_one_generation()
            #self.show_generation_summary()  #uncomment if you want to see the summary 
            nb_of_generations += 1

        pass  # REPLACE WITH YOUR CODE

city_dict = cities.load_cities("cities.txt") 
#we run a game
solver = GASolver() 
solver.reset_population() 
solver.evolve_until() 
best = solver.get_best_individual() 
print (cities.road_length(city_dict, best.chromosome))
cities.draw_cities(city_dict, best.chromosome) 
