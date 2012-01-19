.. Objectives
.. ----------
   
   .. At the end of this tutorial, you will be able to:
   
   ..   1. Copy files from one location to another.
   ..   2. Remove files and directories.
   ..   3. Change permissions and ownership of files.
   ..   4. Navigate through directories and files.

.. Prerequisites
.. -------------

..   1. Using Linux tools - Part 1

 
Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and Welcome to the tutorial on 
'Using linux tools - Part 2'.

.. L2

{{{ Show slide with objectives }}} 

.. R2

At the end of this tutorial, you will be able to,

 1. Copy files from one location to another.
 #. Remove files and directories.
 #. Change permissions and ownership of files.
 #. Navigate through directories and files.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Using Linux tools - Part 1".

.. R4

Let us start with the concept of basic file handling.
Let's begin with removing files.
The ``rm`` command  is used to delete files. 

Here's example to remove a file named "foo" from the directory "sdes", 

.. L4

{{{ Navigate to /home/user/sdes/ }}}
::

    rm foo
    ls

.. R5

Note that, as such, ``rm`` works only for files and not for directories.
For instance, if you try to remove a directory named ``bar`` using, 

.. L5
::

    rm bar

.. R6

we get an error saying, cannot remove `bar`: Is a directory. But ``rm``
takes additional arguments which can be used to remove a directory and all
of it's content, including sub-directories.We use the ``-r`` option. 

.. L6
::

    rm -r bar
    ls

.. R7

It removes the directory ``bar`` and all of it's content including
sub-directories, recursively. The ``-r`` stands for recursive. 

Let's say we wish to copy a file, ``foo`` from ``sdes/linux-tools/scripts``, 
which is the source location to the target location ``sees/linux-tools``, 
how would we do it? 

.. L7
::

    pwd 
    cp linux-tools/scripts/foo linux-tools/

.. R8

Note, that we haven't changed the name of the file name at the target
location. We could have done that by specifying a new filename at the
target location,as,

.. L8
::

    cp linux-tools/scripts/foo linux-tools/bar

.. R9

This copies the file ``foo`` to the new location, but with the new name,
``bar``. 

But, what would have happened if we had a file named ``bar`` already at the
new location? Let's try doing the copy again, and see what happens. 

.. L9
::

    cp linux-tools/scripts/foo linux-tools/bar

.. R10

We get no error message, what happened? ``cp`` actually overwrites files.
In this case, it's not a problem since, we just re-copied the same content,
but in general it could be a problem, and we could lose data. To prevent
this, we use the ``-i`` flag with ``cp``. 

.. L10
::

    cp -i linux-tools/scripts/foo linux-tools/bar

.. R11

We are now prompted, whether the file should be over-written. To over-write
say ``y``, else say ``n``. 

Now, let's try to copy the directory ``sdes`` to a new directory called
``course``. How do we do it?

.. L11
::

    cd /home/user
    cp -i sdes course
   
.. R12

``cp`` refuses to copy the directory ``sdes``. We use the option ``-r``
(recursive) to copy the directory and all it's content. 

.. L12
::

    cd /home/user
    cp -ir sdes course
    ls

.. R13

We see that a new directory named course has been created with all it's 
contents.

Now, If we want to move files, instead of copying them, one way to go about
it, would be to ``cp`` the file to the new location and ``rm`` the old
file. Instead, you can make use of only one command which can do this task at 
one go. The ``mv`` command can move files or directories. It also takes 
the ``-i`` option to prompt before overwriting. 

.. L14
::

    cd /home/user
    mv -i sdes/ course/

.. R15

Let us understand what exactly happened when we used the ``mv`` command

.. L15
::

    ls course

.. R16

We can see that the ``sdes`` directory has been inserted as sub-directory
of the ``course`` directory. The move command doesn't over-write
directories, but the ``-i`` option is useful when moving files around.

A common way to rename files (or directories), is to copy a file (or a
directory) to the same location, with a new name. 

.. L16
::

    mv sdes/linux-tools sdes/linux

.. R17

It renames the ``linux-tools`` directory to just ``linux``

While moving around our files and directories, we have been careful to stay
within the ``/home/`` directory, but other than that there are many other 
directories too. Let us take this opportunity to understand a few things 
about the linux file hierarchy and file permissions. 

.. L17
::

    cd /

{{{ Switch to slide, Linux File Hierarchy }}}

.. R18

The ``/`` directory is called the root directory. All the files and
directories, (even if they are on different physical devices) appear as
sub-directories of the root directory. 

.. L18

{{{ Switch to terminal }}}
::

    ls 

.. R19

You can see the various directories present at the top most level.

.. L19

{{{ Pause for sometime and then continue }}}

.. R20

For more information, it is recommended that you look at the ``man`` page
of ``hier``. 

.. L20
::

    man hier

{{{ Pause for sometime and then hit q }}}

.. R21

Let us now look at file permissions. Linux is a multi-user environment and
allows users to set permissions to their files to allow only a set of
people to read or write it. Similarly, it is not "safe" to allow system
files to be edited by any user. All this access control is possible in
Linux. 

To start, in the root directory, say,

.. L21
::

    ls -l

.. R22

You again get a list of all the sub-directories, but this time with a lot
of additional information. Let us try and understand what this output says
Consider the first line of the output,

.. L22

{{{ Highlight the required portions accordingly while narrating }}}

.. R23

