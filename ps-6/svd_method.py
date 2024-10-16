# -*- coding: utf-8 -*-


import numpy as np
import timeit
from astropy.io import fits
import matplotlib.pyplot as plt

# loads the data
hdu_list = fits.open('specgrid.fits')
logwave = hdu_list['LOGWAVE'].data
flux = hdu_list['FLUX'].data


# Rescaling of flux
norms = np.sum(flux, axis = 1)      # sum up the flux for normalization   
flux_norm = flux/norms[:, np.newaxis]   # normalized flux

wavelength = (np.power(10, logwave))/10  # convert logwave to wavelength in nm

means = np.mean(flux_norm, axis = 1)    # mean spectrum
flux_res = flux_norm - means[:, np.newaxis]  # flux residual



# function using svd
def eigen_svd(A):
    u, w, vT = np.linalg.svd(A)
    eig_values_svd = w**2
    eig_vectors_svd = vT.T
    return eig_values_svd, eig_vectors_svd

eig_values_svd, eig_vectors_svd = eigen_svd(flux_res)



w_R = np.max((eig_values_svd))/np.min((eig_values_svd)) # The condition number
print(f'The condition number of C is {w_R}')
print(' ')
# t_svd = timeit.timeit('eigen_svd(flux_res), globals = globals(), number = 2')

# print(f'It took {t_svd} seconds to perform the svd computation')





# A Subplot of c0 against c1 and c2
nc = 5
basis = eig_vectors_svd[:, :nc] 
recon = np.dot(flux_res[:nc].T, basis.T)

fig, axs = plt.subplots(2)
axs[0].plot(recon[1],recon[0], 'k.')
axs[0].set_xlabel(r'$c_{1}$')
axs[0].grid()

axs[1].plot( recon[2], recon[0], 'g.')
axs[1].set_xlabel(r'$c_{2}$')
axs[1].grid()

fig.supylabel(r'$c_{0}$')
fig.suptitle(r'Plots of $c_{0}$ against $c_{1}$ and $c_{2}$')
plt.savefig('c0_vs_c1_and_c2.png')



