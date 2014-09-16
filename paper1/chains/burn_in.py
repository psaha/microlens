import numpy
import pylab

chain = ['CC','CD','CG','DC','DD','DG','GC','GD','GG']
chain = ['CG']
spec = ['k','b','g','k','m','g','k','y','c']
for i in range(len(chain)):
	data = numpy.genfromtxt('%s.chain'%chain[i])
	x = numpy.linspace(1,len(data)+1,len(data))
	pylab.semilogx(x,-2.0*data[:,0],spec[i],label='$\mathtt{CrescentFit\ to\ GaussianDiskData}$')
pylab.xlabel('$\mathtt{Number\ of\ MCMC\ steps}$',fontsize=22)
pylab.ylabel('$\mathtt{\chi^2}$',fontsize=22)
pylab.xlim(min(x),max(x))
pylab.legend(loc=3,fontsize=20)
pylab.savefig('burnin_cg.eps')
pylab.show()