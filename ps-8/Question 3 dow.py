# -*- coding: utf-8 -*-


#Question 3

import numpy as np
import matplotlib.pyplot as plt


dow = np.loadtxt('dow.txt')
dow_ft = np.fft.rfft(dow)

#make copies of the dow fourier transformed data
dow_copy1 = np.copy(dow_ft)
dow_copy2 = np.copy(dow_ft)


## 
dow_copy1[int(dow.size*.1):]=0  # makes the first 10 percent values zero
dow_copy2[int(dow.size*.02):]=0  # makes the frist 2 percent values zero

dow_10 = np.fft.irfft(dow_copy1)
dow_2 = np.fft.irfft(dow_copy2)


plt.plot(np.log(dow), label = 'dow')
plt.plot(np.log(abs(dow_10)), label = 'dow_10')
plt.plot(np.log(abs(dow_2)), label = 'dow_2')
plt.title('A Plot of dow, dow_10 and dow_2')
plt.legend()
plt.savefig('dows.png')