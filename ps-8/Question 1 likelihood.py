# -*- coding: utf-8 -*-


# Question 1
import numpy as np
from scipy.optimize import minimize
import pandas as pd
import matplotlib.pyplot as plt

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


b = res.x
print('The covariance matrix is', res.hess_inv)
print('The error is', np.sqrt(res.hess_inv[0,0]))

def p(b, age):
    return 1./(1+np.exp(-(b[0] + b[1]*age)))


plt.plot(age, p(b, age), 'ko', label = 'Logistic Function')
plt.plot(age, response, 'ro', label = 'Actual Response')
plt.title('A Graph of the Logistic Function and Response against Age')
plt.xlabel('Age (years)')
plt.ylabel('p(age)')
plt.legend()
plt.savefig('Likelihood.png')


