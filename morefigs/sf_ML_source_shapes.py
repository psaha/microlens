import numpy

def theta(value):
	lista_poz = numpy.where(value > 0)[0]
	lista_neg = numpy.where(value < 0)[0]
	theta = value.copy()
	theta[lista_poz] = numpy.ones(len(lista_poz))
	theta[lista_neg] = numpy.zeros(len(lista_neg))
	return theta


def zerofy(value):
	lista = numpy.where(value**2 > 100000)[0]
	value[lista] = numpy.zeros(len(lista))


def S1D(time, shift, r, S_0):
	lista_non = numpy.where(1-((time-shift)/r)**2 < 0)[0]
	S1D = time.copy()
	S1D = 2*S_0/numpy.pi/r*(1-((time-shift)/r)**2)**0.5*theta(r**2 - (time-shift)**2)
	S1D[lista_non] = numpy.zeros(len(lista_non))
	return S1D


S_0 = 1.
r_half = 1.

time = numpy.linspace(-2., 2., 1000)

#gaussian
sigma = r_half/ (numpy.log(4)**0.5)
S1D_g = S_0/(2*numpy.pi)**0.5/sigma*numpy.exp(-time**2/2/sigma**2)
print "sigma", sigma

#disk
r = r_half*2**0.5
shift = 0
S1D_d = S1D(time, 0, r, S_0)# 2*S_0/numpy.pi/r*(1-((time-shift)/r)**2)**0.5*theta(r**2 - (time-shift)**2)

print "radius", r 

#crescent
R_p = r_half/0.72754
R_n = 0.4*R_p
a1 = 0.3*R_p
a2 = -0.3*R_p


S_0dp = S_0*R_p**2/(R_p**2-R_n**2)
S_0dn = S_0*R_n**2/(R_p**2-R_n**2)



S1D_dp = S1D(time, 0, R_p, S_0dp)

S1D_dn1 = S1D(time, a1, R_n, S_0dn)


S1D_dn2 = S1D(time, a2, R_n, S_0dn)

zerofy(S1D_dp)
zerofy(S1D_dn1)
zerofy(S1D_dn2)

path = "./" #"/zbox/data/mihai/GIT_ML/figures2/"

#Right figure 4
from matplotlib import pyplot


#
pyplot.figure(figsize=(8.7,7))


pyplot.plot(time, S1D_dp - S1D_dn2, 'k', label = "forward crescent")
pyplot.plot(time, S1D_dp - S1D_dn1, 'b', label =  "backward crescent")
pyplot.plot(time, S1D_d, 'g', label ='disc')
pyplot.plot(time, S1D_g, 'r', label ='gaussian')
pyplot.xlabel('p  [r$_{1/2}$]', fontsize = 20)
pyplot.ylabel('S$_{1D}$  [S$_0$/r$_{1/2}$]', fontsize = 20)
pyplot.legend(loc = 8)

pyplot.tick_params(axis='both', which='major', labelsize=20)
pyplot.tick_params(axis='both', which='minor', labelsize=20)

pyplot.savefig(path+"S1D_all.eps")
pyplot.cla()
#right figure 5
R_p = r_half
R_n = 0.4*R_p

a11 = 0.3*R_p
a12 = 0.15*R_p
a13 = 0
a14 = -0.15*R_p
a15 = -0.30*R_p

S_0dp1 = S_0*R_p**2/(R_p**2-R_n**2)
S_0dn1 = S_0*R_n**2/(R_p**2-R_n**2)

S1D_dp1 = S1D(time, 0, R_p, S_0dp1)
S1D_dn11 = S1D(time, a11, R_n, S_0dn1)
S1D_dn12 = S1D(time, a12, R_n, S_0dn1)
S1D_dn13 = S1D(time, a13, R_n, S_0dn1)
S1D_dn14 = S1D(time, a14, R_n, S_0dn1)
S1D_dn15 = S1D(time, a15, R_n, S_0dn1)


pyplot.figure(figsize=(8.7,7))

pyplot.plot(time, S1D_dp1 - S1D_dn11, 'k', label = "a = 0.30 $R_p$")
pyplot.plot(time, S1D_dp1 - S1D_dn12, 'b', label = "a = 0.15 $R_p$")
pyplot.plot(time, S1D_dp1 - S1D_dn13, 'g', label = "a = 0")
pyplot.plot(time, S1D_dp1 - S1D_dn14, 'r', label = "a = -0.15 $R_p$")
pyplot.plot(time, S1D_dp1 - S1D_dn15, 'm', label = "a = -0.30 $R_p$")
pyplot.xlabel('p  [R$_p$]', fontsize = 20)
pyplot.ylabel('S$_{1D}$  [S$_0$/R$_p$]', fontsize = 20)
pyplot.legend(loc = 8)

pyplot.tick_params(axis='both', which='major', labelsize=20)
pyplot.tick_params(axis='both', which='minor', labelsize=20)


