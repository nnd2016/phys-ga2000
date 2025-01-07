import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brent


def func(x):
    return np.power((x-0.3), 2) * np.exp(x)


# Plot of the function
x = np.linspace(-1, 1, 100)
plt.plot(x, func(x), 'm')
plt.xlabel('x')
plt.ylabel('func(x)')
plt.grid()
plt.title('A Plot of func(x) against x')
plt.show()


def golden(func=None, a=None, b=None, c=None, tol=1.e-5):
    gsection = (3. - np.sqrt(5)) / 2     #golden ratio
    
    while(np.abs(c - a) > tol):
        
        if((b - a) > (c - b)):
            x = b
            b = b - gsection * (b - a)
        else:
            x = b + gsection * (c - b)
        step = np.array([b, x])
        fb = func(b)
        fx = func(x)
        if(fb < fx):
            c = x
        else:
            a = b
            b = x 
        return brent1D(func, a, b, c, tol)   



def brent1D(func = None, a = None, b=None, c = None, tol=1.e-5):
     
        fa = func(a)
        fb = func(b)
        fc = func(c)
        denom = (b - a) * (fb - fc) - (b -c) * (fb - fa)
        numer = (b - a)**2 * (fb - fc) - (b -c)**2 * (fb - fa)
        minim = b - 0.5 * numer / denom


        x = [a, b, c]
        fx = np.argsort([fa, fb, fc])

        if np.abs(x[fx[0]]-minim) <= tol:
            return minim
        elif minim < np.min(x):
            return golden(func, minim, b, c, 0.001)
        elif minim > np.max(x):
            return golden (func, a, b, minim, 0.001)
        else:
            return brent1D(func, x[0], minim, x[1], 0.001)
        
    
        

myBrentval = brent1D(func, 0, 0.5, 1, 0.001)
print("The minimum using my Brent's Method is at x = ", myBrentval)

sci_brent = brent(func, brack = (0, 0.5, 1))
print("The minimum using Scipy's Brent's Method is at x =", sci_brent)

print('The difference between the two values is ', np.abs(myBrentval-sci_brent))