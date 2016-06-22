all: lcurv.f90
	f2py -c lcurv.f90 -m lcurv

check: lcurv.f90
	gfortran -c lcurv.f90

clean:
	rm lcurv.so
	rm -r lcurv.so.dSYM
	rm -r __pycache__

