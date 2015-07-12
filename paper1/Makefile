all:
	pdflatex ms
	bibtex ms
	pdflatex ms
	pdflatex ms
	dvipdfm ms

clean:
	rm -f *.log *.aux *.dvi *.blg *~
	rm -f msdiff.ps msdiff.bbl
	rm -f ms.ps ms.bbl
