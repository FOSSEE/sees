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

  1. Consider the following use case: We are given a large list of
     items called *data* where each item is a again a list with three
     values: username, which is a string; status of the user which
     can be one of the following three strings 'new', 'valid' or
     'invalid'; and the last login time which is a datetime Python
     object.  Write a function called **query** that takes a filter
     dictionary as a parameter and returns the result of the items in
     the *data* list. They keys of the dictionary can be 'user',
     'status' and 'logtime' and their corresponding values can be any
     of the valid values for the corresponding key. Example filter
     dictionary::

       filter = {
           'user': 'john'
           'status': 'new'
           }

     Place your function in a file called query.py. Before writing the
     actual function, follow the test driven development
     approach. First write a stub, fail the tests and then write the
     code and make sure the tests pass. Specifically use unittest
     framework to test this function. Place your tests in a file
     called test_query.py

     A developer wrote a small utility function in a file named
     user_utils.py which uses your **query** function which looks as
     follows::

       def login_util(user=None):
           """Takes a user name and returns his last login time if the
           user is a valid user, else return None. If the user is
           'host' it returns the last login time of all the users.
           """

           filter_dict = {
               'user': user
               'status': 'active'
               }

           if user == 'host':
               filter_dict['status'] + ['new', 'invalid']

           return query(filter_dict)

     Unfortunately the developer did not provide us with the test
     cases. We wrote the following test cases for you to only discover
     that the function miserably fails. 

     The tests were placed in a file called test_user_utils.py and we
     have used the unittest framework::

       import query
       import user_utils
       import unittest

       class TestUserUtils(unittest.TestCase):
        
           def setUp(self):
               """Boiler plate method to provide common data to all
               the test methods.
               """
               self.test_names = ['Alex', 'Guido', 'Thomas', 'host',
                   'Tom', 'James']
               self.data_len = len(query.data)

           def test_login_utils(self):
               """Tests for the login_utils function.
               """

               for name in self.test_names:
                   if name == 'host':
                       assertEqual(len(user_utils.login_utils(name)), self.data_len)
                   else:
                       assertLess(len(user_utils.login_utils(name)), self.data_len)

           def tearDown(self):
               """Boiler plate method to clean up all the data created
               for tests.
               """

               del self.test_names
               del self.data_len

     Fix the bug, run the tests to make sure the function passes the
     tests and if possible refactor the code with a better approach.
