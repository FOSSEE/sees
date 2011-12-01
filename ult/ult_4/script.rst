.. Objectives
.. ----------
   
   .. At the end of this tutorial, you will be able to:
   
   ..   1. Understand what is Redirection and Piping.
   ..   2. Learn various features of shell.

.. Prerequisites
.. -------------

..   1. Using Linux tools - Part 1
..   2. Using Linux tools - Part 2
..   3. Using Linux tools - Part 3
 
Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and Welcome to the tutorial on 
'Using linux tools - Part 4'.

.. L2

{{{ Show slide with objectives }}} 

.. R2

At the end of this tutorial, you will be able to,

 1. Understand what is Redirection and Piping. 
 #. Learn various features of the shell.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Using Linux tools from Part 1 to Part 3".

.. R4

Let us begin with the concept of 'Redirection and Piping'  which can do the 
same operations as the ``cut`` and ``paste`` commands.

Consider the files ``marks.txt`` and ``students.txt``, which has the 
following contents

.. L4

{{{ Open the terminal }}}
::

    cat marks1.txt
    cat students.txt

.. R5

Let us view the contents of both the files side-by-side

.. L5
::

    cut -d " " -f 2- marks1.txt | paste -d " " students.txt -

.. R6

Now, in order to view the same ouput in a file at a new location, we say,

.. L6
::

    cut -d " " -f 2- marks1.txt > /tmp/m_tmp.txt
    paste -d " " students.txt m_tmp.txt

.. R7

Let's first try to understand the second solution, which is a two step
solution. Later, we shall look at the first solution. 

.. L7

.. L8

{{{ Show slide, with Redirection }}}

.. R8

The standard output, in general, goes to the display.
Hence, the output of the commands that we type, come out to the display.
This may not always be what we require. 

For instance, in the solution above, we use the cut command and get only
the required columns of the file and write the output to a new temporary
file. The ``>`` character is used to state that we wish to redirect the
output, and it is followed by the location to which we wish to redirect. 
For example,

    command > file1

.. L9

{{{ Show slide, with Redirection... }}}

.. R9

Similarly, the standard input (stdin) can be redirected as,
    
    command < file1

The input and the output redirection could be combined in a single command, as, 

    command < infile > outfile

There is actually a third kind of standard stream, called the Standard
error (stderr). Any error messages that you get, are coming through this
stream. Like ``stdout``, ``stderr`` also streams to the display by default,
but it could be redirected to a file, as well. 

.. R10

For instance, let's introduce an error into the ``cut`` command used
before. We change the ``-f`` option to ``-c`` 

.. L10

{{{ Switch to terminal }}}
::

    cut -d " " -c 2- marks1.txt > /tmp/m_tmp.txt

.. R11

This prints an error that says the delimiter option should be used with the
fields option only, and you can verify that the ``m_tmp.txt`` file is
empty.  We can now, redirect the ``stderr`` also to a file, instead of
showing it on the display. 

.. L11
::

    cut -d " " -f 2- marks1.txt 1> /tmp/m_tmp.txt 2> /tmp/m_err.txt

.. R12

The above command redirects all the errors to the ``m_err.txt`` file
and the output to ``m_tmp.txt`` file. When redirecting, 1 stands
for ``stdout`` and 2 stands for ``stderr``. 

Let us complete the solution by using the ``paste`` command

.. L12
::

    paste -d " " students.txt m_tmp.txt

.. R13

So, in two steps we solved the problem of getting rid of the roll numbers
from the marks file and displaying the marks along with the names of the
students. Now, that we know how to redirect output, we could choose to
write the output to a file, instead of showing on the display. 

Let us now look at the first solution. 

.. L13
::

    cut -d " " -f 2- marks1.txt | paste -d " " students.txt -

.. L14

{{{ Show slide, with Piping }}}

.. R14

First of all, the hyphen at the end is to ask the paste command to read the
standard input, instead of looking for a FILE. The ``man`` page of ``paste``
command gives us this information. 

