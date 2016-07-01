import numpy as np
import lcurv
import sys
import scipy.stats as st

fname = sys.argv[1]

Rp = 39.4
sig = 20/(np.log(4))**.5
Rn,a,b = 0.4, 0, 0.3
pars = [51,290]
if fname[1] == 'c':
    pars += [ 1.0, Rp,  Rn, a, b ]
elif fname[1] == 'g':
    pars += [ 1.0, sig, -2, 0, 0 ]
else:
    print('Filename error')
    sys.exit()
pars = np.array(pars)
print(pars)

lcurv.readmap()

errlev = 0.04
lcurv.mockdata(pars,errlev)

chain = np.genfromtxt(fname+'.chain', skip_header=0, skip_footer=1)
print(chain.shape)

minchis=1e30
for i in range(chain.shape[0]):
    x = chain[i,:]
    if x[1] < minchis:
        q = x[3:]
        minchis = x[1]

print(q)
print(minchis,lcurv.chis(q),1-st.chi2.cdf(minchis,pars[1]-pars[0]+1-7))
lcurv.writecurves(q)
