from numpy import linspace, polyfit, polyval
from scipy.integrate import dblquad
from pylab import plot, show

def circle(yc):
    def ylo(x):
        return -(1-x*x)**.5
    def yhi(x):
        return (1-x*x)**.5
    def func(x,y):
        if y > yc:
            return (y-yc+1e-8)**-0.5
        return 0
    return dblquad(func, -1, 1, ylo, yhi)

N = 40
x = linspace(-1,1,N)
y = 1*x
for k in range(N):
    y[k] = circle(x[k])[0]

deg = 6
p = polyfit(x,y,deg)

plot(x,y)
plot(x,polyval(p,x))
show()



