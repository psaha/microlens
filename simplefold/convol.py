# FT of 1/sqrt(x) for x > 0  (Just to see how it looks)

from numpy import pi, arange, sign
from pylab import plot, show
from numpy.fft import fft,fftshift,ifftshift

N = 2**9
R = (pi*N/2)**.5
step = 2*R/N
step = 0.01
x = (arange(N)-N/2)*step
k = 2*pi/N*(arange(N)-N/2)/step

theta = (1+sign(x))/2
theta[N/2] = 0
f = theta/(abs(x)**.5+1e-16)

F = ifftshift(fft(fftshift(f)))

plot(k,F.real)
plot(k,F.imag)
show()

