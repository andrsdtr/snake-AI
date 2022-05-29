from random import randint, choice
from snake_game_ai import *


#Calculating the fitness value of the current game based on the given chromosome
def calculate_population_fitness(pop):
    fitness = []
    for i in range(pop.shape[0]):
        fit = play_game_with_GA(display,clock,pop[i])
        print('Fitness value of the following chromosome' + str(i) + ': ', fitness)
        fitness.append(fitness)
    
    return np.array(fitness)

#Get the best individuals from the current generation and use them as the parents for the following generation
def selecting_best_indiv(pop, fitness, num_parents):
    parents = np.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        max_fitness_idx = np.where(fitness == np.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parent_num, :] = pop[max_fitness_idx, :]
        fitness[max_fitness_idx] = -99999999
    return parents



