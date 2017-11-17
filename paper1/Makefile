all:
	latexdiff msold4.tex ms.tex > msdiff.tex
	latex msdiff
	bibtex msdiff
	latex msdiff
	latex msdiff
	dvipdfm msdiff

clean:
	rm -f *.log *.aux *.dvi *.blg *~
	rm -f msdiff.*
	rm -f ms.ps ms.bbl
