======================================
Lab Workbook - Test Driven Development
======================================

The notation that follows every question denotes the level on the
Revised Bloom's Taxonomy.

Lab - 1
=======

  1. Write a stub function for calculating the LCM of two numbers.
  2. Write the tests for the LCM function, place the tests in if
     __name__ == '__main__': part of the Python file. Demonstrate that
     the tests fail.
  3. Implement the code for the LCM function, using the gcd function
     provided in the examples in the chapter. Demonstrate the tests
     pass. (For the algorithm refer to Wikipedia - [0])
  4. Alternatively, build a set of test cases, preferably a large
     number of cases, place it in a text file and use these test cases
     to test your LCM function. Demonstrate that tests still continue
     to pass.

[0] - http://en.wikipedia.org/wiki/Least_common_multiple#Reduction_by_the_greatest_common_divisor

Lab - 2
=======

  1. Write the stub function, followed by the tests(demonstrating the
     failed tests), in turn followed by the code(demonstrating the
     passing tests) to calculate the number of days between two
     dates. Name your function num_of_days(). The function should take
     two arguments, both being tuples. Each tuple represents the date
     in the format of (dd, mm, yyyy) where dd, mm and yyyy are
     integers.
  2. Rewrite the num_of_days() function to take the start date as an
     optional argument. If the start date is not specified calculate
     the number of days between the only specified date since Unix
     epoch. Prior to manipulating the code to do this, make sure you
     change the tests, make them fail and then refactor the code.


Lab -3
======

  1. Move the tests that were written to GCD function in the examples
     of this chapter to a separate function called test_gcd(). Do the
     same for LCM function and num_of_days() function. Make sure when
     the respective Python files are executed as stand alone scripts
     these tests executed.
  2. Put all these files in a single directory called utils and run
     the nosetests command. Make a report of the results.
  3. Write doctests to each of the above functions. Demonstrate and
     report the results as executed by running the doctests using
     doctest.testmod() function and using nosetests command.

Lab - 4
=======

  1. 
