Strings
=======

We looked at strings, when looking at the sequence data-types of Python. We
shall now look at them in a greater detail.

So, what are strings? In Python anything within either single quotes or
double quotes or triple single quotes or triple double quotes are strings.

::

  'This is a string'
  "This is a string too'
  '''This is a string as well'''
  """This is also a string"""
  'p'
  ""

Note that it really doesn't matter how many characters are present in the
string. The last example is a null string or an empty string.

Having more than one control character to define strings is handy when one of
the control characters itself is part of the string. For example::

  "Python's string manipulation functions are very useful"

By having multiple control characters, we avoid the need for escaping
characters -- in this case the apostrophe.

The triple quoted strings let us define multi-line strings without using any
escaping. Everything within the triple quotes is a single string no matter
how many lines it extends

::

   """Having more than one control character to define
   strings come as very handy when one of the control
   characters itself is part of the string."""

We can assign this string to any variable

::

  a = 'Hello, World!'

Now ``a`` is a string variable. A string is a sequence of characters, as we
have already seen. In addition string is an immutable collection. So all the
operations that are applicable to any other immutable collection in Python
works on string as well. So we can add two strings

::

  a = 'Hello'
  b = 'World'
  c = a + ', ' + b + '!'

We can add string variables as well as the strings themselves all in the same
statement. The addition operation performs the concatenation of two strings.

Similarly we can multiply a string with an integer

::

  a = 'Hello'
  a * 5

gives another string in which the original string 'Hello' is repeated
5 times.

Let's now look at accessing individual elements of strings. Since, strings
are collections we can access individual items in the string using the
subscripts

::

  a[0]

gives us the first character in the string. The indexing starts from 0
for the first character and goes up to n-1 for the last character. We
can access the strings from the end using negative indices

::

  a[-1]

gives us the last element of the string and 

::

    a[-2]

gives us second element from the end of the string

Let us attempt to change one of the characters in a string::

  a = 'hello'
  a[0] = 'H'

As said earlier, strings are immutable. We cannot manipulate a string.
Although there are some methods which let us manipulate strings, we will look
at them in the advanced session on strings. In addition to the methods that
let us manipulate the strings we have methods like split which lets us break
the string on the specified separator, the join method which lets us combine
the list of strings into a single string based on the specified separator.

Let us now learn to manipulate strings, specifically slicing and reversing
them, or replacing characters, converting from upper to lower case and
vice-versa and joining a list of strings.

Let us consider a simple problem, and learn how to slice strings and get
sub-strings.

Let's say the variable ``week`` has the list of the names of the days of the
week.

::

    week = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]


Now given a string ``s``, we should be able to check if the string is a
valid name of a day of the week or not. 

::

    s = "saturday"


``s`` could be in any of the forms --- sat, saturday, Sat, Saturday,
SAT, SATURDAY. For now, shall now be solving the problem only for the forms,
sat and saturday. We shall solve it for the other forms, at the end of
the tutorial. 

So, we need to check if the first three characters of the given string
exists in the variable ``week``. 

As, with any of the sequence data-types, strings can be sliced into
sub-strings. To get the first three characters of s, we say,

::

    s[0:3]

Note that, we are slicing the string from the index 0 to index 3, 3
not included. 

::

    s = "saturday"
    s[:3]

Now, we just check if that substring is present in the variable ``week``.

::

    s[:3] in week          

Let us now consider the problem of finding out if a given string is
palindromic or not. First of all, a palindromic string is a string that
remains same even when it has been reversed.

Let the string given be ``malayalam``.

::

    s = "malayalam"

Now, we need to compare this string with it's reverse. 

Again, we will use a technique common to all sequence data-types,
[::-1]

So, we obtain the reverse of s, by simply saying, 

::

    s[::-1]

Now, to check if the string is ``s`` is palindromic, we say
::

    s == s[::-1]

As, expected, we get ``True``. 

Now, if the string we are given is ``Malayalam`` instead of ``malayalam``,
the above comparison would return a False. So, we will have to convert the
string to all lower case or all upper case, before comparing. Python provides
methods, ``s.lower`` and ``s.upper`` to achieve this.

Let's try it out. 
::

   s = "Malayalam"

   s.upper()

   s

As you can see, s has not changed. It is because, ``upper`` returns a new
string. It doesn't change the original string.

