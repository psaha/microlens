from numpy import pi, cos, linspace, polyfit, polyval
from scipy.integrate import dblquad
from pylab import plot, show

def circle(yc):
    def ylo(x):
        return -(1-x*x)**.5
    def yhi(x):
        return (1-x*x)**.5
    def func(x,y):
        if y < yc:
            return (yc-y+1e-8)**-0.5
        return 0
    return dblquad(func, -1, 1, ylo, yhi)

def crescent(r,dr,phi,yc):
    big = circle(yc)[0]
    small = circle(yc+dr*cos(phi))[0]
    return (big - r*r*small) / (pi*(1-r*r))

N = 40
x = linspace(-1,4,N)
y = 1*x
r,dr,phi = 0.5,0.25,0
for k in range(N):
    y[k] = circle(x[k])[0]/pi
    if x[k] > 1:
        y[k] *= x[k]**.5
        

deg = 12
p = polyfit(x,y,deg)
yf = polyval(p,x)

for k in range(N):
    if x[k] > 1:
        y[k] /= x[k]**.5
        yf[k] /= x[k]**.5

plot(x,y)
# plot(x,yf)
show()



