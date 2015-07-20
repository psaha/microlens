import numpy
import pylab

pylab.figure(figsize=(8.7,7))


chain = ['CC','CD','CG','DC','DD','DG','GC','GD','GG']
chain = ['CG']
spec = ['k','b','g','k','m','g','k','y','c']
for i in range(len(chain)):
	data = numpy.genfromtxt('%s.chain'%chain[i])
	x = numpy.linspace(1,len(data)+1,len(data))
	pylab.semilogx(x,-2.0*data[:,0],spec[i],label='$\mathrm{CrescentFit\ to\ GaussianDiskData}$')
pylab.xlabel('$\mathrm{Number\ of\ MCMC\ steps}$',fontsize=22)
pylab.ylabel('$\mathrm{\chi^2}$',fontsize=22)
pylab.xlim(min(x),max(x))
pylab.legend(loc=3,fontsize=20)
pylab.tick_params(axis='both', which='major', labelsize=20)
pylab.tick_params(axis='both', which='minor', labelsize=20)
pylab.savefig('burnin_cg.eps')
pylab.show()