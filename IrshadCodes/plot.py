import numpy
import pylab

data = numpy.genfromtxt('data_crescent_reverse_noise.txt')
fit = numpy.genfromtxt('fort.11')


pylab.errorbar(data[:,0],data[:,1],data[:,1]*0.1)
pylab.plot(fit[:,0],fit[:,1],'r')

pylab.xlim(-800,-600)

pylab.show()
