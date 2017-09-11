import numpy
import scipy
from scipy import integrate
import m_general
from matplotlib import pyplot


def magnification_function(p, mu_0, C_0):
    if p < 0:
        return mu_0
    elif p == 0:
        return mu_0
    else:

        return mu_0 + C_0/p**0.5
        

def crescent_1D(S_0, R_p, R_n, p_sp, p_sn,  p):
    factor = 2* S_0/numpy.pi/(R_p**2-R_n**2)
    if (R_p**2 > (p-p_sp)**2) and (R_n**2 > (p-p_sn)**2):
        value = ((R_p**2-(p-p_sp)**2))**0.5 -  ((R_n**2-(p-p_sn)**2))**0.5
    elif (R_p**2 > (p-p_sp)**2) and (R_n**2 < (p-p_sn)**2):
        value = (R_p**2-(p-p_sp)**2)**0.5 
    else:
        value = 0
    return value*factor 

def gaussian_1D(S_0G, sig, p_s, p):
    return S_0G/((2*numpy.pi)**0.5*sig)*numpy.exp(-(p-p_s)**2/2/sig**2)

def disk_1D(S_0D, R, p_s, p):
    factor = 2* S_0D/numpy.pi/R * (1-(p-p_s)**2/R**2)**0.5
    if R**2 > (p-p_s)**2:
        return factor
    else:
        return 0


def function(p, mu_0, C_0, S_0, parameters, type = "crescent"):  #gaussian parameters= [sig, p_s], disk parameters= [ R, p_s] 
    if type not in ["crescent", "disk", "gaussian"]:
	print "Shape of source unrecognized"

    if type == "crescent":
    	return magnification_function(p, mu_0, C_0)* crescent_1D(S_0, parameters[0], parameters[1], parameters[2], parameters[3], p)
    if type == "disk":
        return magnification_function(p, mu_0, C_0)* disk_1D(S_0, parameters[0], parameters[1], p)
    if type == "gaussian":
        return magnification_function(p, mu_0, C_0)* gaussian_1D(S_0, parameters[0], parameters[1], p)


def flux_value( mu_0, C_0, S_0, parameters_v,  type_v = "crescent"  ):
    func = lambda p: function(p, mu_0, C_0, S_0, type = type_v , parameters = parameters_v)
    value   = integrate.quad(func, -10, 10, limit = 200)[0]
    return value

def crescent_2D(S_0, R_p, R_n, p_sp, p_sn, q_sp, q_sn, p, q):
    factor = S_0/numpy.pi/(R_p**2-R_n**2)
    if (R_p**2 - (p-p_sp)**2-(q-q_sp)**2 > 0) and ((R_n**2 - (p-p_sn)**2 - (q-q_sn)**2) > 0):
	value = 0
    elif (R_p**2 - (p-p_sp)**2 - (q-q_sp)**2 > 0) and (R_n**2 - (p-p_sn)**2 - (q-q_sp)**2 < 0):
	value = 1.
    else:
	value = 0
    return value*factor


def centroid_offcenter(R_p, R_n, a):
    func = lambda x: crescent_1D(1., R_p, R_n,0,a, x)
    value_above, value_below = 1., 0.
    y = -R_p
    while (value_above - value_below)**2>0.0000001:
    	value_above = integrate.quad(func, y, 10*R_p)[0]
    	value_below = integrate.quad(func, -10*R_p, y)[0]
        y = y+ 0.001
    centroid = y
    return centroid

def half_radius(R_p, R_n, a, c):
    r = R_p/4.
    value = 0.0
    print "c", c
    print "computing half radius"
    while (value < 0.5) and (r < 2*R_p):
        r = r + max([0.001*(0.5-value)/0.0055555,0.001])
	value, error = integrate.dblquad(lambda x, y: crescent_2D(1.0, R_p, R_n, c, a+c, 0., 0., x,y),-r, r, lambda x: -(r**2-x**2)**0.5, lambda x:(r**2-x**2)**0.5)
    	print value, error, r
    return r

    
S_0 = 1.0
C_0 = 1.0
mu_0 = 1.0

#Crescent
R_p = 1.0
R_n = 0.4
a  = 0.3
a1 = -a
#Disk
R   = 1.0
#Gaussian
sig = 0.3


#b < (R_p - R_n)**2 - a**2 

