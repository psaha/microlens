import numpy
import pylab
def plottinghist(chain,specs):
	from numpy import genfromtxt,mean,std,log,max,linspace
	from scipy.stats import gaussian_kde
	from pylab import plot,legend
	datafull = genfromtxt(chain,skip_header = 1000)
	data = datafull[:,2]
	chi2 = -2.0*log(max(datafull[:,0]))
	print
	print mean(data),std(data),chi2,'for',chain
	density = gaussian_kde(data)
	xs = linspace(10,65,1000)
	density.covariance_factor = lambda : .25
	density._compute_covariance()
	plot(xs,density(xs),specs,label=chain+'   %1.2f'%chi2,linewidth=2.0)


print '# mean, st. dev., best $\chi^2$'
plottinghist('cc2.chain','r')
plottinghist('dc2.chain','--r')
plottinghist('gc2.chain','.-.r')
plottinghist('cd2.chain','b')
plottinghist('dd2.chain','--b')
plottinghist('gd2.chain','.-.b')
plottinghist('cg2.chain','g')
plottinghist('dg2.chain','--g')
plottinghist('gg2.chain','.-.g')

pylab.legend(loc='upper center')
pylab.xlim(10,65)
pylab.xlabel('$\mathtt{R_{1/2}}$',fontsize=24)


pylab.savefig('Rhalf4all.eps')
pylab.show()
