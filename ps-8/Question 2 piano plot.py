# -*- coding: utf-8 -*-
## Question 2

## Piano data plot

import numpy as np
import matplotlib.pyplot as plt


piano_data = np.loadtxt('piano.txt')
plt.plot(piano_data, color = 'magenta')
plt.xlabel('Time (s)')
plt.title('Piano Sound Plot')
plt.savefig('piano.png')

