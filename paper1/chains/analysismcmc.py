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
	xs = linspace(10,110,1000)
#	xs = linspace(10,52,250)
	density.covariance_factor = lambda : .25
	density._compute_covariance()

	bname = '../data/'+chain.lower().replace('chain','bestfit')
	b = numpy.genfromtxt(bname)
	nop = len(b)
	print bname,nop

	plot(xs,density(xs),specs,\
		label=chain+'   %1.2f'%(chi2/nop),linewidth=2.0)

burn = 3500
print '# mean, st. dev., best $\chi^2$'
plottinghist('CC.chain','r',900)
plottinghist('DC.chain','b',burn)
plottinghist('GC.chain','g',burn)
plottinghist('CD.chain','--r',700)
plottinghist('DD.chain','--b',700)
plottinghist('GD.chain','--g',900)
plottinghist('CG.chain','.-.r',8500)
plottinghist('DG.chain','.-.b',burn)
plottinghist('GG.chain','.-.g',500)

pylab.legend(loc=9,fontsize=12)
pylab.xlim(25,110)
#pylab.xlim(10,52)
pylab.xlabel('$\mathtt{R_{p}}$',fontsize=20)
pylab.ylabel('$\mathtt{Probability\ density\ function}$',fontsize=20)
pylab.ylim(ymax=1.0)

pylab.savefig('Rp4all.eps')
pylab.show()
