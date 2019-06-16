import numpy as np

# Set up matplotlib
import matplotlib.pyplot as plt
#matplotlib inline

from astropy.io import fits
#download the example FITS files 
from astropy.utils.data import download_file
#image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True )
'''
#Method1 of getting image data
#image_file = C:\Users\manoj\.astropy\cache\download\py3\2c9202ae878ecfcb60878ceb63837f5f#didn't work
#image_file = "C:\Users\manoj\.astropy\cache\download\py3\2c9202ae878ecfcb60878ceb63837f5f" #didn't work
hdu_list = fits.open(image_file)
hdu_list.info()

image_data = hdu_list[0].data

print(type(image_data))
print(image_data.shape)

hdu_list.close()
'''

#Method2 of getting image data
image_data = fits.getdata(image_file)
print(type(image_data))
print(image_data.shape)

plt.imshow(image_data, cmap='gray')
plt.colorbar()
