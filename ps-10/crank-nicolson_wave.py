# -*- coding: utf-8 -*-


### Crank-Nicolson Animation
import numpy as np
import matplotlib.pyplot as plt



# Constants
M = 9.109e-31  
L = 1e-8  
hbar = 1.0545718e-34  
N = 1000  
a = L / N  
h = 1e-18  
x0 = L / 2
sigma = 1e-10
k = 5e10



# Spatial grid
x = np.linspace(0, L, N)

# Initial wavefunction
psi_0 = np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.exp(1j * k * x)
psi_0[0] = psi[-1] = 0  # Boundary conditions

# Crank-Nicolson Matrices
r = hbar * h / (2 * M * a**2)  
diagonal = 1 + 2j * r
off_diagonal = -1j * r

# A and B matrices
A = np.diag([diagonal] * N) + np.diag([off_diagonal] * (N - 1), 1) + np.diag([off_diagonal] * (N - 1), -1)
B = np.diag([1 - 2j * r] * N) + np.diag([1j * r] * (N - 1), 1) + np.diag([1j * r] * (N - 1), -1)

# Time evolution
def crank_nicolson_step(psi):
    v = B @ psi
    psi_new = np.linalg.solve(A, v)
    psi_new[0] = psi_new[-1] = 0  
    return psi_new




## Plots of wave progression
times = [5e-17 , 5.7e-16,  9.5e-16, 1.4e-15]

num_plots = len(times)
fig, ax = plt.subplots(num_plots, figsize = (8, 8), sharex = True)
psi = psi_0.copy()

for i, time in enumerate(times):
    ax[i].plot(x/(1e-9),  np.real(crank_nicolson_step(psi))


fig.supylabel(r'$\Psi(x, t)$')
fig.suptitle('Wave Propagation via Crank-Nicolson Method')
plt.xlabel('x (nm)')
plt.savefig('cn_wave_prop.png')