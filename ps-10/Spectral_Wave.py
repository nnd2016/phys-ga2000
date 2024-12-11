# -*- coding: utf-8 -*-




## Spectral Method

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dst, idst






# Constants
M = 9.109e-31  
hbar = 1.0545718e-34  
L = 1e-8  
N = 1000  
x = np.linspace(0, L, N, endpoint=False)
#dx = x[1] - x[0] 
h = 1e-18  

# Initial wavefunction
x0 = L / 2  
sigma = 1e-10  
k = 5e10  

# Real and imaginary parts of psi(x, 0)
psi_real = np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.cos(k * x)
psi_imag = np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.sin(k * x)



# Compute coefficients a_k and eta_k using the discrete sine transform (DST)
alpha_k = dst(psi_real, type=1) / N
eta_k = dst(psi_imag, type=1) / N




# Computes the real part of psi(x, t) using inverse DST
def psi_real_t(t):
    phase = np.exp(-1j * (np.pi**2 * hbar * np.arange(1, N+1) ** 2 * t) / (2 * M * L**2))
    b_k = alpha_k + 1j * eta_k
    coeffs = np.real(b_k * phase)
    return idst(coeffs, type=1) * N



# Plot at t = 1x10^-16 s
t_test = 1e-16
psi_t = psi_real_t(t_test)

plt.figure(figsize=(8, 4))
plt.plot(x/(1e-9), psi_t)
plt.xlabel("x (nm)")
plt.ylabel(r"($\Psi(x, t)$)")
plt.title(r"Wavefunction at $t = 10^{-16} s$")
plt.grid()
plt.savefig('spectral_test_time.png')
plt.show()



times = [5e-17 , 5.7e-16,  9.5e-16, 1.4e-15]

num_plots = len(times)
fig, ax = plt.subplots(num_plots, figsize = (8, 8), sharex = True)

for i, time in enumerate(times):
    ax[i].plot(x/(1e-9),  psi_real_t(time), 'r-')
fig.supylabel(r'$\Psi(x, t)$')
fig.suptitle('Propagation of Wave at Different Times (Spectral Method)', fontsize = '20')
plt.xlabel('x (nm)')
plt.savefig('spectral_wave_progression.png')






