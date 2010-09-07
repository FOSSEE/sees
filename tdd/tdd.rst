=======================
Test Driven Development
=======================

Fundamentals
============

Test Driven Development, abbreviated as TDD is a method of software
development which banks on the idea of writing test cases that fail for the
code that doesn't even exist yet. The actual code is written later to pass
the test and then refactored.

First "Test"
============

Writing a test is simple. Writing a failing test? It is much more simple.
Let us consider a very simple program which returns the Greatest Common
Divisor (GCD) of two numbers. Since the test cases for the code is written
prior to the code itself, it is necessary to have a clear idea of the code
units that our program will contain. Let us attempt to clearly define the
code units in our case of a GCD program. Let our program contain one and
only one function called gcd() which takes in two arguments as parameters.
These arguments are the numbers for which GCD must be computed. The gcd()
function returns a single value which is the GCD of the two arguments
passed. So if we want to find out GCD of 44, 23, I will call my code unit
as c = gcd(44, 23) where c will contain the GCD of those two numbers.

Now we have defined our code units, how will we write tests? Before writing
the test, a very fundamental question arises in our minds. How do tests
look like? So let us answer this question first. Tests are nothing but a
series of assertions which are either True or False depending on the
expected behaviour of the code. We tell our tests whether our code unit
asserts True or asserts False based on the expected behaviour of the code
units. If we happen to run the tests now we are sure to get errors. Oh! But
why? We don't even have the function gcd to call. The test code doesn't
even compile! So what should we do now? So the idea is to first write the
stubs for the code units before we start writing tests. This is necessary
for two reasons. Firstly, by writing the stubs for the code units we will
be able to correctly decide and fix on to the code units that we have
planned to include in our program. We have a clear cut idea as to how our
program is structured, how the tests must be written among other
things. Secondly, the tests must at least compile and then fail! If the
tests don't even compile, that doesn't mean the tests failed. It means
it was a failure on the programmer's part. Let us define our stub::

  def gcd(a, b):
      pass

This stub does nothing other than defining a new function called gcd
which takes two parameters a and b for which the GCD must be
calculated. The body of the function just contains Python's **pass**
statement which means it does nothing, i.e. empty. We have our stub
ready. One important thing we need to keep in mind when we adopt TDD
methodology is that we need to have a clear set of results defined for
our code units. To put it more clearly, for every given set of inputs
as test case we must have, before hand, the exact outputs that are
expected for those input test cases. If we don't have that we have
failed in the first step of the TDD methodology itself. We must never
run looking for outputs for our test cases after we have the code
ready or even while writing tests. The expected outputs/behaviour must
be in our hands before we start writing tests. Therefore let us define
our test cases and the expected output for those inputs. Let one of
our test cases be 48 and 64 as *a* and *b* respectively. For this test
case we know that the GCD is 16. So that is the expected output. Let
our second test case be 44 and 19 as *a* and *b* respectively. We know
that their GCD is 1 by simple paper and pen calculation.

Now we know what a test is? What are the ingredients required to write
tests? So what else should we wait for? Let us write our first test!::

  tc1 = gcd(48, 64)
  if tc1 != 16:
      print "Test failed for the case a=48 and b=64. Expected 16. Obtained %d instead." % tc1
      exit(1)
  
  tc2 = gcd(44, 19)
  if tc2 != 1:
      print "Test failed for the case a=44 and b=19. Expected 1. Obtained %d instead." % tc2
      exit(1)

  print "All tests passed!"

Let us put all these in a file and call this file **gcd.py**::

  def gcd(a, b):
      pass

  if __name__ == '__main__':
      tc1 = gcd(48, 64)
      if tc1 != 16:
          print "Test failed for the case a=48 and b=64. Expected 16. Obtained %d instead." % tc1
          exit(1)

      tc2 = gcd(44, 19)
      if tc2 != 1:
          print "Test failed for the case a=44 and b=19. Expected 1. Obtained %d instead." % tc2
          exit(1)

      print "All tests passed!"

Note that we have introduced a new semantic which uses two new magic names
in Python *__name__* and *__main__*. This is a very common idiom used in
Python. Every Python code in a file can be run in two ways: Either as an
independent stand-alone script or as a Python module which can be imported
by other Python scripts or modules. When the idiom::

  if __name__ == '__main__':

