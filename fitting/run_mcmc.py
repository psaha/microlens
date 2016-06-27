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

	# Crescent
	means = np.array([100.0, 400.0, 1.0, 20.0, 0.7, 0.5, 0.5])
	mins = np.array([750.0, 450.0, 0.5, 1.0, 0.0, -1.0, -1.0])
	maxs = np.array([850.0, 550.0, 2.5, 100.0, 1.0, 1.0, 1.0])
	sds = np.array([5, 5, 0.01, 1.4, 2.35, 0.55, 0.55])
	obj = run(7, means, mins, maxs, sds, 'cc.chain', goodchi2=350.0)
	obj.MainChain()


	# Crescent forward
	means = np.array([100.0, 400.0, 1.0, 20.0, 0.7, 0.5, 0.5])
	mins = np.array([50.0, 350.0, 0.5, 1.0, 0.0, -1.0, -1.0])
	maxs = np.array([150.0, 450.0, 2.5, 100.0, 1.0, 1.0, 1.0])
	sds = np.array([5, 5, 0.01, 1.4, 2.35, 0.55, 0.55])
	obj = run(7, means, mins, maxs, sds, 'cc_forward.chain', goodchi2=350.0)
	obj.MainChain()

	# Gaussian
	means = np.array([100.0, 400.0, 1.0, 20.0, -10.0, 0.5, 0.5])
	mins = np.array([750.0, 450.0, 0.5, 1.0, -20.0, -1.0, -1.0])
	maxs = np.array([850.0, 550.0, 2.5, 100.0, -5.0, 1.0, 1.0])
	sds = np.array([5, 5, 0.01, 1.4, 2.35, 0.55, 0.55])
	obj = run(7, means, mins, maxs, sds, 'gg.chain', goodchi2=350.0)
	obj.MainChain()
	
	# Crescent to Gaussian Data
	means = np.array([100.0, 400.0, 1.0, 20.0, -10.0, 0.5, 0.5])
	mins = np.array([750.0, 450.0, 0.5, 1.0, 0.0, -1.0, -1.0])
	maxs = np.array([850.0, 550.0, 2.5, 100.0, 1.0, 1.0, 1.0])
	sds = np.array([5, 5, 0.01, 1.4, 2.35, 0.55, 0.55])
	obj = run(7, means, mins, maxs, sds, 'cg.chain', goodchi2=400.0)
	obj.MainChain()

	# Gaussian to Crescent Data
	means = np.array([100.0, 400.0, 1.0, 20.0, 0.7, 0.5, 0.5])
	mins = np.array([750.0, 450.0, 0.5, 1.0, -20.0, -1.0, -1.0])
	maxs = np.array([850.0, 550.0, 2.5, 100.0, -5.0, 1.0, 1.0])
	sds = np.array([5, 5, 0.01, 1.4, 2.35, 0.55, 0.55])
	obj = run(7, means, mins, maxs, sds, 'gc.chain', goodchi2=400.0)
	obj.MainChain()


