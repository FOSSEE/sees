Functions
=========

We are now going to learn about functions in Python --- how to define
them, passing arguments to them, docstrings, and return values.

While writing code, fewer lines of code is a good thing, since it reduces the
scope of error. Also, we would like to reduce duplication of code and
abstract out pieces of code, wherever possible. Functions allow us to do all
of this. 

Now let us at functions in a greater detail, 

Consider a mathematical function ``f(x) = x^2``. Here ``x`` is a variable and
with different values of ``x`` the value of function will change. When ``x``
is one f(1) will return the value 1 and f(2) will return us the value 4. Let
us now see how to define the function f(x) in Python.

::

    def f(x):
    	return x*x

Well that defined the function, so before learning what we did let us
see if it returns the expected values, try,

::

    f(1)
    f(2)

Yes, it returned 1 and 4 respectively. And now let us see what we did. We
wrote two lines: The first line ``def f(x):`` defines the name of the
function and specifies the parameters to the function. The second line
specifies what the function is supposed to return. ``def`` is a keyword and
``f`` is the name of the function and ``x`` the parameter of the function.

You can also have functions without any arguments. 

Let us define a new function called ``greet`` which will print ``Hello
World``. 

::

    def greet():
    	print "Hello World!"

now try calling the function,

::

   greet()

Well that is a function which takes no arguments. Also note that it is not
mandatory for a function to return values. The function ``greet`` isn't
taking any argument. Also, it is not returning any value explicitly. But for
such functions, Python returns a ``None`` object by default

Now let us see how to write functions with more than one argument.

::

    def avg(a, b):
    	return (a + b)/2

If we want a function to accept more arguments, we just list them separated
with a comma between the parenthesis after the function's name in the ``def``
line.

It is always a good practice to document the code that we write, and
for a function we define we should write an abstract of what the
function does, and that is called a docstring. 

Let us modify the function ``avg`` and add docstring to it. 

::

    def avg(a,b):
        """ avg takes two numbers as input, and
	returns their average"""

	return (a+b)/2

Note that docstrings are entered in the line immediately after the function
definition and put as a triple quoted string. 

Now we try this in the IPython interpreter,

::

    avg?

it displays the docstring as we gave it. Thus docstring has practical utility
also, and is not just a good "practice". 

Try to do this,

::

    greet?

It doesn't have a docstring associated with it. Also we cannot infer anything
from the function name, and thus we are forced to read the code to understand
about the function.

Let's now write a function named ``circle`` which returns the area and
perimeter of a circle given radius ``r``.

The function needs to return two values instead of just one which was being
returned until now. 

::

    def circle(r):
    	"""returns area and perimeter of a circle given radius r"""
	pi = 3.14
	area = pi * r * r
	perimeter = 2 * pi * r
	return area, perimeter

Similarly, you could have a function returning three or four or any number of
values. A Python function can return any number of values and there is not
restriction on it. 

Let us call the function ``circle`` as,

::

    a, p = circle(6)
    print a
    print p

Let us now do a little code reading, as opposed to writing. 

What does the function ``what`` do?

::

    def what( n ):
        if n < 0: n = -n
        while n > 0:
            if n % 2 == 1:
                return False
            n /= 10
        return True

The function returns ``True`` if all the digits of the number ``n`` are even,
otherwise it returns ``False``.

::

    def even_digits( n ):
       """returns True if all the digits in the number n are even,
       returns False if all the digits in the number n are not even"""
        if n < 0: n = -n
        while n > 0:
            if n % 2 == 1:
                return False
            n /= 10
        return True


Now one more code reading exercise,

What does this function ``what`` do?

::

    def what( n ):
        i = 1
        while i * i < n:
            i += 1
        return i * i == n, i

The function returns ``True`` and the square root of ``n`` if n is a perfect
square, otherwise it returns ``False`` and the square root of the next
perfect square.

::

    def is_perfect_square( n ):
        """returns True and square root of n, if n is a perfect square,
        otherwise returns False and the square root of the 
        next perfect square"""
        i = 1
        while i * i < n:
            i += 1
        return i * i == n, i

Default & Keyword Arguments
---------------------------

Let us now look at specifying default arguments to functions when defining
them and calling functions using keyword arguments. 

Let's use the ``round`` function as an example to understand what a default
value of an argument means. Let's type the following expressions in the
terminal.

::

    round(2.484)

    round(2.484, 2)

Both the first expression and the second are calls to the ``round`` function,
but the first calls it with only one argument and the second calls it with
two arguments. By observing the output, we can guess that the first one is
equivalent to call with the second argument being 0. 0 is the default value
of the argument.

