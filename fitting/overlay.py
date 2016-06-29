import numpy
import lcurv

lcurv.readmap()

pcr = numpy.array([ 150, 350, 1, 26.25, 0.4, 0, 0.3 ])
pg = numpy.array([ 150, 350, 1, 20/(numpy.log(4))**.5, -0.4, 0, 0.3 ])
p = pg
errlev = 0.1
lcurv.mockdata(p,errlev)

"""
fname = ('gc.chain')
chain = numpy.genfromtxt(fname, skip_header=0, skip_footer=1)
print(chain.shape)

minchis=1e30
for i in range(chain.shape[0]):
    x = chain[i,:]
    if x[1] < minchis:
        q = x[3:]
        minchis = x[1]
"""
q = p
minchis = 0

print(minchis,lcurv.chis(q))
lcurv.writecurves(q)



