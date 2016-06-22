import numpy
import lcurv
import metrop
from scipy.optimize import leastsq

lcurv.readmap()

t1 = (1,100,200)
t2 = (300,400,500)
norm = (0.5,1,2.5)
rp = (10,20,30)
rn = (0,0.7,1)
a = (-1,.5,1)
b = (-1,.5,1)

p = []
lo = []
hi = []
for f in (t1,t2,norm,rp,rn,a,b):
    p.append(f[1])
    lo.append(f[0])
    hi.append(f[2])
p = numpy.array(p)
lo = numpy.array(lo)
hi = numpy.array(hi)

errlev = 0.05

print(lo)
print(p)
print(hi)

lcurv.mockdata(p,errlev)

def resid(p):
    nobs,x = lcurv.residuals(p)
    x = x[:nobs] 
    return x

lo[0],hi[0] = 750,850
lo[1],hi[1] = 450,550
p[0] = 780
p[1] = 480

q = leastsq(resid,p)[0]

"""
rawlnp,ans = metrop.samp(lnprob, lo, hi, 200)

q = 0*p
for k in range(7):
    print(min(ans[:,k]), max(ans[:,k]))
    q[k] = numpy.median(ans[:,k])
print(q)
print('chi^2 = ',lcurv.chis(q))
"""
print(q)
print(lcurv.chis(q))
lcurv.writecurves(q)