is used, the code within this if block is executed first when we run the
Python file as a stand-alone script. In other words, when we run this
python file as a stand-alone script the control of the program first starts
from the code that is within this if block from which the control is
transferred to other parts of the program or to other modules from
here. This comes as an extremely handy feature especially when we want to
test our modules individually. Now let us run our code as a stand-alone
script.::

  $ python gcd.py
  Traceback (most recent call last):
    File "gcd.py", line 7, in <module> print "Test failed for the case a=48 and b=64. Expected 16. Obtained %d instead." % tc1
  TypeError: %d format: a number is required, not NoneType

Now we have our tests, the test cases and the code unit stub at
hand. We also have the failing test. So we know for sure that we have
cleared the first check point of TDD where the tests have failed. The
failing tests also give a green signal for us to go ahead to our next
check point i.e. to write the actual code in our code unit and make
the test pass. So let us write the code for the gcd function by
removing the **pass** control statement which had just created a gcd
function stub for us.

Most of us have learnt in high school math classes that the best and
the easiest known algorithm to compute the gcd of two numbers was
given to us 2300 years ago by a greek mathematician named Euclid. So
let us use the Euclid's algorithm to compute the gcd of two numbers a
and b::

  def gcd(a, b):
      if a == 0:
          return b
      while b != 0:
          if a > b:
              a = a - b
          else:
              b = b - a
      return a

**Note**: If you are unaware of Euclidean algorithm to compute the gcd
of two numbers please refer to it on wikipedia. It has a very detailed
explanation of the algorithm and its proof of validity among other
things.

Now let us run our script which already has the tests written in it
and see what happens::

  $ python gcd.py
  All tests passed!

Success! We managed to pass all the tests. But wasn't that code simple
enough? Indeed it was. If you take a closer look at the code you will
soon realize that the chain of subtraction operations can be replaced
by a modulo operation i.e. taking remainders of the division between
the two numbers since they are equivalent operations. Also modulo
operation is far better than chain of subtractions because you will
reduce much faster using modulo operation than the subtraction. For
example if let us take 25, 5 as a and b in our example. If we write
down the steps of the algorithm written above we have the following:

Step 1: a = 25 b = 5: Since both a and b are not 0 and b is greater
than a: b = 25 - 5 = 20
Step 2: Since b is still not 0 and b is greater than a: b = 20 - 5 =
15
Step 3: Since b is still not 0 and b is greater than a: b = 15 - 5 =
10
Step 4: Since b is still not 0 and b is greater than a: b = 10 - 5 = 5
Step 5: Since b is still not 0 and b is equal to a: b = 5 - 5 = 0
Step 6: Since b is 0 the gcd is a = 5 which is returned

If we adopt the modulo operation instead of subtraction and follow the
steps:

Step 1: a = 25 b = 5: Since both a and b are not 0 and b is greater
than a: b = 25 % 5 = 0
Step 2: Since b is 0 the gcd is a = 5 which is returned

Wow! That was overwhelmingly lesser number of steps! So now we are
convinced that if we replace the subtraction operation with the modulo
operation our code performs much better. But if we think carefully we
know that the modulo of a and b is less than b irrespective of how
large the value of a is, including the case where a is already less
than b. So we can eliminate that extra conditional **if** statement by
just swapping the result of the modulo operation to the position of b
and b to the position of a. This ensures that a is always greater than
b and if not the swapping combined with modulo operation takes care of
it. To exemplify it, if a = 5 and b = 25 then by swapping and
performing modulo we have a = b = 25 and b = a % b = 5 % 25 = 5 and
hence we proceed. So let us replace our original code with this new
improved code we have come up with simple observations::

  def gcd(a, b):
      while b != 0:
          a, b = b, a % b
      return a

Executing our script again we will see that all the tests pass. One
final improvement we can think of which is not necessary in terms of
efficiency but is certainly good to do keeping in mind the readability
is that we can use the concept of recursion for the same
algorithm. Without going into much detail this is how the code looks
if we use a recursive approach::

  def gcd(a, b):
      if b == 0:
          return a
      return gcd(b, a%b)

