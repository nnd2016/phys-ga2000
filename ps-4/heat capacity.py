# -*- coding: utf-8 -*-

import numpy as np
from gaussxw import gaussxw
import matplotlib.pyplot as plt


def f(x):
    return ((x**4)*np.exp(x)) / (np.exp(x) - 1)**2
    
V = 1000 * 1e-6
rho = 6.022e28
theta_D = 428
N = 50
kB = 1.3806e-23


def cv(T):
    
    const = 9*V*rho*kB
    
    a = 0
    b = (theta_D/T)
    
    x,w = gaussxw(N)
    xp = 0.5*(b-a)*x + 0.5*(b+a)
    wp = 0.5*(b-a)*w
    
    s = 0.0
    for k in range(N):
        
        s+= wp[k]*f(xp[k])
    
    return const * (T/theta_D)**3 * s


# 1b
temp = np.linspace(5, 500)
h_capacity = [cv(T) for T in temp]

plt.plot(temp, h_capacity)
plt.ylabel('Heat Capacity ($C_v$) / (J/K)')
plt.xlabel('Temperature (T) / K')
plt.title('Heat Capacity of Aluminium as a function of Temperature')
plt.savefig('heat_capacity.png')