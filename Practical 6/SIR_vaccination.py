import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Define SIR model parameters
beta = 0.3  # Infection rate
gamma = 0.05  # Recovery rate
N = 10000  # Total population
t_end = 1000  # End time of simulation
dt = 0.1  # Time step
t = np.arange(0, t_end, dt)

# Different vaccination percentages
vaccination_percentages =[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

# Store the number of infected people for different vaccination percentages
infected_data = []

for vaccination_percentage in vaccination_percentages:
    # Initialize the population
    vaccinated = int(N * vaccination_percentage)
    susceptible = N - vaccinated - 1
    infected = 1
    recovered = 0

    S = np.zeros_like(t)
    I = np.zeros_like(t)
    R = np.zeros_like(t)

    S[0] = susceptible
    I[0] = infected
    R[0] = recovered

    for i in range(1, len(t)):
        dS = -beta * S[i - 1] * I[i - 1] / N
        dI = beta * S[i - 1] * I[i - 1] / N - gamma * I[i - 1]
        dR = gamma * I[i - 1]

        S[i] = S[i - 1] + dS * dt
        I[i] = I[i - 1] + dI * dt
        R[i] = R[i - 1] + dR * dt

    infected_data.append(I)

# Plot the number of infected people for different vaccination percentages
plt.figure(figsize=(10, 6))
for i, percentage in enumerate(vaccination_percentages):
    plt.plot(t, infected_data[i], color=cm.viridis(int(255 * i / len(vaccination_percentages))),
             label=f'{percentage * 100:.0f}% vaccinated')

plt.xlabel('Time')
plt.ylabel('Number of Infected People')
plt.title('SIR Model with Vaccination')
plt.legend()
plt.grid(True)
plt.show()

# Try to estimate the herd immunity threshold
# When the peak number of infected people drops significantly, the corresponding vaccination percentage may be close to the herd immunity threshold
threshold_index = None
for i in range(1, len(infected_data)):
    if max(infected_data[i]) < 0.1 * max(infected_data[0]):
        threshold_index = i
        break

if threshold_index is not None:
    herd_immunity_threshold = vaccination_percentages[threshold_index]
    print(f"Approximate herd immunity threshold: {herd_immunity_threshold * 100:.0f}%")
else:
    print("Could not estimate herd immunity threshold from the data.")