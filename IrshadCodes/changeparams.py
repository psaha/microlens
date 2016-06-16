import numpy
from scipy.integrate import odeint

def Rhalf(Rp,Rn,a,b):

	r = numpy.linspace(0.001,Rp,100)

	def pmthr(area,r):
		c = (a**2 + b**2)**0.5
		ctheta = (r**2 + c**2 - Rn**2)/(2*c*r)
		if ctheta < -1:
			return 0
		if ctheta > 1:
			return numpy.pi*r
		return (numpy.pi - numpy.arccos(ctheta))*r


	area = odeint(pmthr,[0],r)

	for i in range(1,len(r)):
		if area[i-1] < 0.5*area[-1] and area[i] > 0.5*area[-1]:
			return r[i]


# burn_in = 2000
# data = numpy.genfromtxt('fort.1114',skip_header = burn_in)

# newdata = []
# for i in range(len(data)):
# 	Rp = data[i,2]
# 	Rn = data[i,3]
# 	a = data[i,4]
# 	b = data[i,5]
	
# 	Rh = Rhalf(Rp,Rn,a,b)
# 	ratio = Rn/Rp

# 	newdata.append([Rp,Rn,a,b,Rh,ratio])
# 	print i

# newdata = numpy.array(newdata)

# '''
# pylab.subplot(121,aspect='equal')
# pylab.plot(newdata[:,0],newdata[:,1],'or')
# pylab.xlabel('Rp')
# pylab.ylabel('Rn')

# pylab.subplot(122,aspect='equal')
# pylab.plot(newdata[:,4],newdata[:,5],'ob')
# pylab.xlabel('R_half')
# pylab.ylabel('Rp/Rn')

# pylab.savefig('plot.eps')
# pylab.show()
# '''

# numpy.savetxt('CrescentFitGaussData_Rhalf.txt',newdata)

print Rhalf(69.72, 10.0, 15.0, -10.0)
