FILES := file1.pdf file2.pdf file3.pdf
AUXFILES := $(FILES:.pdf=.aux)
LOGFILES := $(FILES:.pdf=.log)

all: $(FILES)

%.pdf: %.tex
	pdflatex $<

.PHONY: clean
clean:
	$(RM) $(FILES) $(AUXFILES) $(LOGFILES)
