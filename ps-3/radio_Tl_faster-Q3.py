# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt



# Constants
N = 1000  
tau = 3.053 * 60  # Half-life in (s)
tmax = 1000  # Max time in (s)

# faster method
random_numbers = np.random.random(N)
decay_times = -(tau/np.log(2) )* np.log(1 - random_numbers)  # Inverse transform sampling
decay_times = np.sort(decay_times)  # Sort decay times


time_points = np.linspace(0, tmax, 1000)
remaining_atoms = [np.sum(decay_times > t) for t in time_points]

# Plot 
plt.figure(figsize=(10, 6))
plt.plot(time_points, remaining_atoms, 'g-', label="Remaining Atoms")
plt.xlabel("Time (s)")
plt.ylabel("Number of Atoms (N)")
plt.title(r"A Graph of the Number of Undecayed Atoms of $^{208}Tl$ against Time")
plt.xlim(0, tmax)
plt.ylim(0, N + 20)
plt.grid()
plt.legend()
plt.show()


