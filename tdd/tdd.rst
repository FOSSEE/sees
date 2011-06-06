=======================
Test Driven Development
=======================

What is TDD?
============

Objectives
----------
At the end of this section, you will be able to:

1. Write your code using the TDD paradigm. 
#. Use doctests to test your Python code. 
#. Use unittests to test your Python code. 
#. Use the nose module to test your code. 


Test Driven Development (TDD), as the name suggests, is a style or method
of software development based on the idea of writing code, after writing
tests for them. As the tests are written for code, that doesn't even exist
yet, it is bound to fail. Actual code is later written, to pass the test
and later on refactored.

The basic steps of TDD are roughly as follows - 

1. Decide upon the feature to implement and the methodology of testing it. 
#. Write the tests for the feature decided upon. 
#. Just write enough code, so that the test can be run, but it fails. 
#. Improve the code, to just pass the test and at the same time passing all
 previous tests. 
#. Run the tests to see, that all of them run successfully. 
#. Refactor the code we've just written -- optimize the algorithm, remove
 duplication, add documentation, etc. 
#. Run the tests again, to see that all the tests still pass. 
#. Go back to 1. 

First "Test"
============

Now, that we have an overview of TDD, let's get down to writing our first
test. Let us consider a very simple program which returns the Greatest
Common Divisor (GCD) of two numbers. 

Before being able to write our test, we need to have a clear idea of the
code units our program will contain, so that we can test each of them.
Let's first define the code units that our GCD program is going to have. 

Our program is going to contain only one function called ``gcd``, which
will take in two arguments, and return a single value, which is the GCD of
the two arguments. So if we want to find out GCD of 44, 23, we call the
function, with the arguments 44 and 23. 

::

    c = gcd(44, 23) 

c will contain the GCD of the two numbers.

We have defined the code units in our program. So, we can go ahead and
write tests for it. 

When adopting the TDD methodology, it is important to have a clear set of
results defined for our code units i.e., for every given set of inputs as
that we wish use as a test case, we must have, before hand, the exact
outputs that are expected for those input test cases. We must not be
running around looking for outputs for our test cases after we have the
code ready, or even while we are writing the tests.

Let one of our test cases be 48 and 64 as ``a`` and ``b``, respectively.
For this test case we know that the expected output, the GCD, is 16. Let
our second test case be 44 and 19 as ``a`` and ``b``, respectively. We know
that their GCD is 1, and that is the expected output. 

But before writing one, we should What does a test look like? What does it
do? Let's answer this question first.

Tests are just a series of assertions which are either True or False
depending on the expected behaviour of the code and the actual behaviour.
Tests for out GCD function could be written as follows.

::

  tc1 = gcd(48, 64)
  if tc1 != 16:
      print "Failed for a=48, b=64. Expected 16. Obtained %d instead." % tc1
      exit(1)
  
  tc2 = gcd(44, 19)
  if tc2 != 1:
      print "Failed for a=44, b=19. Expected 1. Obtained %d instead." % tc2
      exit(1)

  print "All tests passed!"

The next step is to run the tests we have written, but if we run the tests
now, the tests wouldn't even run. Why? We don't even have the function
``gcd`` defined, for it to be called by the tests. The test code doesn't
even run! What is the way out? We shall first write a very minimal
definition (or a stub) of the function ``gcd``, so that it can be called by
the tests.

A minimal definition for the ``gcd`` function would look like this

::

    def gcd(a, b):
        pass

As you can see, the stub for ``gcd`` function does nothing, other than
define the required function which takes the two arguments a and b. No
action is done upon the arguments, passed to the function, yet. The
function definition is empty and just contains the ``pass`` statement. 

Let us put all these in a file and call this file ``gcd.py`` 

::

  def gcd(a, b):
      pass

  if __name__ == '__main__':
      tc1 = gcd(48, 64)
      if tc1 != 16:
          print "Failed for a=48 and b=64. Expected 16. Obtained %d instead." % tc1
          exit(1)

      tc2 = gcd(44, 19)
      if tc2 != 1:
          print "Failed for a=44 and b=19. Expected 1. Obtained %d instead." % tc2
          exit(1)

      print "All tests passed!"

Recall that, the condition ``__name__ == '__main__'`` becomes true, only
when the python script is ran directly as a stand-alone script. So any code
within this ``if`` block is executed only when the script is run as a
stand-alone script and doesn't run when it is used as a module and
imported.

Let us run our code as a stand-alone script.

::

  $ python gcd.py
  Traceback (most recent call last):
    File "gcd.py", line 7, in <module> print "Failed for a=48 and b=64. Expected 16. Obtained %d instead." % tc1
  TypeError: %d format: a number is required, not NoneType

