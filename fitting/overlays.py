import numpy as np
import lcurv
import sys
import scipy.stats as st
import matplotlib.pyplot as pl

def mockdata():
    global pars
    lcurv.readmap()
    Rp = 39.4
    sig = 20/(np.log(4))**.5
    Rn,a,b = 0.4, 0, 0.3
    pars = [ 51, 290, 1.0, Rp,  Rn, a, b ]
    pars = np.array(pars)
    print(pars)
    errlev = 0.04
    lcurv.mockdata(pars,errlev)


def gencurves(fname):
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


fig = pl.figure()

mockdata()

gencurves('cc_forward')
p = fig.add_subplot(311)
p.get_xaxis().set_visible(False)
plotcurves(p)

gencurves('cc_backward')
p = fig.add_subplot(312)
p.get_xaxis().set_visible(False)
plotcurves(p)

gencurves('gc_forward')
p = fig.add_subplot(313)
plotcurves(p)

pl.show()

