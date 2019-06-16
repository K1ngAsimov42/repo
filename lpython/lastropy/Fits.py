import numpy as np

# Set up matplotlib
import matplotlib.pyplot as plt
#matplotlib inline

from astropy.io import fits
#download the example FITS files 
from astropy.utils.data import download_file
image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True )

#Method2 of getting image data
image_data = fits.getdata(image_file)
print(type(image_data))
print(image_data.shape)

plt.imshow(image_data, cmap='gray')
plt.colorbar()
