!To use this MCMC engine, replace subroutine 'straightline' with your likelihood subroutine/function at two places in this code.
!To find these two places search 'call for likelihood'
!An example subroutine (straightline) is given after this main program body (search 'subroutine straightline(parameters,likelihood)')
!Run this program with your favorite fortran compiler as: 'gfortran mcmc.f90' and then './a.out'
!About output file: In this version output will be written in file name fort.12. First column: Posterior probability, 
!		    second column: how many times chain came back to this point, third column and onwards: value of parameters.
program main
implicit none

! Defining variables/arrays as integers or real
integer i,j,numberofparameters,numberofsteps,idum,multiplier,burn_in
parameter (numberofparameters=7, numberofsteps=200000)	! Set number of parameters and number of MCMC steps
real parameters(numberofparameters,4),parametersi(numberofparameters)
real stepmultiplier,posteriorold,posteriornew,parametersold(numberofparameters)
real parametersnew(numberofparameters),randomnumber01,likelihood
real gasdev, ran1,acceptedpoints,f_accepted
double precision posteriorratio
!===============================================================================
external gasdev,ran1	!External functions used; gasdev: Gaussian random number, ran1: random number between (0,1)

idum=1379688	! random number seed (integer)
stepmultiplier=2.0	!Each parameter step is multiplied by this number. Reduce to get higher acceptance rate.
burn_in=1		!number of steps in burn in, i.e., initial step points to be removed (only an integer)
!===============================================================================
!parameters (m,n) where m is number number of the parameter and n decides if that is mean, starting, end of SD as follows:
parameters(1,1)=50.	!mean value [for forecasts this may be the fiducial value]
parameters(1,2)=20.	!starting value
parameters(1,3)=80.	!last value
parameters(1,4)=0.05	!standard deviation

parameters(2,1)=30.
parameters(2,2)=1.
parameters(2,3)=60.
parameters(2,4)=0.08

!Uncomment these/following arrays if more than 2 parameters. Add more similar arrays with same definitions if more than 5 parameters
parameters(3,1)=15.	
parameters(3,2)=-5.
parameters(3,3)=25.
parameters(3,4)=0.08

parameters(4,1)=10.
parameters(4,2)=-10.
parameters(4,3)=30.
parameters(4,4)=0.08

parameters(5,1)=0
parameters(5,2)=-10
parameters(5,3)=10
parameters(5,4)=1

parameters(6,1)=0
parameters(6,2)=-10
parameters(6,3)=10
parameters(6,4)=1

parameters(7,1)=1
parameters(7,2)=0.5
parameters(7,3)=1.5
parameters(7,4)=0.02
!===============================================================================
!Initial random point. This is the first point of the chain (parametersi). 
do i=1,numberofparameters
	parametersi(i) = parameters(i,2) + ran1(idum)*(parameters(i,3)-parameters(i,2))
	parametersold(i) = parametersi(i)	
end do


parametersold(1) = 50.0
parametersold(2) = 30.0
parametersold(3) = 15.0
parametersold(4) = -10.0
parametersold(5) = 0.0
parametersold(6) = 0.0
parametersold(7) = 1.0

!	call for likelihood with parametersold as posteriorold
	call lightcurveCrescent(parametersold,posteriorold)
!	posteriorold = (posteriorold)
!===============================================================================
!===============================================================================
!starting the chains
multiplier=0	!set these values to zero, later they will add to give numbers.
acceptedpoints=0.
do i=1,numberofsteps
	if (mod(i,5000).eq.0) then
		write(*,*) i,"steps completed!!"
	end if

	idum = idum + i			!Random seed is changing.
	multiplier = multiplier + 1	
	do j=1,numberofparameters	!new step in the parameter step is chosen with random number.
		parametersnew(j) = parametersold(j) + gasdev(idum)*parameters(j,4)*stepmultiplier
	end do

	if (parametersnew(1).lt.0.0.or.parametersnew(2).lt.0.0.or.parametersnew(2).gt.&
		parametersnew(1).or.parametersnew(1).gt.&
		100.0.or.(abs(parametersnew(3))+abs(parametersnew(4))).gt.&
		parametersnew(1).or.(abs(parametersnew(5))).gt.50.or.(abs(parametersnew(6))).gt.&
		50.or.parametersold(7).lt.0.0.or.parametersold(7).gt.5.0) then
		posteriornew = -1d35
	else
!	call for likelihood with parametersnew as posteriornew
	call lightcurveCrescent(parametersnew,posteriornew)
!	posteriornew = exp(posteriornew)
	end if

