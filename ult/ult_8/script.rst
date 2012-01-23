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
..   5. Using Linux tools - Part 5
..   6. Using Linux tools - Part 6
..   7. Using Linux tools - Part 7

 
Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and Welcome to the tutorial on 
'Using linux tools - Part 8'.

.. L2

{{{ Show slide with objectives }}} 

.. R2

At the end of this tutorial, you will be able to,

 1. Search for files in many different ways.
 #. Compare files with same names.
 #. Create and extract an archive. 
 #. Customize a shell.
 
.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Using Linux tools from Part 1 to Part 7".

There are a bunch of tools, that will prove to be handy in your day
to day work. These tools will help you quickly perform tasks like searching
for files, comparing files and checking if they are the same, viewing the
exact differences between them, etc.

.. L4

{{{ Show slide, find }}}

.. R4

Let us start with the first tool - 'find' .
The ``find`` command lets you find files in a directory hierarchy. It
offers a very complex feature set allowing you to search for files with a
wide range of restrictions. We shall only look at some of the most
frequently used ones.

.. R5

To find the files, which end with an extension, ``.pdf``, saved in the current
folder and all it's subfolders, we say 

.. L5

{{{ Open the terminal }}}
::

    find . -name "*.pdf"

.. R6

The ``find`` command also lists out the directory and sub-directory names
To list them, we say,

.. L6
::

    find . -type d 

.. R7

In short, ``find`` allows you to set limits on file-size, modification time 
and whole lot of other things which you can explore on seeing the man page 
of ``find``. 

.. L7

.. R8

Let us now move on to the next tool, the compare tool.

To compare two files, whether they are identical or not, we can use the
``cmp`` command. Let us consider some situation. Suppose, we run the ``find`` 
command to locate some file, and it turns out that we have a file with same 
name in different location. 

In this case, if we are unsure, whether both the files are the same, we can use 
the ``cmp`` command to check if the files are identical. 

.. L8
::

   find . -name quick.c
   ./Desktop/programs/quick.c
   ./c-folder/quick.c
   cmp Desktop/programs/quick.c c-folder/quick.c

.. L9

{{{ Show slide, cmp }}}

.. R9

If the cmp command doesn't return any output, it means that both files are
exactly identical. If there are any differences in the file, it gives you
the exact byte location at which the first difference occurred. 

.. R10

Let us now make a small change in one of quick.c file and run the ``cmp`` 
command again.

.. L10
{{{ Switch to the terminal }}}

::

   cmp Desktop/programs/quick.c c-folder/quick.c

.. R11
   
As we can see, it gives the exact location as to where a change is made.

Now, we may not be happy with just the knowledge that the files are
different. We may want to see the exact differences between the two files.
The ``diff`` command can be used to find the exact differences between the
files. 

.. L11

.. L12
::

   diff Desktop/programs/quick.c c-folder/quick.c

.. R12

We get back a line by line difference between the two files. 

.. L13

{{{ Show slide, diff }}}

.. R13

The ``>`` mark indicates the content that has been added to the second file, 
which was not present in the first file. The ``<`` mark indicates the lines 
that were present in the first file, but are not existent in the second file. 

.. L14

{{{ Show slide, tar }}}

.. R14

You would often come across (archive) files which are called *tarballs*. A
tar ball is essentially a collection of files, which may or may not be
compressed. Essentially, it eases the job of storing, backing up and
transporting multiple files, at once. 

.. R15

The following set of commands extracts the contents of the ``allfiles.tar`` 
tarball to the directory extract. 

.. L15

{{{ Switch to terminal }}}
::

   mkdir extract
   cp allfiles.tar extract/
   cd extract
   tar -xvf allfiles.tar 

.. L16

{{{ Show slide, extracting an archive }}}

.. R16

The option, ``x`` tells ``tar`` to extract the files in the archive file
specified by the ``f`` option. The ``v`` option tells ``tar`` to give out a
verbose output. 

.. R17

Similarly, if we wish to create a ``tar`` archive, we use the ``c`` option
instead of the ``x`` option. For instance, the command below creates an
archive from all the files with the ``.txt`` extension. 

.. L17

{{{ Switch to terminal }}}
::

    tar -cvzf newarchive.tar *.txt

.. R18

You can also create and extract compressed archives using ``tar``. It
supports a wide variety of compressions like gzip, bzip2, lzma, etc. 

We need to add an additional option to ``tar`` to handle these
compressions. 


+-------------+------------+
| Compression | Option     |
+-------------+------------+
| gzip        | ``-z``     |
| bzip2       | ``-j``     |
| lzma        | ``--lzma`` |
+-------------+------------+

.. L18

.. R19

So, if we wished to create a gzip archive in the previous command, we
change it to the following

.. L19
::

    tar -cvzf newarchive.tar.gz *.txt

.. L20

{{{ Show slide, customizing your shell }}}

.. R20

What would you do, if you want bash to execute a particular command each
time you start it up? For instance, say you want the current directory to
be your Desktop instead of your home folder, each time bash starts up.
Bash reads and executes commands in a whole bunch
of files called start-up files, when it starts up.

When bash starts up as an interactive login shell, it reads the files
``/etc/profile``, ``~/.bash_profile``, ``~/.bash_login``, and
``~/.profile`` in that order.

When an interactive shell that is not a login shell is started, bash reads 
and executes commands from ~/.bashrc. This can be prevented using the ``--norc``
option. Instead of using the ``~/.bashrc`` file on start-up, we can force 
the bash to use another file, for which the ``--rcfile`` option may be used.

Now, you know what you should do, to change the current directory to you
Desktop. Just put a ``cd ~/Desktop`` into your ``~/.bashrc`` and you are
set!
But as you know that the start-up files are used for a lot more complex things 
than this. You could set (or unset) aliases and a whole bunch of environment 
variables in the ``.bashrc``, like changing environment variables etc. 

.. L21

{{{ Switch to 'Summary' slide }}}

.. R21

This brings us to the end of the end of this tutorial.
In this tutorial, we have learnt to, 

 1. Make use of the ``find`` command to find files in a directory hierarchy.
 #. Find the differences between files with the same name, using the
    ``cmp`` and ``diff`` commands.
 #. Extract and create compressed archive's using the ``tar`` command.
 #. Customize one's shell according to one's choice. 
 
.. L22

{{{ Show self assessment questions slide }}}
 
.. R22

Here are some self assessment questions for you to solve

 1. Look at the man page of ``find`` and state the options which
    deal with symbolic links.
     
 2. How do you append tar files to an archive?

.. L23

{{{ Solution of self assessment questions on slide }}}

.. R23

And the answers,

1. The  -H,  -L  and  -P options with the ``find`` command control 
    the treatment of symbolic links.

 2. To append tar files to an archive, we can use the ``tar`` command 
    either with the ``-A`` option or the ``-r`` option, as,
::

    $ tar -Af <tar_file> <tar_file_to_be_added> 
                   OR
    $ tar -rf <tar_file> <tar_file_to_be_added>     


.. L24

{{{ Show the Thank you slide }}}

.. R24

Hope you have enjoyed this tutorial and found it useful.
Thank you!



