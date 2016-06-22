import numpy as np
import lcurv
import metrop
from scipy.optimize import leastsq
from sys import exit

lcurv.readmap()
errlev = 0.05
params = np.array([100, 400, 1, 20, 0.7, 0.5, 0.5], dtype='float')

lcurv.mockdata(params,errlev)
lcurv.writecurves(params)

print lcurv.chis(params)

