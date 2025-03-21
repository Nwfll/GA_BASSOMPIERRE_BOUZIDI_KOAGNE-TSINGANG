"""
Example of implementation of the GA Solver package to solve the Traveling Salesperson Problem.
"""
from ga_solver import GAProblem, GASolver
import mastermind as mm
import random


class MastermindProblem(GAProblem):
    """Implementation of GAProblem for the Mastermind problem."""

    def __init__(self, match=None):
        """Initialize the problem with a MastermindMatch instance."""
        self.match = match if match else mm.MastermindMatch()

    def create_chromosome(self):
        """Creates a random chromosome as a list."""
        return self.match.generate_random_guess()

    def fitness(self, chromosome):
        """Evaluates how close the chromosome is to the correct solution."""
        return self.match.rate_guess(chromosome)

    def cross_population(self, parent1: list, parent2: list):
        """Performs one-point crossover."""
        crossing_point = random.randrange(0, len(parent1))
        return parent1[:crossing_point] + parent2[crossing_point:]

    def mutation(self, chromosome: list):
        """Mutates a random gene in the chromosome."""
        valid_colors = mm.get_possible_colors()
        gene_mutated = random.randrange(0, len(chromosome))
        chromosome[gene_mutated] = random.choice(valid_colors)
        return chromosome


if __name__ == '__main__':
    match = mm.MastermindMatch()
    problem = MastermindProblem(match)  
    solver = GASolver(problem)

    solver.reset_population()
    solver.evolve_until()

    print(f"Best guess {mm.encode_guess(solver.get_best_individual().chromosome)} {solver.get_best_individual()}")
    print(f"Problem solved? {match.is_correct(solver.get_best_individual().chromosome)}")
