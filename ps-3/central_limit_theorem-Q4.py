# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis




# Parameters
N_values = [1, 10, 50, 100, 500, 1000]  # Different values of N
num_samples = 10000  # Number of random samples for averaging



# Function to compute properties of the distribution for given N
def compute_statistics(N, num_samples):
    samples = np.mean(np.random.exponential(scale=1, size=(num_samples, N)), axis=1)
    mean = np.mean(samples)
    variance = np.var(samples)
    skewness = skew(samples)
    kurt = kurtosis(samples, fisher=True)  # Fisher's definition (subtract 3)
    return samples, mean, variance, skewness, kurt


statistics = []


for N in N_values:
    samples, mean, variance, skewness, kurt = compute_statistics(N, num_samples)
    statistics.append((N, mean, variance, skewness, kurt))

    # Plot 
    plt.hist(samples, bins=50, alpha=0.9, density=True, label=f'N={N}', histtype='step')

    

# Show the evolution of the distribution

plt.title('Distribution of y for Different N')
plt.xlabel('y')
plt.ylabel('Probability Density')
plt.xlim(0, 2)
plt.legend()
plt.figure(figsize=(12, 8))
plt.show()


# Extract and plot mean, variance, skewness, and kurtosis as a function of N
means = [stat[1] for stat in statistics]
variances = [stat[2] for stat in statistics]
skewnesses = [stat[3] for stat in statistics]
kurtoses = [stat[4] for stat in statistics]



# Subplots for vaious statistical methods
plt.figure(figsize = (12, 8))

# Subplot Mean
plt.subplot(2, 2, 1)
plt.plot(N_values, means, marker='o')
plt.title('Mean vs N')
plt.xlabel('N')
plt.ylabel('Mean')
plt.grid()



# Subplot Variance
plt.subplot(2, 2, 2)
plt.plot(N_values, variances, marker='o')
plt.title('Variance vs N')
plt.xlabel('N')
plt.ylabel('Variance')
plt.grid()



# Estimate N where skewness and kurtosis are within 1% of their value
initial_skewness = skewnesses[0]
initial_kurtosis = kurtoses[0]


# Subplot Skewness
plt.subplot(2, 2, 3)
plt.plot(N_values, skewnesses, marker='o')
plt.title('Skewness vs N')
plt.xlabel('N')
plt.ylabel('Skewness')
plt.axhline(0.01*abs(initial_skewness), color='r', linestyle='--', label='1 % of initial skewness')
plt.legend()
plt.grid()


# Subplot Kurtosis
plt.subplot(2, 2, 4)
plt.plot(N_values, kurtoses, marker='o')
plt.title('Kurtosis vs N')
plt.xlabel('N')
plt.ylabel('Kurtosis')
plt.axhline(0.01*abs(initial_kurtosis), color='r', linestyle='--', label='1 % of initial kurtosis')
plt.legend()

plt.suptitle('Mean, Variance, Skewness and Kurtosis as a function of N')
plt.tight_layout()
plt.grid()
plt.show()





