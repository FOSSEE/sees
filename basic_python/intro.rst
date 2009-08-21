=====================
Basic Python Workshop
=====================

This document is intended to be handed out at the end of the workshop. It has
been designed for Engineering students who are Python beginners and have basic
programming skills. The focus is on basic numerics and plotting using Python.

The system requirements:
  * Python - version 2.5.x or newer.
  * IPython 
  * Text editor - scite, vim, emacs or whatever you are comfortable with.

1. Introduction
===============

The Python programming language was created by a dutch named Guido van Rossum.
The idea of Python was conceived in December 1989. The name Python has nothing
to do with the reptilian, but its been named after the 70s comedy series 
"Monty Python's Flying Circus", since it happens to be Guido's favourite 
TV series. 

Current stable version of Python is 2.6.x, although Python 3.0 is also the stable
version, it is not backwards compatible with the previous versions and is hence
not entirely popular at the moment. This material will focus on the 2.6.x series.
  
Python is licensed under the Python Software Foundation License (PSF License) 
which is GPL compatible Free Software license (excepting license version 1.6 and 2.0)
It is a no strings attached license, which means the source code is free to modify
and redistribute.

The Python docs define Python as "Python is an interpreted, object-oriented, 
high-level programming language with dynamic semantics." A more detailed summary
can be found at http://www.python.org/doc/essays/blurb.html. Python is a language that
has been designed to help the programmer concentrate on solving the problem at hand
and not worry about the programming language idiosyncrasies.

Python is a highly cross platform compatible language on account of it being an 
interpreted language. It is highly scalable and hence has been adapted to run on 
the Nokia 60 series phones. Python has been designed to be readable and easy to use

**Resources available for reference**

* Web: http://www.python.org
* Doc: http://www.python.org/doc
* Free Tutorials:
    * Official Python Tutorial: http://docs.python.org/tut/tut.html
    * Byte of Python: http://www.byteofpython.info/
    * Dive into Python: http://diveintopython.org/

**Advantages of Python - Why Python??**

* Python has been designed for readability and ease of use. Its been designed in 
  such a fashion that it imposes readability on the programmer. Python does away
  with the braces and the semicolons and instead implements code blocks based on 
  indentation, thus enhancing readability. 

* Python is a high level, interpreted, modular and object oriented language.
  Python performs memory management on its own, thus the programmer need not bother
  about allocating and deallocating memory to variables. Python provides extensibility
  by providing modules which can be easily imported similar to headers in C and 
  packages in Java. Python is object oriented and hence provides all the object oriented
  characterstics such as inheritence, encapsulation and polymorphism.

* Python offers a highly powerful interactive programming interface in the form
  of the 'Interactive Interpreter' which will be discussed in more detail in the 
  following sections.

* Python provides a rich standard library and an extensive set of modules. The 
  power of Python modules can be seen in this slightly exaggerated cartoon
  http://xkcd.com/353/

* Python interfaces well with most other programming languages such as C, C++ 
  and FORTRAN.

1.1 The Python Interpreter
--------------------------

