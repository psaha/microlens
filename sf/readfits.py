import numpy as np
import matplotlib.pyplot as pl
from astropy.io import fits

hdul = fits.open('IRIS406.fits')
im = hdul[0].data
print(im.shape)
mag = (1024-im)/256
x = 10**(-mag/2.5)
pl.imshow(np.log(x))
pl.show()