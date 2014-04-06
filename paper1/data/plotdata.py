import numpy
import pylab
from matplotlib import pyplot as pl

cr = numpy.genfromtxt('data_crescent_reverse_corr.txt')
dr = numpy.genfromtxt('data_disk_reverse_corr.txt')
gr = numpy.genfromtxt('data_gauss_reverse_corr.txt')

err = 0.05
low = 1-err
high= 1+err

pylab.plot(cr[:,0]+800,cr[:,1],'r',label='Crescent')
pylab.fill_between(cr[:,0]+800,cr[:,1]*low,cr[:,1]*high,\
		alpha=0.5,facecolor='r',edgecolor=None,interpolate=True)

pylab.plot(dr[:,0]+800,dr[:,1],'b',label='Uniform Disk')
pylab.fill_between(dr[:,0]+800,dr[:,1]*low,dr[:,1]*high,\
		alpha=0.5,facecolor='b',edgecolor=None,interpolate=True)

pylab.plot(gr[:,0]+800,gr[:,1],'g',label='Gaussian Disk')
pylab.fill_between(gr[:,0]+800,gr[:,1]*low,gr[:,1]*high,\
		alpha=0.5,facecolor='g',edgecolor=None,interpolate=True)

pylab.legend(loc=2)
pylab.xlim(0,200)
pylab.xlabel('Time')
pylab.ylabel('Brightness')
pylab.savefig('data_with_error.eps')
pylab.show()
