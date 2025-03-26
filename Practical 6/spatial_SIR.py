import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.animation import FuncAnimation

# Initialize the population
population = np.zeros((100, 100))

# Randomly select an outbreak point
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

# Set model parameters
beta = 0.3
gamma = 0.1

# Set the number of time points
time_points = 100

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 4), dpi=150)
im = ax.imshow(population, cmap=cm.viridis, interpolation='nearest')
ax.set_title(f'Time step: 0')


def update(frame):
    global population
    # Find infected points
    infected_points = np.where(population == 1)
    for i in range(len(infected_points[0])):
        x, y = infected_points[0][i], infected_points[1][i]
        # Check 8 neighbors
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                new_x, new_y = x + dx, y + dy
                # Check if the neighbor is within the grid
                if 0 <= new_x < 100 and 0 <= new_y < 100:
                    if population[new_x, new_y] == 0:
                        # Infect the neighbor with probability beta
                        if np.random.rand() < beta:
                            population[new_x, new_y] = 1
        # Infected individual recovers with probability gamma
        if np.random.rand() < gamma:
            population[x, y] = 2

    # Update the image
    im.set_array(population)
    ax.set_title(f'Time step: {frame}')
    return im,


# Create the animation
ani = FuncAnimation(fig, update, frames=time_points, interval=200, blit=True)

plt.show()