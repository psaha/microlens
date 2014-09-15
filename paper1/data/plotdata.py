import numpy
import pylab


def plot(filename,filename_bestfit1,filename_bestfit2,filename_bestfit3,name):
	x = numpy.genfromtxt(filename)
	y1 = numpy.genfromtxt(filename_bestfit1)
	y2 = numpy.genfromtxt(filename_bestfit2)
	y3 = numpy.genfromtxt(filename_bestfit3)
	pylab.errorbar(x[:,0],x[:,1],x[:,1]*0.1,color='k',\
		label='$\mathtt{%s}$'%name)
	pylab.plot(y1[:,0]-y1[1,0]+y1[1,2],y1[:,1],'r',lw=2,label='$\mathtt{Crescent\ fit}$')
	pylab.plot(y2[:,0]-y2[1,0]+y2[1,2],y2[:,1],'b',lw=2,label='$\mathtt{Uniform\ disk\ fit}$')
	pylab.plot(y3[:,0]-y3[1,0]+y3[1,2],y3[:,1],'g',lw=2,label='$\mathtt{Gaussian\ disk\ fit}$')


plot('data_gauss_reverse_noise.txt','cg.bestfit','dg.bestfit','gg.bestfit','Gaussian\ disk\ data')
pylab.legend(loc=2,fontsize=16)
pylab.xlim(-850,-600)
pylab.ylim(ymin=2)
pylab.xlabel('$\mathtt{Time}$',fontsize=22)
pylab.ylabel('$\mathtt{Brightness}$',fontsize=22)
pylab.savefig('data_gg.eps')
pylab.show()