We now have our tests, the code unit stub, and a failing test. The next
step is to write code, so that the test just passes. 

Let's us the algorithm given by a greek mathematician, 2300 years ago, the
Euclidean algorithm, to compute the GCD of two numbers. 

**Note**: If you are unaware of Euclidean algorithm to compute the gcd of
two numbers please refer to it on wikipedia. It has a very detailed
explanation of the algorithm and its proof of validity among other things.

The ``gcd`` stub function can be modified to the following function, 

::

    def gcd(a, b):
        if a == 0:
            return b
        while b != 0:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a

Now let us run our script which already has the tests written in it and see
what happens

::

    $ python gcd.py
    All tests passed!

Success! We managed to write code, that passes all the tests. The code we
wrote was simplistic, actually. If you take a closer look at the code you
will soon realize that the chain of subtraction operations can be replaced
by a modulo operation i.e. taking remainders of the division between the
two numbers since they are equivalent operations. The modulo operation is
far better, since it combines a lot of subtractions into one operation and
the reduction is much faster. Take a few examples, and convince yourself
that using the modulo operation is indeed faster than the subtraction
method.

::

    def gcd1(a, b):
        while b != 0 and a != 0:
            if a > b:
                a = a%b
            else:
                b = b%a
        if a == 0:
            return b
        else:
            return a

But we know that the modulo of ``a%b`` is always less than b. So, if the
condition ``a>b`` is True in this iteration, it will definitely be False in
the next iteration. Also note that , and in the case when ``a < b``,
``a%b`` is equal to ``a``. So, we could, essentially, get rid of the
``if-else`` block and combine a swapping operation along with the modulo
operation. 

::

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

Let's run our tests again, and check that all the tests are passed, again.

We could make one final
improvement to our ``gcd`` function, which is strictly not necessary in
terms of efficiency, but is definitely more readable and easy to
understand. We could make our function a recursive function, as shown below

::

  def gcd(a, b):
      if b == 0:
          return a
      return gcd(b, a%b)

Much shorter and sweeter! We again run all the tests, and check that they
are passed. It indeed does pass all the tests! 

But there is still one small problem. There is no way, for the users of
this function, to determine how to use it, how many arguments it takes and
what it returns, among other things. This is a handicap for the people
reading your code, as well. This is well written function, with no
documentation whatsoever. 

Let's add a docstring as shown,

::

    def gcd(a, b):
        """Returns the Greatest Common Divisor of the two integers
        passed as arguments.
  
        Args:
          a: an integer
          b: another integer
  
        Returns: Greatest Common Divisor of a and b
        """
        if b == 0:
            return a
        return gcd(b, a%b)

Now we have refactored our code enough to make it well written piece
of code. We have now successfully completed writing our first test, writing
the relevant code, ensuring that the tests are passed and refactoring the
code, until we are happy with the way it works and looks. 

Let's now build on what we have learnt so far and learn more about writing
tests and improve our methodology of writing tests and simplify the process
of writing them. 

Persistent Test Cases
---------------------

As already stated, tests should be predetermined and you should have your
test cases and their outputs ready, even before you write the first line of
code. This test data is repeatedly used in the process of writing code. So,
it makes sense to have the test data to be stored in some persistent format
like a database, a text file, a file of specific format like XML, etc.

Let us modify the test code for the GCD function and save our test data in
a text file. Let us decide upon the following format for the test data. 

  1. The file has multiple lines of test data.
  2. Each line in this file corresponds to a single test case.
  3. Each line consists of three comma separated values --

     i. First two coloumns are the integers for which the GCD has to
        be computed
     ii. Third coloumn is the expected GCD to the preceding two
         numbers.

Now, how do we modify our tests to use this test data? We read the file
line by line and parse it to obtain the required numbers whose GCD we wish
to calculate, and the expected output. We can now call the ``gcd`` function
with the correct arguments and verify the output with the expected output. 

Let us call our data file ``gcd_testcases.dat``

::

    if __name__ == '__main__':
        for line in open('gcd_testcases.dat'):
            values = line.split(', ')
            a = int(values[0])
            b = int(values[1])
            g = int(values[2])
  
            tc = gcd(a, b)
            if tc != g:
                print "Failed for a=%d and b=%d. Expected %d. Obtained %d instead." % (a, b, g, tc)
                exit(1)

        print "All tests passed!"

When we execute the gcd.py script again we will notice that the code passes
all the tests. 

Now, we have learnt how to write simple test cases and develop code based
on these test cases. We shall now move on to learn to use some testing
frameworks available for Python, which make some of the task easier. 

