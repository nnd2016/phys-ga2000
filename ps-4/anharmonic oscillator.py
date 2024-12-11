# -*- coding: utf-8 -*-

import numpy as np
from gaussxw import gaussxw
import matplotlib.pyplot as plt

N = 20
m = 1

def f(a, x):
    const = (8*m)**0.5
    return const/((a**4- x**4)**0.5)


def T(a):
    A = 0
    B = a
    
    x,w = gaussxw(N)
    xp = 0.5*(B - A)*x + 0.5*(B + A)
    wp = 0.5*(B - A)*w
    
    s = 0.0
    for k in range(N):
        s += wp[k]*f(a, xp[k])
    
    return s


amps = np.linspace(0, 2, N)
K = [T(a) for a in amps]

    
plt.plot(amps, K, 'b^', mec = 'k')
plt.xlabel('Amplitude (a)/ m')
plt.ylabel('Period (T)/ s')
plt.title('A Graph of Period against Amplitude')
plt.grid()
plt.savefig('anharmonic period.png')    