::

    s.split() # split on spaces. 
    s.split(';') # split on ';' 

    range(10) # returns a list with numbers from 0 to 9
    range(1, 10) # returns a list with numbers from 1 to 9
    range(1, 10, 2) # returns a list with odd numbers from 1 to 9

Let's now define a simple function that uses default arguments. We define a
simple function that prints a welcome message to a person, given a greeting
and his/her name.

::

    def welcome(greet, name="World"):
        print greet, name

Let us first call the function with two arguments, one for ``greet`` and
other for ``name``.

::

    welcome("Hi", "Guido")          

We get the expected welcome message, "Hi Guido". 

Now let us call the function with just one argument "Hello". 

::

    welcome("Hello")

"Hello" is treated as the ``greet`` and we get "Hello World" as the output.
"World" is the default value for the argument ``name``.

If we redefined the function ``welcome``, by interchanging it's arguments and
placed the ``name`` argument with it's default value of "World" before the
``greet`` argument, what happens?

::

    def welcome(name="World", greet):
        print greet, name

We get an error that reads ``SyntaxError: non-default argument follows
default argument``. When defining a function all the argument with default
values should come at the end.

Let us now learn what keyword arguments or named arguments are. We shall
refer to them as keyword arguments, henceforth.

When you are calling functions in Python, you don't need to remember the
order in which to pass the arguments. Instead, you can use the name of the
argument to pass it a value. Let us understand this using the ``welcome``
function that we have been using all along. Let us call it in different ways
and observe the output to see how keyword arguments work.

::

    welcome()
    welcome("Hello", "James")

    welcome("Hi", name="Guido")

When no keyword is specified, the arguments are allotted based on their
position. So, "Hi" is the value of the argument ``greet`` and name is passed
the value "Guido".

::

    welcome(name="Guido", greet="Hey! ")

When keyword arguments are used, the arguments can be called in any order.

::

    welcome(name="Guido", "Hey")

This call returns an error that reads, ``non keyword arg after keyword arg``.
Python expects all the keyword to be present towards the end.

That brings us to the end of what we wanted to learn about ``keyword``
arguments.

Before defining a function of your own, make sure that you check the standard
library, for a similar function. Python is popularly called a "Batteries
included" language, for the huge library that comes along with it. Refer
`here <http://docs.python.org/library/functions.html>`_.

Variable scope
--------------

Before we end the discussion on functions, a short note on the scope of
variables in Python is in order. 

Arguments passed to a function are local. They are not available outside of
the function. 

::

    def change(q):
        q = 10
        print q

    change(1)
    print q

The variables used inside a function definition are considered to be "local"
variables and their existence is restricted to within the function. Global
variables are those variables, which are accessible from anywhere within a
Python program.

Variables that are assigned to within a function, are treated as local
variables by default.

::

    n = 5

    def change():
        n = 10
        print n

    change()
    print n
        
As you can see, the value of n hasn't changed after the function ``change``
was called. 

To assign to global variables (or variables which can be accessed from
outside the function), we need to use the global statement. We could redefine
the change function as shown below.

::

    def change():
        global n
        n = 10
        print n

    change()
    print n

There is a subtle difference in the behavior when we assign not directly to a
variable, but a list element or a list slice etc. In this case, Python looks
up for the name, from the innermost scope (the function), outwards, until it
finds the name. 

For example

::

    name = ['Mr.', 'Steve', 'Gosling']
    
    def change_name():
        name[0] = 'Dr.'

    change_name()
    print name

As, you can see, even though there was no variable ``name`` within the scope
of the function ``change_name``, calling it has changed the list ``name``. 

Also, let us tweak the examples above to learn about the way values are
passed to functions. 

::

    n = 5

    def change(n):
        n = 10
        print "n = %s, inside change" %n

    change(n)
    print n

::

    name = ['Mr.', 'Steve', 'Gosling']
    
    def change_name(n):
        n[0] = 'Dr.'
        print "n = %s, inside change_name" %n

    change_name(n)
    print name


Notice that the value of ``n`` does not get changed in the first case,
because numbers are immutable datatypes and they cannot be modified. In the
second case when a list was passed to the function ``change_name``, it is
changed because a list is mutable and it's first element is chaned by the
function. 

That brings us to the end of this section on functions. We have learnt how to
define functions, use them with default values and keyword arguments. We have
also looked briefly at variables and their scopes. 

.. 
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: nil
   fill-column: 77
   End:


