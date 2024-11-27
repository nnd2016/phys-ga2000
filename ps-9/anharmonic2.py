# -*- coding: utf-8 -*-



 # Question 1 c plot 2
 

import numpy as np
import matplotlib.pyplot as plt


a = 0.0
b = 50.0
N = 1000
h = (b-a)/N

def f(r, t):
    x = r[0]
    v = r[1]
    fx = v
    fv = -omega**2*x**3
    return np.array([fx, fv], float)


omega = 1.0

def dsolve(x0, f):
    tpoints = np.arange(a, b, h)    ## a is the initial time and b is the final time
    xpoints = []
    vpoints = []
    r = np.array([x0, 0.0] )
    
    for t in tpoints:
        
        xpoints.append(r[0])
        vpoints.append(r[1])
        
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6
    return tpoints, xpoints
  
    

t, x = dsolve(3, f)
plt.plot(t, x,  label = 'x = 3 m')

t, x = dsolve(1, f)
plt.plot(t, x, label = 'x = 1 m')

t, x = dsolve(2, f)
plt.plot(t, x, label = 'x = 2 m')

figsize = (12, 8)
plt.xlabel("Time (t)/ s")
plt.ylabel('Position(x)/ m')
plt.title("A graph of an Anharmonic Oscillator with larger varying Amplitudes")
plt.grid()
plt.legend()
plt.xlim(0, 50)
plt.savefig('anharmonic2.png')



