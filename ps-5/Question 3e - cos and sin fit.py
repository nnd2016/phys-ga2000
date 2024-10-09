# -*- coding: utf-8 -*-
# import modules
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


max = 31
T = (np.max(tp)-np.min(tp))/2


A = np.zeros((len(tp), max))
A[:, 0] = 1

for i in range(1, max, 2):
    A[:, i] = np.cos(2*np.pi*(i+1)/2*tp/T)
    A[:, i+1] = np.sin(2*np.pi*(i+1)/2*tp/T)
    
    
(u, w, vt) = np.linalg.svd(A, full_matrices=False)
print('The singular values are ', w)

print('')


ainv = vt.transpose().dot(np.diag(1. / w)).dot(u.transpose())
c = ainv.dot(y)


ym = A.dot(c)

print('The condition number is', np.max(w)/np.min(w))

plt.plot(t, y, '.', label='data')
plt.plot(t, ym, 'k.', label='model')
plt.xlabel('time (t)')
plt.ylabel('signal')
plt.legend()
plt.title('Harmonic Sequence Fit')
plt.savefig('harmonic sequence fit.png')