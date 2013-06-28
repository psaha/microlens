import numpy
import scipy
from scipy import integrate
from scipy.optimize import leastsq
from pylab import plot, show


def func_yp(y_p, R_p, y):
    if y < 0:
        return 0
    elif y == 0:
        return 0
    else:
        return (R_p**2 - (y_p -y)**2)**0.5/y**0.5 + 1.0

#limits of the path on the y axis
y_min = -1
y_max = 4
y_p = numpy.linspace(y_min,y_max,50)

def lcurve(R_p,R_n,b):
    #light curve data
    l_m = []
    for element in y_p:
        #Luminous part of the large disk
        func = lambda y: func_yp(element, R_p, y)
        if element <= - R_p:
            m = 0
        if (element > - R_p and element < R_p):
            m = integrate.quad(func, 0, R_p+element)[0] 
        if element > R_p:
            m = integrate.quad(func, element - R_p, R_p + element)[0]
        #Dark part of the large disk / small disk
        y_n_i = element + b
        func2 = lambda t: func_yp(element+b, R_n, t)
        if element+b <= -R_n:
            n = 0
        if (element+b > - R_n and element+b < R_n ):
            n  = integrate.quad(func2, 0, R_n + element+b)[0]
        if element +b > R_n:
            n = integrate.quad(func2,element +b - R_n, R_n + element +b)[0]
        #Subtracting them
        l_m = l_m +[m-n]
    #Division by surface area
    Area = numpy.pi*R_p**2 - numpy.pi*R_n**2
    l_m = numpy.array(l_m)/Area
    return l_m

def resid(params):
    global data
    print params
    Rp,Rn,b = params
    return data - lcurve(Rp,Rn,b)

Rn = 0.85

for b in numpy.linspace(Rn-1,1-Rn,10):
    data = lcurve(1.,Rn,b)
    plot(y_p,data)

trial = (0.5,0,0)
fit = leastsq(resid,trial)
plot(y_p,resid(fit[0]))

show()
