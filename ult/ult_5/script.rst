.. Objectives
.. ----------
   
   .. At the end of this tutorial, you will be able to:
   
   ..   1. 
   ..   2.

.. Prerequisites
.. -------------

..   1. Using Linux tools - Part 1
..   2. Using Linux tools - Part 2
..   3. Using Linux tools - Part 3
..   4. Using Linux tools - Part 4

 
Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and Welcome to the tutorial on 
'Using linux tools - Part 5'.

.. L2

{{{ Show slide with objectives }}} 

.. R2

At the end of this tutorial, you will be able to,

 1. Learn text editing tools of linux. 

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Using Linux tools from Part 1 to Part 4".

.. R4

In this tutorial, we shall learn about text processing.
Consider data kept in two files, namely marks1.txt and students.txt
Let us see what data they contain,

.. L4

{{{ Open the terminal }}}
::

    cat marks1.txt
    cat students.txt

.. R5

Let's say we wish to sort the output in the alphabetical order
of the names of the files. We can use the ``sort`` command for this
purpose.

We just pipe the previous output to the ``sort`` command as,

.. L5
::

    cut -d " " -f 2- marks1.txt | paste -d " " students.txt -| sort

.. R6

Let's say we wish to sort the names, based on the marks in the first
subject i.e. the first column after the name. ``sort`` command also allows us to
specify the delimiter between the fields and sort the data on a particular
field. ``-t`` option is used to specify the delimiter and ``-k`` option
is used to specify the field. 

.. L6
::

    cut -d " " -f 2- marks1.txt | paste -d " " students.txt -| sort -t " " -k 2

.. L7

{{{ Show slide with, Sort... }}}

.. R7

This command give us a sorted output as required. But, it would be
nicer to have the output sorted in the reverse order.

.. R8

 ``-r`` option allows the output to be sorted in the reverse order and 
the ``-n`` option is used to choose a numerical sorting. 

.. L8

{{ Switch to the terminal }}}
::

    cut -d " " -f 2- marks1.txt | paste -d " " students.txt -| sort -t " " -k 2 -rn

.. R9

Suppose, While you are compiling the student marklist, Anne walks up to you and
wants to know her marks. You, being a kind person that you are, oblige.
But you do not wish to her to see the marks that others have scored. What
do you do? The ``grep`` command comes to your rescue. 

``grep`` is a command line text search utility. You can use it to search
for Anne and show her, what she scored. ``grep`` allows you to search for a
search string in files. But you could, like any other command, pipe the
output of other commands to it. So, we shall use the previous combination
of cut and paste that we had, to get the marks of students along with their
names and search for Anne in that. 

.. L9
::

    cut -d " " -f 2- marks1.txt | paste -d " " students.txt - | grep Anne 

.. R10

This will give you only the line containing the word Anne as the output.
The grep command is by default case-sensitive. So, you wouldn't have got
the result if you had searched for anne, with a small a, instead of 
Anne, with a capital a. But, what if you didn't know, whether the name was 
capitalized or not? ``grep`` allows you to do case-insensitive searches 
by using the ``-i`` option. 

.. L10
::

    cut -d " " -f 2- marks1.txt | paste -d " " students.txt - | grep -i Anne 

.. R11

Now, in another scenario, if you wished to print all the lines, which do
not contain the word Anne, you could use the ``-v`` option. 

.. L11
::

    cut -d " " -f 2- marks1.txt | paste -d " " students.txt - | grep -iv Anne

.. R12

grep allows you to do more complex searches, for instance, searching for
sentences starting or ending with a particular pattern and regular
expression based searches. 

{{{ Show slide with, tr }}}

``tr`` is a command that takes two sets of characters as parameters, and
replaces occurrences of the characters in the first set with the
corresponding elements from the other set. It reads from the standard
output and writes to the standard output. 

For instance, if you wish to replace all the lower case letters in the
students file with upper case, you can do it as, 

.. L12

{{{ Switch to the terminal }}}
::

    cat students.txt | tr a-z A-Z

.. R13

A common task is to remove empty newlines from a file. The ``-s`` flag
causes ``tr`` to compress sequences of identical adjacent characters in its
output to a single token. For example,

.. L13
::

    tr -s '\n' '\n'

.. R14

Hit enter 2-3 times and see that every time we hit enter we get a newline.

.. L14
::

    <Enter>
    <Enter> 

.. R15

It replaces sequences of one or more newline characters with a single newline.

The ``-d`` flag causes ``tr`` to delete all tokens of the specified set of
characters from its input. In this case, only a single character set
argument is used. The following command removes carriage return characters,
thereby converting a file in DOS/Windows format to the Unix format. 

.. L15
::

    cat foo.txt | tr -d '\r' > bar.txt

.. R16

The ``-c`` flag complements the first set of characters.

.. L16
::

    tr -cd '[:alnum:]' 

.. R17

therefore removes all non-alphanumeric characters.

Suppose we have a list of items, say books, and we wish to obtain a list 
which names of all the books only once, without any duplicates. We use 
the ``uniq`` command to achieve this. Let us first have a look at our file

.. L17
::

    cat items.txt

.. R18

Now, let us try and get rid of the duplicate lines from this file using 
the ``uniq`` command.

.. L18
::

    uniq items.txt

.. R19

Nothing happens! Why? The ``uniq`` command removes duplicate lines only when they 
are next to each other. So, henceforth, we get a sorted file from the original file and work 
with that file. 

.. L19
::

    sort items.txt | uniq

.. R20

``uniq -u`` command gives the lines which are unique and do not have any 
duplicates in the file. ``uniq -d`` outputs only those lines which have duplicates. 

.. L20 
::

    uniq -u items-sorted.txt 

.. R21

The ``-c`` option displays the number of times each line occurs in the file.

.. L21
::

    uniq -dc items-sorted.txt

.. L22

{{{ Show summary slide }}}

.. R22

This brings us to the end of the end of this tutorial.
In this tutorial, we have learnt to, 
 
  1. Use the ``sort`` command to sort lines of text files.
  #. Use the ``grep`` command to search text pattern.
  #. Use the ``tr`` command to translate and/or delete characters.
  #. Use the ``uniq`` command to omit repeated lines in a text. 

.. L23

{{{ Show self assessment questions slide }}}

.. R23

Here are some self assessment questions for you to solve

.. L24

{{{ Solution of self assessment questions on slide }}}

.. R24

And the answers,

.. L25

{{{ Show the Thank you slide }}}

.. R25

Hope you have enjoyed this tutorial and found it useful.
Thank you!
