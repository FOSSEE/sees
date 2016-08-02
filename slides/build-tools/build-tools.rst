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
