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

