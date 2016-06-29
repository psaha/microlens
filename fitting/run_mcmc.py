import numpy as np
import lcurv

from mcmc import MCMC
class run(MCMC):
	def __init__(self, NP, means, mins, maxs, sds, outfile, errlev=0.1, goodchi2=350.0):
		"""
		Instantiates the class by synthetically generating data.
		"""
		MCMC.__init__(self, TargetAcceptedPoints=6301, NumberOfParams=NP, Mins=mins, Maxs=maxs, SDs=sds, \
			write2file=True, outputfilename=outfile, alpha=0.1, debug=False,\
                                EstimateCovariance=True, CovNum=100, goodchi2=goodchi2)
		lcurv.readmap()
		lcurv.mockdata(means,errlev)

	def chisquare(self, Params):
		return lcurv.chis(Params)

#==========================================

if __name__=="__main__":

	Rp = 26.25
	sig = 20/(numpy.log(4))**.5
	Rn,a,b = 0.4, 0, 0.3
	t1min,t1,t1max = 100,150,200
	t2min,t2,t2max = 300,350,400
	t3min,t3max = 700,800
	t4min,t4max = 500,600

	fname = 'gg_forward'

	if fname[1] == 'c':
		pars = [t1, t2, 1.0, Rp,  Rn, a, b ]
	if fname[1] == 'g':
		pars = [t1, t2, 1.0, sig, -2, 0, 0 ]
	if fname[0] == 'c':
		mins = [ t1min, t2min, 0.5,   1,  0, -1, -1]
		maxs = [ t1max, t2max, 2.5, 100,  1,  1,  1]
	if fname[0] == 'g':
		mins = [ t1min, t2min, 0.5,   1, -3, -1, -1]
		maxs = [ t1max, t2max, 2.5, 100, -1,  1,  1]
	if fname[-7:] == 'backward':
		mins[0], mins[1] = t3min, t4min
		maxs[0], maxs[1] = t3max, t4max

	pars = np.array(pars)
	mins = np.array(mins)
	maxs = np.array(maxs)
	sds = np.array([5, 5, 0.01, 1, 0.1, 0.5, 0.5])
	obj = run(7, means, mins, maxs, sds, fname, goodchi2=250.0)
	obj.MainChain()