The first column denotes the type and the access permissions of the file.
The second is the number of links. The third and fourth are the owner and
group of the file. The next field is the size of the file in bytes. The
next field is the date and time of modification and the last column is the
file name.
We shall look at the permissions of the file now, ie., the first column of
the output. 

The first character in the first column specifies, whether the item is a
file or a directory. Files have a ``-`` as the first character and
directories have a ``d``. 

The next 9 characters define the access permissions of the file. Before
looking at it, we need to briefly study groups and users and ownership. 

We already know what the first character in the first column (in the output
of ``ls -l``) is for. The rest of the 9 characters are actually sets of 3
characters of each. The first set of 3 characters defines the permissions
of the user, the next 3 is for the group and the last three is for others.
Based on the values of these characters, access is provided or denied to
files, to each of the users. 

So, what does each of the three characters stand for? Let's suppose we are
looking at the set, corresponding to the permissions of the user. In the
three characters, the first character can either be an ``r`` or a ``-``.
Which means, the user can either have the permissions to read the file or
not. If the character is ``r``, then the user has the permissions to read
the file, else not. Similarly, ``w`` stands for write permissions and
decides whether the user is allowed to write to the file. ``x`` stands for
execute permissions. You cannot execute a file, if you do not have the
permissions to execute it.

Similarly, the next set of characters decides the same permissions for the
members of the group, that the file is associated with. The last set of
characters defines these permissions for the users, who are neither owners
of the file nor in the group, with which the file is associated. 

Now, it's not as if these permissions cannot be changed. If you are the
owner of a file, you can change the permissions of a file, using the
``chmod`` command.

.. L23

.. R24

Let's say, we wish to give the execute permissions for a file, to both the
user and the group, how do we go about doing it? To be more explicit, given
a file ``foo.sh``, with the permissions flags as ``-rw-r--r--``, change it
to ``-rwxr-xr--``. 

The following command does it for us, 

.. L24
::

    chmod ug+x foo.sh
    ls -l foo.sh

.. R25

As you can see, the permissions have been set to the required value. But
what did we exactly do? Let us try and understand. 

.. L25

{{{ Switch to slide,Symbolic modes }}}

.. R26

In the command, the parameter ``ug+x`` is the mode parameter to the
``chmod`` command. It specifies the changes that need to be made to the
permissions of the file ``foo.sh``. 
The ``u`` and ``g`` stand for the user and group, respectively. The ``x``
stands for the execute permission and ``+`` stands for adding the
specified permission. So, essentially, we are asking ``chmod`` command to
add the execute permission for the user and group. The permission of others
will remain unchanged. 

So, if we wished to add the execute permission to all the users, instead of
adding it to just the user and group, we would have instead said 

.. L26
::

    chmod a+x foo.sh 

.. R27

or 

.. L27
::

    chmod ugo+x foo.sh

.. R28

Pause the video here, try out the following exercise and resume the video.

.. L28

.. L29

{{{ Show slide with exercise 1 }}}

.. R29

Change the permissions of a directory along with all of its
sub-directories and files.

.. L30

{{{ Show slide with solution 1 }}}

.. R30

To change the permissions of a directory along with all of its
sub-directories and files, recursively, we use the ``-R`` option
with the chmod command as shown

  chmod go-r -R <directory name>/

.. R31

It is important to note that the permissions of a file can only be changed
by a user who is the owner of a file or the superuser.

What if we wish to change the ownership of a file? The ``chown`` command is
used to change the owner and group. 
By default, the owner of a file (or directory) is the user that
created it. The group is a set of users that share the same access
permissions i.e., read, write and execute. 
For instance, to change the user and the group of the file
``wonderland.txt`` to ``alice`` and ``users``, respectively, we say.

.. L31
::

    chown fossee:users wonderland.txt

.. R32

We get an error saying, the operation is not permitted.
We have attempted to change the ownership of a file that we own, to a
different user. Logically, this shouldn't be possible, because, this can
lead to problems, in a multi-user system. 
Only the superuser is allowed to change the ownership of a file from one
user to another. The superuser or the ``root`` user is the only user
empowered to a certain set of tasks and hence is called the superuser. The
command above would have worked, if you did login as the superuser and
then changed the ownership of the file. 

.. L32

.. L33

{{{ Show summary slide }}}

.. R33

This brings us to the end of the tutorial.In this tutorial, we have learnt to,

 1. Copy and move files from one location to another, using the ``cp`` 
    and ``mv`` commands respectively.
 #. Remove files using ``rm`` command. 
 #. Understand the Linux file hierarchy.
 #. Change permissions and ownership of files, using the ``chmod`` 
    and ``chown`` commands respectively.

.. L34

{{{ Show self assessment questions slide }}}

.. R34

Here are some self assessment questions for you to solve

1. How to copy all the contents of one folder into another?

2. How will you rename the file wonderland.txt to alice.txt using the 
   commands learnt so far?

.. L35

{{{ Solution of self assessment questions on slide }}}

.. R35

And the answers,

1. We use the ``cp`` command along with a star sign. The star denotes that 
   it will copy all the files of folder 1 to folder 2.
::

    cp folder1/* folder2 

2. To rename a file, we use the ``mv`` command as,
::

    mv wonderland.txt alice.txt

.. L36

{{{ Show the Thankyou slide }}}

.. R36

Hope you have enjoyed this tutorial and found it useful.
Thank you!
     
