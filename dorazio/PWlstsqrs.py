import sys
import numpy
import scipy
import pylab
import math
import radialProfile
from StringIO import StringIO
from numpy import *
from scipy import *
from pylab import *
from math import *

#############################
def pwspin(NRO, Nup, a, mu0, rgrid, Lpow, deriv, seqnum, data, offsetx, offsety, vmx):

 ### Universal constants read from file

 ###number of geodesics
 nn=len(data)/(Nup+1)

 ###total length of padded image
 Npad=NRO*10.0#int((nn)/20)

 ###start of nonzero entries in padded image
 cor=int(Npad/2) - int(NRO/2)

 ###outer edge of accretion disk
 rout=15.0#+seqnum/float(seqlen)*12.0

 ### file specific constants
 ufa=zeros(nn)
 alpha=zeros(nn)
 beta=zeros(nn)

 ### Luminosity as a function of Impact Params
 Lra=zeros(( (Npad),(Npad) ))


 ##########################
 #Fill final radius arrays
 for i in range (int((nn-1))):
  ufa[i] = data[Nup+i*(Nup+1)][0]

 #Fill alpha and beta arrays
 for i in range (int((nn-1))):
  alpha[i] = data[i*(Nup+1)][0]
  beta[i]  = data[i*(Nup+1)][1]

 ##########################
 #Define Kerr parameters for ISCO (prograde only!)
 r = 1.0/ufa
 M = 1.0

###Define margianlly stable orbits in Kerr spacetime#######
 Z1  = 1+(1-a**2/M**2)**(1.E0/3.E0) * ( ( 1+a/M )**(1.E0/3.E0) + ( 1-a/M )**(1.E0/3.E0) )
 Z2  = ( 3*(a/M)**2+Z1**2 )**(1.E0/2.E0)
 rms = M*( 3+Z2 - ( (3-Z1)*(3+Z1+2*Z2) )**(1.E0/2.E0) )

 C3  = r>=rms


####RELATIVISTIC BEAMING PARAMS#############
 spec_indx = 0.7 #synchrotron spectral index
 phi       = arctan(alpha/beta) #angle around top of brightness profile 

 for i in range (0,len(alpha)):   #fix arctan symmetries
  if (beta[i]>=0.0):
   phi[i]=-phi[i]
###vmx is a user defind parameter = v/c which is passed to PWleastsqrs.py
 vmax = vmx*sin(acos(mu0)) #Fraction of speed of light of disk rotation along LOS
 vr   = (rms/r)**(1.0/2.0)*vmax  #keplerian Disk has v prop to 1/sqrt(r)
 Bet  = vr * numpy.sin( phi )    #Beta=v/c as a function of azimuth (phi)


###Define L(r) with REL BEAMING ##########################
 for i in range(  int(cor), int(cor + NRO) ):
  for j in  range(  int(cor), int(cor + NRO) ):
   if (r[(j-cor)+(i-cor)*NRO]<=rout and C3[(j-cor)+(i-cor)*NRO]):
    #BEAMING EQUATION: L_{obs}=L_{instrinsic}*sqrt[(1+B)/(1-B)]^(3-spec_indx)
    Lra[j][i] = (  (ufa[(j-cor)+(i-cor)*NRO])**( Lpow )  ) * (sqrt( (1+Bet[(j-cor)+(i-cor)*NRO])/(1-Bet[(j-cor)+(i-cor)*NRO]) ))**(3.0-spec_indx)




###Define L(r) without REL BEAMING ##########################
# for i in range(  int(cor), int(cor + NRO) ):
#  for j in  range(  int(cor), int(cor + NRO) ):
#   # Now asign intrinsic luminosity for photons which eminated
#   # from region between rms and rout
#   if (r[(j-cor)+(i-cor)*NRO]<=rout and C3[(j-cor)+(i-cor)*NRO]):
#    Lra[j+offsety][i+offsetx] = (ufa[(j-cor)+(i-cor)*NRO])**( Lpow )
###############################################################
  

#################Some previous Luminosty profiles #####################
#3.0*M*Md/(2.0*(r[(j-cor)+(i-cor)*NRO])**3)*( 1-B*(rms/r[(j-cor)+(i-cor)*NRO])**(1.E0/2.E0) )
#(ufa[(j-cor)+(i-cor)*NRO])**( Lpow )
 ### NY 2008 ADAF two temp ###
##  for i in range(  int(cor), int(cor + NRO) ):
##   for j in  range(  int(cor), int(cor + NRO) ):
##    if (r[(j-cor)+(i-cor)*NRO]<=rout and C3[(j-cor)+(i-cor)*NRO]):
##     if (10.0*ufa[(j-cor)+(i-cor)*NRO] > 1.0):
##      Lra[j][i] = 10.0*(ufa[(j-cor)+(i-cor)*NRO])**( Lpow ) + 1.0
##     if (10.0*ufa[(j-cor)+(i-cor)*NRO] <= 1.0):
##      Lra[j+offset][i+offset] = 20.0*(ufa[(j-cor)+(i-cor)*NRO])**( Lpow ) 
#####################################################################3



 #########################  
 ### FFT ###
 IfLa = fft2(Lra)




 ########################
 ### shift FFT to be centerad at 0 ###  
 IfLas=fftpack.fftshift(IfLa)


 ### Get rid of extra zeros in 2-d ifft ###
 ii = int(-1)
 jj = int(0)
 IfLas_n=zeros(  ((NRO),(NRO)), 'complex')
 for i in range(  int(cor), int(cor + NRO) ):
  ii = ii+1
  for j in  range(  int(cor), int(cor + NRO) ):
   IfLas_n[jj][ii] = IfLas[j][i]
   jj = jj+1
   if (j==int(cor + NRO-1)):
    jj=0


 ### imaginary part ##
 IfaIm = IfLas_n.imag


 #########################
 ### compute power (sqrd ifft) ###
 pwIm   = abs(IfaIm)**2
 If2mag = abs(IfLas_n)**2



 ########################
 ### Azimuthal Average ###
 pw1dIm  = radialProfile.azimuthalAverage(pwIm)
 pw1dmag = radialProfile.azimuthalAverage(If2mag)
 
 ###########################
 ### ANGULAR AVG ###
 pwang=radialProfile.angularAverage(pwIm)

 ## SMOOTH ###
 from savitzky_golay import *
 numpnts     = 3
 polydeg     = 2
 coeff       = calc_coeff(numpnts, polydeg, diff_order=deriv)
 pwIm_smooth = smooth(pw1dIm, coeff)

### NORMALIZE POW ###
 pwImmx      = max(pwIm_smooth)
 pwmagmx     = max(pw1dmag)
 pwIm_smooth = pwIm_smooth/pwmagmx
 pwang       = pwang/pwmagmx
 pwIm        = pwIm/pwmagmx

 ###########################

 ### The smoothed azimuthally averaged imaginary power spectrum is returned ###
 return pwIm_smooth


