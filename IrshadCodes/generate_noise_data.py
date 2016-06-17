import numpy
import pylab

sigma = 0.1
filename = 'data_crescent_corr.txt'
x = numpy.genfromtxt(filename)
noise = numpy.random.normal(0,sigma,len(x[:,1])) * x[:,1]

pylab.plot(x[:,0],x[:,1],'b')
pylab.plot(x[:,0],x[:,1]+noise,'g')
pylab.xlim(-800,-600)
y = numpy.transpose([x[:,0],x[:,1]+noise])
print numpy.shape(y),numpy.shape(x),filename.replace('corr','noise')
numpy.savetxt(filename.replace('corr','noise'),y)

pylab.show()
