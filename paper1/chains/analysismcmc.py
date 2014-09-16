import numpy
import pylab
def plottinghist(chain,specs,burn):
	from numpy import genfromtxt,mean,std,log,max,linspace
	from scipy.stats import gaussian_kde
	from pylab import plot,legend
	datafull = genfromtxt(chain,skip_header = burn)
	data = datafull[:,2]
	chi2 = -2.0*(max(datafull[:,0]))
	index = list(datafull[:,0]).index(-chi2/2.0)
	bestfit = datafull[index,:]
#	print mean(data),std(data),chi2,'for',chain
#	print bestfit,chain

	density = gaussian_kde(data)
#	xs = linspace(10,110,1000)
	xs = linspace(10,52,250)
	density.covariance_factor = lambda : .25
	density._compute_covariance()

#	bname = '../data/'+chain.lower().replace('chain','bestfit')
#	b = numpy.genfromtxt(bname)
#	nop = len(b)
#	print bname,nop

	plot(xs,density(xs),specs,linewidth=2.0)
#	plot(xs,density(xs),specs,\
#		label=chain+'   %1.2f'%(chi2/nop),linewidth=2.0)


burn = 3500
print '# mean, st. dev., best $\chi^2$'
plottinghist('CC2.chain','r',900)
plottinghist('DC2.chain','--r',burn)
plottinghist('GC2.chain','.-.r',burn)
plottinghist('CD2.chain','b',700)
plottinghist('DD2.chain','--b',700)
plottinghist('GD2.chain','.-.b',900)
plottinghist('CG2.chain','g',8500)
plottinghist('DG2.chain','--g',burn)
plottinghist('GG2.chain','.-.g',500)

pylab.legend(loc=9,fontsize=12)
#pylab.xlim(25,110)
pylab.xlim(10,52)
pylab.xlabel('$\mathtt{R_{p}}$',fontsize=20)
pylab.ylabel('$\mathtt{Probability\ density\ function}$',fontsize=20)
pylab.ylim(ymax=1.0)
#pylab.axvline(x=35.3553,color='b')
#pylab.axvline(x=50,color='k')
#pylab.savefig('Rhalf4all.eps')
pylab.show()
