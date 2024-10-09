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


## Question 3a

t = data['time']
y = data['signal']
plt.plot(t, y, 'g.')
plt.xlabel('time (t)')
plt.ylabel('signal')
plt.title("Signal as a function of Time")
plt.savefig('signal data plot.png')
plt.show()



