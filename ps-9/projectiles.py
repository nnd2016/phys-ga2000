# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

g = 9.81  
C = 0.47  
rho = 1.22 
R = 0.08
a = 0
b = 10
N = 1000
A = 4 * np.pi * R**2  


def f(t, r, m):
    x, y, vx, vy = r
    v = np.sqrt(vx**2 + vy**2)
    T = (np.sqrt((rho * C * A * g)/m))
    const =  0.5 * np.pi * R**2 * rho * C * g * T**2 / m
    
    fvx = -const * vx * v
    fvy = -1 - const * vy * v
    
    return np.array([vx, vy, fvx, fvy])



def dsolve(func, r, t, h, m):
    k1 = func(t, r, m)
    k2 = func(t + h / 2, r + h * k1 / 2, m)
    k3 = func(t + h / 2, r + h * k2 / 2, m)
    k4 = func(t + h, r + h * k3, m)

    return r + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6


v0 = 100  
angle = 30  # (degrees)
masses = [0.5, 1, 1.5, 2]   
h = (b-a)/N  


def projectile(m):
    # Initial conditions
    x, y = 0, 0
    vx = v0 * np.cos(np.radians(angle))
    vy = v0 * np.sin(np.radians(angle))
    r = np.array([x, y, vx, vy])

    trajectory = []
    t = 0

    while r[1] >= 0:  # Continue until the projectile hits the ground
        trajectory.append((r[0], r[1]))
        r = dsolve(f, r, t, h, m)
        t += h

    return np.array(trajectory)

plt.figure(figsize=(10, 6))
for m in masses:
    trajectory = projectile(m)
    plt.plot(trajectory[:, 0], trajectory[:, 1], label=f"Mass = {m} kg")


plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Trajectories of Projectiles with Different Masses")
plt.ylim(0, None)
plt.legend()
plt.grid()
plt.savefig('projectiles.png')