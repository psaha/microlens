import numpy as np
import lcurv
import sys

from mcmc import MCMC

class run(MCMC):
	def __init__(self, NP, means, mins, maxs, sds, outfile, errlev=0.1, goodchi2=350.0):
		"""
		Instantiates the class by synthetically generating data.
		"""
		MCMC.__init__(self, TargetAcceptedPoints=1000, NumberOfParams=NP, Mins=mins, Maxs=maxs, SDs=sds, \
			write2file=True, outputfilename=outfile, alpha=0.1, debug=False,\
                                EstimateCovariance=True, CovNum=100, goodchi2=goodchi2)
		lcurv.readmap()
		lcurv.mockdata(means,errlev)

	def chisquare(self, Params):
		return lcurv.chis(Params)

#==========================================

if __name__=="__main__":

	fname = sys.argv[1]

	Rp = 39.4
	sig = 20/(np.log(4))**.5
	Rn,a,b = 0.4, 0, 0.3

	pars = [51,290]
	if fname[-7:] == 'forward':
		mins = [1,250]
		maxs = [100,350]
	elif fname[-8:] == 'backward':
		mins = [700,450]
		maxs = [800,550]
	else:
		print('Filename error')
		sys.exit()
	if fname[1] == 'c':
		pars += [ 1.0, Rp,  Rn, a, b ]
	elif fname[1] == 'g':
		pars += [ 1.0, sig, -2, 0, 0 ]
	else:
		print('Filename error')
		sys.exit()
	if fname[0] == 'c':
		mins += [ 0.5,   1,  0, -1, -1 ]
		maxs += [ 2.5, 100,  1,  1,  1 ]
	elif fname[0] == 'g':
		mins += [ 0.5,   1, -3, -1, -1 ]
		maxs += [ 2.5, 100, -1,  1,  1 ]
	else:
		print('Filename error')
		sys.exit()

	pars = np.array(pars)
	mins = np.array(mins)
	maxs = np.array(maxs)
	sds = np.array([5, 5, 0.01, 0.5, 0.1, 0.5, 0.5])
	print(pars)
	print(mins)
	print(maxs)
	obj = run(7, pars, mins, maxs, sds, fname+'.chain',
                  errlev=0.04,goodchi2=300.0)
	obj.MainChain()
