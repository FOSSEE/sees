============
Basic Python
============

This document is intended to be handed out at the end of the workshop. It has
been designed for Engineering students who are Python beginners and have basic
programming skills. The focus is on basic numerics and plotting using Python.

The system requirements:
  * Python - version 2.5.x or newer.
  * IPython
  * Text editor - scite, vim, emacs or whatever you are comfortable with.

Introduction
============

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
  characteristics such as inheritance, encapsulation and polymorphism.

* Python offers a highly powerful interactive programming interface in the form
  of the 'Interactive Interpreter' which will be discussed in more detail in the 
  following sections.

* Python provides a rich standard library and an extensive set of modules. The 
  power of Python modules can be seen in this slightly exaggerated cartoon
  http://xkcd.com/353/

* Python interfaces well with most other programming languages such as C, C++ 
  and FORTRAN.

Although, Python has one setback. Python is not fast as some of the compiled 
languages like C or C++. Yet, the amount of flexibility and power more than make
up for this setback.


The Python Interpreter
======================

The Interactive Interpreter
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Typing *python* at the shell prompt on any standard Unix/Gnu-Linux system and
hitting the enter key fires up the Python 'Interactive Interpreter'. The Python
interpreter is one of the most integral features of Python. The prompt obtained
when the interactive interpreter is similar to what is shown below. The exact
appearance might differ based on the version of Python being used. The ``>>>``
thing shown is the python prompt. When something is typed at the prompt and the
enter key is hit, the python interpreter interprets the command entered and
performs the appropriate action.

::

  Python 2.5.2 (r252:60911, Oct  5 2008, 19:24:49) 
  [GCC 4.3.2] on linux2
  Type "help", "copyright", "credits" or "license" for more information.
  >>> 

Lets try with an example, type ``print 'Hello, World!'`` at the prompt and hit
the enter key. 

::

  >>> print 'Hello, World!'
  Hello, World!

This example was quite straight forward, and thus we have written our first
line of Python code. Now let us try typing something arbitrary at the prompt.
For example: 

::
  
  >>> arbit word
    File "<stdin>", line 1
      arbit word
              ^
  SyntaxError: invalid syntax
  >>>
    
The interpreter gave an error message saying that 'arbit word' was invalid
syntax which is valid. The interpreter is an amazing tool when learning to
program in Python. The interpreter provides a help function that provides the
necessary documentation regarding all Python syntax, constructs, modules and
objects. Typing *help()* at the prompt gives the following output:

::
  
  >>> help()
  
  Welcome to Python 2.5!  This is the online help utility.
  
  If this is your first time using Python, you should definitely check out
  the tutorial on the Internet at http://www.python.org/doc/tut/.
  
  Enter the name of any module, keyword, or topic to get help on writing
  Python programs and using Python modules.  To quit this help utility and
  return to the interpreter, just type "quit".
  
  To get a list of available modules, keywords, or topics, type "modules",
  "keywords", or "topics".  Each module also comes with a one-line summary
  of what it does; to list the modules whose summaries contain a given word
  such as "spam", type "modules spam".
  
  help> 
  

As mentioned in the output, entering the name of any module, keyword or topic
will provide the documentation and help regarding the same through the online
help utility. Pressing *Ctrl+d* exits the help prompt and returns to the
python prompt. 

Let us now try a few examples at the python interpreter. 

Eg 1:
::
  
  >>> print 'Hello, python!'
  Hello, python!
  >>>
  
Eg 2:
::
  
  >>> print 4321*567890
  2453852690
  >>> 
  
Eg 3:
::
  
  >>> 4321*567890
  2453852690L
  >>>

::
  
  Note: Notice the 'L' at the end of the output. The 'L' signifies that the
  output of the operation is of type *long*. It was absent in the previous
  example because we used the print statement. This is because *print* formats
  the output before displaying.
  
Eg 4:
::
  
  >>> big = 12345678901234567890 ** 3
  >>> print big
  1881676372353657772490265749424677022198701224860897069000
  >>> 

::
  
  This example is to show that unlike in C or C++ there is no limit on the
  value of an integer.

*ipython* - An enhanced interactive Python interpreter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The power and the importance of the interactive interpreter was the highlight
of the previous section. This section provides insight into the enhanced
interpreter with more advanced set of features called **ipython**. Entering
*ipython* at the shell prompt fires up the interactive interpreter. 

::
  
  $ ipython
  Python 2.5.2 (r252:60911, Oct  5 2008, 19:24:49) 
  Type "copyright", "credits" or "license" for more information.
  
  IPython 0.8.4 -- An enhanced Interactive Python.
  ?         -> Introduction and overview of IPython's features.
  %quickref -> Quick reference.
  help      -> Python's own help system.
  object?   -> Details about 'object'. ?object also works, ?? prints more.
  
  In [1]: 
  
This is the output obtained upon firing ipython. The exact appearance may
change based on the Python version installed. The following are some of the
various features provided by **ipython**:
  
    Suggestions - ipython provides suggestions of the possible methods and
    operations available for the given python object.

Eg 5:
  
