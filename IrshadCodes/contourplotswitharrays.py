import pylab
import numpy

dim = 30
f = open('CrescentFitGaussData_Rhalf.txt','r')

x = []
y = []
while True:
	l = f.readline()
	if not l:
		break
	x.append(float(l.split()[0]))
	y.append(float(l.split()[1]))

xmin = numpy.amin(x)
xmax = numpy.amax(x)
dx = (xmax-xmin)/dim

ymin = numpy.amin(y)
ymax = numpy.amax(y)
dy = (ymax-ymin)/dim

#print xmin,xmax,ymin,ymax
xxx = []
for i in range(dim):
	xx = xmin + float(i-1)/(dim-1)*(xmax-xmin)
	xxx.append(xx)
yyy = []
for j in range(dim):
	yy = ymin + float(j-1)/(dim-1)*(ymax-ymin)
	yyy.append(yy)

matrix = numpy.zeros((dim,dim))
for k in range(len(x)):
	for i in range(dim-1):
		x1=xxx[i] - dx/2
		x2=xxx[i] + dx/2
		for j in range(dim-1):
			y1=yyy[j] - dy/2
			y2=yyy[j] + dy/2
			if x[k]>x1 and x[k]<=x2 and y[k]>y1 and y[k]<=y2:
				matrix[i,j] = matrix[i,j] + 1.0


#pylab.plot(y,x,'.r')				
pylab.contour(xxx,yyy,matrix)
#pylab.xlim(8,12)
#pylab.ylim(4,6)
pylab.show()
