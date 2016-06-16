import numpy
#import pylab

cc = numpy.genfromtxt('CC.chain')
#dc = numpy.genfromtxt('DC.chain')
#gc = numpy.genfromtxt('GC.chain')
cd = numpy.genfromtxt('CD.chain')
dd = numpy.genfromtxt('DD.chain')
gd = numpy.genfromtxt('GD.chain')
cg = numpy.genfromtxt('CG.chain')
dg = numpy.genfromtxt('DG.chain')
gg = numpy.genfromtxt('GG.chain')

print 'CC',numpy.mean(cc[:,2]),numpy.std(cc[:,2]),-2.0*numpy.log(numpy.max(cc[:,0]))
#print 'DC',numpy.mean(dc[:,2]),numpy.std(dc[:,2]),-2.0*numpy.log(numpy.max(dc[:,0]))
#print 'GC',numpy.mean(gc[:,2]),numpy.std(gc[:,2]),-2.0*numpy.log(numpy.max(gc[:,0]))
print 'CD',numpy.mean(cd[:,2]),numpy.std(cd[:,2]),-2.0*numpy.log(numpy.max(cd[:,0]))
print 'DD',numpy.mean(dd[:,2]),numpy.std(dd[:,2]),-2.0*numpy.log(numpy.max(dd[:,0]))
print 'GD',numpy.mean(gd[:,2]),numpy.std(gd[:,2]),-2.0*numpy.log(numpy.max(gd[:,0]))
print 'CG',numpy.mean(cg[:,2]),numpy.std(cg[:,2]),-2.0*numpy.log(numpy.max(cg[:,0]))
print 'DG',numpy.mean(dg[:,2]),numpy.std(dg[:,2]),-2.0*numpy.log(numpy.max(dg[:,0]))
print 'GG',numpy.mean(gg[:,2]),numpy.std(gg[:,2]),-2.0*numpy.log(numpy.max(gg[:,0]))
