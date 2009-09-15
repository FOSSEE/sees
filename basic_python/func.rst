Functional Approach
===================

*Functions* allow us to enclose a set of statements and call the function again
and again instead of repeating the group of statements everytime. Functions also
allow us to isolate a piece of code from all the other code and provides the
convenience of not polluting the global variables.

*Function* in python is defined with the keyword **def** followed by the name
of the function, in turn followed by a pair of parenthesis which encloses the
list of parameters to the function. The definition line ends with a ':'. The
definition line is followed by the body of the function intended by one block.
The *Function* must return a value::

  def factorial(n):
    fact = 1
    for i in range(2, n):
      fact *= i

    return fact

The code snippet above defines a function with the name factorial, takes the
number for which the factorial must be computed, computes the factorial and
returns the value.

A *Function* once defined can be used or called anywhere else in the program. We
call a fucntion with its name followed by a pair of parenthesis which encloses
the arguments to the function.

The value that function returns can be assigned to a variable. Let's call the
above function and store the factorial in a variable::

  fact5 = factorial(5)

The value of fact5 will now be 120, which is the factorial of 5. Note that we
passed 5 as the argument to the function.

It may be necessary to document what the function does, for each of the function
to help the person who reads our code to understand it better. In order to do
this Python allows the first line of the function body to be a string. This
string is called as *Documentation String* or *docstring*. *docstrings* prove
to be very handy since there are number of tools which can pull out all the
docstrings from Python functions and generate the documentation automatically
from it. *docstrings* for functions can be written as follows::

  def factorial(n):
    'Returns the factorial for the number n.'
    fact = 1
    for i in range(2, n):
      fact *= i

    return fact

An important point to note at this point is that, a function can return any
Python value or a Python object, which also includes a *Tuple*. A *Tuple* is
just a collection of values and those values themselves can be of any other
valid Python datatypes, including *Lists*, *Tuples*, *Dictionaries* among other
things. So effectively, if a function can return a tuple, it can return any
number of values through a tuple

Let us write a small function to swap two values::

  def swap(a, b):
    return b, a

  c, d = swap(a, b)

Function scope
---------------
The variables used inside the function are confined to the function's scope
and doesn't pollute the variables of the same name outside the scope of the
function. Also the arguments passed to the function are passed by-value if
it is of basic Python data type::

  def cant_change(n):
    n = 10

  n = 5
  cant_change(n)

Upon running this code, what do you think would have happened to value of n
which was assigned 5 before the function call? If you have already tried out
that snippet on the interpreter you already know that the value of n is not
changed. This is true of any immutable types of Python like *Numbers*, *Strings*
and *Tuples*. But when you pass mutable objects like *Lists* and *Dictionaries*
the values are manipulated even outside the function::

  >>> def can_change(n):
  ...   n[1] = James
  ...

  >>> name = ['Mr.', 'Steve', 'Gosling']
  >>> can_change(name)
  >>> name
  ['Mr.', 'James', 'Gosling']

If nothing is returned by the function explicitly, Python takes care to return
None when the funnction is called.

Default Arguments
-----------------

There may be situations where we need to allow the functions to take the
arguments optionally. Python allows us to define function this way by providing
a facility called *Default Arguments*. For example, we need to write a function
that returns a list of fibonacci numbers. Since our function cannot generate an
infinite list of fibonacci numbers, we need to specify the number of elements
that the fibonacci sequence must contain. Suppose, additionally, we want to the
function to return 10 numbers in the sequence if no option is specified we can
define the function as follows::

  def fib(n=10):
    fib_list = [0, 1]
    for i in range(n - 2):
      next = fib_list[-2] + fib_list[-1]
      fib_list.append(next)
    return fib_list

When we call this function, we can optionally specify the value for the
parameter n, during the call as an argument. Calling with no argument and
argument with n=5 returns the following fibonacci sequences::

  fib()
  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
  fib(5)
  [0, 1, 1, 2, 3]

Keyword Arguments
-----------------

When a function takes a large number of arguments, it may be difficult to
remember the order of the parameters in the function definition or it may
be necessary to pass values to only certain parameters since others take
the default value. In either of these cases, Python provides the facility
of passing arguments by specifying the name of the parameter as defined in
the function definition. This is known as *Keyword Arguments*. 

In a function call, *Keyword arguments* can be used for each argument, in the
following fashion::

  argument_name=argument_value
  Also denoted as: keyword=argument

  def wish(name='World', greetings='Hello'):
    print "%s, %s!" % (greetings, name)

This function can be called in one of the following ways. It is important to
note that no restriction is imposed in the order in which *Keyword arguments*
can be specified. Also note, that we have combined *Keyword arguments* with
*Default arguments* in this example, however it is not necessary::

  wish(name='Guido', greetings='Hey')
  wish(greetings='Hey', name='Guido')

Calling functions by specifying arguments in the order of parameters specified
in the function definition is called as *Positional arguments*, as opposed to
*Keyword arguments*. It is possible to use both *Positional arguments* and 
*Keyword arguments* in a single function call. But Python doesn't allow us to
bungle up both of them. The arguments to the function, in the call, must always
start with *Positional arguments* which is in turn followed by *Keyword
arguments*::

  def my_func(x, y, z, u, v, w):
    # initialize variables.
    ...
    # do some stuff 
    ...
    # return the value

It is valid to call the above functions in the following ways::

  my_func(10, 20, 30, u=1.0, v=2.0, w=3.0)
  my_func(10, 20, 30, 1.0, 2.0, w=3.0)
  my_func(10, 20, z=30, u=1.0, v=2.0, w=3.0)
  my_func(x=10, y=20, z=30, u=1.0, v=2.0, w=3.0)

