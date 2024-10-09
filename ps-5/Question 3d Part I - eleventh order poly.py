# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_path = 'signal.dat'
data = pd.read_csv(data_path, sep = '\s+', header = 0)
data = pd.DataFrame(data)

column_names = list(data.columns)
print(column_names)

t = data['time']
y = data['signal']

std = 2.                      # standard deviation
tp = (t - t.mean())/std                # rescaling of the time values



poly_order_high = 11                     # order of the polynomial
A = np.zeros((len(tp), poly_order_high + 1))  # the design matrix 
A[:, 0]= 1

for i in range(1, poly_order_high + 1):
    A[:, i] = tp**i



(u, w, vt) = np.linalg.svd(A, full_matrices=False)
print('The singular values are ', w)




ainv = vt.transpose().dot(np.diag(1. / w)).dot(u.transpose())
c = ainv.dot(y)
ym = A.dot(c)

print('')
print('The condition number is', np.max(w)/np.min(w))

plt.plot(t, y, '.', label='data')
plt.plot(t, ym, 'k.', label='model')
plt.xlabel('time (t)')
plt.ylabel('signal')
plt.title('Eleventh Order Polynomial Fit')
plt.legend()
plt.savefig('eleventh order polynomial.png')

