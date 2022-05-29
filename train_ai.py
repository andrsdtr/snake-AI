from snake_game_manuel import *
from neuronal_network import *
import numpy as np

#Define Initial Population for the Training
population = 50
amount_weights = n_x*n_h + n_h*n_h2 + n_h2*n_y

# Get the Population Size
population_size = (population,amount_weights)

# Create new Population based on population_size
new_population = np.random.choice(np.arange(-1,1, step=0.01),size=population_size, replace=True)