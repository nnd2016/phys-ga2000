# -*- coding: utf-8 -*-


import numpy as np
import timeit
from astropy.io import fits
import matplotlib.pyplot as plt

hdu_list = fits.open('specgrid.fits')
logwave = hdu_list['LOGWAVE'].data
flux = hdu_list['FLUX'].data


norms = np.sum(flux, axis = 1)      # sum up the flux for normalization   
flux_norm = flux/norms[:, np.newaxis]   # normalized flux

wavelength = (np.power(10, logwave))/10   # convert logwave to wavelength in nm

means = np.mean(flux_norm, axis = 1)    # mean spectrum
flux_res = flux_norm - means[:, np.newaxis]  # flux residual


cov = np.dot(flux_res, flux_res.T)     # covariance matrix



# function using covariance matrix
def eigen_cov(A):
    eig_values_cov, eig_vectors_cov = np.linalg.eigh(A)
    idx = np.argsort(eig_values_cov)[::-1]
    eig_values_cov = eig_values_cov[idx]
    eig_vectors_cov = eig_vectors_cov[idx]
    return eig_values_cov, eig_vectors_cov


eig_values_cov, eig_vectors_cov = eigen_cov(cov)


# Makes a plot of the first 5 eigenvectors
for i in range(5):
    plt.plot(eig_vectors_cov[:, i], label = f'Eigenvector {i+1}')
    
plt.xlabel('Wavelength')
plt.ylabel('Eigenvector')
plt.title('Plot of the First Five Eigenvectors')
plt.legend()
plt.grid()
plt.savefig('eigenvector_plots.png')



# t_cov = timeit.timeit('eigen_cov(cov), globals = globals(), number = 2')


# print(f'It took {t_cov} seconds to perform the covariance computation')

print(' ')
w_C = np.max((eig_values_cov))/np.min((eig_values_cov)) # The condition number
print(f'The condition number of C is {w_C}')
