Introduction
============

Python in a powerful, high-level, interpreted and multi-platform programming
language with an elegant and readable syntax, efficient high-level data
structures and a simple but effective approach to object programming. 

Python is easy to learn. It has been designed to help the programmer
concentrate on solving the problem at hand and not worry about the
programming language idiosyncrasies. Programmers often fall in love with
Python, for the increased productivity it brings.

Python was created by Guido van Rossum. The idea of Python was conceived in
December 1989. The name Python comes from the 70s comedy series "Monty
Python's Flying Circus" and has nothing to do with the reptilian.

Why Python?
-----------

* Python code is extremely readable. It has no braces and semi-colons and
  uses indentation, instead, for defining code blocks. This forces the
  programmers to write readable code. 

* It is interactive and the interactive environment offers a very fast
  edit-test-debug cycle. 

* It has a good set of high-level data structures and has been designed to
  let the programmer focus on the problem, rather than worry about the
  idiosyncrasies of the language.  

* It handles memory management and takes the burden, of allocating and
  de-allocating memory to variables off the programmer. 

* It is a Batteries included language. It comes with a huge standard library
  that allows us to do a wide range of tasks. 

* It is object-oriented. 

* It interfaces with other programming languages such as C, C++ and FORTRAN.
  This allows us to use legacy code available in these languages. 

* It not as fast as some of the compiled languages like C or C++. But, we
  think that the programmer's time is more valuable than machine time. Given
  the flexibility and power that Python gives the programmer, Python is a
  valuable tool to learn.


The Interpreter
===============

Let us get our hands dirty, right away. Typing ``python`` at the terminal,
will start up the Python interpreter. You should see something like this, if
you do have Python installed. 

