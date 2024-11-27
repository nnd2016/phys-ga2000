# -*- coding: utf-8 -*-


# Question 1 e

import numpy as np
import matplotlib.pyplot as plt



def f(r, t):
    x = r[0]
    v = r[1]
    fx = v
    fv = mu*(1-x**2)*v - omega**2*x
    return np.array([fx, fv], float)


def dsolve(a, b, N, r, f):
    
    tpoints = np.arange(a, b, h)      ## a is the initial time and b is the final time                       
    xpoints = []
    vpoints = []


    for t in tpoints:
        xpoints.append(r[0])
        vpoints.append(r[1])
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6    

    return tpoints, xpoints, vpoints

r = np.array([1.0, 0.0], float)


a = 0.0
b = 20.0
N = 2000
h = (b-a)/N
omega = 1


mu = 1
tp, xp, vp = dsolve(a, b, N, r, f)
plt.plot(xp, vp, label = r'$\mu = 1$')

mu = 2
tp, xp, vp = dsolve(a, b, N, r, f)
plt.plot(xp, vp, label = r'$\mu = 2$')

mu = 4
tp, xp, vp = dsolve(a, b, N, r, f)
plt.plot(xp, vp, label = r'$\mu = 4$')

plt.xlabel('Position (x)/m')
plt.ylabel(r'$Velocity (v)/ ms^{-1}$')
plt.title('Phase Space of the Van der Pol Oscillator')
plt.legend()
plt.grid()
plt.savefig('vanderpol.png')
