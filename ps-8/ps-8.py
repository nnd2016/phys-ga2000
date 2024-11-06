# -*- coding: utf-8 -*-


# Question 1
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import pandas as pd

survey = pd.read_csv('survey.csv')
heading = list(survey.columns)
print(heading)

age = survey['age']
response = survey['recognized_it']

def p_likelihood(b, age, response):
    p = 1./(1+np.exp(-(b[0] + b[1]*age)))
    y = response
    return -np.sum(np.log(1-p)+y*np.log(p/(1-p)))

res = minimize(p_likelihood,(.1,.1), args=(age, response), options = {'disp' : True})

print(res.x)
print(res.hess_inv)
print('The error is', np.sqrt(res.hess_inv[0,0]))
