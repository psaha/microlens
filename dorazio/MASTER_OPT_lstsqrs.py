import sys
import subprocess
import scipy
import numpy
import pylab
import math
from scipy import *
from numpy import *
from pylab import *
from math import *
import FUNC_lstsqrs
import PWlstsqrs
#from PWlstsqrs import pwspin
#from FUNC_lstsqrs import fres



### FIXED COMPARISON PLOT
################################################
NRO    = 101      #NROxNRO grid of impact parameters
Nup    = 10       #Nup points along a geodesic
rgrid  = 20.E0    #number of graviational radii corresponding to NRO
angle  = 0.5      #inclination angle for refernce data
Lpowf  = 3.0      #Luminosity power law for refernce data
deriv  = 0        #tells the S-G smoother to only smooth funciton not deriv
spin   = 0.3      #spin for refernce data
vmxfix = 0.0      #v/c for maximum speed of rotating disk (for beaming)
### Fit over offset from center of Bprofile? ###
offon = 0   #Fit over offsets form center? yes=1 no=0
beam  = 1   #Fit over disk roatation beaming parameter? yes=1 no=0
if (offon==1):
 offsetxf=0
 offsetyf=0
elif (offon==0):
 offsetxf=0
 offsetyf=0
 offsetx=0
 offsety=0
 offtx=0
 offty=0

### Number of runs given to xargs ###
seqnum = int(sys.argv[1])
seqlen = int(sys.argv[2])

geokerr = './geokerr'

### CHECKS ###
i=0
plot=0
burn=0
rej=0

### Fixed comparison geokerr input ###
input='''2
%(angle)f
%(spin)f
2
2
-%(rgrid)f %(rgrid)f -%(rgrid)f %(rgrid)f
%(NRO)i %(NRO)i %(Nup)i
#STANDARD
#MUO(1)
#A
#RCUT
#NROTYPE
#A1,A2,B1,B2
#RO,NPHI,NUP''' % {'angle':angle, 'spin':spin, 'NRO':NRO, 'Nup':Nup, 'rgrid':rgrid}


