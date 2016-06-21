program main
  implicit none
  integer ipix,ipix1,pixmax,i1,i2
  parameter(ipix=1000,ipix1=500)
  integer*2 pix(ipix,ipix),pix1(ipix1,ipix1)
  real pix_real(ipix,ipix)
  common /magmap/ pix_real
  character*80 fileread
  real parameters(7)


      fileread  = 'IRIS567'
      write(*,*)' reading from file ',fileread
      open(3,file=fileread ,status='old',form='unformatted')
      read(3) pix,pix1
      close(3)
      write(*,*) '                    ...  done'
       pixmax = 0
       do i1 = 1,ipix
          do i2 = 1,ipix
	     pixmax = max(pixmax,pix(i2,i1))
	     pix_real(i2,i1) = 10**(0.4*(float(pix(i2,i1)-1024)/256.0))
          enddo
       enddo


  parameters(1) = 0.0
  parameters(2) = 0.0
  parameters(3) = 1.0
  parameters(4) = 15.0
  parameters(5) = 0.7
  parameters(6) = 0.4
  parameters(7) = 0.1
  call mockdata(parameters)

end

subroutine mockdata(parameters)
  implicit none
  integer n,nsim,nobs
  real parameters(7),simul(1000),observ(1000),error
  common /data/ observ,nobs,error
  call lightcurve(parameters,simul,nsim)
  nobs = nsim
  open(26,file='data_simul.txt')
  do n=1,nobs
    observ(n) = simul(n)
    write(26,*) n,observ(n)
  end do
  close(26)
  write(*,*) 'Done',nobs
  return
end subroutine

subroutine lnprob(parameters,likelihood)
  implicit none
  integer n,nsim,nobs,nlo,nhi
  real parameters(7),simul(1000),observ(1000),error,norm,chis,likelihood
  common /data/ observ,nobs,error
  nlo = nint(parameters(1))
  nhi = nint(parameters(2))
  norm = parameters(3)
  call lightcurve(parameters,simul,nsim)
  chis = 0
  do n=1,nobs
     chis = chis + ((norm*simul(n)/observ(n)-1)/error)**2
  end do
  likelihood = -chis/2
  return
end subroutine


subroutine lightcurve(parameters,simul,nsim)
  implicit none
  integer ipix
  parameter(ipix=1000)
!  integer*2 pix(ipix,ipix),pix1(ipix1,ipix1)
  real  pix_real(ipix,ipix)
  common /magmap/ pix_real
  integer nsim
  real simul(1000)
  integer pixlow,i1,i2,iii,i0,ixxx,iyyy, &
       ilines,iamp,ipoints,ix,iy,i
  double precision aaa,x1,x2,y1,y2,slope, alpha,sinalpha,cosalpha,x0, &
       y0,x_end,y_end,x_start,y_start,x_diff,y_diff,xxx,yyy,value
  real data_crescent1(4*ipix),data_crescent2(4*ipix)
  character*80 fileread
  parameter(ipoints = 505)
  real  x(ipoints),y(ipoints), xx(ipoints),yy(ipoints)
  real Rp,Rn,a,b,norm,parameters(7),likelihood
  
  Rp = parameters(4)
  Rn = parameters(5)*Rp
  a = parameters(6)*Rp
  b = parameters(7)*Rp
!*
!* name of magnification pattern to be read:
!*
      fileread  = 'IRIS567'
!*
      x1 = 490.
      y1 = 900.
      x2 = 550.
      y2 = 10.

!      write(*,*)' reading from file ',fileread
!      open(3,file=fileread ,status='old',form='unformatted')
!      read(3) pix,pix1
!      close(3)
!      write(*,*) '                    ...  done'
!*

!*
!* determine points of line:
!*
         slope = (y2-y1)/(x2-x1)
         alpha = atan(slope)
         sinalpha = sin(alpha)
         cosalpha = cos(alpha)
!*
!* points for x = 1    and    y = 1:
!*
         y0  =   y1 + (1.0d0-x1)*slope
         x0  =   x1 + (1.0d0-y1)/slope
