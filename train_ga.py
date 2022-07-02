from snake_game_manuel import *
from neuronal_network import *
from gen_alg import *
import numpy as np

#Define Initial Population for the Training
population = 50
amount_weights = n_x*n_h + n_h*n_h2 + n_h2*n_y

# Get the Population Size
population_size = (population,amount_weights)

# Create new Population based on population_size
new_population = np.random.choice(np.arange(-1,1, step=0.01),size=population_size, replace=True)


num_generations = 150

num_parents_mating = 12
for generation in range(num_generations+10):
    if generation > num_generations:
        clock_tick = 20
    else:
        clock_tick = 50000
    print('')
    print('GENERATION', str(generation))
    print('')
    # Measuring the fitness of each chromosome in the population.
    fitness = calculate_population_fitness(new_population, clock_tick)
    print('')
    print('---> chromosome with best fittness in generation', str(generation), 'has a fitness value of:', np.max(fitness))
    # Selecting the best parents from the current population, to use them for the next generation
    parents = selecting_best_indiv(new_population, fitness, num_parents_mating)

    # Generating the next generation with the help of crossover
    offspring_crossover = crossover(parents, offspring_size=(population_size[0] - parents.shape[0], amount_weights))

    # Offspring receives some variations with mutation
    offspring_mutation = mutation(offspring_crossover)

    # A new generation gets created based on the parents and the offspring.
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation