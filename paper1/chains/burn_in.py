import numpy
import pylab

chain = ['CC','CD','CG','DC','DD','DG','GC','GD','GG']
spec = ['r','b','g','k','m','g','k','y','c']
for i in range(9):
	data = numpy.genfromtxt('%s.chain'%chain[i])
	x = numpy.linspace(1,len(data)+1,len(data))
	pylab.plot(x,-2.0*data[:,0],spec[i],label=chain[i])
pylab.legend(loc=1,fontsize=12)
pylab.show()