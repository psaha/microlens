import numpy
import pylab


def plot(filename,filename_bestfit1,filename_bestfit2,filename_bestfit3,name):
	x = numpy.genfromtxt(filename)
	y1 = numpy.genfromtxt(filename_bestfit1)
	y2 = numpy.genfromtxt(filename_bestfit2)
	y3 = numpy.genfromtxt(filename_bestfit3)
	pylab.errorbar(x[:,0]+850,x[:,1],x[:,1]*0.1,color='k',\
		label='$\mathtt{%s}$'%name)
	pylab.plot(y1[:,0]-y1[1,0]+y1[1,2]+850,y1[:,1],'r',lw=2)
	pylab.plot(y2[:,0]-y2[1,0]+y2[1,2]+850,y2[:,1],'b',lw=2)
	pylab.plot(y3[:,0]-y3[1,0]+y3[1,2]+850,y3[:,1],'g',lw=2)


plot('data_gauss_reverse_noise.txt','cg.bestfit','dg.bestfit','gg.bestfit','Gaussian\ Disk\ data')
pylab.legend(loc=2,fontsize=22)
#pylab.axes().set_aspect(20.0)
pylab.xlim(0,250)
pylab.ylim(ymin=2)
pylab.xlabel('$\mathtt{Time}$',fontsize=22)
pylab.ylabel('$\mathtt{Brightness}$',fontsize=22)
pylab.savefig('data_gg.eps')
pylab.show()

