FILES = file1.pdf file2.pdf file3.pdf

all: $(FILES)

%.pdf: %.tex
	pdflatex $<

.PHONY: clean
clean:
	$(RM) $(FILES)
