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

  madhu@madhu:~/Desktop$ python gcd.py
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

  madhu@madhu:/media/python/sttp/tdd$ python gcd.py
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

Much shorter and sweeter! And it passes all the tests!


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

Let us  start writing tests  for more realistic test  cases. Generally
tests  are predetermined  as said  above, if  not the  code  itself is
flawed. The predetermined tests are stored along with the test code in
some  persistent way  like  in a  database,  a text  file,  a file  of
specific format  like XML or  in other way.  Let us continue  with our
example of  GCD function. We  will keep all  our test cases in  a text
file,  which  is  indeed   persistent.  Let  our  file  have  multiple
lines. Each line in this file  corresponds to a single test case. Each
line consists of  three coloumns: first two coloumns  are the integers
for  which the GCD  has to  be computed  and the  last coloumn  is the
expected GCD  to the  preceding two  numbers. So how  do we  write our
tests  to use  these  test cases?  Pretty  simple, let  us review  the
machinery required first.

  1. File reading: We already have learnt this in our chapters on
     Basic Python.
  2. Parsing read data from file: This just involves a for loop over
     the data since we know that file contains lines which are
     equivalent to file records and hence parse the data line by line
     as strings as we iterate Over it and convert it to required data
     type.

Since we already have all the machinery required, let us proceed writing
our test cases.





%%%%%%%%% Much Later %%%%%%%%%%%%%%%%%
The idea of placing the tests with in the Python scripts and to
execute them when the script is run as a stand-alone script works well
as long as we have our code in a single Python file or the tests for
each script can be run separately. But in a more realistic software
development scenario, often this is not the case. The code is spread
around multiple Python scripts, each Python script also being called
as a Python module, and across several Python packages. In such a
scenario we may want to do more.
