# -*- coding: utf-8 -*-



import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
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



# Animation of the wavefunction
figure, ax = plt.subplots()
line, = ax.plot(x/(1e-9), psi_real_t(0),'g-')
ax.set_xlim(0, L)
ax.set_ylim(-1, 1)
ax.set_xlabel("x (nm)")
time_text = ax.text(0.8*L, 0.8, " ", fontsize = 10)
ax.set_ylabel(r'$\Psi(x, t)$')
             




def update(frame):
    t = frame*h
    psi_t = psi_real_t(t)
    line.set_data(x/(1e-9), psi_t)
    time_text.set_text(f't = {t:.1e} s')
    return line, time_text

anim = FuncAnimation(figure, update, frames = 200, interval = 100, blit = True)
anim.save('spectral_SE.mp4')
plt.show()
