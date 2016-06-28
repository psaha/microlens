import numpy
import lcurv

lcurv.readmap()

p = numpy.array([100.0, 400.0, 1.0, 20.0, 0.7, 0.5, 0.5])
errlev = 0.1
lcurv.mockdata(p,errlev)

fname = ('gc.chain')
chain = numpy.genfromtxt(fname, skip_header=0, skip_footer=1)
print(chain.shape)

minchis=1e30
for i in range(chain.shape[0]):
    x = chain[i,:]
    if x[1] < minchis:
        q = x[3:]
        minchis = x[1]

print(minchis,lcurv.chis(q))
lcurv.writecurves(q)



