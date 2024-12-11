# -*- coding: utf-8 -*-

import numpy as np
from gaussxw import gaussxw
import matplotlib.pyplot as plt

# Question 3

 # 3a
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





# 3a plot
N = 200
x = np.linspace(-4, 4, N)
n_list = [0, 1, 2 ,3]

for n in n_list:
    psi_vals = psi(n,x)    
    plt.plot(x, psi_vals, label = 'n = ' + str(n))
    
plt.xlim(-4, 4)
plt.legend()
plt.title('A 1D quantum wavefunction as a function of x for n = 0,1,2,3')
plt.xlabel('x (m)')
plt.ylabel('Wavefunction ($\psi_{n})$')

plt.grid()
plt.savefig('oscillator_wavefuntion_multiple_n.png')





# 3c

N = 100
a = -1
b = 1
n = 5

def f(z):
    coeff = ((1 + z**2)/((1 - z**2)**2)) * (((z/(1 - z**2))**2))  
    wavef = psi(n, z/(1 - z**2))
    return coeff * np.abs(wavef)**2

x, w = gaussxw(N)
xp = 0.5*(b-a)*x + 0.5*(b+a)
wp = 0.5*(b-a)*w
    
s = 0
for k in range(N):
    s += wp[k]*f(xp[k])

print(f'The uncertainty for n = {n} is {np.sqrt(s)}')