::

    Python 2.7.1 (r271:86832, Feb 21 2011, 01:28:26) 
    [GCC 4.5.2 20110127 (prerelease)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

The first line shows the version of Python that we are using. In this example
the version of Python being used is 2.7.1

``>>>`` is called the prompt and it implies that the interpreter is ready and
waiting for your command!

Let's write our first line of Python code, the ubiquitous ``Hello World``. 

::

  >>> print 'Hello, World!'
  Hello, World!

Typing ``print 'Hello World'`` and hitting enter, printed out the words
*Hello World*. 

Let us now exit the interpreter. Hitting ``Ctrl-D``, exits the python
interpreter. 

Now we shall learn to use IPython, an enhanced interpreter, instead of the
vanilla interpreter, which we just saw. 

A note on Versions
------------------

Before we continue, a not on the versions of Python is in order. Python
currently has two stable branches or versions, 2.x and 3.x. 3.x branch was
created with the idea of cleaning up some areas of Python, to make it more
consistent, without bothering about backward compatibility with older
versions. So, 3.x is not compatible with 2.x, and is deemed to be the future
of Python. But, we shall use 2.x for this course, since the ecosystem around
3.x is still growing and a lot of packages don't yet work with Python 3.x.
  
IPython - An enhanced interactive Python interpreter
----------------------------------------------------

IPython is an enhanced Python interpreter that provides features like
tabcompletion, easier access to help and lot of other functionality which are
not available in the vanilla Python interpreter.

invoking IPython
~~~~~~~~~~~~~~~~

First let us see how to invoke the ``ipython`` interpreter.

We type
::

  ipython

at the terminal prompt to invoke the ipython interpreter.

The prompt is now, ``In [1]:`` instead of the ``>>>`` in the vanilla Python
interpreter. We also get the same information about the version of Python
installed. But additionally, we get some IPython help information, instead of
the vanilla interpreter's help. 

``In`` stands for input and the number in the brackets indicates the number
of the current command in this session. We shall see how it's useful in a
short while. 

If you get an error saying something like ``ipython is not installed``,
install it and continue with the course. 

Let's try out the same ``Hello World`` in ``ipython``. 

::
    
    print 'Hello World!'

Now, to quit the ipython interpreter, type Ctrl-D. You are prompted asking if
you really want to exit, type y to say yes and quit ipython.

Start ipython again, as you did before.

History and Arrow Keys
~~~~~~~~~~~~~~~~~~~~~~

Now let us see, how we can type some commands into the interpreter.

Start with the simplest thing, addition.

Let's type 

::

    1 + 2 

at the prompt. IPython promptly gives back the output as 3.  Notice
that the output is displayed with an ``Out[1]`` indication.

Let's try out few other mathematical operations.

::

    5 - 3
    7 - 4
    6 * 5

Now let's ``print 1+2``. Instead of typing the whole thing, we make use of
the fact that IPython remembers the history of the commands that you have
already used. We use the up arrow key to go back the command ``1+2``. We then
use the left-arrow key to navigate to the beginning of the line and add the
word ``print`` and a space. Then hit enter and observe that the interpreter
prints out the value as 3, without the Out[] indication.

Now, let's change the previous command ``print 1+2`` to ``print 10*2``. We
use the up arrow again to navigate to the previous command and use the left
arrow key to move the cursor on to the + symbol and then use the delete key
to remove it and type 0 and * to change the expression as required. We hit
enter to see the output of ``print``.

Tab-completion
~~~~~~~~~~~~~~

Now, let's say we want to use the function ``round``. We type ``ro`` at the
prompt and hit the tab key. As you can see, IPython completes the command.
This feature is called the tab-completion.

Now, we remove all the characters and just type ``r`` and then hit tab.
IPython does not complete the command since there are many possibilities. It
just lists out all the possible completions.

Now, let's see what these functions are used for. We will use the help
features of ipython to find this out.

Help using ?
~~~~~~~~~~~~

To get the help of any function, we first type the function, ``abs`` in our
case and then add a ? at the end and hit enter.

As the documentation says, ``abs`` accepts a number as an input and returns
it's absolute value.

We say,

::

    abs(-19)

    abs(19)

We get 19, as expected, in both the cases.

Does it work for decimals (or floats)? Let's try typing abs(-10.5) and we do
get back 10.5.

Let us look at the documentation of the ``round`` function. 

::

    round?

If you notice, there are extra square brackets around the ``ndigits``. This
means that ``ndigits`` is optional and 0 is the default value. Optional
parameters are shown in square brackets anywhere in Python documentation.

The function ``round``, rounds a number to a given precision.

::

    round(2.48)
    round(2.48, 1)
    round(2.48, 2)

    round(2.484)
    round(2.484, 1)
    round(2.484, 2)

We get 2.0, 2.5 and 2.48, which are what we expect. 

Interrupting
~~~~~~~~~~~~

Let's now see how to correct typing errors that we make while typing at the
terminal. As already shown, if we haven't hit the enter key already, we could
navigate using the arrow keys and make deletions using delete or backspace
key and correct the errors.

Let's now type ``round(2.484`` and hit enter, without closing the
parenthesis. We get a prompt with dots. This prompt is the continuation
prompt of ``ipython``. It appears, the previous line is incomplete in some
way. We now complete the command by typing, the closing parenthesis and
hitting enter. We get the expected output of 2.5.

In other instances, if we commit a typing error with a longer and more
complex expression and end up with the continuation prompt, we can type
Ctrl-C to interrupt the command and get back the ``ipython`` input prompt.

For instance, 

::
  
    round(2.484 
    ^C

    round(2.484, 2)
  

Now that we know how to use the interpreter, we shall move look at the basic
data-types Python provides, and basic operators. 

Basic Datatypes and Operators
=============================

Python provides the following basic datatypes. 

  * Numbers

    * int 
    * float 
    * complex 

  * Boolean
  * Sequence

    * Strings
    * Lists
    * Tuples


Numbers
-------

We shall start with exploring the Python data types in the domain of numbers.

There are three built-in data types in python to represent numbers, namely:

  * int 
  * float 
  * complex 

Let us first talk about ``int`` 

::

    a = 13
    a


Now, we have our first ``int`` variable ``a``.

To verify this, we say

::

     type(a)
     <type 'int'>

``int`` data-type can hold integers of any size lets see this by an example.

::

    b = 99999999999999999999
    b

As you can see, even when we put a value of 9 repeated 20 times Python did
not complain. 

Let us now look at the ``float`` data-type. Decimal numbers in Python are
represented by the ``float`` data-type 

::

    p = 3.141592
    p

If you notice the value of output of ``p`` isn't exactly equal to ``p``. This
is because floating point values have a fixed precision (or bit-length) and
it is not possible to represent all numbers within the given precision. Such
numbers are approximated and saved. This is why we should never rely on
equality of floating point numbers in a program.

Finally, let us look at the ``complex`` data-type. 

::

    c = 3+4j

gives us a complex number, ``c`` with real part 3 and imaginary part 4.

To get the real and imaginary parts of ``c``, we say

::

    c.real
    c.imag

Note that complex numbers are a combination of two floats, i.e., the real and
the imaginary parts, 3 and 4 are floats and not integers. 

::

    type(c.real)
    type(c.imag)

We can get the absolute value of c, by

::
 
    abs(c)

Let's now look at some operators common operations on these data-types.

::

    23 + 74
    23 - 56
    45 * 76

    8 / 3 
    8.0 / 3

The first division, 8/3 is an integer division and results in an integer
output. In the second division, however, the answer is a float. To avoid
integer division, at least one of the operands should be a float.

``%`` is used for the modulo operation. 

::

    87 % 6

and ``**`` is for exponentiation. 

::

    7 ** 8

All of the above operations can be performed with variables, as well. 

::

    a = 23 
    b = 74
    a * b

    c = 8 
    d = 8.0 
    f = c / 3
    g = d / 3  

In the last two commands, the results of the operations are being assigned to
new variables.

In case, we wish to assign the result of an operation on the
variable to itself, we can use a special kind of assignment.

::

    c /= 3

is the same as 

::
   
    c = c / 3

Booleans
--------

Now let us look at the Boolean data-type. 

::  
  
    t = True

creates a boolean variable ``t``, whose value is ``True``. Note that T in
true is capitalized.
  
You can apply different Boolean operations on ``t`` now. 

For example 

::

    f = not t 
    f
    f or t
    f and t   

What if you want to use multiple operators? Here's an example. 

::

    (f and t) or t

Note that we have used parenthesis, to explicitly state what we want to do.
We are not going to discuss operator precedence and shall use parenthesis,
when using multiple operators.

The following expression, for instance is different from the one above.  

::
  
    f and (t or t) 

Sequences
---------

Let's now discuss the sequence data types in Python. The data-types which
hold a bunch of elements in them, in a sequential order are called sequence
data-types. The elements can be accessed using their position in the
sequence. 

The sequence datatypes in Python are -

  * str
  * list
  * tuple

::

    greet_str = "hello"

``greet_str`` is now a string variable with the value ``hello`` 

Anything within quotes is a string.

Items enclosed in square brackets separated by commas constitute a list.

:: 
  
    num_list = [1, 2, 3, 4, 5, 6, 7, 8]
    num_list

To create a tuple we use parentheses ('(') instead of square brackets ('[')

::

    num_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
  
Operations on sequences
~~~~~~~~~~~~~~~~~~~~~~~

Due to their sequential nature, there are certain kind of operations, which
can be performed on all of them. 

Firstly, accessing elements. Elements in sequences can be accessed using
indexes. 

::

    num_list[2]
    num_tuple[2]
    greet_str[2]

As you can see, indexing starts from 0. 

Secondly, you can add two sequences of the same type, to each other to give
new sequences.

::

    num_list + [3, 4, 5, 6]
    greet_str + " world!"  


Thirdly, you can get the length of a sequence, by using the ``len`` function.

:: 

    len(num_list)
    len(greet_str)


Fourthly, we can check the containership of an element using the ``in``
keyword 

::

    3 in num_list
    'h' in greet_str
    'w' in greet_str
    2 in num_tuple  

We see that it gives True and False accordingly.

Next, we can find the maximum and minimum elements from a sequence. 

::

    max(num_tuple)
    min(greet_str)

As a consequence of their order, we can access a group of elements in a
sequence. They are called called slicing and striding.

First lets discuss slicing, on the list ``num_list``. We can access a part of
this sequence by slicing the sequence. Lets say we want elements starting
from 2 and ending in 5.

::

    num_list[1:5]

Note that the elements starting from the first index to the last one, the
last one not included are being returned. We shall look at the details,
later. 

Striding is similar to slicing except that the step size here is not one.

::
  
    num_list[1:8:2]


The colon two added in the end signifies all the alternate elements. This is
why we call this concept striding because we move through the list with a
particular stride or step. The step in this example being 2.

This brings us to the end of our discussion on basic data-types and
operations on them. 

.. 
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: nil
   fill-column: 77
   End:

