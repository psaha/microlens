import numpy as np
import matplotlib.pyplot as pl
from astropy.io import fits

hdul = fits.open('IRIS406.fits')
im = hdul[0].data
print(im.shape)
mag = (1024-im)/256
m = 10**(-mag/2.5)


x = np.linspace(-1,1,30)
x,y = np.meshgrid(x,x)
s = 0*x
s[x*x+y*y < 1] = 1
s[x**2 + (y-.5)**2 < .25] = 0

lx = 420
ly = 400

total = np.sum(m[lx:lx+30,ly:ly+30]*s[:,:])

m[lx:lx+30,ly:ly+30] = s[:,:]*100

print(total)

pl.imshow(m)
pl.show()