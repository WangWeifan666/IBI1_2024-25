import numpy as np
import matplotlib.pyplot as plt

# Define the basic variables
N = 10000  # Total population
S = N - 1  # Initial number of susceptible individuals
I = 1  # Initial number of infected individuals
R = 0  # Initial number of recovered individuals
beta = 0.3  # Infection probability
gamma = 0.05  # Recovery probability

# Create arrays to track the evolution of variables over time
S_array = [S]
I_array = [I]
R_array = [R]
time_points = 1000

# Pseudocode for the time loop
# For each time point from 1 to 1000:
#     Calculate the infection probability = beta * (current number of infected people / total population)
#     Randomly select a portion of susceptible people to be infected according to the infection probability
#     Randomly select a portion of infected people to recover according to the recovery probability
#     Update the numbers of susceptible, infected, and recovered people
#     Record the numbers of susceptible, infected, and recovered people at the current time point

# Time loop
for t in range(1, time_points):
    # Calculate the infection probability
    infection_prob = beta * (I / N)
    # Randomly select susceptible people to be infected
    new_infections = np.sum(np.random.choice([1, 0 ], S, p=[infection_prob, 1 - infection_prob]))
    # Randomly select infected people to recover
    new_recoveries = np.sum(np.random.choice([1, 0], I, p=[gamma, 1 - gamma]))
    # Update the population numbers
    S = S - new_infections
    I = I + new_infections - new_recoveries
    R = R + new_recoveries
    # Record the results
    S_array.append(S)
    I_array.append(I)
    R_array.append(R)

# Set the figure size and resolution
plt.figure(figsize=(6, 4), dpi=150)
# Plot the results
plt.plot(range(time_points), S_array, label='Susceptible')
plt.plot(range(time_points), I_array, label='Infected')
plt.plot(range(time_points), R_array, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR Model')
plt.legend()
# Save the plot
plt.savefig('SIR_plot.png')
# Display the plot
plt.show()    
