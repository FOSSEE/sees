Exercises
=========

1. Round a float to the nearest integer using ``int()``. 

#. What does this do? round(amount * 10)/10.0. How to round it to the nearest
   5 paise?

#. Print out the fibonacci sequence less than 30

#. Write a program that displays all three digit numbers that are equal to
   the sum of the cubes of their digits. That is, print numbers :math:`$abc$`
   that have the property :math:`$abc = a^3 + b^3 + c^3$` These are called
   :math:`$Armstrong$` numbers.

#. Collatz sequence                                              
                                                                 
   #. Start with an arbitrary (positive) integer.                
   #. If the number is even, divide by 2; if the number is odd multiply by 3
      and add 1.
   #. Repeat the procedure with the new number.                  
   #. There is a cycle of 4, 2, 1 at which the procedure loops.  
                                                                 
   Write a program that accepts the starting value and prints out the Collatz
   sequence.


#. Kaprekar’s constant                                             
                                                                   
   #. Take a four digit number–with at least two digits different. 
   #. Arrange the digits in ascending and descending order, giving A and D
      respectively.
   #. Leave leading zeros in A!                                    
   #. Subtract A from D.                                           
   #. With the result, repeat from step 2.                         
                                                                   
   Write a program to accept a 4-digit number and display the progression to
   Kaprekar’s constant.

#. Write a program that prints the following pyramid on the screen.  

   ::                                                                
                                                                     
       1                                                             
       2  2                                                          
       3  3  3                                                       
       4  4  4  4                                                    
                                                                     
                                                                     
   The number of lines must be obtained from the user as input. When can your
   code fail?

#. Write a function to return the gcd of two numbers.

#. Write a program to find Primitive Pythagorean Triads A pythagorean triad
   :math:`$(a,b,c)$` has the property :math:`$a^2 + b^2 = c^2$`. By primitive
   we mean triads that do not ‘depend’ on others. For example, (4,3,5) is a
   variant of (3,4,5) and hence is not primitive. And (10,24,26) is easily
   derived from (5,12,13) and should not be displayed by our program. Write a
   program to print primitive pythagorean triads. The program should generate
   all triads with a, b values in the range 0—100

#. Write a program that generates a list of all four digit numbers that have
   all their digits even and are perfect squares. For example, the output
   should include 6400 but not 8100 (one digit is odd) or 4248 (not a perfect
   square).


#. The aliquot of a number is defined as: the sum of the *proper* of the
   number. 

   For example, the ``aliquot(12) = 1 + 2 + 3 + 4 + 6 = 16``. 

   Write a function that returns the aliquot number of a given number.

#. A pair of numbers (a, b) is said to be *amicable* if the aliquot number of
   a is b and the aliquot number of b is a. 

   Example: ``220, 284`` 

   Write a program that prints all five digit amicable pairs.

#. Given an empty chessboard and one Bishop placed in any square, say (r, c),
   generate the list of all squares the Bishop could move to.

#. Given a string like, "1, 3-7, 12, 15, 18-21", produce the list
   ``[1,3,4,5,6,7,12,15,18,19,20,21]``

#. You are given date strings of the form “29, Jul 2009”, or “4 January
   2008”. In other words a number a string and another number, with a comma
   sometimes separating the items.Write a function that takes such a string
   and returns a tuple (yyyy, mm, dd) where all three elements are ints.

#. Count word frequencies in a file.

#. Given a dictionary of the names of students and their marks, identify how
   many duplicate marks are there? and what are these?

#. Given a string of the form "4-7, 9, 12, 15" find the numbers missing in
   this list for a given range.


.. 
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: nil
   fill-column: 77
   End:

