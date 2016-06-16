import numpy
import pylab as plt 


def reverse_curve(filename, outfilename):
	data = numpy.genfromtxt(filename)

	x = data[:,0]
	y = data[:,1]

	y = y[::-1]

	plt.plot(x,y)
	plt.show()

	newdata = [x,y]
	newdata = numpy.transpose(newdata)
	print numpy.shape(newdata)
	numpy.savetxt(outfilename,newdata)


reverse_curve('fort.11', 'data_crescent_reverse_corr.txt')
reverse_curve('fort.22', 'data_disk_reverse_corr.txt')
reverse_curve('fort.33', 'data_gauss_reverse_corr.txt')

