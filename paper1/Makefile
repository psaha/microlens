all:
	latex msdiff
	bibtex msdiff
	latex msdiff
	latex msdiff
	dvipdfm msdiff
	latex ms
	bibtex ms
	latex ms
	latex ms
	dvipdfm ms

clean:
	rm -f *.log *.aux *.dvi *.blg *~
	rm -f msdiff.*
	rm -f ms.ps ms.bbl
