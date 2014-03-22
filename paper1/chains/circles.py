from numpy import linspace, pi, cos, sin, arccos
from scipy.integrate import odeint
from pylab import figure, show

def theta_lohi(Rn,c,d,r):
    if abs(d) < 1e-10:
        hi = pi
    else:
        ctheta = (r*r + d*d - 1)/(2*d*r)
        if ctheta > 1:
            hi = 0
        elif ctheta < -1:
            hi = pi
        else:
            hi = arccos(ctheta)
    d += c
    ctheta = (r*r + d*d - Rn*Rn)/(2*d*r)
    if ctheta > 1:
	lo = 0
    elif ctheta < -1:
        lo = pi
    else:
	lo = arccos(ctheta)
    return (lo,hi)

def Rhalf(Rp,Rn,a,b):
    Rn /= Rp
    c = (a*a + b*b)**0.5 / Rp
    r = linspace(0.001,1,100)

    def numer(f,r):
        lo,hi = theta_lohi(Rn,c,0,r)
        return r*r * (sin(lo)-sin(hi))

    def denom(f,r):
        lo,hi = theta_lohi(Rn,c,0,r)
        return r * (hi - lo)

    def arc(f,r):
        lo,hi = theta_lohi(Rn,c,d,r)
        return r * (hi - lo)

    up = odeint(numer,[0],r)
    dn = odeint(denom,[0],r)

    d = up[-1,0]/dn[-1,0]
    area = odeint(arc,[0],r)

    for i in range(1,len(r)):
        if area[i-1] < 0.5*area[-1] and area[i] > 0.5*area[-1]:
            return Rp * r[i]


panel = figure().add_subplot(1,1,1)
panel.set_aspect('equal')

Rn = 0.8
c = 0.2
d = 0.038
for r in linspace(.02,1+d,50):
    lo,hi = theta_lohi(Rn,c,d,r)
    u = linspace(lo,hi,20)
    x,y = r*cos(u)-d,r*sin(u)
    panel.plot(x,y)

# show()

def cfile(fname):
    inf = open(fname)
    fname = fname.split('.')
    flag = fname[0][1]
    fname = fname[0]+'2.'+fname[1]
    print fname
    ouf = open(fname,'w')
    for l in range(10):
        lyne = inf.readline()
        if not lyne:
            break
        lyne = lyne.split()
        if flag == 'C':
            Rp,Rn,a,b = float(lyne[2]),float(lyne[3]), \
                        float(lyne[4]),float(lyne[5])
            Rh = Rhalf(Rp,Rn,a,b)
        if flag == 'G':
        lyne[2] = '   %7.4f' % Rh
        lyne = '  '.join(lyne)
        ouf.write(lyne+'\n')
    ouf.close()

cfile('CC.chain')
