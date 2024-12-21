# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


# Constants
N0 = 10000  # Initial number of 213Bi atoms
half_life_213Bi = 46*60  # (s)
half_life_209Tl = 2.2*60  # (s)
half_life_209Pb = 3.3*60  # (s)
delta_t = 1  # time step in (s)
time_steps = 20000  # total simulation time in (s)



# Decay probabilities
P_213Bi = 1 - np.exp(-np.log(2) / half_life_213Bi)
P_209Tl = 1 - np.exp(-np.log(2) / half_life_209Tl)
P_209Pb = 1 - np.exp(-np.log(2) / half_life_209Pb)

# Route probabilities for 213Bi decay
route1_prob = 0.9791  # 213Bi -> 209Tl
route2_prob = 1 - route1_prob  # 213Bi -> 209Pb

# Initialize populations
N_213Bi = N0
N_209Tl = 0
N_209Pb = 0
N_209Bi = 0


populations = {
    "213Bi": [],
    "209Tl": [],
    "209Pb": [],
    "209Bi": [],
}


for _ in range(time_steps):
    # Record current populations
    populations["213Bi"].append(N_213Bi)
    populations["209Tl"].append(N_209Tl)
    populations["209Pb"].append(N_209Pb)
    populations["209Bi"].append(N_209Bi)
    
    # Decay 209Pb -> 209Bi
    decay_209Pb = np.sum(np.random.rand(N_209Pb) < P_209Pb)
    N_209Pb -= decay_209Pb
    N_209Bi += decay_209Pb
    
    # Decay 209Tl -> 209Pb
    decay_209Tl = np.sum(np.random.rand(N_209Tl) < P_209Tl)
    N_209Tl -= decay_209Tl
    N_209Pb += decay_209Tl
    
    # Decay 213Bi
    decay_213Bi = np.sum(np.random.rand(N_213Bi) < P_213Bi)
    route1 = np.sum(np.random.rand(decay_213Bi) < route1_prob)
    route2 = decay_213Bi - route1
    N_213Bi -= decay_213Bi
    N_209Tl += route1
    N_209Pb += route2


# Plot 
time = np.arange(time_steps)
plt.figure(figsize=(10, 6))
plt.plot(time, populations["213Bi"], label=r"$^{213}Bi$")
plt.plot(time, populations["209Tl"], label=r"$^{209}Tl$")
plt.plot(time, populations["209Pb"], label=r"$^{209}Pb$")
plt.plot(time, populations["209Bi"], label=r"$^{209}Bi$")
plt.xlabel("Time (s)")
plt.ylabel("Number of Atoms (N)")
plt.title(r"Radioactive Decay of $^{213}Bi$")
plt.xlim(0,20000)
plt.ylim(0,10100)
plt.legend()
plt.grid()
plt.show()