::

   s.lower()

   s.lower() == s.lower()[::-1]
   
So, as you can see, now we can check for presence of ``s`` in ``week``, in
whichever format it is present -- capitalized, or all caps, full name or
short form.

We just convert any input string to lower case and then check if it is
present in the list ``week``.

Now, let us consider another problem. We often encounter e-mail id's which
have @ and periods replaced with text, something like info[at]fossee[dot]in.
We now wish to get back proper e-mail addresses.

Let's say the variable email has the email address.

::

   email = "info[at]fossee[dot]in"

Now, we first replace the ``[at]`` with the ``@``, using the replace method
of strings.

::

   email = email.replace("[at]", "@")
   print email

   email = email.replace("[dot]", ".")        
   print email

Now, let's look at another interesting problem where we have a list of e-mail
addresses and we wish to obtain one long string of e-mail addresses separated
by commas or semi-colons.

::

  email_list = ["info@fossee.in", "enquiries@fossee.in",  "help@fossee.in"]

Now, if we wish to obtain one long string, separating each of the
email id by a comma, we use the join operator on ``,``. 

::

  email_str = ", ".join(email_list)
  print email_str

Notice that the email ids are joined by a comma followed by a space. 

That brings us to the end of our discussion on strings. Let us now look at
conditionals. 

Conditionals
============

Whenever we have two possible states that can occur depending on a whether a
certain condition we can use if/else construct in Python.

For example, say, we have a variable ``a`` which stores integers and we are
required to find out whether ``a`` is even or odd. an even number or an odd
number. Let's say the value of ``a`` is 5, now. 

::

  a = 5

In such a case we can write the if/else block as

::

  if a % 2 == 0:
      print "Even"
  else:
      print "Odd"

If ``a`` is divisible by 2, i.e., the result of "a modulo 2" is 0, it prints
"Even", otherwise it prints "Odd".

Note that in such a case, only one of the two blocks gets executed depending
on whether the condition is ``True`` or ``False``.

There is a very important sytactic element to understand here. Every code
block begins with a line that ends with a ``:``, in this example the ``if``
and the ``else`` lines. Also, all the statements inside a code block are
intended by 4 spaces. Returning to the previous indentation level, ends the
code block.

The if/else blocks work for a condition, which can take one of two states.
What do we do for conditions, which can take more than two states?

Python provides if/elif/else blocks, for such conditions. Let us take an
example. We have a variable ``a`` which holds integer values. We need to
print "positive" if ``a`` is positive, "negative" if it is negative or "zero"
if it is 0.

Let us use if/elif/else ladder for it. For the purposes of testing our
code let us assume that the value of a is -3

::

  a = -3

  if a > 0:
      print "positive"
  elif a < 0:
      print "negative"
  else:
      print "zero"    

All the syntax and rules as said for if/else statements hold. The only
addition here is the ``elif`` statement which can have another condition of
its own.

Here too, exactly one block of code is executed -- the block of code which
first evaluates to ``True``. Even if there is a situation where multiple
conditions evaluate to True all the subsequent conditions other than the
first one which evaluates to True are neglected. Consequently, the else block
gets executed if and only if all the conditions evaluate to False.

Also, the ``else`` block in both if/else statement and if/elif/else is
optional. We can have a single if statement or just if/elif statements
without having else block at all. Also, there can be any number of elif's
within an if/elif/else ladder. For example

::

  if user == 'admin':
      # Do admin operations
  elif user == 'moderator':
      # Do moderator operations
  elif user == 'client':
      # Do customer operations

is completely valid. Note that there are multiple elif blocks and there
is no else block.

In addition to these conditional statements, Python provides a very
convenient ternary conditional operator. Let us take the following example
where we have a score string, which can either be a number in the range 0 to
100 or the string 'AA', if the student is absent. We wish to convert the
score string, into an integer, whenever possible. If the score string is
'AA', we wish to make the corresponding value 0. Let us say the string score
is stored in score_str variable. We can do it using an ``if-else`` construct
as below

::

    if score_str != 'AA':
        score = int(score_str)
    else:
        score = 0

The same thing can be done using a ternary operator, which reads more natural
and has greater brevity. 

::

    score = int(score_str) if score_str != 'AA' else 0