Much shorter and sweeter! And it passes all the tests! But there is
one small problem yet. For the users of this function there is no way
to determine how to use it, how many parameters it takes what it
returns among other things. And same as well for those who read the
code. So this function is not a very well written piece of code since
it lacks documentation. So to make this function mode readable let us
add the docstring for this function. Rewriting the function with the
docstring looks like this::

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
of code. Let us move on.

More realistic "Tests"
======================

Now we have successfully completed writing our first test, writing the
relevant code and ensured the tests passed. We also refactored our
code to perform better. With the knowledge of all these and some
concepts and semantics like __main__ magic names we learnt we have
come a long way with respect to writing tests. But our thirst is still
unquenched! We want to do more and more tests! Not just write better
code but also better tests! So let us keep building upon what we have
learnt so far.

Let us start writing tests for more realistic test cases. Generally
tests are predetermined as said above, if not the software design in
itself is flawed. The predetermined tests are stored along with the
test code in some persistent format like in a database, a text file, a
file of specific format like XML or in some other way. Let us continue
with our example of GCD function. We will keep all our test cases in a
text file, which is indeed persistent. Let us specify the format of
the test data in our file as follows.

  1. The file has multiple lines of test data.
  2. Each line in this file corresponds to a single test case.
  3. Each line consists of three comma separated coloumns:

     i. First two coloumns are the integers for which the GCD has to
        be computed
     ii. Third coloumn is the expected GCD to the preceding two
         numbers.

So how do we write our tests to use these test cases? Pretty simple, let
us review the machinery required first.

  1. File reading: We already have learnt this in the modules on
     Basic Python.
  2. Parsing the read data from the file: This just involves a using a
     **for** loop which iterates over the data line by line since we
     know that the file contains each test case as a sepate line which
     are equivalent to the file records and hence parse the data line
     by line as strings as we iterate over it and convert it to the
     required data type.

Since we already have all the machinery required, let us proceed writing
our test cases. We do not need not make any changes to the gcd
function so we will just write down the test here. Let us call our
data file gcd_testcases.dat::

  if __name__ == '__main__':
      for line in open('gcd_testcases.dat'):
          values = line.split(', ')
          a = int(values[0])
          b = int(values[1])
          g = int(values[2])

          tc = gcd(a, b)
          if tc != g:
              print "Test failed for the case a=%d and b=%d. Expected %d. Obtained %d instead." % (a, b, g, tc)
              exit(1)

      print "All tests passed!"

When we execute the gcd.py script again we will notice that all the
tests passed.

Python Testing Framework
========================

Python provides two ways to test the code we have written. One of them
is the unittest framework and the the other is the doctest module.

doctest
~~~~~~~

To start with let us discuss the doctest module. As we have already
discussed a well written piece of code must always be accompanied by
its documentation. For a function or a module we document them in their
respective docstrings. In addition to this, we can also place the
samples of using these functions or modules in the Python interactive
interpreter in the docstrings. When we run the doctest module it picks
up all such interactive session samples, executes them and determines
if the documented piece of code runs as it is documented. Let us see
how to write doctests for our gcd function::

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

This is all a doctest is. To explain it in more simple terms tests
which are written as part of the docstrings are called as
doctests. Now how do we use our doctest module to execute this
tests. That is fairly straight forward as well. All we need to do is
tell the doctest module to execute. Let us place this piece of code at
the same place where we placed our tests earlier. So putting all these
together we have our gcd.py module which looks as follows::

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

All we need to do is import the doctest module that is part of the
Python's standard library. Call the testmod() function in this
module. This function automatically checks for all the docstrings that
have sample sessions from the interactive interpreter, if they exist
it executes them and compares the output with the results as specified
in the sample sessions. It complains if the results don't match as
documented. When we execute this script as a stand-alone script we
will get back the prompt with no messages which means all the tests
passed::

  $ python gcd.py
  $ 

If we further want to get a more detailed report of the tests that
were executed we can run python with -v as the command line option
to the script::

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
outputs of the test cases do not contain any blank lines. In such
cases we may have to use the exact string *<BLANKLINE>*

For the sake of illustrating a failing test case, let us assume that
we made a small mistake in our code. Instead of returning **a** when b
= 0 we typed it as return b when b = 0. So all the gcds returned will
have the value of 0 in such a piece of code. The code looks as
follows::

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

