# Set up matplotlib
import matplotlib.pyplot as plt
#%matplotlib inline
#import tarfile
#from astropy.utils.data import download_file
#url = 'http://data.astropy.org/tutorials/UVES/data_UVES.tar.gz'
#f = tarfile.open(download_file(url, cache=True), mode='r|*')
working_dir_path = '.'  # CHANGE TO WHEREVER YOU WANT THE DATA TO BE EXTRACTED
#f.extractall(path=working_dir_path)

from glob import glob
import os

import numpy as np

from astropy.wcs import WCS
from astropy.io import fits

# os.path.join is a platform-independent way to join two directories
globpath = os.path.join(working_dir_path, 'UVES/*.fits')

print(globpath)
# glob searches through directories similar to the Unix shell
filelist = glob(globpath)
print("Number of files =",len(filelist))
# sort alphabetically - given the way the filenames are
# this also sorts in time
filelist.sort()

sp = fits.open(filelist[0])
print("Printing info")
sp.info()

header = sp[0].header

wcs = WCS(header)
#make index array
index = np.arange(header['NAXIS1'])

wavelength = wcs.wcs_pix2world(index[:,np.newaxis], 0)
wavelength.shape
#Ahh, this has the wrong dimension. So we flatten it.
wavelength = wavelength.flatten()
print("wavelength array size=",len(wavelength))
flux = sp[0].data

print("flux=",flux)

def read_spec(filename):
    '''Read a UVES spectrum from the ESO pipeline

    Parameters
    ----------
    filename : string
    name of the fits file with the data

    Returns
    -------
    wavelength : np.ndarray
    wavelength (in Ang)
    flux : np.ndarray
    flux (in erg/s/cm**2)
    date_obs : string
    time of observation
    '''
    sp = fits.open(filename)
    header = sp[0].header

    wcs = WCS(header)
    #make index array
    index = np.arange(header['NAXIS1'])

    wavelength = wcs.wcs_pix2world(index[:,np.newaxis], 0)
    wavelength = wavelength.flatten()
    flux = sp[0].data

    date_obs = header['Date-OBS']
    return wavelength, flux, date_obs

def read_setup(filename):
    '''Get setup for UVES spectrum from the ESO pipeline

    Parameters
    ----------
    filename : string
    name of the fits file with the data

    Returns
    -------
    exposure_time : float
    wavelength_zero_point : float
    optical_arm : string
    '''
    sp = fits.open(filelist[0])
    header = sp[0].header

    return header['EXPTIME'], header['CRVAL1'], header['HIERARCH ESO INS PATH']

# Let's just print the setup on the screen
# We'll see if it's all the same.
for f in filelist:
    print(read_setup(f))

#####use of read_spec##########################
flux = np.zeros((len(filelist), len(wavelength)))
# date comes as string with 23 characters (dtype = 'S23')
date = np.zeros((len(filelist)), dtype = 'U23')

for i, fname in enumerate(filelist):
    w, f, date_obs = read_spec(fname)
    flux[i,:] = f
    date[i] = date_obs
    