import numpy

burn_in = 2000
x = numpy.genfromtxt('../chains/CrescentFitCrescentDataReverse_Rhalf.txt',skip_header=burn_in)
xx = numpy.genfromtxt('../chains/CrescentFitCrescentData_Rhalf.txt',skip_header=20,skip_footer=6000)
y = numpy.genfromtxt('../chains/CrescentFitDiskData_Rhalf.txt',skip_header=2000)
z = numpy.genfromtxt('../chains/CrescentFitGaussData_Rhalf.txt',skip_header=2000)
print numpy.mean(x[:,2]),numpy.mean(x[:,3]),numpy.mean(x[:,4]),numpy.mean(x[:,5])
print numpy.std(x[:,2]),numpy.std(x[:,3]),numpy.std(x[:,4]),numpy.std(x[:,5])


from matplotlib.pyplot import figure, show,plot, xlabel, ylabel,legend

markers = 'or'
fig = figure()

ax0 = fig.add_subplot(1,2,1)
ax0.plot(x[:,4],x[:,5],'r',label='Reverse Crescent')
ax0.plot(xx[:,4],xx[:,5],'b',label='Crescent')
ax0.plot(y[:,4],y[:,5],'g',label='Uniform Disk')
ax0.plot(z[:,4],z[:,5],'m',label='Gaussian Disk')
legend(loc=2)
ax0.set_xlim(30.0, 60.0)
ax0.set_ylim(0.0, 2.0)
x0, x1 = ax0.get_xlim()
y0, y1 = ax0.get_ylim()
ax0.set_aspect((x1-x0)/(y1-y0))
xlabel('R_half')
ylabel('Rn/Rp')

ax1 = fig.add_subplot(1,2,2)
ax1.plot(x[:,2]/x[:,0],x[:,3]/x[:,0],'r',label='Reverse Crescent')
ax1.plot(xx[:,2]/xx[:,0],xx[:,3]/xx[:,0],'b',label='Crescent')
ax1.plot(y[:,2]/y[:,0],y[:,3]/y[:,0],'g',label='Disk')
ax1.plot(z[:,2]/z[:,0],z[:,3]/z[:,0],'m',label='Gaussian Disk')
legend(loc=2)
ax1.set_xlim(-1.0, 1.0)
ax1.set_ylim(-1.0, 1.0)
x0, x1 = ax1.get_xlim()
y0, y1 = ax1.get_ylim()
ax1.set_aspect((x1-x0)/(y1-y0))
xlabel('a/Rp')
ylabel('b/Rp')

show()
