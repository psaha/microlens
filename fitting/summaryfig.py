import numpy as np
import scipy.stats as st
import matplotlib.pyplot as pl
import lcurv
import sys
from rhalf import Rhalf


def mockdata():
    global pars
    lcurv.readmap()
    Rp = 39.4
    Rn,a,b = 0.4, 0, 0.3
    pars = [ 51, 290, 1.0, Rp,  Rn, a, b ]
    pars = np.array(pars)
    print(pars)
    errlev = 0.04
    lcurv.mockdata(pars,errlev)


def gencurves(fname):
    global rh,wt
    chain = np.genfromtxt(fname+'.chain', skip_header=0, skip_footer=1)
    print(chain.shape)
    rh = []
    wt = []
    minchis=1e30
    for i in range(chain.shape[0]):
        x = chain[i,:]
        if x[1] < minchis:
            q = x[3:]
            minchis = x[1]
        if chain[i,0] > 100:
            rp,rn,a,b = chain[i,6],chain[i,7],chain[i,8],chain[i,9]
            if rn < 0:
                v = rp*(np.log(4))**.5
            else:
                rn *= rp
                a *= rp
                b *= rp
                v = Rhalf(rp,rn,a,b)
            rh.append(v/30)
            w = chain[i,0] - chain[i-1,0]
            w /= chain[-1,0]
            wt.append(w)
    print(q)
    print(minchis,lcurv.chis(q),1-st.chi2.cdf(minchis,pars[1]-pars[0]+1-7))
    lcurv.writecurves(q)


def plotcurves(p):
    fil = open('curves.txt')
    all = fil.readlines()
    t = []
    m = []
    b = []
    db = []
    for l in all:
        s = l.split()
        t.append(int(s[0])/30.)
        m.append(float(s[1]))
        b.append(float(s[2]))
        db.append(float(s[3]))
    p.plot(t,m)
    p.axis([0,6,0,7])
    p.errorbar(t,b,yerr=db,linestyle='none',color='gray')
    p.set_yticks(np.arange(0,7,2))
    p.set_xlabel('$t [r_{1/2}/v]$')
    p.set_ylabel('magnification')

def plothist(p):
    p.hist(rh,np.linspace(0.75,1.25,26),weights=wt)
    p.set_xlabel('inferred:actual $r_{1/2}$')

fig = pl.figure()

mockdata()

#gencurves('cc_forward')
#gencurves('cc_backward')
gencurves('gc_forward')

p = fig.add_subplot(211)
plotcurves(p)

p = fig.add_subplot(212)
plothist(p)
p.get_yaxis().set_visible(False)

pl.show()

