import numpy as np
import lcurv

from mcmc import MCMC
class run(MCMC):
	def __init__(self, NP, means, mins, maxs, sds, errlev=0.1):
		"""
		Instantiates the class by synthetically generating data.
		"""
		MCMC.__init__(self, NumberOfSteps=50000, NumberOfParams=NP, Mins=mins, Maxs=maxs, SDs=sds, \
			write2file=True, outputfilename='test.chain', alpha=0.1, debug=False)
		lcurv.readmap()
		lcurv.mockdata(means,errlev)

	def chisquare(self, Params):
		return lcurv.chis(Params)

#==========================================

if __name__=="__main__":

	means = np.array([100.0, 400.0, 1.0, 20.0, 0.7, 0.5, 0.5])
	mins = np.array([750.0, 450.0, 0.5, 10.0, 0.0, -1.0, -1.0])
	maxs = np.array([850.0, 550.0, 2.5, 30.0, 1.0, 1.0, 1.0])

	sds = np.array([5, 5, 0.01, 2.0, 0.2, 0.2, 0.1])

	obj = run(7, means, mins, maxs, sds)
	obj.MainChain()
