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

This stub does nothing other than defining a new function called gcd which
takes two parameters a and b for which the GCD must be calculated. The body
of the function just contains pass which means it does nothing, i.e. empty.
We have our stub ready. One important thing we need to keep in mind when
we adopt TDD methodology is that we need to have a clear set of results
defined for our code units. To put it more clearly, for every given set of
inputs as test case we must have, before hand, the exact outputs that are
expected for those input test cases. If we don't have that we have failed
in the first step of the TDD methodology itself. We must never run for
outputs for our test cases after we have the code ready or even while
writing tests. The expected outputs/behaviour must be in our hands before
we start writing tests. Therefore let us define our test cases and the
expected output for those inputs. Let one of our test cases be 48 and 64
as *a* and *b* respectively. For this test case we know that the GCD is
16. So that is the expected output. Let our second test case be 44 and
19 as *a* and *b* respectively. We know that their GCD is 1 by simple paper
and pen calculation.

Now we know what a test is? What are the ingredients required to write
tests? So what else should we wait for? Let us write our first test!::

  tc1 = gcd(48, 64)
  if tc1 != 16:
      print "Test failed for the case a=48 and b=64. Expected 16. Obtained
          %d instead." % tc1
      exit(1)
  
  tc2 = gcd(44, 19)
  if tc2 != 1:
      print "Test failed for the case a=44 and b=19. Expected 1. Obtained
          %d instead." % tc2
      exit(1)

  print "All tests passed!"

More realistic "Tests"
======================

Now we have completed writing our first test. Let us start writing tests
for more realistic