centroid_a = centroid_offcenter(R_p, R_n, a)
centroid_a1 = centroid_offcenter(R_p, R_n, a1)
#centroid_a3 = centroid_offcenter(R_p, R_n, 0)
#print centroid_a1, centroid_a2, centroid_a3
#r_half = half_radius(R_p, R_n, a, centroid_a)
r_half = 0.763
#print "r_half", r_half, "Centroid", centroid_a
R      = r_half*2.**0.5
sig    = r_half/(-2.*numpy.log(0.5))**2
print "r_disk", R, "sigma", sig 


#limits of the path on the Oy axis
y_min = -2.*r_half
y_max = 2.*r_half

p_s_array = numpy.arange(y_min,y_max,0.01, dtype = float)
p_s_array = numpy.array(p_s_array)

#light curve data
l_c1 = []
l_c2 = []
l_g = []
l_d = []
for p_s in p_s_array:
    parameters_v= [R_p, R_n, p_s, p_s+a1]
    value_crescent = flux_value( mu_0, C_0, S_0, parameters_v, type_v = "crescent")
    l_c1 = l_c1 + [value_crescent]
    parameters_v= [R_p, R_n, p_s, p_s+a]
    value_crescent = flux_value( mu_0, C_0, S_0, parameters_v, type_v = "crescent")
    l_c2 = l_c2 + [value_crescent]

    value_gaussian = flux_value( mu_0, C_0, S_0,type_v = "gaussian", parameters_v= [sig, p_s])
    l_g = l_g + [value_gaussian]
    value_disk = flux_value( mu_0, C_0, S_0,type_v = "disk"    , parameters_v= [R, p_s])
    l_d = l_d + [value_disk]

l_c1, l_c2, l_d, l_g = numpy.array(l_c1),numpy.array(l_c2), numpy.array(l_d), numpy.array(l_g)

pyplot.figure(figsize=(8.7,7))


pyplot.plot(p_s_array/r_half, l_c1-1,"k-",label="forward crescent")
pyplot.plot(p_s_array/r_half, l_c2-1,"b-",label = "backward crescent")
pyplot.plot(p_s_array/r_half, l_d-1, "g-", label = "disc")
pyplot.plot(p_s_array/r_half, l_g-1, "r-", label="gaussian")
pyplot.legend(loc = 4)
pyplot.xlabel("t [$r_{1/2}$/$v_{p}$]", fontsize = 20)
pyplot.ylabel("m [$C_{0}$/$r_{1/2}^{1/2}$] - m$_0$", fontsize = 20)
pyplot.ylim((0,2))

pyplot.tick_params(axis='both', which='major', labelsize=20)
pyplot.tick_params(axis='both', which='minor', labelsize=20)



pyplot.savefig("4source_magnification.eps")

#pyplot.savefig("/zbox/data/mihai/GIT_ML/figures2/4source_magnification.eps")


l_c3 = []
l_c4 = []
l_c5 = []
l_c6 = []
l_c7 = []
l_c8 = []

#for p_s in p_s_array:
#    parameters_v= [R_p, R_n, p_s, p_s+a]
#    value_crescent = flux_value( mu_0, C_0, S_0, parameters_v, type_v = "crescent")
#    l_c1 = l_c1 + [value_crescent]
#    parameters_v= [R_p, R_n, p_s, p_s+a/2.]
#    value_crescent = flux_value( mu_0, C_0, S_0, parameters_v, type_v = "crescent")
#    l_c2 = l_c2 + [value_crescent]

#    parameters_v= [R_p, R_n, p_s, p_s+a*0]
#    value_crescent = flux_value( mu_0, C_0, S_0, parameters_v, type_v = "crescent")
#    l_c3 = l_c3 + [value_crescent]
#    parameters_v= [R_p, R_n, p_s, p_s-a/2.]
#    value_crescent = flux_value( mu_0, C_0, S_0, parameters_v, type_v = "crescent")
#    l_c4 = l_c4 + [value_crescent]


#    parameters_v= [R_p, R_n, p_s, p_s-a]
#    value_crescent = flux_value( mu_0, C_0, S_0, parameters_v, type_v = "crescent")
#    l_c5 = l_c5 + [value_crescent]



 
#l_c1,l_c2, l_c3, l_c4, l_c5 = numpy.array(l_c1),numpy.array(l_c2), numpy.array(l_c3), numpy.array(l_c4), numpy.array(l_c5)

