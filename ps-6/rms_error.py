# -*- coding: utf-8 -*-

import numpy as np
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



error_list = []
NC = list(range(1, 21))

for nc in NC:
    basis = eig_vectors_svd[:, :nc]
    reduced = np.dot(basis.T, flux_res.T)
    recon_res = (np.dot(basis, reduced)).T  # reconstituted residuals 
    recons = (means[:, np.newaxis]+recon_res)*norms[:,np.newaxis]
    error = np.sqrt(np.mean(np.square(recons - flux)))  # rms error
    error_list.append(error)


plt.plot(NC, error_list, 'DarkMagenta')
plt.xlabel(r"$N_{c}$")
plt.title(r'A Plot of the root mean squared error against $N_{c}$ from 1 to 20')
plt.ylabel('rms')
plt.grid()
plt.savefig('rms_vs_nc.png')


