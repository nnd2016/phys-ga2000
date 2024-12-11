# -*- coding: utf-8 -*-



## Crank-Nicolson Method

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
dx = x[1] - x[0]

# Initial wavefunction
psi = np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.exp(1j * k * x)
psi[0] = psi[-1] = 0  # Boundary conditions

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




# Animation

fig, ax = plt.subplots()
line, = ax.plot(x/(1e-9), np.real(psi), 'g-', label=r"Re($\Psi(x, t)$)")
ax.set_xlim(0, L)
ax.set_ylim(-1, 1)
ax.set_xlabel("x (nm)")
ax.set_ylabel(r"$\Psi$")
fig.suptitle('Propagation of Wavefunction')
time_text = ax.text(0.8 * L, 0.8, "", fontsize=10)

def update(frame):
    global psi
    psi = crank_nicolson_step(psi)
    line.set_data(x, np.real(psi))
    time_text.set_text(f"t = {frame * h:.2e} s")
    return line, time_text

anim = FuncAnimation(fig, update, frames=500, interval=100, blit=True)
anim.save('crank_nicolson_SE_animation.mp4')
plt.show()