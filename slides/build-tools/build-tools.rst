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

