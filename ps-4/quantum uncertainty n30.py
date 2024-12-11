# -*- coding: utf-8 -*-



import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxw



def H(n, x):
    
    if int(n) != n:
        print('Please input an integer n')
    
    elif n < 0:
        print('Please input a number n >= 0')
        
    elif n == 0:
        return 1
    
    elif n == 1:
        return 2*x
    
    else:
        return 2*x * H(n-1, x) - 2 *(n-1) * H(n-2, x)
    
    
def psi(n, x):
    return (1 / (np.sqrt(2**n * np.math.factorial(n) * np.sqrt(np.pi)))) * np.exp((-x**2) /2) * H(n, x)


N = 200
n = 30
x = np.linspace(-10, 10, N)

psi_vals = psi(n, x)

plt.plot(x, psi_vals, label = "n = "+ str(n))
    

plt.xlim(-10, 10)
plt.legend()
plt.title('A 1D quantum wavefunction as a function of x for n = 30')
plt.xlabel('x (m)')
plt.ylabel(r'Wavefunction ($\psi_{n})$')

plt.grid()

plt.savefig('oscillator_wavefunction_n_30.png')