!	write(*,*) parametersnew,posteriornew

	posteriorratio = exp(posteriornew - posteriorold)	!Ratio of new posterior probability to the old
	randomnumber01=ran1(idum)			!random number between (0,1)

	if (posteriorratio.lt.randomnumber01) then
		goto 100	!if posteriorratio < randomnumber01, then chain goes back to previous step
	else			!if posteriorratio > randomnumber01, then chain go to parameternew become parameterold (so the point is accepted)

		acceptedpoints = acceptedpoints + 1.	!number of accepted points increases
		f_accepted  = acceptedpoints/i		!acceptance ratio is inreasing
		do j=1,numberofparameters		!parametersnew become parameterold
			parametersold(j) = parametersnew(j)
		end do
		posteriorold=posteriornew		!posteriornew becomes posteriorold
		if (i.gt.burn_in) then
			!7863,2000
			write(78613,2000) (posteriorold),multiplier,parametersold(1),&
				parametersold(2),parametersold(3),parametersold(4),parametersold(5),&
				parametersold(6),parametersold(7)
				!writing the accepted points, its multiplier and posterior in file fort.12
			2000 format(E15.7, i5, f10.4, f10.4, f10.4, f10.4, f10.4, f10.4, f10.4)
		end if
		multiplier = 0
	end if
	
100 continue	
end do			
!===============================================================================
!===============================================================================					!Chain terminated
write(*,*) 'Accepted fraction',f_accepted*100.,'percent'	!writing accepted fraction in the terminal at the end of the chain
end

!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
!Replace this subroutine with your own likelihood subroutine
subroutine straightline(parameters,likelihood)
implicit none

integer i,j,nx,numberofparameters
parameter (nx=11,numberofparameters=2)
real m,x,c,y,z,likelihood,x_data(nx),y_data(nx),chi2,percenterror
real parameters(numberofparameters)

	m=parameters(1)		!first parameter as slope of the line
	c=parameters(2)		!second parameter as the intercept of the line
	percenterror = 0.02	!error percentage in data points

	open (2,file='fort.11111') 	!Reading data file for x and y(x)
		do j=1,nx
			read (2,*) x_data(j),y_data(j)	!Reading first array as x and second as y(x)
		end do
	close(2)			!closing file: Very important if MCMC is to run

	chi2=0.				!setting chi^2 to zero at the beginning
do i=1,nx
	x = 0. + float(i-1)/(nx-1)*10.	!making an array of x
	y = m*x + c 			!Calculating corresponding y(x) using the m and c from MCMC program
	chi2 = chi2 + ((y_data(i)-y)/(percenterror*y))**2.	!Calculating chi2 or how good this line is fitting the data file.
end do

likelihood = exp(-chi2/2.)		!likelihood is exponential of minus chi^2 by 2.

end subroutine

!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
!Gaussian random number between -1 and 1 with mean 0
      FUNCTION gasdev(idum)
      INTEGER idum
      REAL gasdev
!CU    USES ran1
      INTEGER iset
      REAL fac,gset,rsq,v1,v2,ran1
      SAVE iset,gset
      DATA iset/0/

      if (iset.eq.0) then
1       v1=2.*ran1(idum)-1.		!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
        v2=2.*ran1(idum)-1.
        rsq=v1**2+v2**2
        if(rsq.ge.1..or.rsq.eq.0.)goto 1
        fac=sqrt(-2.*log(rsq)/rsq)
        gset=v1*fac
        gasdev=v2*fac
        iset=1
      else
        gasdev=gset
        iset=0
      endif
      return
      END function



!Random number from uniform distribution (0,1)
      FUNCTION ran1(idum)
      INTEGER idum,IA,IM,IQ,IR,NTAB,NDIV
      REAL ran1,AM,EPS,RNMX
      PARAMETER (IA=16807,IM=2147483647,AM=1./IM,IQ=127773,IR=2836,NTAB=32,NDIV=1+(IM-1)/NTAB,EPS=1.2e-7,RNMX=1.-EPS)
      INTEGER j,k,iv(NTAB),iy
      SAVE iv,iy
      DATA iv /NTAB*0/, iy /0/
      if (idum.le.0.or.iy.eq.0) then
        idum=max(-idum,1)
        do 11 j=NTAB+8,1,-1
          k=idum/IQ
          idum=IA*(idum-k*IQ)-IR*k
          if (idum.lt.0) idum=idum+IM
          if (j.le.NTAB) iv(j)=idum
11      continue
        iy=iv(1)
      endif
      k=idum/IQ
      idum=IA*(idum-k*IQ)-IR*k
      if (idum.lt.0) idum=idum+IM
      j=1+iy/NDIV
      iy=iv(j)
      iv(j)=idum
      ran1=min(AM*iy,RNMX)
      return
      END function