Moving on, there are certain situations where we will have no operations or
statements within a block of code. For example, we have a code where we are
waiting for the keyboard input. If the user enters "c", "d" or "x" as the
input we would perform some operation nothing otherwise. In such cases "pass"
statement comes very handy.

::

  a = raw_input("Enter 'c' to calculate and exit, 'd' to display the existing
  results exit and 'x' to exit and any other key to continue: ")

  if a == 'c':
     # Calculate the marks and exit
  elif a == 'd':
     # Display the results and exit
  elif a == 'x':
     # Exit the program
  else:
     pass

In this case "pass" statement acts as a place holder for the block of code.
It is equivalent to a null operation. It literally does nothing. It can used
as a place holder when the actual code implementation for a particular block
of code is not known yet but has to be filled up later.

That brings us to the end of our discussion of conditionals. 

Loops
=====

We shall now, look at ``while`` and ``for`` loops. We shall look at how to
use them, how to break out of them, or skip some iterations in loops.

We shall first begin with the ``while`` loop. The ``while`` loop is used for
repeated execution as long as a condition is ``True``.

Let us print the squares of all the odd numbers less than 10, using the
``while`` loop.

::

    i = 1

    while i<10:
        print i*i
        i += 2

This loop prints the squares of the odd numbers below 10. 

The ``while`` loop, repeatedly checks if the condition is true and executes
the block of code within the loop, if it is. As with any other block in
Python, the code within the ``while`` block is indented to the right by 4
spaces.

Let us now solve the same problem of printing the squares of all odd numbers
less than 10, using the ``for`` loop. The ``for`` loop iterates over a list
or any other sequential data type. 

::

    for n in [1, 2, 3]:
        print n

Each of the elements of the list, gets printed. The variable ``n``, called
the loop variable, successively takes the value of each of the elements in
the list, in each iteration. 

Now, we could solve the problem of calculating the squares, by 

::

    for n in [1, 3, 5, 7, 9]: 
        print n*n

But, it is "unfair" to generate the list by hand. So, we use the ``range``
function to get a list of odd numbers below 10, and then iterate over it and
print the required stuff.

::

    for n in range(1, 10, 2):
        print n*n

The first argument to the ``range`` function is the start value, the second
is the stop value and the third is the step-size. The ``range`` function
returns a list of values from the start value to the stop value (not
included), moving in steps of size given by the step-size argument. 

Also, The start and the step values are optional. For instance, the code
below prints numbers from 0 to 9. 

::

    for n in range(10):
        print n

Let us now look at how to use the keywords, ``pass``, ``break`` and
``continue``.

As we already know, ``pass`` is just a syntactic filler. It is used
for the sake of completion of blocks, that do not have any code within
them. 

::

    for n in range(2, 10, 2):
        pass

``break`` is used to break out of the innermost loop. The ``while``
loop to print the squares of all the odd numbers below 10, can be
modified using the ``break`` statement, as follows
::

    i = 1

    while True:
        print i*i
        i += 2
        if i<10:
            break

``continue`` is used to skip execution of the rest of the loop on this
iteration and continue to the end of this iteration. 

Say, we wish to print the squares of all the odd numbers below 10, which are
not multiples of 3, we would modify the ``for`` loop as follows. 

::

    for n in range(1, 10, 2):
        if n%3 == 0:
            continue      
        print n*n
  
This brings us to the end of the section on loops. We have learned how to use
the ``for`` and ``while`` loops. 

Lists
=====

We have already seen lists as a kind of sequence data-type. We shall look at
them in greater detail, now. 

We will first create an empty list with no elements. 

::

    empty = [] 
    type(empty)
   
This is an empty list without any elements.

Let's now define a non-empty list. 

::

     p = ['spam', 'eggs', 100, 1.234]

Thus the simplest way of creating a list is typing out a sequence of
comma-separated values (or items) between two square brackets.

As we can see lists can contain different kinds of data. They can be
heterogeneous. In the previous example 'spam' and 'eggs' are strings whereas
100 and 1.234 are integer and float respectively. Below, is another example. 

::

      q = [[4, 2, 3, 4], 'and', 1, 2, 3, 4]

As you already know, we access an element of a list using its index. Index of
the first element of a list is 0. 

::
    p[0] 
    p[1] 
    p[3]


List elements can also be accessed using negative indexing. p[-1]
gives the last element of p. 

::
    p[-1]

As you can see you get the last element which is 1.234.

Similarly, -2 gives the second to last element and -4 gives the fourth from
the last which, in this case, is the first element.

::
   
    p[-2] 
    p[-4]

Using ``len`` function we can check the number of elements in the list
p. 

::
	 
    len(p)

We can append elements to the end of a list using the method append.

::

    p.append('onemore') 
    p
    p.append([1, 6])
    p
   
As we can see ``p`` is appended with 'onemore' and [1, 6] at the end.

Just like we can append elements to a list we can also remove them. There are
two ways of doing it. First, is by using the ``del`` command and the index of
the element. 

::

    del p[1]



will delete the element at index 1, i.e the second element of the list,
'eggs'. 

The other way is removing element by choosing the item. Let's say one wishes
to delete 100 from p list the syntax of the command would be

::

    p.remove(100)

but what if there were two 100's. To check that lets do a small
experiment. 

::

    p.append('spam') 
    p
    p.remove('spam') 
    p

If we check now we will see that the first occurence 'spam' is removed and
therefore `remove` removes the first occurence of the element in the sequence
and leaves others untouched.

Another other basic operation that we can perform on lists is concatenation
of two or more lists. We can combine two lists by using the "plus" operator.
Say we have

::

    a = [1, 2, 3, 4]
    b = [4, 5, 6, 7]
    a + b

When we concatenate lists using the "plus" operator we get a new list. We can
store this list in a new variable

::

    c = a + b
    c

It is important to observe that the "plus" operator always returns a new list
without altering the lists being concatenated in any way.

Let us now look at slicing and striding on lists. Let's create a list primes.

::

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

To obtain all the primes between 10 and 20 from the above list of primes we
say

::

    primes[4:8]

This gives us all the elements in the list starting from the element with the
index 4, which is 11 in our list, upto the element with index 8 (not
included). 

::

    primes[0:4]

will give us the primes below 10. Recall that the element with the index 4 is
not included in the slice that we get. 

By default the slice fetches all the elements between start and stop (stop
not-included). But, Python also provides the functionality to specify a step
size, when picking elements. Say, we have

::

    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

If we want to obtain all the odd numbers less than 10 from the list
``num`` we have to start from element with index 1 upto the index 10 in
steps of 2

::

    num[1:10:2]

When no step is specified, it is assumed to be 1. Similarly, there are
default values for start and stop indices as well. If we don't specify the
start index it is implicitly taken as the first element of the list

::

    num[:10]

This gives us all the elements from the beginning upto the 10th element but
not including the 10th element in the list "num". Similary if the stop index
is not specified it is implicitly assumed to be the end of the list,
including the last element of the list

::

    num[10:]

gives all the elements starting from the 10th element in the list
"num" upto the final element including that last element. Now

::

    num[::2]

gives us all the even numbers in the list "num".

We know that a list is a collection of data. Whenever we have a collection we
run into situations where we want to sort the collection. Lists support sort
method which sorts the list in-place

::

    a = [5, 1, 6, 7, 7, 10]
    a.sort()

Now the contents of the list ``a`` will be

::

    a
    [1, 5, 6, 7, 7, 10]

As the sort method sorts the elements of a list, the original list we had is
overwritten or replaced. We have no way to obtain the original list back. One
way to avoid this is to keep a copy of the original list in another variable
and run the sort method on the list. 

However, Python also provides a built-in function called sorted which sorts
the list which is passed as an argument to it and returns a new sorted list

::

    a = [5, 1, 6, 7, 7, 10]
    sorted(a)
  
We can store this sorted list another list variable

::

    sa = sorted(a)

Python also provides the reverse method which reverses the list in-place

::

    a = [1, 2, 3, 4, 5]
    a.reverse()

reverses the list ``a`` and stores the reversed list inplace i.e. in ``a``
itself. Let's see the list ``a``

::

    a
    [5, 4, 3, 2, 1]

But again the original list is lost. 

To reverse a list, we could use striding with negative indexing.

::

    a[::-1]

We can also store this new reversed list in another list variable.

That brings us to the end of our discussion on lists. 

.. 
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: nil
   fill-column: 77
   End:


