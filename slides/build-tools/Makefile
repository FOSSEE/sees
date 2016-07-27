RST2S5 = $(shell if which rst2s5.py > /dev/null; then echo rst2s5.py; else echo rst2s5; fi)

all: build-tools.html

build-tools.html: build-tools.rst
	$(RST2S5) --theme=small-white $< $@
