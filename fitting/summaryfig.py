import numpy as np
import scipy.stats as st
import matplotlib.pyplot as pl
import lcurv
import sys
from rhalf import Rhalf


def mockdata():
    global pars
    lcurv.readmap()
    Rp = 39.4              # scaled by 30
    Rn,a,b = 0.4, 0, 0.3
    print('r_half = ',Rhalf(1,Rn,a,b)*Rp/30)
    pars = [ 51, 290, 1.0, Rp,  Rn, a, b ]
    pars = np.array(pars)
    print(pars)
    errlev = 0.04
    lcurv.mockdata(pars,errlev)


def gencurves(fname):
    global rh,rns,wt
    chain = np.genfromtxt(fname+'.chain', skip_header=0, skip_footer=1)
    print(chain.shape)
    rh = []
    rns = []
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
            rns.append(rn/rp)
            w = chain[i,0] - chain[i-1,0]
            w /= chain[-1,0] - 100
            wt.append(w)
    rh = np.array(rh)
    rns = np.array(rns)
    wt = np.array(wt)
    print(np.sum(wt))
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
    p.axis([0,6,0,7])
    p.errorbar(t,b,yerr=db,linestyle='none',color='gray')
    p.plot(t,m,color='black')
    p.set_yticks(np.arange(0,7,2))
    p.set_xlabel('$t [r_{1/2}/v]$',labelpad=10, fontsize=16)
    p.set_ylabel('magnification', fontsize=16)

def plothist(p):
    rmin,rmax,nr = 0,1.2,61
    p.hist(rh,np.linspace(rmin,rmax,nr),weights=wt,
           histtype='step',lw=2,color='black')
    p.plot([1,1],[.43,.48],lw=2,color='black')
    fl = max(rns)
    if fl > 0:
        p.hist(rns,np.linspace(rmin,rmax,nr),weights=wt,
               histtype='step',lw=2,color='black',linestyle='dashed')
        p.plot([.4,.4],[.43,.48],lw=2,color='black',linestyle='dashed')
        p.set_xlabel('inferred $R_n/R_p$ and $r_{1/2}$',labelpad=10)
    else:
        p.set_xlabel('inferred $r_{1/2}$',labelpad=10, fontsize=16)
    p.axis([rmin,rmax,0,0.5])



mockdata()

for fname in ['gc_forward','cc_forward','cc_backward']:
    gencurves(fname)

    fig = pl.figure(figsize=(5,10))
    fig.subplots_adjust(hspace=0.2)

    p = fig.add_subplot(211)
    plotcurves(p)

    p = fig.add_subplot(212)
    plothist(p)
    p.get_yaxis().set_visible(False)

    fig.savefig('../paper1/figures/%s.eps'%fname)

    pl.show()
