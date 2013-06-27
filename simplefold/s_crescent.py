import numpy
import scipy
from scipy import integrate
import m_general


def func_yp(y_p, R_p, y):
    if y < 0:
        return 0
    elif y == 0:
        return 0
    else:
        return (R_p**2 - (y_p -y)**2)**0.5/y**0.5 + 1.0


R_p = 1.0
R_n = 0.3
b   = 0.1
#b < (R_p - R_n)**2 - a**2 

#limits of the path on the Oy axis
y_min = -2
y_max = 2

y_p = numpy.arange(y_min,y_max,0.001, dtype = float)
y_p = numpy.array(y_p)

#light curve data
l_m = []



for element in y_p:
    
    #Luminous part of the large disk
    func = lambda y: func_yp(element, R_p, y)
    if element <= - R_p:
        m = 0
    
    if (element > - R_p and element < R_p):
        m   = integrate.quad(func, 0, R_p+element)[0] 
    
    if element > R_p:
        m   = integrate.quad(func, element - R_p, R_p + element)[0]

    #Dark part of the large disk / small disk
    y_n_i = element + b
    func2 = lambda t: func_yp(element+b, R_n, t)
    if element+b <= -R_n:
        n = 0
    
    if (element+b > - R_n and element+b < R_n ):
        n   = integrate.quad(func2, 0, R_n + element+b)[0]
    
    if element +b > R_n:
        n   = integrate.quad(func2,element +b - R_n, R_n + element +b)[0]
    
    
    #Subtracting them
    l_m = l_m +[m-n]
    

#Division by surface area
Area =numpy.pi*R_p**2 - numpy.pi*R_n**2
l_m = numpy.array(l_m)/Area

#Plotting the data
m_general.quick_plot(y_p, l_m)    

