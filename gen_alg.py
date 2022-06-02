from dataclasses import replace
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



#Create the children for the next generation (or for the best individuals which are now representing the parents)
def crossover(parents, offspring_size):
    offspring = np.empty(offspring_size)

    for k in range(offspring_size[0]):
        while True:
            parents1_idx = random.randint(0, parents.shape[0] - 1)
            parents2_idx = random.randint(0, parents.shape[0] - 1)
            #If two parents are different from each other, then offspring gets created

            if parents1_idx != parents2_idx:
                for j in range(offspring_size[1]):
                    if random.uniform(0, 1) <0.5:
                        offspring[k, j] = parents[parents1_idx, j]
                    else:
                        offspring[k, j] = parents[parents2_idx, j]
                break
    return offspring


#The offsprings which where generated from the crossover, are getting mutated to maintain variation in the population
def mutation(offspring_crossover):
    for idx in range(offspring_crossover.shape[0]):
        for _ in range(25):
            i = randint(0, offspring_crossover.shape[1]-1)

        random_value = np.random.choice(np.arange(-1,1,step=0.001), size=(1), replac=False)
        offspring_crossover[idx, i] = offspring_crossover[idx, i] + random_value

        return offspring_crossover