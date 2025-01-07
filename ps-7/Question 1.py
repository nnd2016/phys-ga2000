## Question 1

import numpy as np
from jax import grad
import matplotlib.pyplot as plt



## Constants and Parameters
m_earth = 5.974*10**24
m_moon = 7.384 * 10**22
m_sun = 1.988*10**30
m_jupiter = 1.898*10**27

r_moon = 3.844*10**8
r_earth = 1.496*10**11

m_em = m_moon/m_earth
m_es = m_earth/m_sun
m_js = m_jupiter/m_sun


# Function
def f(r, m):
    return m/((1-r)**2) + r - 1/(r**2)


# Plot of the Earth-Moon System function
x = np.linspace(0, 1, 100)
plt.plot(x, f(x, m_em))
plt.xlabel("r'")
plt.ylabel("f(r')")
plt.title("A Plot of f(r') against r'")
plt.grid()
plt.show()



f_prime = grad(f)  # derivative of the function


# Newton's Method
def newton_method(r, m, tol = 0.001):
    if np.absolute(f(r, m)) < tol:
        return r
    else:
        return newton_method(r - f(r,m)/f_prime(r,m), m, tol)
    

lp_em = newton_method(0.0001, m_em, tol=0.001) # Earth-Moon
lp_se = newton_method(0.0001, m_es, tol=0.001)  # Sun-Earth
lp_sj = newton_method(0.0001, m_js, tol=0.001)   # Sun-Jupiter


print('The Lagrange Point for the Earth-Moon system is ', r_moon*lp_em)
print('The Lagrange Point for the Sun-Earth system is ', r_earth*lp_se)
print('The Lagrange Point for the Sun-Jupiter system is ', r_moon*lp_sj)   

