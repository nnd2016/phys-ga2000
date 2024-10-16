# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
from astropy.io import fits
import numpy as np


hdu_list = fits.open('specgrid.fits')
logwave = hdu_list['LOGWAVE'].data
flux = hdu_list['FLUX'].data



# Question 1


# Make figure and axes
num_plots = 4    # the number of galaxies to be plotted
fig, axs = plt.subplots(num_plots, figsize = (12, 12))
fig.subplots_adjust(hspace = 0.4)
fig.suptitle(f'Plots of the Spectra of the First {num_plots} Galaxies', fontsize = 18, y = 0.95)

h = list(range(num_plots))


col = [ 'tab:cyan', 'mediumseagreen', 'tab:olive', 'Teal',  'aquamarine']

wavelength = (np.power(10, logwave))/10   # converts logwave to wavelength in nm

for i in h:
    axs[i].plot(wavelength, flux[i], color = col[i])
    axs[i].set_title(f'Galaxy {i+1}')
    axs[i].grid()
    

fig.supylabel(r'$Flux (10^{-17} erg s^{-1} cm^{-2} \AA^{-1}$)')
plt.xlabel('Wavelength (nm)')
plt.savefig('galaxy_plots.png')