#pyplot.plot(p_s_array, l_c1-1,"k-",label="a = 0.30 $R_{p}$")
#pyplot.plot(p_s_array, l_c2-1,"b-",label = "a = 0.15 $R_{p}$")
#pyplot.plot(p_s_array, l_c3-1, "g-", label = "a = 0")
#pyplot.plot(p_s_array, l_c4-1, "r-", label="a = -0.15 $R_{p}$")
#pyplot.plot(p_s_array, l_c5-1,"c-",label = "a = -0.30 $R_{p}$")

#pyplot.legend(loc = 4)
#pyplot.xlabel("t [$R_{p}$/$v_{p}$]")
#pyplot.ylabel("m [$C_{0}$/$R_{p}^{1/2}$] - $m_{0}$ ")
#pyplot.show()
#pyplot.savefig("/home/ics/mihai/4avar_magnification.png")




#pyplot.plot(p_s_array, l_c1, "g-", p_s_array, l_c2, "b-", p_s_array, l_c3, "r-", p_s_array, l_c4, "y-", p_s_array, l_c5, "c-")

#x = p_s_array
#y = l_m
#x_label ="time"
#y_label ="F(t)"
#file_save = "/home/ics/mihai/Documents/Papers/Microlensing_Lightcurves_of_Crescent_Shaped_Sources_Around_Fold_Singularities/paper1/lightcurves_control.png"
#pyplot.savefig(file_save)
#for p_s in p_s_array:
#    parameters_v= [R_p, 0.7, p_s, p_s+a]
#    value_crescent = flux_value( mu_0, C_0, S_0, parameters_v, type_v = "crescent")
#    l_c1 = l_c1 + [value_crescent]
#    parameters_v= [R_p, 0.6, p_s, p_s+a]
#    value_crescent = flux_value( mu_0, C_0, S_0, parameters_v, type_v = "crescent")
#    l_c2 = l_c2 + [value_crescent]

#    parameters_v= [R_p, 0.5, p_s, p_s+a]
#    value_crescent = flux_value( mu_0, C_0, S_0, parameters_v, type_v = "crescent")
#    l_c3 = l_c3 + [value_crescent]

#    parameters_v= [R_p, 0.4, p_s, p_s+a]
#    value_crescent = flux_value( mu_0, C_0, S_0, parameters_v, type_v = "crescent")
#    l_c4 = l_c4 + [value_crescent]


#    parameters_v= [R_p, 0.3, p_s, p_s+a]
#    value_crescent = flux_value( mu_0, C_0, S_0, parameters_v, type_v = "crescent")
#    l_c5 = l_c5 + [value_crescent]


#    parameters_v= [R_p, 0.2, p_s, p_s+a]
#    value_crescent = flux_value( mu_0, C_0, S_0, parameters_v, type_v = "crescent")
#    l_c6 = l_c6 + [value_crescent]
  
#    parameters_v= [R_p, 0.1, p_s, p_s+a]
#    value_crescent = flux_value( mu_0, C_0, S_0, parameters_v, type_v = "crescent")
#    l_c7 = l_c7 + [value_crescent]


#    parameters_v= [R_p, 0.0, p_s, p_s+a]
#    value_crescent = flux_value( mu_0, C_0, S_0, parameters_v, type_v = "crescent")
#    l_c8 = l_c8 + [value_crescent]

#l_c1,l_c2   = numpy.array(l_c1),numpy.array(l_c2)#, l_c3, l_c4, l_c5, l_c6, l_c7, l_c8 = numpy.array(l_c1),numpy.array(l_c2), numpy.array(l_c3), numpy.array(l_c4), numpy.array(l_c5), numpy.array(l_c6), numpy.array(l_c7), numpy.array(l_c8)



#pyplot.plot(p_s_array, l_c1, "g-", p_s_array, l_c2, "b-")#, p_s_array, l_c3, "r-", p_s_array, l_c4, "y-", p_s_array, l_c5, "c-", p_s_array, l_c6, 'k-',  p_s_array, l_c7, 'c-',  p_s_array, l_c8, 'r-')
#pyplot.show()
#file_save = "/home/ics/mihai/Documents/Papers/Microlensing_Lightcurves_of_Crescent_Shaped_Sources_Around_Fold_Singularities/paper1/lightcurves_control_2.png"
#pyplot.savefig(file_save)