Executing this code snippet without -v option to the script::

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
the script. This is pretty much about the doctest module in
Python. doctest is extremely useful when we want to test each Python
function or module individually. For more information about the
doctest module refer to the Python library reference on doctest[0].

unittest framework
~~~~~~~~~~~~~~~~~~

Not too far ahead we go we, we will start complaining that the doctest
is not sufficient to write complicated tests especially when we want
to automate our tests, write tests that need to test for more
convoluted code pieces. For such scenarios Python provides a unittest
framework.  unittest framework provides methods to efficiently
automate tests, setup and teardown functionalities which helps to
setup the initializing code and data for executing the specific tests
and cleanly shutting them down once the tests are executed and ways to
aggregate tests into collections and better way of reporting the
tests.

Let us continue testing our gcd function in the Python module named
gcd.py. To get ourselves started, the unittest framework expects us to
subclass TestCase class in unittest module and place all our test code
as methods of this class. We will begin the name of the test method
with **test_** so that the test runner knows which methods are to be
executed as tests. We will use the test cases supplied by
gcd_testcases.dat. Lastly, to illustrate the way to test Python code
as a module let create a new file called test_gcd.py following the
same convention used to name the test methods. We will place our test
code within test_gcd.py module. Our test code looks like this::
  
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

Please note that although we highly recommend to write a docstring for
all the classes, functions and modules we have not done so to keep
above code compact and we have left it as an exercise for the you to
add them.

Coming back to tests themselves, since we don't want to read this file
into memory each time we run a separate test method, we will read all
the data in the file into Python lists in the setUp method. The entire
data file is kept in a list called test_cases which happens to be an
attribute of the TestGCDFunction class. In the tearDown method of the
class we will delete this attribute to free up the memory and close
the opened file.

Our actual test code sits in the method which begins with the name
**test_** as said earlier, the test_gcd method. Note that we import
the gcd Python module we have written at the top of this test file and
from this test method we call the gcd function within the gcd module
to be tested with the each set of **a** and **b** values in the
attribute test_cases. Once we execute the function we obtain the
result and compare it with the expected result as stored in the
corresponding test_cases attribute using the assertEqual methods
provided by our parent class TestCase in the unittest framework. There
are several other assertion methods supplied by the unittest
framework. For a more detailed information about this, refer to the
unittest library reference at [1].

nose
====

Now we know almost all the varities of tests we may have to use to
write self-sustained, automated tests for our code. There is one last
thing that is left. However one question remains, how do we easily
organize choose and run the tests that is scattered around several
files? 

To further explain, the idea of placing tests with in the Python
scripts and executing that test scripts themselves as stand-alone
scripts works well as long as we have our code in a single Python file
or as long as the tests for each script can be run separately. But in
a more realistic software development scenario, often this is not the
case. The code is spread around multiple Python modules and may be
even across several Python packages.

In such a such a scenario we wish we had a better tool to
automatically aggregate these tests and execute them. Fortunately for
us there exists a tool called nose. Although nose is not part of the
standard Python distribution itself, it can be very easily installed
by using easy_install command as follows::

  $ easy_install nose

Or download the nose package from [2], extracting the archive and
running the command from the extracted directory::

  $ python setup.py install

Now we have nose up and running, but how do we use it? It is very
straight forward as well. We will use the command provided by nose
called as nosetests. Run the following command in the top level
directory of your code::

  $ nosetests

Thats all, nose automatically picks all the tests in all the
directories and subdirectories in our code base and executes them
all. However if we want to execute specific tests we can pass the test
file names or the directories as arguments to nosetests command. For a
detailed explanation about this, refer to [3]

Conclusion
==========

Now we have all the trappings we want to write state-of-the art
tests. To emphasize the same point again, any code which was written
before writing the test and the testcases in hand is flawed by
design. So it is recommended to follow the three step approach while
writing code for any project as below:

  1. Write failing tests with testcases in hand.
  2. Write the code to pass the tests.
  3. Refactor the code for better performance.

This approach is very famously known to the software development world
as "Red-Green-Refactor" approach[4].


[0] - http://docs.python.org/library/doctest.html
[1] - http://docs.python.org/library/unittest.html
[2] - http://pypi.python.org/pypi/nose/
[3] - http://somethingaboutorange.com/mrl/projects/nose/0.11.2/usage.html
[4] - http://en.wikipedia.org/wiki/Test-driven_development
