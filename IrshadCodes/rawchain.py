import numpy
import pylab

filename = 'fort.78612'
data = numpy.genfromtxt(filename)

p1 = 3
p2 = -3

if p2<0:
	pylab.hist(data[:,p1],len(data)/20)
else:
	pylab.plot(data[:,p1],data[:,p2],'g',lw=2,ms=14)

pylab.show()
