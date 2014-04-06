0all:
	latex ms
	bibtex ms
	latex ms
	latex ms
	dvipdfm -p letter ms
clean:
	rm -f *.log *.aux *.dvi *.blg *~
	rm -f msdiff.ps msdiff.bbl
	rm -f ms.ps ms.bbl
