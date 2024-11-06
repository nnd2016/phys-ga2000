# -*- coding: utf-8 -*-


## Question 2


import numpy as np
import matplotlib.pyplot as plt



#piano data
piano_data = np.loadtxt('piano.txt')

#trumpet data
trumpet_data = np.loadtxt('trumpet.txt')



piano_ft = np.fft.rfft(piano_data)
trumpet_ft = np.fft.rfft(trumpet_data)

# unscaled graph
# plt.plot(abs(piano_ft), linewidth = 0.9, color = 'darkslateblue', label = 'piano')
# plt.plot(abs(trumpet_ft), linewidth = 0.4, color = 'indianred', label = 'trumpet')
# plt.legend()
# plt.xlim([0, 10000])


#log graph
plt.plot(np.log(abs(piano_ft)), linewidth = 0.9, color = 'k', label = 'piano')
plt.plot(np.log(abs(trumpet_ft)), linewidth = 0.4, color = 'mediumvioletred', label = 'trumpet')
plt.legend()
plt.title('A Graph of Piano and Trumpet FFT')
plt.xlabel('Frequency (Hz)')
plt.xlim([0, 10000])
plt.ylim([5, 19])
plt.savefig('piano_trumpet_ft.png')