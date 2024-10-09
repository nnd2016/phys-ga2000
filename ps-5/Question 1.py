# -*- coding: utf-8 -*-

# import modules
import numpy as np
import matplotlib.pyplot as plt


h = 0.01
xs = np.linspace(-2, 2, 100)

def f(x):
    return  (1 + ((1/2) * np.math.tanh(2*x)))

# numeric solution
nlist = []

for x in xs:
    dfdx = (f(x + h) - f(x - h))/(2*h)  # gradient using central difference
    nlist.append(dfdx)
        
    

# analytic solution    
def analytic(x):
    return 1 - (np.math.tanh(2*x))**2

alist = []
for x in xs:
    alist.append(analytic(x))
    
    
plt.plot(xs, alist, 'k', label = 'analytic')
plt.plot(xs, nlist, 'm.', label = 'numeric')
plt.title('Gradient of Analytical & Numerical Gradient of $f(x) = 1 + (1/2)tanh2x$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()

plt.savefig('analytic vs numeric.png')


