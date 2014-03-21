from numpy import linspace, pi, cos, sin, arccos
from scipy.integrate import odeint
from pylab import figure, show

def theta_lohi(Rn,c,d,r):
    ctheta = (r*r + d*d - 1)/(2*d*r)
    if ctheta > 1:
	hi = 0
    elif ctheta < -1:
        hi = pi
    else:
	hi = arccos(ctheta)
    d = (c*c + d*d)**.5
    ctheta = (r*r + d*d - Rn*Rn)/(2*d*r)
    if ctheta > 1:
	lo = 0
    elif ctheta < -1:
        lo = pi
    else:
	lo = arccos(ctheta)
    return (lo,hi)

panel = figure().add_subplot(1,1,1)
panel.set_aspect('equal')

Rn = 0.4
c = 0.4
d = 0.2
for r in linspace(.02,1+d,50):
    lo,hi = theta_lohi(Rn,c,d,r)
    u = linspace(lo,hi,20)
    x,y = r*cos(u)-d,r*sin(u)
    panel.plot(x,y)

show()


