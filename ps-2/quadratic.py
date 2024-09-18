# -*- coding: utf-8 -*-
# Question 5
import numpy as np

# a code for +/- and -/+
pm = np.array([+1, -1])    # plus or minus
mp = np.array ([-1, +1])    # minus or plus


#The solutions to the equation
def quadratic(a, b, c):
    x1, x2 = (-b + pm * (b**2 - 4 * a * c) ** 0.5) / (2 * a)  # For the standard equation solution
    x_1n, x_2n = 2 * c / (-b + mp*( b ** 2 - 4*a*c) ** 0.5)  # For the other equation solution
    return x1, x2, x_1n, x_2n

# Inputs for a, b, and c
a = float(input('Enter the number a: '))
b = float(input('Enter the number b: '))
c = float(input('Enter the number c: '))

x1, x2, x_1n, x_2n = quadratic(a, b, c)

print('The roots of the equation are x1 =', x1, 'and x2 =', x2)
print('The roots of the equation are x_1n = ', x_1n,'and x_2n = ', x_2n)