!*
!*
         if(x0.ge.1.0d0.and.x0.le.dble(ipix))then
            x_start = x0
            y_start = 1.0d0
         elseif(y0.ge.1.0d0.and.y0.le.dble(ipix))then
            x_start = 1.0d0
            y_start = y0
         endif
!*
!* points for x = ipix    and    y = ipix:
!*
         y0  =   y1 + (dble(ipix)-x1)*slope
         x0  =   x1 + (dble(ipix)-y1)/slope
!*
!*
         if(x0.ge.1.0d0.and.x0.le.dble(ipix))then
            x_end = x0
            y_end = y1 + (x_end-x1)*slope
         elseif(y0.ge.1.0d0.and.y0.le.dble(ipix))then
            y_end = y0
            x_end = x1 + (y_end-y1)/slope
         endif
         x_diff = x_end - x_start
         y_diff = y_end - y_start
!*
!* mark pixels along line:
!*
!* AND   determine light curve:
!*
	nsim=0
        do i0 = -2*ipix,2*ipix
	    xxx = x_start + i0*cosalpha
	    yyy = y_start + i0*sinalpha
	    ixxx = nint(xxx)
	    iyyy = nint(yyy)
	    if(ixxx.ge.1+3*Rp.and.ixxx.le.ipix-3*Rp.and.iyyy.ge.1+3*Rp.and.iyyy.le.ipix-3*Rp)then
                call source(Rp,Rn,a,b,xxx,yyy,value,pix_real,ipix)
		nsim = nsim+1
                simul(nsim) = value
            endif
	 enddo
!	write(*,*) 'chi2',chi2
end subroutine

subroutine source(isig,iRn,ia,ib,xxx,yyy,value,pix,ipix)
  integer i1,i2,isig3sq,ix,iy,ipix,test,pixarea	
  real      pix(ipix,ipix),isig,iRn,ia,ib
  double precision normfac,factorex,sigsq2,value,dum,xxx,yyy,delx,dely,dist2,dist3
	
	ix    =  nint(xxx)
	iy    =  nint(yyy)
	delx  =  xxx - dble(ix)
	dely  =  yyy - dble(iy)
!        write(*,*) ix,iy
	isig3 = 3*isig 
	isig3sq = isig3**2
 	sigsq2  = 2.0*dble(isig)**2
	value = 0.0
	
	test=300
	pixarea=0	

	      normfac = 0.0
	      do i1 = -isig3,isig3
		if(iy.eq.test)then
		write(*,*)
		endif 
	         do i2 = -isig3,isig3
!*
!c	            dist2 = i2*i2 + i1*i1
!c		    dist3 = (i2-ib)*(i2-ib) + (i1-ia)*(i1-ia)		
!*
	            dist2 = (i1-delx)**2  + (i2-dely)**2
		    dist3 = (i1-delx-ia)**2  + (i2-dely-ib)**2	
!*
	            if(isig.ne.0)then
  	               if(dist2.le.dble(isig*isig))then	
!c 	                   factorex = exp(-dist2/sigsq2)
	                   factorex = 1.0
			  if(dist3.le.dble(iRn**2))then
			   factorex = 0.0
			  endif
			  if(factorex.eq.1.0)then
			   pixarea=pixarea+1
			  endif	 		
			   dum = pix(ix+i1,iy+i2)
	                   value = value + dum*factorex
	                   normfac = normfac + factorex	
			elseif(dist2.ge.dble(isig**2))then 	
			   factorex = 0.0		
                           dum = pix(ix+i1,iy+i2)
	                   value = value + dum*factorex
	                   normfac = normfac + factorex
	               endif
	            elseif(isig.eq.0)then
                      factorex = 1.0
                      dum = pix(ix+i1,iy+i2)
	              value = value + dum*factorex
	              normfac = normfac + factorex
		    endif
		if(iy.eq.test)then
		write(*,"(i1)",advance="no")  int(factorex)
		endif
	         enddo
	      enddo
	if(iy.eq.test)then
		write(*,*)
		write(*,*)
		write(*,*) 'Area in pixels =', pixarea
	endif 
	
!*
 	value = value/normfac 
		
	return
end subroutine


