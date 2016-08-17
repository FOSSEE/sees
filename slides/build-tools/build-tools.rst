=======================
An introduction to Make
=======================

.. class:: center

    July 27, 2016

    Department of Electrical Engineering,
    IIT Bombay

    :Author: Kumar Appaiah



Agenda
======

- Introduction to build tools

- Makefiles: simple examples

- Writing good make rules

- Advanced concepts


Motivation
==========

- Much of what we write is code that is compiled/built/rendered

- Single run of ``gcc``, ``pdflatex``, etc. is easy

- But what about large code trees, or large documents, bib files etc.?

Motivation
==========

- Simple: create a ``build.sh`` to compile

- Problem: wastes time recompiling even when not needed

- What we really need: something that builds only what is needed based
  on some **rules**

- Potential solutions: ``make``, ``ant``, ``scons``, ``qmake``,
  ``jam`` and many more

- We restrict this treatment to **GNU Make**

Example
=======
``mylib.h``::

  int myadd(int a, int b);

``mylib.c``::
    
  int myadd(int a, int b) { return a + b; }

``main.c``::

  #include "mylib.h"
  int main(void) { int a = myadd(2, 3); return 0; }

Example
=======

.. image:: Figures/example-dependencies.svg
    :scale: 50%
    :align: center

Note that changing ``mylib.h`` would require rebuilding ``main.c`` and
``mylib.c``, but not so if you edit any of the C files.

Steps to build
==============

1. ``gcc -c main.c -o main.o``
2. ``gcc -c mylib.c -o mylib.o``
3. ``gcc -o main main.o mylib.o``

How do we write a Makefile for this?

Our first Makefile
==================
Format::

  target: prerequisites
  	recipe

Rule for the build::

  main: main.o
  	gcc -c main.c -o main.o
  	gcc -c mylib.c -o mylib.o
  	gcc -o main main.o mylib.o

Our first Makefile
==================
Run::

  # make
  gcc -c main.c -o main.o
  gcc -c mylib.c -o mylib.o
  gcc -o main main.o mylib.o
  # make
  make: 'main' is up to date.

Issue: Even updating main.c will cause a recompile of all files.

Our first Makefile v2
=====================
Makefile::

  main: main.o mylib.o
  	gcc -o main main.o mylib.o

  main.o: main.c mylib.h
  	gcc -c -o main.o main.c

  mylib.o: mylib.c mylib.h
  	gcc -c -o mylib.o mylib.c

Cleaning up: phony rules
========================
We can use ``make`` to handle cleanups as well::

  clean:
  	rm mylib.o main.o main

Issue: what if you create a file called ``clean``? Ignore it by
calling it a ``.PHONY``::

  .PHONY: clean

  clean:
  	rm mylib.o main.o main

Simplifying with variables, implicit rules
==========================================
Example::

  objects := main.o mylib.o
  main: $(objects)

  main.o: mylib.h
  mylib.o: mylib.h
  .PHONY: clean
  clean:
  	rm main $(objects)

Another style
=============
Example::

  objects := main.o mylib.o
  main: $(objects)

  $(objects): mylib.h

  .PHONY: clean
  clean:
  	rm main $(objects)

Another style
=============
Suppose that ``main.o`` depends on ``mylib.h`` and ``main.h`` and ``mylib.o`` depends
on ``mylib.h`` and ``utils.h``, then::

  objects := main.o mylib.o
  main: $(objects)

  $(objects): mylib.h
  main.o: main.h
  mylib.o: utils.h

  .PHONY: ...

Handling errors during clean
============================

- As you may have seen in bash, commands return status messages

- ``make`` passes the status to the shell

- Usually useful, except when using the ``clean`` rule

- Avoid error status with ``clean`` rule by prepending the commands
  with a hyphen

Handling errors during clean
============================
Example to handle ``clean``::

  objects := main.o mylib.o
  main: $(objects)

  $(objects): mylib.h

  .PHONY: clean
  clean:
  	-rm main $(objects)

Rules for multiple targets
==========================
Example::

  FILES := file1.pdf file2.pdf file3.pdf
  AUXFILES := $(FILES:.pdf=.aux)
  LOGFILES := $(FILES:.pdf=.log)
  all: $(FILES)
  %.pdf: %.tex
  	pdflatex $<
  .PHONY: clean
  clean:
  	$(RM) $(FILES) $(AUXFILES) $(LOGFILES)


Handling shell requests
=======================
Example: This presentation is built with ``rst2s5``. But some people
have it in their computer as ``rst2s5.py``. To handle both::

  RST2S5 = $(shell if which rst2s5.py > /dev/null; \
  then echo rst2s5.py; else echo rst2s5; fi)
  all: build-tools.html
  build-tools.html: build-tools.rst
	$(RST2S5) --theme=small-white $< $@
  .PHONY: clean
  clean:
  	$(RM) build-tools.html