Python Testing Frameworks
=========================

Python provides two ways to test the code we have written. One of them is
the unittest framework and the the other is the doctest module. To start
with, let us discuss the doctest module.

doctest
~~~~~~~

As we have already discussed, a well written piece of code must always be
accompanied by documentation. We document functions or modules using
docstrings. In addition to writing a generic description of the function or
the module, we can also add examples of using these functions in the
interactive interpreter to the docstrings. 

Using the ``doctest`` module, we can pick up all such interactive session
examples, execute them, and determine if the documented piece of code runs,
as it was documented. 

The example below shows how to write ``doctests`` for our ``gcd`` function.

::

    def gcd(a, b):
        """Returns the Greatest Common Divisor of the two integers
        passed as arguments.
  
        Args:
          a: an integer
          b: another integer
  
        Returns: Greatest Common Divisor of a and b
  
        >>> gcd(48, 64)
        16
        >>> gcd(44, 19)
        1
        """
        if b == 0:
            return a
        return gcd(b, a%b)

That is all there is, to writing a ``doctest`` in Python. Now how do we use
the ``doctest`` module to execute these tests. That too, is fairly straight
forward. All we need to do is tell the doctest module to execute, using the
``doctest.testmod`` function. 

Let us place this piece of code at the same place where we placed our tests
earlier. So putting all these together we have our ``gcd.py`` module which
looks as follows

::

    def gcd(a, b):
        """Returns the Greatest Common Divisor of the two integers
        passed as arguments.
  
        Args:
          a: an integer
          b: another integer
  
        Returns: Greatest Common Divisor of a and b
  
        >>> gcd(48, 64)
        16
        >>> gcd(44, 19)
        1
        """
        if b == 0:
            return a
        return gcd(b, a%b)
  
    if __name__ == "__main__":
        import doctest
        doctest.testmod()

The ``testmod`` function automatically picks up all the docstrings that
have sample sessions from the interactive interpreter, executes them and
compares the output with the results as specified in the sample sessions.
If all the outputs match the expected outputs that have been documented, it
doesn't say anything. It complains only if the results don't match as
documented, expected results. 

When we execute this script as a stand-alone script we will get back the
prompt with no messages which means all the tests passed

::

    $ python gcd.py
    $ 

If we further want to get a more detailed report of the tests that were
executed we can run python with -v as the command line option to the script

::

  $ python gcd.py -v
  Trying:
      gcd(48, 64)
  Expecting:
    16
  ok
  Trying:
      gcd(44, 19)
  Expecting:
      1
  ok
  1 items had no tests:
      __main__
  1 items passed all tests:
     2 tests in __main__.gcd
  2 tests in 2 items.
  2 passed and 0 failed.
  Test passed.


**Note:** We can have the sample sessions as test cases as long as the
outputs of the test cases do not contain any blank lines. In such cases we
may have to use the exact string ``<BLANKLINE>``

For the sake of illustrating a failing test case, let us assume that we
made a small mistake in our code. Instead of returning ``a`` when b = 0, we
typed it as ``return b`` when b = 0. Now, all the GCDs returned will have
the value 0. The code looks as follows

::

    def gcd(a, b):
        """Returns the Greatest Common Divisor of the two integers
        passed as arguments.
  
        Args:
          a: an integer
          b: another integer
  
        Returns: Greatest Common Divisor of a and b
  
        >>> gcd(48, 64)
        16
        >>> gcd(44, 19)
        1
        """
        if b == 0:
            return b
        return gcd(b, a%b)

Executing this code snippet without -v option to the script

::

  $ python gcd.py
  **********************************************************************
  File "gcd.py", line 11, in __main__.gcd
  Failed example:
      gcd(48, 64)
  Expected:
      16
  Got:
      0
  **********************************************************************
  File "gcd.py", line 13, in __main__.gcd
  Failed example:
      gcd(44, 19)
  Expected:
      1
  Got:
      0
  **********************************************************************
  1 items had failures:
     2 of   2 in __main__.gcd
  ***Test Failed*** 2 failures.

The output clearly complains that there were exactly two test cases
that failed. If we want a more verbose report we can pass -v option to
the script. 

This is all there is, to using the ``doctest`` module in Python.
``doctest`` is extremely useful when we want to test each Python function
or module individually. 

For more information about the doctest module refer to the Python library
reference on doctest[0].

unittest framework
~~~~~~~~~~~~~~~~~~

We needn't go too far ahead, to start complaining that ``doctest`` is not
sufficient to write complicated tests especially when we want to automate
our tests, write tests that need to test for more convoluted code pieces.
For such scenarios, Python provides a ``unittest`` framework.

