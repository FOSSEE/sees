.. Objectives
.. ----------
   
   .. At the end of this tutorial, you will be able to:
   
   ..   1. Prepare scripts using 'Control Operators'.
   ..   2. Understand what 'Environment Variables' are.

.. Prerequisites
.. -------------

..   1. Using Linux tools - Part 1
..   2. Using Linux tools - Part 2
..   3. Using Linux tools - Part 3
..   4. Using Linux tools - Part 4
..   5. Using Linux tools - Part 5
..   6. Using Linux tools - Part 6


 
Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and Welcome to the tutorial on
'Using linux tools - Part 7'.

.. L2

{{{ Show the 'Objectives' slide }}}

.. R2

At the end of this tutorial, you will be able to,

 1. Prepare scripts using 'Control Operators'.
 2. Understand what 'Environment Variables' are.
 
.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial, we suggest you to complete the
tutorials, "Using Linux tools, Part 1 to Part 6".

.. R4

We have many 'Control Structures and Operators' available in the linux bash.
Let us look at how to use them.
To write an 'if', or an 'if-else' construct, we need to check or test for a
condition(s). The ``test`` command allows us to test for condition(s). It has
a whole range of tests that can be performed. The man page of ``test``
gives you the complete listing of various types of tests that can be performed 
with it.

Let's write a simple script with an ``if`` condition that tests whether a
directory with a particular name, exists or not.

.. L4

.. L5

{{{ Show slide, 'if' }}}

.. R5

Let us create a script named ``dir-test.sh`` with this code.

    #!/bin/bash
    if test -d $1
    then
      echo "Yes, the directory" $1 "is present"
    fi

When the script is run with an argument, it will print a message, if a
directory with the said name exists in the current working directory.

.. R6

Let's write a simple script which returns back whether the argument passed
is negative or not.

.. L6

{{{ Open the file sign.sh and show }}}
::

   #!/bin/bash
   if test $1 -lt 0
   then
     echo "number is negative"
   else
     echo "number is non-negative"
   fi

.. R7

We can run the file with a set of different inputs and see if it works.

.. L7

{{{ Switch to terminal }}}
::

   ./sign.sh -11

.. R8

Instead of using the ``test`` command, square brackets may also be used.

.. L8

.. L9

{{{ Show slide, [ ] - alias for test }}}

.. R9

Note that the spacing is important, when using the square brackets.
The left square bracket ( ``[`` ) should be followed by a space and the right 
square bracket ( ``]`` ) should be preceded by a space.

Let's create something interesting using the 'if-else' clause. Let's write a
script, that greets the user, based on the time.

.. L10

{{{ Open the file clause.sh and show }}}
{{{ Highlight the required content wherever necessary, while narrating }}}

.. R10

There are a couple of new things in this script. ``$LOGNAME`` is another
'environment variable', which has the login name of the  user. The variables,
``hour`` and ``now`` are actually taking the output of the commands that
are placed in the back quotes.

Now, let us see how to run loops in bash. We shall look at the ``for`` and
the ``while`` loops.

.. L11

{{{ Show slide, 'for' }}}

.. R11

Suppose we have a set of files, whose file-names contain numbers before the 
text, say ``08 - Society.mp3``. We would like to rename these files by 
removing the numbers before the text. How would we go about doing that?

It is clear from the problem statement that we could loop over the list of
files and rename each of them.

.. R12

First, let us look at a simple ``for`` loop, to understand how it works.

.. L12

{{{ Switch to terminal }}}
::

    for animal in rat cat dog man
    do
      echo $animal
    done

.. R13

We just wrote a list of animals, each name separated by a space
and then printed each name on a separate line. The variable ``animal`` is a
'dummy' or a 'loop variable'. It can then be used to refer to the element of
the list that is currently being dealt with. We could, obviously, use
something as lame as ``i`` in place of ``animal``.

.. L13

.. R14

To generate a range of numbers and iterate over them, we do the following.

.. L14

{{{ Open the script ``for-1.sh`` and show }}}

.. R15

Now, let us run the script and see what we get,

.. L15

{{{ Switch to terminal }}}
::

    sh for-1.sh

