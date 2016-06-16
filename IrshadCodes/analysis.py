# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:23:09 2013

@author: irshad
"""

import numpy
import pylab
'''-------------------------------------------------------------------------'''
filename = 'output/CrescentFitCrescentData.txt'    # Extention has to be .txt.
outputfilename = filename+'_output'  # Statistics will be written here
burn = 500
'''-------------------------------------------------------------------------'''
outfile = open(outputfilename,'w')
data = numpy.genfromtxt(filename,skip_footer = 1,skip_header = burn)
data = numpy.transpose(data)
dataR = numpy.genfromtxt('output/CrescentFitCrescentDataReverse.txt',skip_footer = 1,skip_header = burn)
dataR = numpy.transpose(dataR)
'''-------------------------------------------------------------------------'''
bestindex = numpy.argmax(data[0])
print "Best Likelihood: ",data[:,bestindex]
print >>outfile,"Best Likelihood: ",data[:,bestindex]
print >>outfile,"Mean, Standard_deviation"
for i in range(len(data)):
    print>>outfile, numpy.mean(data[i]),numpy.std(data[i])
'''-------------------------------------------------------------------------'''
pylab.subplot(1,2,1)
pylab.plot(dataR[2],dataR[3],'r',label='Reverse Fold')
pylab.plot(data[2],data[3],'g',label='Forward Fold')
pylab.legend(loc = 2)
pylab.plot(50.0,30.0,'xk')
pylab.xlabel('Rp')
pylab.ylabel('Rn')

pylab.subplot(1,2,2)
pylab.plot(dataR[4],dataR[5],'r',label='Reverse Fold')
pylab.plot(data[4],data[5],'g',label='Forward Fold')
pylab.legend(loc = 2)
pylab.plot(15.0,10.0,'xk')
pylab.xlabel('a')
pylab.ylabel('b')
pylab.hold('on')

pylab.savefig('output/CrescentFitReverse.eps')
pylab.show()
'''-------------------------------------------------------------------------'''


