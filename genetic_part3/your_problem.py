# -*- coding: utf-8 -*-
"""
Template of the Genetic problem you want to solve, you need to adapt the functions
create_chromosome, fitness, cross_population and mutation; and to read its definition
to ensure that you respect its parameters and its return.
"""
from ga_solver import GAProblem

#### PARAMETERS OF THE GENETIC ALGORITHM. UPDATE THEIR VALUES TO CUSTOMIZE THE PROGRAM'S BEHAVIOUR
population_size = 200
max_nb_of_generations = 100
treshold_fitness = None
selection_rate = 0.5
mutation_rate = 0.1

### CUSTOMIZED CLASS TAILORED TO YOUR PROBLEM. DEFINE EACH FUNCTION CORRECTLY WITH YOUR RULES TO RUN THE PROGRAM
class YourProblem(GAProblem):
    """Implementation of GAProblem for the mastermind problem"""

    def create_chromosome(self):
        """ Function that creates a random chromosome as a list."""
        pass  # YOUR CODE HERE

    def fitness(
            self, chromosome):
        """Takes a chromosome and returns its fitness as a numerical value.
        The better the chromosome is, the higher the fitness should be"""
        pass  # YOUR CODE HERE

    def cross_population(
            self, parent1: list,
            parent2: list):
        """Takes two chromosomes to cross them and create a new chromosome."""
        pass  # YOUR CODE HERE

    def mutation(
            self, chromosome: list):
        """Takes one chromosome and returns it after a mutation"""
        pass  # YOUR CODE HERE


#  MAIN EXECUTION BLOCK: Modify this section if you have specificities when calling the classe "YourProblem"
if __name__ == '__main__':
    from ga_solver import GASolver
    problem = YourProblem()
    solver = GASolver(problem)
    solver.reset_population()
    solver.evolve_until()