.. R16

Now, we use a ``for`` loop to list the files that we are interested in.

.. L16

{{{ Open the script ``for-2.sh`` and show }}}
{{{ Switch to terminal }}}
::

    sh for-2.sh

.. R17
    
If the file-names contain spaces, ``for`` assumes, each word separated by a 
space,to be a single item in the list and prints it in a separate line. We 
could modify the script slightly to overcome this problem.

.. L17

{{{ Open the script ``for-3.sh`` and show }}}
{{{ Switch to terminal }}}
::

    sh for-3.sh

.. R18

Now, we have each file name printed on a separate line. The file names are
in the form ``dd - Name.mp3`` and it has to be changed to the format
``Name.mp3``. Also, if the name has spaces, we wish to replace it with
hyphens.

.. L18
 
{{{ Open the script ``for-4.sh`` and show }}}
{{{ Switch to terminal }}}
::

    sh for-4.sh

.. R19

Now, we simply replace the echo command with a ``mv``  command.

.. L19

{{{ Open the script ``for-5.sh`` and show }}}
{{{ Switch to terminal }}}
::

    sh for-5.sh

.. R20

We see that we get our required output. All the files have been renamed and
the spaces are removed.
Now let us move ahead with ``while`` loop.
The ``while`` command allows us to continuously execute a block of commands
until the command that is controlling the loop is executing successfully.

.. L20

.. R21

Let's start with the lamest example of a ''while'' loop.

.. L21

{{{ Open the script ``while-1.sh`` and show }}}
{{{ Switch to terminal }}}
::

    sh while-1.sh

.. R22

This, as you can see, is an infinite loop that prints ``True``.

Say, we wish to write a simple program that takes input from the user
and prints it back, until the input is ``quit``, which then quits the program.

.. L22

{{{ Open the script ``while-2.sh`` and show }}}
{{{ Switch to terminal }}}
::

    sh while-2.sh

.. L23

{{{ Show slide, Environment Variables }}}

.. R23

'Environment variables' are a way of passing information from the shell to the
programs that are run in it. Standard UNIX variables are split into two 
categories,'Environment variables' and 'Shell variables'. In broad terms, 
'Shell variables' apply only to the current instance of the shell and are 
used to set short-term working conditions; 'Environment variables' have a 
farther reaching significance, and are set at login, valid for the duration of 
the session. By convention, 'Environment variables' have UPPER CASE and 'Shell 
variables' have lower case names.

You can see an example of environment variables in the slide.

.. R24

To see all the variables and their values, we could use any of the
following,  

.. L24

{{{ Switch to terminal }}}
::

    printenv | less
    env
    
.. R25

We have looked at the 'PATH' variable, in the previous tutorial. We shall now
use the ``export`` command to change it's value.  

.. L25
::

   export PATH=$PATH:$HOME/bin

.. R26

Observe the difference in the value of 'PATH' variable before and after 
modifying it.

``export`` command is used to export a variable to the environment of all
the processes that are started from that shell.

.. L26

.. L27

{{{ Switch to 'Summary' slide }}}

.. R27

This brings us to the end of this tutorial.
In this tutorial, we have learnt to,
 
 1. Prepare scripts using control structures like ``if``, ``if-else``,
    ``for`` and ``while``.
 2. Use 'environment variables'.
 3. Export a variable to the environment of all the processes, using
    the ``export`` command.

.. L28

{{{ Show self assessment questions slide }}}

.. R28

Here are some self assessment questions for you to solve:

 1. Print the text ``dog man`` in such a way that the prompt
    continues after the text.

 2. How can you add a new path variable ``/data/myscripts`` to $PATH variable ?

.. L30

{{{ Solutions of self assessment questions on slide }}}

.. R30

And the answers,

 1. We print the given text using the ``echo`` command by using an additional
    option -n as,
::

    $echo -n dog man

 2. We can add a new path variable by using the export command as,
    
::

    $export PATH=$PATH://data/myscripts

.. L31

{{{ Show the Thank you slide }}}

.. R31

Hope you have enjoyed this tutorial and found it useful.
Thank you!