#
### Run geokerr and write the input to stdin. Read the output into 'output'.###
#
process = subprocess.Popen(geokerr, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
print >> process.stdin, input
data  = loadtxt(process.stdout, dtype='float', skiprows=1, usecols=(0,1))

#############################################
##AZ AVG
pwspin1 = PWlstsqrs.pwspin(NRO, Nup, spin, angle, rgrid, Lpowf, deriv, seqnum, data, offsetxf, offsetyf, vmxfix)
##############################################




### START MCMC
seed(seqnum*323)
print 'Running sequence %i/%i' % (seqnum, seqlen)

### Inital seeds ###
if (offon==1):
 while (burn <= 50+random()*50):
  a    = random()
  mu0  = cos(0.5*random()*pi)
  Lpow = random()*5.0
  vmx    = random() 
  #offsetx=int(random()*10) - 5
  #offsety=int(random()*10) - 5
  burn = burn + 1
elif (offon==0):
 while (burn <= 50+random()*50):
  a    = random()
  mu0  = cos(0.5*random()*pi)
  Lpow = random()*5.0
  vmx  = random() 
  burn = burn + 1

print a
print mu0
print Lpow
print vmx
#a=random()
#mu0=cos(0.5*random()*pi)
#Lpow=random()*5.0
### IF STARTING AT FIXED PARAMS###
#mu0=angle
#Lpow=Lpowf
print 'Initial Call'
######################################################  
### INITIAL CALL ###
f = FUNC_lstsqrs.fres(mu0, Lpow, a, offsetx, offsety, vmx, args=[pwspin1, deriv, i, plot, NRO, rgrid, Nup, seqnum, spin, angle, Lpowf, vmxfix])
print "burnin"
####################################################
###################################################"
### MCMC COARSE GRAIN ###
#astep=0.05
#mstep=5*pi/180.0 
#Lstep=0.5
#offstep=1.0
if (beam==0):  #Vary over a, lpow, mu0, fix vmx
 astep = 0.02
 mstep = 3.0*pi/180.0 
 Lstep = 0.2
 vmx=vmxfix
 vstep=0.0
if (beam==1):  #Vary over a and vmx fix angle and Lpow
 astep = 0.02
 vstep = 0.02
 mstep = 0.0 
 Lstep = 0.0
 mu0   = angle
 Lpow  = Lpowf
print 'starting MCMC now %i/%i' % (seqnum, seqlen)
while((f>0.0001)):
 
 #counter   
 i=i+1

 #step a
 at = a - astep + 2*random()*astep
 while (at>1.0 or at<0.0):
  at = a - astep + 2*random()*astep

 #step mu0
 mu0t = cos( acos(mu0) - mstep + 2*random()*mstep )
 while (mu0t>1.0 or mu0t<0.0):
  mu0t = cos( acos(mu0) - mstep + 2*random()*mstep )

 #step Lpow 
 Lpowt = Lpow - Lstep + 2*random()*Lstep
 while(Lpowt < 0.0 ):
  Lpowt = Lpow - Lstep + 2*random()*Lstep
 
#step vmx
 vmxt = vmx - vstep + 2*random()*vstep
 while (vmxt>1.0 or vmxt<0.0):
  vmxt = vmx - vstep + 2*random()*vstep



###OLD####################################
 #mu0t= mu0 - mstep + 2*random()*mstep
 #while (mu0t>1.0 or mu0t<0.0):
  #mu0t = mu0 - mstep + 2*random()*mstep
  #print '%.3f' %mu0t
##########################################

###OLD OFFSET STUFF#####################################
 #if (offon==1): 
  #offtx=int(-offstep + 2*random()*offstep) + offsetx
  #offty=int(-offstep + 2*random()*offstep) + offsety
########################################################

 plot=0
 ###TRIAL EVAL###
 ft = FUNC_lstsqrs.fres(mu0t, Lpowt, at, offtx, offty, vmxt, args=[pwspin1, deriv, i, plot, NRO, rgrid, Nup, seqnum, spin, angle, Lpowf, vmxfix])

 

## Is new value better? ###
 if (f/ft>=1.0): #If it is better take the trial parameters
  a    = at
  mu0  = mu0t
  Lpow = Lpowt
  vmx  = vmxt
  #offsetx=offtx
  #offsety=offty
  plot = 1         #And output or plot new params
  #Call fucntion Eval with new params to reset value of f
  f = FUNC_lstsqrs.fres(mu0, Lpow, a, offsetx, offsety, vmx, args=[pwspin1, deriv, i, plot, NRO, rgrid, Nup, seqnum, spin, angle, Lpowf, vmxfix])

 elif (f/ft>=random()):  ### If not better, accept it with
                         ### probability f/ft (ft bigger)
  a    = at
  mu0  = mu0t
  Lpow = Lpowt
  vmx  = vmxt
  #offsetx=offtx
  #offsety=offty 
  plot = 1
  f = FUNC_lstsqrs.fres(mu0, Lpow,a, offsetx, offsety, vmx, args=[pwspin1, deriv, i, plot, NRO, rgrid, Nup, seqnum, spin, angle, Lpowf, vmxfix])
 else:
  rej=rej+1   # If Not count as rejection

####################################################


rejrate=float(rej)/float(i)

print 'DONE WITH %i/%i' % (seqnum, seqlen)


###record final results of MCMC 
f2=open('MCfinalBEAM_a%.3f_mu0%.3f_Lpow%.3f_vmx%.3f_offx%02i_offy%02i_1DAZ.dat' % (spin, angle, Lpowf, vmxfix, offsetxf, offsetyf), 'a')
s= str(f) +' '+ '%.3f' %mu0 +' '+ '%.3f' %a +' ' + '%.3f' %Lpow + ' ' +'%02i'% offsetx + ' ' +'%02i'% offsety + ' ' +'%.3f' %vmx + '%.3f' % rejrate +'\n'
f2.write(s)  
f2.close()

### throw flag to plot final fit against reference plot
#i=-1
#FUNC_lstsqrs.fres(mu0, Lpow, a, offsetx, offsety, vmx, args=[pwspin1, deriv, i, plot, NRO, rgrid, Nup, seqnum, spin, angle, Lpowf])



