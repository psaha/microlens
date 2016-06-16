import numpy
import matplotlib.pyplot as pylab

x1 = numpy.genfromtxt('data_crescent.txt')
x2 = numpy.genfromtxt('data_crescent_reverse_corr.txt')
x3 = numpy.genfromtxt('data_disk.txt')
x4 = numpy.genfromtxt('data_gauss.txt')

pylab.plot(x2[:,0]+800,x2[:,1],'r',label='Reverse Crescent',linewidth = 2.0)
pylab.plot(x1[:,0]+800,x1[:,1],'b',label='Crescent',linewidth = 2.0)
pylab.plot(x3[:,0]+800,x3[:,1],'g',label='Disk',linewidth = 2.0)
pylab.plot(x4[:,0]+800,x4[:,1],'m',label='Gauss',linewidth = 2.0)

pylab.xlim(0,200)

pylab.legend(loc=4)
pylab.xlabel('Time')
pylab.ylabel('Convolved magnitude')
#pylab.savefig('data.eps')
pylab.show()
