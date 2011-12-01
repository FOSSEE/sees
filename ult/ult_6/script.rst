.. Objectives
.. ----------
   
   .. At the end of this tutorial, you will be able to:
   
   ..   1. Prepare a simple shell script. 
   ..   2. Run a script successfully and print it's result.
   ..   3. Understand what an environment variable is.

.. Prerequisites
.. -------------

..   1. Using Linux tools - Part 1
..   2. Using Linux tools - Part 2
..   3. Using Linux tools - Part 3
..   4. Using Linux tools - Part 4
..   5. Using Linux tools - Part 5

 
Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and Welcome to the tutorial on 
'Using linux tools - Part 6'.

.. L2

{{{ Show slide with objectives }}} 

.. R2

At the end of this tutorial, you will be able to,

 1. Prepare a simple shell script. 
 #. Run a script successfully and print it's result.
 #. Understand what an environment variable is.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Using Linux tools from Part 1 to Part 5".

Let us start with creating a simple shell script.
A shell script is simply a sequence of commands, that are put into a file,
instead of entering them one by one onto the shell. The script can then be
run, to run the sequence of commands in a single shot instead of manually
running, each of the individual commands. 
For instance, let's say we wish to create a directory called ``marks`` in the
home folder and save the results of the students into a file
``results.txt``. 

.. R4

We open our editor and save the following text to ``results.sh``

.. L4

{{{ Open an editor and type the following }}}
::

    #!/bin/bash
    mkdir ~/marks
    cut -d " " -f 2- marks1.txt | paste -d " " students.txt - | sort > ~/marks/results.txt

.. R5

We can now run the script as, 

.. L5

{{{ Open the terminal }}}
::

    ./results.sh

.. R6

We get an error saying, Permission denied! Why? Can you think of the
reason? Yes, the file doesn't have execute permissions.
We make the file executable and then run it. 

.. L6
::

    chmod u+x results.sh
    ./results.sh

.. R7

We get back the prompt. We can check the contents of the file
``results.txt`` to see if the script has run. 

So, here, we have our first shell script. The first line of the script is used 
to specify the interpreter or shell which should be used to execute the script. 
In this case, we are asking it to use the bash shell.
Once, the script has run, we get back the prompt. Here, we had to manually check,
if the contents of the file are correct. It would be useful to have our script 
print out messages. For this, we can use the ``echo`` command. We can edit our 
``results.sh`` script, as follows.

.. L7

{{{ Open an editor and type the following }}}
::

    #!/bin/bash
    mkdir ~/marks
    cut -d " " -f 2- marks1.txt | paste -d " " students.txt - | sort > ~/marks/results.txt
    echo "Results generated."

.. R8

Now, on running the script, we get a message on the screen informing us,
when the script has run. 

Let's now say, that we wish to let the user decide the file to which the
results should be written to. The results file, should be specifiable by an
argument in the command line. We can do so, by editing the file, as below. 

.. L8

{{{ Make the necessary changes in the previous script }}}

::

    #!/bin/bash
    mkdir ~/marks
    cut -d " " -f 2- marks1.txt | paste -d " " students.txt - | sort > ~/marks/$1
    echo "Results generated."


{{{ Highlight the text ``$1`` }}}

.. R9

The ``$1`` above, corresponds to the first command line argument to the
script. So, we can run the script as shown below, to save the results to
``grades.txt``. 

.. L9
::

    ./results.sh grades.txt    

.. R10

When we run the ``results.sh`` file, we are specifying the location of the
script by using ``./``. But for any of the other commands, 
we didn't have to specify their locations. Why? The
shell has a set of locations where it searches, for the command that we are
trying to run. 

.. L10

.. L11

{{{ Show slide, PATH }}}

.. R11

These set of locations are saved in an "environment"
variable called PATH.let us look at what the value of the PATH variable is. To view the
values of variables, we can use the echo command.

.. L12

{{{ Switch to the terminal }}}
::

    echo $PATH

.. R12

So, these are all the paths that are searched, when looking to execute a
command. If we put the results.sh script in one of these locations, we
could simply run it, without using the ``./`` at the beginning. 

.. L13

{{{ Show slide, variables & comments }}}

.. R13

As expected, it is possible to define our own variables inside our shell
scripts. For example,

.. L14

{{{ Switch to the terminal }}}
::

    name="FOSSEE"

.. R14

It creates a new variable ``name`` whose value is ``FOSSEE``. To refer to this
variable, inside our shell script, we would refer to it, as ``$name``.
Note that, there is no space around the ``=`` sign. 

.. L15
::

    ls $name*

.. R15

.. R16

It is possible to store the output of a command in a variable, by enclosing
the command in back-quotes. 

.. L16
::

    count=`wc -l wonderland.txt`

.. R17

It saves the number of lines in the file ``wonderland.txt`` in the variable
count. 

The ``#`` character is used to comment out content from a shell script.
Anything that appears after the ``#`` character in a line, is ignored by
the bash shell. 

.. L18

.. L19

{{{ Switch to 'Summary' slide }}}

.. R19

This brings us to the end of the end of this tutorial.
In this tutorial, we have learnt to, 

 1. Prepare a shell script.
 #. Display the result of a script, using the ``echo`` command.
 #. Use the environment variable ``PATH``.
 #. Create variables and comment out content using the ``#`` sign.

.. L20

{{{ Show self assessment questions slide }}}

.. R20

Here are some self assessment questions for you to solve

.. L21

{{{ Solution of self assessment questions on slide }}}

.. R21

And the answers,

.. L22

{{{ Show the Thank you slide }}}

.. R22

Hope you have enjoyed this tutorial and found it useful.
Thank you!


