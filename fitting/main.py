import numpy
import lcurv
import metrop

lcurv.readmap()

p = [100,400,1,20,.7,.5,.5]
p = numpy.array(p)
errlev = 0.05

lcurv.mockdata(p,errlev)

lo = [0,300,0.5,10,0,-1,-1]
hi = [200,500,2.5,30,1,1,1]
lo = numpy.array(lo)
hi = numpy.array(hi)

print(lo)
print(p)
print(hi)

def lnprob(p):
    return -lcurv.chis(p)/2

rawlnp,ans = metrop.samp(lnprob, lo, hi, 100)

q = 0*p
for k in range(7):
    print(min(ans[:,k]), max(ans[:,k]))
    q[k] = numpy.median(ans[:,k])
print(q)
print('chi^2 = ',lcurv.chis(q))

lcurv.writecurves(p)