pyplot.savefig(path+"S1D_var_a.eps")
pyplot.cla()

#right figure 6
R_p = r_half
R_n21 = 0.7*R_p
R_n22 = 0.55*R_p
R_n23 = 0.4*R_p
R_n24 = 0.25*R_p
R_n25 = 0.10*R_p


a21 = 0.3*R_p

S_0dp21 = S_0*R_p**2/(R_p**2-R_n21**2)
S_0dn21 = S_0*R_n21**2/(R_p**2-R_n21**2)

S_0dp22 = S_0*R_p**2/(R_p**2-R_n22**2)
S_0dn22 = S_0*R_n22**2/(R_p**2-R_n22**2)

S_0dp23 = S_0*R_p**2/(R_p**2-R_n23**2)
S_0dn23 = S_0*R_n23**2/(R_p**2-R_n23**2)

S_0dp24 = S_0*R_p**2/(R_p**2-R_n24**2)
S_0dn24 = S_0*R_n24**2/(R_p**2-R_n24**2)

S_0dp25 = S_0*R_p**2/(R_p**2-R_n25**2)
S_0dn25 = S_0*R_n25**2/(R_p**2-R_n25**2)


S1D_dp21 = S1D(time, 0, R_p, S_0dp21)
S1D_dp22 = S1D(time, 0, R_p, S_0dp22)
S1D_dp23 = S1D(time, 0, R_p, S_0dp23)
S1D_dp24 = S1D(time, 0, R_p, S_0dp24)
S1D_dp25 = S1D(time, 0, R_p, S_0dp25)




S1D_dn21 = S1D(time, a21, R_n21, S_0dn21)
S1D_dn22 = S1D(time, a21, R_n22, S_0dn22)
S1D_dn23 = S1D(time, a21, R_n23, S_0dn23)
S1D_dn24 = S1D(time, a21, R_n24, S_0dn24)
S1D_dn25 = S1D(time, a21, R_n25, S_0dn25)




pyplot.figure(figsize=(8.7,7))

pyplot.plot(time, S1D_dp21 - S1D_dn21, 'k', label = "R$_n$ = 0.70 $R_p$")
pyplot.plot(time, S1D_dp22 - S1D_dn22, 'b', label = "R$_n$ = 0.55 $R_p$")
pyplot.plot(time, S1D_dp23 - S1D_dn23, 'g', label = "R$_n$ = 0.40 $R_p$")
pyplot.plot(time, S1D_dp24 - S1D_dn24, 'r', label = "R$_n$ = 0.25 $R_p$")
pyplot.plot(time, S1D_dp25 - S1D_dn25, 'm', label = "R$_n$ = 0.10 $R_p$")
pyplot.xlabel('p  [R$_p$]', fontsize = 20)
pyplot.ylabel('S$_{1D}$  [S$_0$/R$_p$]', fontsize = 20)
pyplot.legend(loc = 1)

pyplot.tick_params(axis='both', which='major', labelsize=20)
pyplot.tick_params(axis='both', which='minor', labelsize=20)




pyplot.savefig(path+"S1D_var_rn_a_poz.eps")
pyplot.cla()
#right figure 7
R_p = r_half
R_n21 = 0.7*R_p
R_n22 = 0.55*R_p
R_n23 = 0.4*R_p
R_n24 = 0.25*R_p
R_n25 = 0.10*R_p


a31 =-0.3*R_p
S1D_dn31 = S1D(time, a31, R_n21, S_0dn21)
S1D_dn32 = S1D(time, a31, R_n22, S_0dn22)
S1D_dn33 = S1D(time, a31, R_n23, S_0dn23)
S1D_dn34 = S1D(time, a31, R_n24, S_0dn24)
S1D_dn35 = S1D(time, a31, R_n25, S_0dn25)



pyplot.figure(figsize=(8.7,7))
pyplot.plot(time, S1D_dp21 - S1D_dn31, 'k', label = "R$_n$ = 0.70 $R_p$")
pyplot.plot(time, S1D_dp22 - S1D_dn32, 'b', label = "R$_n$ = 0.55 $R_p$")
pyplot.plot(time, S1D_dp23 - S1D_dn33, 'g', label = "R$_n$ = 0.40 $R_p$")
pyplot.plot(time, S1D_dp24 - S1D_dn34, 'r', label = "R$_n$ = 0.25 $R_p$")
pyplot.plot(time, S1D_dp25 - S1D_dn35, 'm', label = "R$_n$ = 0.10 $R_p$")
pyplot.xlabel('p  [R$_p$]', fontsize = 20)
pyplot.ylabel('S$_{1D}$  [S$_0$/R$_p$]', fontsize = 20)
pyplot.legend(loc = 2)


pyplot.tick_params(axis='both', which='major', labelsize=20)
pyplot.tick_params(axis='both', which='minor', labelsize=20)



pyplot.savefig(path+"S1D_var_rn_a_neg.eps")



