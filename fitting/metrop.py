from numpy.random import random, random_sample
from numpy import array, exp

def samp(fun,lo,hi,N):
    w = (lo+hi)/2.
    wlyst = [w+0]
    lnplyst = [fun(w)]
    n = 0
    while True:
        dw = 2*random_sample(len(w)) - 1
        w += (hi-lo) * dw/10
        for k in range(len(w)):
            if w[k] < lo[k]:
                w[k] += hi[k] - lo[k]
            if w[k] > hi[k]:
                w[k] -= hi[k] - lo[k]
        lnp = fun(w)
        if random() > exp(lnp-lnplyst[n%N]):
#            print('rejected %10.5e vs %10.5e' % (lnp,lnplyst[n%N]))
            w = wlyst[n%N] + 0
            lnp = lnplyst[n%N]
#        else:
#            print('accepted')
        n += 1
        if n%20 == 0:
            print('lnP = %10.5e after %1i steps' % (lnp,n))
        if n < N:
            wlyst += [w+0]
            lnplyst += [lnp]
        else:
            wlyst[n%N] = w + 0
            lnplyst[n%N] = lnp
            if lnplyst[n%N] <= lnplyst[(n+1)%N]:
                return (array(lnplyst),array(wlyst))


