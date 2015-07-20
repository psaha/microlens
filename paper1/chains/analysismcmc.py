import numpy
import pylab

from circles import Rhalf
pylab.figure(figsize=(8.7,7))

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
	xs = linspace(10,120,500)
	density.covariance_factor = lambda : .25
	density._compute_covariance()

	bname = '../data/'+chain.lower().replace('chain','bestfit')
	b = numpy.genfromtxt(bname)
	nop = len(b)
#	print bname,nop

#	plot(xs,density(xs),specs,linewidth=2.0)
	plot(xs,density(xs),specs,\
		label=chain+'   %1.2f'%(chi2/nop),linewidth=2.0)



burn = 3500
print '# mean, st. dev., best $\chi^2$'
plottinghist('CC.chain','r',900)
plottinghist('DC.chain','--r',burn)
plottinghist('GC.chain',':r',burn)
plottinghist('CD.chain','b',700)
plottinghist('DD.chain','--b',700)
plottinghist('GD.chain',':b',900)
plottinghist('CG.chain','g',8500)
plottinghist('DG.chain','--g',burn)
plottinghist('GG.chain',':g',500)

#pylab.axvline(x=Rhalf(50.0,30.0,15.0,10.0),color='r',ls='-.',lw=2)
#pylab.axvline(x=50.0/2.0**0.5,color='b',ls='-.',lw=2)
#pylab.axvline(x=numpy.log(4.0)**0.5*50.0/3.0,color='g',ls='-.',lw=2)

pylab.legend(loc=9,fontsize=12)
pylab.xlim(25,102)
#pylab.xlim(15,50)
pylab.xlabel('$\mathrm{R_{p}}$',fontsize=20)
pylab.ylabel('$\mathrm{Probability\ density\ function}$',fontsize=20)
pylab.ylim(ymax=1.0)
pylab.axvline(x=50,color='k',ls='-.',lw=2)
pylab.savefig('Rp4all.eps')

pylab.tick_params(axis='both', which='major', labelsize=20)
pylab.tick_params(axis='both', which='minor', labelsize=20)
pylab.show()