::
  
  In [4]: a = 6
  
  In [5]: a.
  a.__abs__           a.__divmod__        a.__index__         a.__neg__          a.__rand__          a.__rmod__          a.__rxor__
  a.__add__           a.__doc__           a.__init__          a.__new__          a.__rdiv__          a.__rmul__          a.__setattr__
  a.__and__           a.__float__         a.__int__           a.__nonzero__      a.__rdivmod__       a.__ror__           a.__str__
  a.__class__         a.__floordiv__      a.__invert__        a.__oct__          a.__reduce__        a.__rpow__          a.__sub__
  a.__cmp__           a.__getattribute__  a.__long__          a.__or__           a.__reduce_ex__     a.__rrshift__       a.__truediv__
  a.__coerce__        a.__getnewargs__    a.__lshift__        a.__pos__          a.__repr__          a.__rshift__        a.__xor__
  a.__delattr__       a.__hash__          a.__mod__           a.__pow__          a.__rfloordiv__     a.__rsub__          
  a.__div__           a.__hex__           a.__mul__           a.__radd__         a.__rlshift__       a.__rtruediv__      

In this example, we initialized 'a' (a variable - a concept that will be
discussed in the subsequent sections.) to 6. In the next line when the *tab* key
is pressed after typing '*a.*' ipython displays the set of all possible methods
that are applicable on the object 'a' (an integer in this context). Ipython
provides many such datatype specific features which will be presented in the
further sections as and when the datatypes are introduced.

Editing and running a python file
=================================

The previous sections focused on the use of the interpreter to run python code.
While the interpeter is an excellent tool to test simple solutions and
experiment with small code snippets, its main disadvantage is that everything
written in the interpreter is lost once its quit. Most of the times a program is 
used by people other than the author. So the programs have to be available in 
some form suitable for distribution, and hence they are written in files. This 
section will focus on editing and running python files. Start by opening a text 
editor ( it is recommended you choose one from the list at the top of this page ).
In the editor type down python code and save the file with an extension **.py** 
(python files have an extension of .py). Once done with the editing, save the 
file and exit the editor. 

Let us look at a simple example of calculating the gcd of 2 numbers using Python:

**Creating the first python script(file)**
::

  $ emacs gcd.py
    def gcd(x,y):
      if x % y == 0:
        return y
      return gcd(y, x%y)
  
    print gcd(72, 92)

To run the script, open the shell prompt, navigate to the directory that 
contains the python file and run `python <filename.py>` at the prompt ( in this 
case filename is gcd.py )

**Running the python script**
::
  
  $ python gcd.py
  4
  $ 

Another method to run a python script would be to include the line

`#! /usr/bin/python`

at the beginning of the python file and then make the file executable by 

$ chmod a+x *filename.py*

Once this is done, the script can be run as a standalone program as follows:

$ ./*filename.py*

Basic Datatypes and operators in Python
=======================================

Python provides the following set of basic datatypes.

  * Numbers: int, float, long, complex
  * Strings
  * Boolean

Numbers
~~~~~~~

Numbers were introduced in the examples presented in the interactive interpreter
section. Numbers include types as mentioned earlier viz., int (integers), float 
(floating point numbers), long (large integers), complex (complex numbers with 
real and imaginary parts). Python is not a strongly typed language, which means 
the type of a variable need not mentioned during its initialization. Let us look
at a few examples.

Eg 6:
::
  
  >>> a = 1 #here a is an integer variable

Eg 7:
::

  >>> lng = 122333444455555666666777777788888888999999999 #here lng is a variable of type long
  >>> lng
  122333444455555666666777777788888888999999999L #notice the trailing 'L'
  >>> print lng
  122333444455555666666777777788888888999999999 #notice the absence of the trailing 'L'
  >>> lng+1
  122333444455555666666777777788888889000000000L


Long numbers are the same as integers in almost all aspects. They can be used in
operations just like integers and along with integers without any distinction.
The only distinction comes during type checking (which is not a healthy practice).
Long numbers are tucked with a trailing 'L' just to signify that they are long.
Notice that in the example just lng at the prompt displays the value of the variable
with the 'L' whereas `print lng` displays without the 'L'. This is because print 
formats the output before printing. Also in the example, notice that adding an 
integer to a long does not give any errors and the result is as expected. So for
all practical purposes longs can be treated as ints.

Eg 8:
::

  >>> fl = 3.14159 #fl is a float variable
  >>> e = 1.234e-4 #e is also a float variable, specified in the exponential form
  >>> a = 1
  >>> b = 2
  >>> a/b #integer division
  0
  >>> a/fl #floating point division
  0.31831015504887655
  >>> e/fl
  3.9279473133031364e-05


Floating point numbers, simply called floats are real numbers with a decimal point.
The example above shows the initialization of a float variable. Shown also in this
example is the difference between integer division and floating point division.
'a' and 'b' here are integer variables and hence the division gives 0 as the quotient.
When either of the operands is a float, the operation is a floating point division,
and the result is also a float as illustrated.

Eg 9:
::

  >>> cplx = 3 + 4j #cplx is a complex variable
  >>> cplx
  (3+4j)
  >>> print cplx.real #prints the real part of the complex number
  3.0
  >>> print cplx.imag #prints the imaginary part of the complex number
  4.0
  >>> print cplx*fl  #multiplies the real and imag parts of the complex number with the multiplier
  (9.42477+12.56636j)
  >>> abs(cplx) #returns the absolute value of the complex number
  5.0

Python provides a datatype for complex numbers. Complex numbers are initialized 
as shown in the example above. The *real* and *imag* operators return the real and
imaginary parts of the complex number as shown. The *abs()* returens the absolute
value of the complex number.