The character ``|`` is called a pipe. 
Now, what is happening with the ``cut`` command. If we look at the command only 
up to the ``|`` character, it is a normal ``cut`` command . So, the ``|`` seems 
to be joining the commands in some way. 
Essentially, what we are doing is, to redirect the output of the first
command to ``stdin`` and the second command takes input from the ``stdin``. 

More generally, 

    command1 | command2

executes ``command1`` and sends it's output to the ``stdin``, which is then
used as the input for ``command2``. This activity is commonly called piping.

.. L15

{{{ Show slide, with Piping... }}}

.. R15

This is roughly equivalent to using two redirects and a temporary file 

    command1 > tempfile
    command2 < tempfile
    rm tempfile

Also, given that a pipe is just a way to send the output of the command to
the ``stdin``, it should be obvious, to you that we can use a chain of
pipes. Any number of commands can be piped together and you need not be
restricted to two commands. 

The Bash shell has some nice features, that make our job of using the shell
easier and much more pleasant. We shall look at a few of them, here. 

Bash provides the feature of tab completion. What does tab completion mean?
When you are trying to type a word and you have entered enough portion of the 
word, bash can complete the word for you, by hitting the tab key. 

If on hitting the tab key, the word doesn't get completed, either the word
doesn't exist or the word cannot be decided unambiguously. If the case is
the latter one, hitting the tab key a second time, will list the
possibilities.

.. L16

{{{ Show slide, with Tab-completion }}}

.. R16

Bash provides tab completion for the following. 

  1. File Names
  2. Directory Names
  3. Executable Names
  4. User Names (when they are prefixed with a ~)
  5. Host Names (when they are prefixed with a @)
  6. Variable Names (when they are prefixed with a $) 

.. R17

For example, 

.. L17

{{{ Switch to terminal }}}
::

    pas<TAB><TAB>
    ~/<TAB><TAB>

.. R18

Bash also saves the history of the commands you have typed. So, you can go
back to a previously typed command and use the up and down arrow keys to
navigate in your bash history. 

.. L18
::

    <UP-ARROW>

.. R19

You can also search incrementally, for commands in your bash history.
``Ctrl-r`` searches for the commands that you have typed before. But, note
that the number of commands saved in the history is limited, generally upto
a 1000 commands. 

.. L19
::

   <Ctrl-r> pas

.. R20

Unix recognizes certain special characters, called "meta characters," as
command directives. The shell meta characters are recognized anywhere they
appear in the command line, even if they are not surrounded by blank space.
For that reason, it is safest to only use the characters A-Z, a-z, 0-9, and
the period, dash, and underscore characters when naming files and
directories on Unix. If your file or directory has a shell meta character
in the name, you will find it difficult to use the name in a shell command.

.. L20

.. L21

{{{ Show slide, with Shell Meta Characters }}}

.. R21

The characters that you can see on the slide are the shell meta characters

.. R22

Lets take an example,

.. L22

{{{ Switch to terminal }}}
::

    ls file.?

.. R23

It means, run on a directory containing the files file, file.c, file.lst, 
and myfile would list the files file.c and file.lst. However,

.. L23
::

    ls file.?

.. R24

Run on the same directory would only list file.c because the ? only matches
one character, no more, no less. This can save you a great deal of typing
time. 

For example, if there is a file called
california_cornish_hens_with_wild_rice and no other files whose names begin
with 'c', you could view the file without typing the whole name by typing
this

.. L24
::

    more c*

.. R25

Here, the c* matches that long file name.
File-names containing meta characters can pose many problems and should
never be intentionally created.

.. L25

.. L26

{{{ Switch to Summary slide }}}

.. R26

This brings us to the end of the end of this tutorial.
In this tutorial, we have learnt to,

 1. Use the ``cut`` and ``paste`` commands in redirection.
 #. Use the pipe ( | ) character. 
 #. Implement features of shell like tab-completion and history.

.. L27
 
{{{ Show self assessment questions slide }}}

.. R27

Here are some self assessment questions for you to solve

.. L28

{{{ Solution of self assessment questions on slide }}}

.. R28

And the answers,

.. L29

{{{ Show the Thank you slide }}}

.. R29

Hope you have enjoyed this tutorial and found it useful.
Thank you!

