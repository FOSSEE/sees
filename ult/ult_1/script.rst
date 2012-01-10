.. Objectives
.. ----------
   
   .. At the end of this tutorial, you will be able to:
   
   ..   1. Know what is linux and it's need.
   ..   2. Understand the need for linux in today's world.
   ..   3. Move around in directories and files.
   ..   4. Use basic commands of Linux.

.. Prerequisites
.. -------------

..   1. None

 
Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and Welcome to the tutorial on 
'Using linux tools - Part 1'.

.. L2

{{{ Show the slide, Objectives }}} 

.. R2

At the end of this tutorial, you will be able to,

 1. Know what is linux. 
 #. Understand the need for linux in today's world.
 #. Move around in directories and files.
 #. Use basic commands of Linux.

.. L3

{{{ Switch to slide, what is linux OS }}}

.. R3

Linux (sometimes called GNU/Linux) is a Free and Open Source Operating
System that is inspired by Unix and runs on a variety of hardware
platforms.

Linux is a modular operating system, with it's basic design based on the
principles established in Unix. It consists of an important and central
piece called the Linux kernel, which, manages system resources like process
control, networking, peripherals and file system access. This is
complemented by the application software, written on top of the kernel that
give the higher level functionality that facilitate the user to carry out
various tasks.

.. L4

{{{ Switch to slide, Why Linux? }}}

.. R4

GNU/Linux can be downloaded in its entirety from the Internet completely
for free with no registration fees, no costs per user, free updates, and
freely available source code.
The security model used in Linux is based on the UNIX idea of security,
which is known to be robust and of proven quality. Also, there are no
viruses in the GNU/Linux world.

Python is used a lot for scientific computing. Why? Beause,
we can share our operating system and the libraries that we are using
with our co-workers, without any headaches of licensing.
There are a host of tools and libraries, that are useful in day-to-day 
scientific computing work.GNU/Linux distributions are very stable and 
known for their up-time. We don't have the fear of losing our 
computational work, due to system crashes.

.. L5

{{{ Switch to slide, Logging in }}}

.. R5

Let's begin with logging into our system. The GNU/Linux OS supports
multiple users and each user logs in with his/her user-name and password.
You can log-in once you provide your authentication details.

It is a popular misconception that GNU/Linux doesn't have a GUI (Graphical
user interface). It does have a fully functional GUI, but for the purpose
of this course we shall start with using the CLI (Command line interface).
Once your system has booted up, hit ``Ctrl + Alt + F1`` to switch to the
command line interface.

You can log out using the ``logout`` command. 

.. R6

Now hit ``Ctrl + Alt + F7`` and come back to the GUI. For the purpose
of the spoken tutorials, we shall use the terminal on the GUI.

.. L6

{{{ Open the terminal }}}

.. R7

Now that we have logged in, where are we? 
To find out the present working directory, we use the ``pwd`` command. 

.. L7
::

    pwd

.. R8

Now, to see what is in the current directory, we use the ``ls`` command.

.. L8
::

    ls

.. R9

It gives us a list of all the files in our present working directory.
``ls`` command takes the directory, in which we want to see the list of
files present, as an argument. To see all the files present in the
``Music`` directory, we say

.. L9
::

    ls Music

.. R10

Note that everything in GNU/Linux and the Unix world is case sensitive.

As you can see, our home folder has two html files.
What if we wanted the files to be more organized? Say,
we would like to put all our work during this course in a separate
directory. Let us now create a directory ``sdes`` by saying

.. L10
::

    mkdir sees

.. R11

Type ``ls`` to see that a new directory has been
created. 

.. L11
::

    ls

.. L12

{{{ Switch to slide, New folders }}}

.. R12

Also, note that special characters need to be escaped. For example if we
wanted to create a directory with the name ``software engineering``, we do
it either as

     mkdir software\ engineering

or as

     mkdir "software engineering"

But it is generally a practice to use hyphens or underscores instead of
spaces in filenames and directory names.
Also in modern GNU/Linux filesystems all characters except the forward 
slash are allowed.

.. R13

Now that we have seen how to create a new empty directory and navigate into
it, let us create a new blank file. We use the ``touch`` command for this.

.. L13

{{{ Switch to the termninal }}}
::

    pwd
    cd sees
    touch first

.. R14

This creates a file named first in our present working directory. Use the
``ls`` command to see that the file has been created.

.. L14
::

    ls 

.. R15

To get a quick description of the command, we could use the ``whatis``
command. It gives a short one-line description of the command that is
passed as an argument to it. For example, 

.. L15
::

    whatis touch

.. R16

To get a more detailed description of the command,
we use the ``man`` command.

.. L16
::

    man touch

.. R17

This page gives a detailed description of the command. We can see that the
``touch`` command has a whole host of options that can be passed to it.
Every command in Linux has such a list of options that can be passed to the
command to do specific tasks. Hit the ``q`` key to quit the ``man`` page.

To see the manual on man itself do,

.. L17
::

    man man

.. L18

{{{ Switch to slide, Using additional options }}}

.. R18

As you may have observed, often the ``man`` page is a bit too much for
quickly cross checking what option to use for a specific task. For this
kind of quick look-up, most of the commands come with a -h or --help
option. This gives a brief description of the options available for that
command.

Pause the video here, try out the following exercise and resume the video.

.. L19

{{{ Show slide with exercise 1 }}}

.. R19

Which option should be used with ``ls`` command to list all the directories,
sub-directories and files contained in it? 
Hint: Use ``man`` or ``--help`` 

.. R20

Switch to terminal for solution. 

.. L20
 
{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    ls -R

.. R21

This lists out all the files in the sub-tree of the current directory,
recursively.

.. L21

.. R22

When you wish to create a new directory deep inside a directory structure,
using a ``-p`` option with the ``mkdir`` command would be useful. For
example,if we wish to create a folder ``scripts`` inside the directory
``linux-tools`` inside the directory ``sees``, we could simply say,

.. L22
::

    pwd
    mkdir -p sees/linux-tools/scripts

.. R23

Let's now say, we wish to remove a directory or a file. How do we find out
what command to use? We use the ``apropos`` command to search for commands
based on their descriptions. To search for the command to remove a
file/directory say,

.. L23
::

    apropos remove

.. R24

This gives us a whole list of commands that have the word ``remove``, in
their description. Looking through the list tells us that ``rm`` or
``rmdir`` is the command to use.

.. L24

.. L25

{{{ Show summary slide }}}

.. R25

This brings us to the end of the tutorial.In this tutorial, we have learnt to,

 1. Understand the basic structure of linux and it's need.
 #. Move around in directories and files.
 #. Use commands like ``mkdir`` and ``rmdir`` to make and remove directories 
    respectively.
 #. Use commands such as ``man`` and ``whatis`` to get a description of 
    what a particular command does.

.. L26
 
{{{ Show self assessment questions slide }}}

.. R26

Here are some self assessment questions for you to solve

1. Which is the default directory after logging into the terminal?

2. How to view file attributes with ls command?

.. L27

{{{ Solution of self assessment questions on slide }}}

.. R27

And the answers,

1. It logins to user's home(/home/user)

2. In order to view the attributes of a file, we use the -l option with 
   the ls command.

::

    ls -l <filename>  

.. L28

{{{ Show the Thankyou slide }}}

.. R28

Hope you have enjoyed this tutorial and found it useful.
Thank you!