Following lists some of the invalid calls::

  my_func(10, 20, z=30, 1.0, 2.0, 3.0)
  my_func(x=10, 20, z=30, 1.0, 2.0, 3.0)
  my_func(x=10, y=20, z=30, u=1.0, v=2.0, 3.0)

Parameter Packing and Unpacking
-------------------------------

The positional arguments passed to a function can be collected in a tuple
parameter and keyword arguments can be collected in a dictionary. Since keyword
arguments must always be the last set of arguments passed to a function, the
keyword dictionary parameter must be the last parameter. The function definition
must include a list explicit parameters, followed by tuple paramter collecting
parameter, whose name is preceded by a *****, for collecting positional
parameters, in turn followed by the dictionary collecting parameter, whose name
is preceded by a ****** ::

  def print_report(title, *args, **name):
    """Structure of *args*
    (age, email-id)
    Structure of *name*
    {
        'first': First Name
        'middle': Middle Name
        'last': Last Name
    }
    """
    
    print "Title: %s" % (title)
    print "Full name: %(first)s %(middle)s %(last)s" % name
    print "Age: %d\nEmail-ID: %s" % args

The above function can be called as. Note, the order of keyword parameters can
be interchanged::

  >>> print_report('Employee Report', 29, 'johny@example.com', first='Johny',
                   last='Charles', middle='Douglas')
  Title: Employee Report
  Full name: Johny Douglas Charles
  Age: 29
  Email-ID: johny@example.com

The reverse of this can also be achieved by using a very identical syntax while
calling the function. A tuple or a dictionary can be passed as arguments in
place of a list of *Positional arguments* or *Keyword arguments* respectively
using ***** or ****** ::

  def print_report(title, age, email, first, middle, last):
    print "Title: %s" % (title)
    print "Full name: %s %s %s" % (first, middle, last)
    print "Age: %d\nEmail-ID: %s" % (age, email)

  >>> args = (29, 'johny@example.com')
  >>> name = {
          'first': 'Johny',
          'middle': 'Charles',
          'last': 'Douglas'
          }
  >>> print_report('Employee Report', *args, **name)
  Title: Employee Report
  Full name: Johny Charles Douglas
  Age: 29
  Email-ID: johny@example.com

Nested Functions and Scopes
---------------------------

Python allows nesting one function inside another. This style of programming
turns out to be extremely flexible and powerful features when we use *Python
decorators*. We will not talk about decorators is beyond the scope of this
course. If you are interested in knowing more about *decorator programming* in
Python you are suggested to read:

| http://avinashv.net/2008/04/python-decorators-syntactic-sugar/
| http://personalpages.tds.net/~kent37/kk/00001.html

However, the following is an example for nested functions in Python::

  def outer():
    print "Outer..."
    def inner():
      print "Inner..."
    print "Outer..."
    inner()
  
  >>> outer()

map, reduce and filter functions
--------------------------------

Python provides several built-in functions for convenience. The **map()**,
**reduce()** and **filter()** functions prove to be very useful with sequences like
*Lists*.

The **map** (*function*, *sequence*) function takes two arguments: *function*
and a *sequence* argument. The *function* argument must be the name of the
function which in turn takes a single argument, the individual element of the
*sequence*. The **map** function calls *function(item)*, for each item in the
sequence and returns a list of values, where each value is the value returned
by each call to *function(item)*. **map()** function allows to pass more than
one sequence. In this case, the first argument, *function* must take as many
arguments as the number of sequences passed. This function is called with each
corresponding element in the each of the sequences, or **None** if one of the
sequence is exhausted::

  def square(x):
    return x*x
  
  >>> map(square, [1, 2, 3, 4])
  [1, 4, 9, 16]
  
  def mul(x, y):
    return x*y
  
  >>> map(mul, [1, 2, 3, 4], [6, 7, 8, 9])

The **filter** (*function*, *sequence*) function takes two arguments, similar to
the **map()** function. The **filter** function calls *function(item)*, for each
item in the sequence and returns all the elements in the sequence for which 
*function(item)* returned True::

  def even(x):
    if x % 2:
      return True
    else:
      return False
  
  >>> filter(even, range(1, 10))
  [1, 3, 5, 7, 9]

The **reduce** (*function*, *sequence*) function takes two arguments, similar to
**map** function, however multiple sequences are not allowed. The **reduce**
function calls *function* with first two consecutive elements in the sequence,
obtains the result, calls *function* with the result and the subsequent element
in the sequence and so on until the end of the list and returns the final result::

  def mul(x, y):
    return x*y

  >>> reduce(mul, [1, 2, 3, 4])
  24

List Comprehensions
~~~~~~~~~~~~~~~~~~~

List Comprehension is a convenvience utility provided by Python. It is a 
syntatic sugar to create *Lists*. Using *List Comprehensions* one can create
*Lists* from other type of sequential data structures or other *Lists* itself.
The syntax of *List Comprehensions* consists of a square brackets to indicate
the result is a *List* within which we include at least one **for** clause and
multiple **if** clauses. It will be more clear with an example::

  >>> num = [1, 2, 3]
  >>> sq = [x*x for x in num]
  >>> sq
  [1, 4, 9]
  >>> all_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  >>> even = [x for x in all_num if x%2 == 0]

The syntax used here is very clear from the way it is written. It can be 
translated into english as, "for each element x in the list all_num, 
if remainder of x divided by 2 is 0, add x to the list."
