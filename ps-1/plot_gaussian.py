# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 19:49:51 2024

@author: User
"""

# importing libraries
import numpy as np
import matplotlib.pyplot as plt

# defines normal distribution function
def normal_distr(sigma, mu, x):
    gauss_points = (1 / sigma * (2 * np.pi) ** 1/2) * np.exp(- 1/2 * ((x - mu)/sigma) ** 2)
    return gauss_points

sigma = 3                          # standard deviation value of 3
mu = 0                             # mean value of 0

x = np.linspace(-10, 10)         # generates x values ranging from -10 to +10
plt.plot(x, normal_distr(sigma, mu, x), 'gold')
plt.xlabel('x-axis')
plt.ylabel('y-axis')                            
plt.savefig('gaussian.png')                      # saves figure as a PNG file
