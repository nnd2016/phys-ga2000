# -*- coding: utf-8 -*-
  

import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxw

# Question 2a
def integrand(a, x):
    return x**(a-1) * np.exp(-x)

alist = [2, 3, 4]
xlist = np.linspace(0, 5)


for a in alist:
    integrand_vals = integrand(a,xlist)    
    plt.plot(xlist, integrand_vals, label = f' a = {a}' )
    
plt.legend()   
plt.xlabel('x')
plt.xlim(0, 5)
plt.ylabel('y')
plt.title(r'Plot of y = $x^{a-1} e^{-x}$ for a = 2, 3, and 4')
plt.grid()
plt.savefig('gamma_integrand.png')
        



# Question 2d, e
def gamma(a):
   
    d = 0.0  # lower integral limit
    e = 1.0   # upper integral limit
    N = 100

    def integrand_mod(a, x):                            # modified integrand
        return np.exp((a-1)*np.log(x)) * np.exp(-x)

    def f(z):
        c = a-1                                # value of c for here to be 
                                              # a maximum at z = 1/2
        dxdz = c /(1 - z)**2  
        gaussfunc = integrand_mod(a, (z*c)/(1 - z))
        return dxdz * gaussfunc

    x, w = gaussxw(N)
    xp = 0.5*(e-d)*x + 0.5*(e+d)
    wp = 0.5*(e-d)*w
    
    s = 0
    for k in range(N):
        s += wp[k]*f(xp[k])
    
    return s                  

print('gamma(3/2) =', gamma(3/2))




# Question 2f
gamma_int_list = [3,6,10]
for i in gamma_int_list:
    print(f'gamma({i}) =', gamma(i))