# Genetic Algorithm Solver (GASolver)

## Overview
This package provides a **modular and reusable** framework for solving **Genetic Algorithm (GA) problems**.  
It is designed to be **problem-agnostic**, meaning you can use it for different optimization problems by simply implementing a new problem class.
YOU ONLY HAVE TO MODIFY THE FILE "your_problem.py". DO NOT CHANGE THE OTHERS

## How to Implement a New Genetic Algorithm Problem

To define a new problem, you need to **create a subclass of `GAProblem`** and implement its required methods.

### 1. Create a New Problem Class

Each problem should **inherit from `GAProblem`** and implement the following methods:

- `create_chromosome(self)`: Generates a random chromosome (list of genes).
- `fitness(self, chromosome)`: Evaluates how good a chromosome is.
- `cross_population(self, parent1, parent2)`: Defines how two parents produce an offspring.
- `mutation(self, chromosome)`: Applies mutation to a chromosome.

### 2. Example: Implementing a Custom Problem

tsp_problem.py is an example of implementing a **simple problem**, where the goal is to find the shortest route to cross several cities.


# Running the genetic algorithm solver
if __name__ == '__main__':
    problem = SumMaximizationProblem()
    solver = GASolver(problem, pop_size=100, max_nb_of_generations=50)
    solver.reset_population()
    solver.evolve_until()
```

### 3. Running Your Genetic Algorithm

To run your newly implemented GA problem, simply execute your script

### 4. Extending and Customizing

- **Tweak parameters** like population size, mutation rate, and selection rate when initializing `GASolver`.
- **Try different fitness functions** depending on your problem's needs.
- **Experiment with crossover and mutation strategies** to improve GA performance.

## File Structure

```
/GA_Solver/
│── ga_solver.py          # Core GA Solver (Do not modify)
│── your_problem.py       # Your custom GA problem
│── tsp_problem.py        # Traveler Salesperson example
│── cities.txt            # Traveler Salesperson example
│── cities.py             # Traveler Salesperson example			
│── README.md             # Documentation
```

## Best Practices
✔ Keep `GASolver` **generic** and free from problem-specific logic.  
✔ Document your problem class so others can understand and reuse it.  
✔ Follow **PEP-8** to maintain clean and readable code.  

## License
This project is open-source. Feel free to modify and improve! 