The ``unittest`` framework provides methods to efficiently automate tests,
easily initialize code and data for executing the specific tests, cleanly
shut them down once the tests are executed and easy ways of aggregating
tests into collections and better way of reporting the tests.

Let us continue testing our gcd function in the Python module named
``gcd.py``. The ``unittest`` framework expects us to subclass the
``TestCase`` class in ``unittest`` module and place all our test code as
methods of this class. The name of the test methods are expected to be
started with ``test_``, so that the test runner knows which methods are to
be executed as tests. We shall use the test cases supplied by
``gcd_testcases.dat``. 

Lastly, to illustrate the way to test Python code as a module, let's create
a new file called ``test_gcd.py`` following the same convention used to
name the test methods, and place our test code in it. 

::
  
    import gcd
    import unittest
  
    class TestGcdFunction(unittest.TestCase):
  
        def setUp(self):
            self.test_file = open('gcd_testcases.dat')
            self.test_cases = []
            for line in self.test_file:
                values = line.split(', ')
                a = int(values[0])
                b = int(values[1])
                g = int(values[2])
  
                self.test_cases.append([a, b, g])
  
        def test_gcd(self):
            for case in self.test_cases:
                a = case[0]
                b = case[1]
                g = case[2]
                self.assertEqual(gcd.gcd(a, b), g)
  
        def tearDown(self):
            self.test_file.close()
            del self.test_cases
  
    if __name__ == '__main__':
        unittest.main()

Please note that although we highly recommend writing docstrings for all
the classes, functions and modules, we have not done so, in this example to
keep it compact. Adding suitable docstrings wherever required is left to
you, as an exercise. 

It would be a waste, to read the test data file, each time we run a test
method. So, in the setUp method, we read all the test data and store it
into a list called test_cases, which is an attribute of the TestGCDFunction
class. In the tearDown method of the class we will delete this attribute to
free up the memory and close the opened file.

Our actual test code sits in the method which begins with the name
``test_``, as stated earlier, the ``test_gcd`` method. Note that, we import
the ``gcd`` Python module we have written at the top of this test file and
from this test method we call the ``gcd`` function within the ``gcd``
module to be tested with the each set of ``a`` and ``b`` values
``test_cases``. Once we execute the ``test_gcd`` function, we obtain the
result and compare it with the expected result as stored in the
corresponding ``test_cases`` attribute using the ``assertEqual`` method
provided by ``TestCase`` class in the ``unittest`` framework. There are
several other assertion methods supplied by the unittest framework. For a
more detailed information about this, refer to the unittest library
reference at [1]. This brings us to the end of our discussion of the
``unittest`` framework. 

nose
====

We have seen the ``unittest`` frame work and Python ``doctest`` module. .
One problem however remains. It is not easy to organize, choose and run
tests, when our code is scattered across multiple files. In the real world
scenario, this is often the case. 

In such a such a scenario, a tool which can aggregate these tests
automatically, and run them. The ``nose`` module, does precisely this, for
us. It can aggregate ``unittests`` and ``doctests`` into a collection and
run them. It also helps output the test-results and aggregate them in
various formats.

Although nose is not part of the standard Python distribution itself, it
can be very easily installed by using easy_install command as follows

::

  $ easy_install nose

Or download the nose package from [2], extracting the archive and running
the command from the extracted directory

::

  $ python setup.py install

Now we have nose up and running, but how do we use it? We shall use the
``nosetests``  command provided by the ``nose`` module, in the top-level
directory of our code. 

::

  $ nosetests

That's all! ``nose`` will now automatically pick all the tests in all the
directories and subdirectories in our code base and execute them.

However if we want to execute specific tests we can pass the test file
names or the directories as arguments to nosetests command. For a detailed
explanation about this, refer to [3]

Conclusion
==========

Now we have all the trappings we want to write state-of-the art tests. To
emphasize the same point again, any code which was written before writing
the test and the testcases in hand is flawed by design. So it is
recommended to follow the three step approach while writing code for any
project as below:

  1. Write failing tests with testcases in hand.
  2. Write the code to pass the tests.
  3. Refactor the code for better performance.

This approach is very famously known to the software development world as
"Red-Green-Refactor" approach[4].

[0] - http://docs.python.org/library/doctest.html
[1] - http://docs.python.org/library/unittest.html
[2] - http://pypi.python.org/pypi/nose/
[3] - http://somethingaboutorange.com/mrl/projects/nose/0.11.2/usage.html
[4] - http://en.wikipedia.org/wiki/Test-driven_development

.. 
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: nil
   fill-column: 75
   End:
