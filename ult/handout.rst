===================
 Using Linux Tools
===================

Introducing Linux
=================

Linux (sometimes called GNU/Linux) is a Free and Open Source Operating
System that is inspired by Unix and runs on a variety of hardware
platforms.

Free 
    Free as in Freedom or Free Speech, not Free Beer. 

Open-source 
    licensed to permit modifications and redistribution of its source code.

Linux is a modular operating system, with it's basic design based on the
principles established in Unix. It consists of an important and central
piece called the Linux kernel, which, manages system resources like process
control, networking, peripherals and file system access. This is
complemented by the application software, written on top of the kernel that
give the higher level functionality that facilitate the user to carry out
various tasks.

Why Linux?
----------

Free as in Free Beer 
  GNU/Linux can be downloaded in its entirety from the Internet completely
  for free. No registration fees, no costs per user, free updates, and
  freely available source code in case you want to change the behavior of
  your system.

Secure & versatile 
  The security model used in Linux is based on the UNIX idea of security,
  which is known to be robust and of proven quality. Also, there are no
  viruses in the GNU/Linux world.

Why Linux for Scientific Computing?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Free as in Free Speech 
  You can share your operating system and the libraries that you are using
  with your co-workers, without any headaches of licensing. Also, you can
  study and improve the implementation of various libraries that you may
  use for your work

Tools for Scientific computing
  There are a host of tools and libraries, written by various (groups of)
  people that are useful in day-to-day scientific computing work. You have
  the benefit of standing on the shoulders of giants.

Keeps on running 
  GNU/Linux distributions are very stable and known for their up-time. You
  don't have the fear of losing your computational work, due to system
  crashes.

Parallel & Distributed computing 
  It is pretty easy to build your own cluster with GNU/Linux and there are
  host of libraries for parallel and distributed computing that work with
  GNU/Linux.


Reading Exercises
-----------------

  1. In the Beginning was the Command Line -- Neal Stephenson
  #. Linux -- Wikipedia
  #. GNU/Linux naming controversy -- Wikipedia

Getting Started
===============


Logging in
----------

Let's begin with logging into our system. The GNU/Linux OS supports
multiple users and each user logs in with his/her user-name and password.
After the machine boots up, the OS prompts you for a user-name and
password. You can log-in once you provide your authentication details.

It is a popular misconception that GNU/Linux doesn't have a GUI (Graphical
user interface). It does have a fully functional GUI, but for the purpose
of this course we shall start with using the CLI (Command line interface).
Once your system has booted up, hit ``Ctrl + Alt + F1`` to switch to the
command line interface.

You can log out using the ``logout`` command. 

Where am I?
-----------

Now that we have logged in, where are we? Where did we get in? 

To find out the present working directory, we use the ``pwd`` command. 

::

  $ pwd
  /home/user

What is in there?
-----------------

To see what is in the current directory, we use the ``ls`` command. It
gives us a list of all the files in our present working directory.

::

    $ ls
    jeeves.rst psmith.html blandings.html Music

``ls`` command takes the directory, in which we want to see the list of
files present, as an argument. To see all the files present in the
``Music`` directory, we say

::

    $ ls Music
    one.mp3 two.mp3 three.mp3 

Note that everything in GNU/Linux and the Unix world is case sensitive. For
example if we had said ``ls music`` instead of ``ls Music``, we would get
an error ``No such file or directory``.

New folders
-----------

As you can see, our home folder has two html files one rst file and a
directory for Music. What if we wanted the files to be more organized? Say,
we would like to put all our work during this course in a separate
directory. Let us now create a directory ``sees`` by saying

::

    $ mkdir sees

Again, note that we are using all small case letters. ``sees`` is different
from ``Sees`` or ``SEES``. Type ``ls`` to see that a new directory has been
created. 

::

    $ ls

Also, note that special characters need to be escaped. For example if we
wanted to create a directory with the name ``software engineering``, we do
it either as

::

    $ mkdir software\ engineering

or as

::

    $ mkdir "software engineering"

But it is generally a practice to use hyphens or underscores instead of
spaces in filenames and directory names.

In modern GNU/Linux filesystems all characters except the forward slash are
allowed.

Moving around
-------------

Now that we have created our directory ``sees``, let us make it our present
working directory by moving into it. We use the ``cd`` command for this
purpose.

::

    $ cd sees
    $ pwd 
    /home/user/sees/

This could alternately have been written as ``cd ./sees``. The dot in the
beginning specifies that we are specifying the path, relative to the
present working-directory.

To go up the directory structure, we use ``..``. Typing

::

    $ cd ..

in the ``sees`` directory will take us back to the home directory.

What will happen if we type ``cd ..`` in the home folder? We go to the
``/home`` directory.

All this while, we have been using what are called relative paths, to
specify the path. We could alternatively use the absolute path, which give
the whole path, starting with a /. The absolute path of the ``sees``
directory is, ``/home/user/sees/``.

New files
---------

Now that we have seen how to create a new empty directory and navigate into
it, let us create a new blank file. We use the ``touch`` command for this.

::

    $ pwd
    /home/user
    $ cd sees
    $ touch first

This creates a file named touch in our present working directory. Use the
``ls`` command to see that the file has been created.

::

    $ ls 
    first


Getting Help
============

What does a command do?
-----------------------

To get a quick description of the command, we could use the ``whatis``
command. It gives a short one-line description of the command that is
passed as an argument to it. For instance let's see what is the ``touch``
command that we just saw.

::

    $ whatis touch
    touch (1)            - change file timestamps

Now, what does it mean by change file timestamps? We used it to create a
file, just a while ago. To get a more detailed description of the command,
we use the ``man`` command.

::

    $ man touch

This shows the ``man`` (short for "manual pages") page of the command. This
page gives a detailed description of the command. We can see that the
``touch`` command has a whole host of options that can be passed to it.
Every command in Linux has such a list of options that can be passed to the
command to do specific tasks. Hit the ``q`` key to quit the ``man`` page.

To see the manual on man itself do

::

    $ man man

Using additional options
------------------------

As you may have observed, often the ``man`` page is a bit too much for
quickly cross checking what option to use for a specific task. For this
kind of quick look-up, most of the commands come with a -h or --help
option. This gives a brief description of the options available for that
command.

Let us look at using a couple of useful options that we can pass to
commands that we have already see.

::

    $ ls -R

This lists out all the files in the sub-tree of the current directory,
recursively.

When you wish to create a new directory deep inside a directory structure,
using a ``-p`` option with the ``mkdir`` command would be useful. For
example, if we wish to create a folder ``scripts`` inside the directory
``linux-tools`` inside the directory ``sees``, we could simply say,

::

    $ pwd
    /home/user/
    $ mkdir -p sees/linux-tools/scripts

This will create the scripts directory, inside the required directory
structure, creating any other new directory required, to maintain the tree
structure.

Searching for a command
-----------------------

Let's now say, we wish to remove a directory or a file. How do we find out
what command to use? We use the ``apropos`` command to search for commands
based on their descriptions. To search for the command to remove a
file/directory say,

::

    $ apropos remove

This gives us a whole list of commands that have the word ``remove``, in
their description. Looking through the list tells us that ``rm`` or
``rmdir`` is the command to use.


Basic File Handling
===================

Removing files
--------------

``rm``   is used to delete files. 

Here's example to remove a file named "foo" from a directory, 

::

    $ rm foo

Note that, as such, ``rm`` works only for files and not for directories.
For instance, if you try to remove a directory named ``bar``, 

::

    $ rm bar

we get an error saying, cannot remove `bar`: Is a directory. But ``rm``
takes additional arguments which can be used to remove a directory and all
of it's content, including sub-directories. 

::

    $ rm -r bar

removes the directory ``bar`` and all of it's content including
sub-directories, recursively. The ``-r`` stands for recursive. 

A function called ``rmdir`` is also available, to remove directories, but
we shall not look into it. 

Copying Files
-------------

Let's say we wish to copy a file, ``foo`` from ``sees/linux-tools/scripts`` to
``sees/linux-tools``, how would we do it? 

::

    $ pwd 
    /home/user/sees/

    $ cp linux-tools/scripts/foo linux-tools/

In general, 

::

    $ cp SourceFile TargetLocation

Note, that we haven't changed the name of the file name at the target
location. We could have done that by specifying a new filename at the
target location. 

::

    $ cp linux-tools/scripts/foo linux-tools/bar

This copies the file ``foo`` to the new location, but with the new name,
``bar``. 

So, ``cp`` is the command to copy a file from one place to another. The
original file remains unchanged, and the new file may have the same or a
different name.

But, what would have happened if we had a file named ``bar`` already at the
new location? Let's try doing the copy again, and see what happens. 

::

    $ cp linux-tools/scripts/foo linux-tools/bar

We get no error message, what happened? ``cp`` actually overwrites files.
In this case, it's not a problem since, we just re-copied the same content,
but in general it could be a problem, and we could lose data. To prevent
this, we use the ``-i`` flag with ``cp``. 

::

    $ cp -i linux-tools/scripts/foo linux-tools/bar
    cp: overwrite `bar'? 

We are now prompted, whether the file should be over-written. To over-write
say ``y``, else say ``n``. 

Now, let's try to copy the directory ``sees`` to a new directory called
``course``. How do we do it?

::

    $ cd /home/user
    $ cp -i sees course
    cp: omitting directory `sees/'

``cp`` refuses to copy the directory ``sees``. We use the option ``-r``
(recursive) to copy the directory and all it's content. 

::

    $ cd /home/user
    $ cp -ir sees course


Moving Files
------------

What if we want to move files, instead of copying them? One way to go about
it, would be to ``cp`` the file to the new location and ``rm`` the old
file. 

But, there's a command that does this for you, ``mv`` (short for move). It
can move files or directories. It also takes the ``-i`` option to prompt
before overwriting. 

::

    $ cd /home/user
    $ mv -i sees/ course/

What happened? Why didn't we get any prompt? Did course get overwritten? 

::

    $ ls course

We can see that the ``sees`` directory has been inserted as sub-directory
of the ``course`` directory. The move command doesn't over-write
directories, but the ``-i`` option is useful when moving files around.

A common way to rename files (or directories), is to copy a file (or a
directory) to the same location, with a new name. 

::

    $ mv sees/linux-tools sees/linux

will rename the ``linux-tools`` directory to just ``linux``. 


Linux File Hierarchy & Permissions and ownership
================================================

While moving around our files and directories, we have been careful to stay
within the ``/home/`` directory, but if you were curious, you may have
ventured out and seen that there are a lot of other directories. Let us
take this opportunity to understand a few things about the linux file
hierarchy and file permissions. 

::

    $ cd /

The ``/`` directory is called the root directory. All the files and
directories, (even if they are on different physical devices) appear as
sub-directories of the root directory. 

::

    $ ls 

You can see the various directories present at the top most level. Below is
a table that briefly describes, what is present in each of these
directories and what their function is. 

+---------------+------------------------------------------------+
|   Directory   |             Description                        |
+===============+================================================+
| /             | Primary hierarchy root and root directory of   |
|               | the entire file system hierarchy.              |
+---------------+------------------------------------------------+
| /bin/         | Essential command binaries that need to be     |
|               | available in single user mode; for all users,  |
|               | e.g., *cat*, *ls*, *cp*.                       |
+---------------+------------------------------------------------+
| /boot/        | Boot loader files, e.g., *kernels*, *initrd*;  |
|               | often a separate partition.                    |
+---------------+------------------------------------------------+
| /dev/         | Essential devices, e.g., /dev/null             |
+---------------+------------------------------------------------+
| /etc/         | Host-specific system-wide configuration files  |
|               | (the name comes from *et cetera*)              |
+---------------+------------------------------------------------+
| /home/        | User's home directories, containing saved      |
|               | files, personal settings, etc.; often a        |
|               | separate partition.                            |
+---------------+------------------------------------------------+
| /lib/         | Libraries essential for the binaries in        |
|               | */bin/* and */sbin/*                           |
+---------------+------------------------------------------------+
| /media/       | Mount points for removable media such as       |
|               | CD-ROMs, external hard disks, USB sticks, etc. |
+---------------+------------------------------------------------+
| /mnt/         | Temporarily mounted file systems               |
+---------------+------------------------------------------------+
| /opt/         | Optional application software packages         |
+---------------+------------------------------------------------+
| /proc/        | Virtual filesystem documenting kernel and      |
|               | process status as text files; e.g., uptime,    |
|               | network. In Linux, corresponds to a *Procfs*   |
|               | mount.                                         |
+---------------+------------------------------------------------+
| /root/        | Home directory for the root user               |
+---------------+------------------------------------------------+
| /sbin/        | Essential system binaries; e.g., *init*,       |
|               | *route*, *mount*.                              |
+---------------+------------------------------------------------+
| /srv/         | Site-specific data which is served by the      |
|               | system.                                        |
+---------------+------------------------------------------------+
| /tmp/         | Temporary files. Often not preserved between   |
|               | system reboots.                                |
+---------------+------------------------------------------------+
| /usr/         | Secondary hierarchy for read-only user data;   |
|               | contains the majority of (multi-)user          |
|               | utilities and applications.                    |
+---------------+------------------------------------------------+
| /var/         | Variable files - files whose content is        |
|               | expected to continually change during normal   |
|               | operation of the system - such as logs, spool  |
|               | files, and temporary e-mail files.             |
|               | Sometimes a separate partition.                |
+---------------+------------------------------------------------+


Note that some of these directories may or may not be present on your Unix
system depending on whether certain subsystems, such as the X Window
System, are installed.

For more information, it is recommended that you look at the ``man`` page
of ``hier``. 

::

    $ man hier

Permissions and Access control
------------------------------

Let us now look at file permissions. Linux is a multi-user environment and
allows users to set permissions to their files to allow only a set of
people to read or write it. Similarly, it is not "safe" to allow system
files to be edited by any user. All this access control is possible in
Linux. 

To start, in the root directory, say,

::

    $ ls -l

You again get a list of all the sub-directories, but this time with a lot
of additional information. Let us try and understand what this output says. 

::

    drwxr-xr-x   5 root users  4096 Jan 21 20:07 home

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

Each file in the Linux filesystem is associated with a user and a group.
The user and the group of the file can be seen in the third and the fourth
columns of the output of ``ls -l`` command. The third column is the user,
and is usually the person who has created the file. A group is simply a
group of users. Users can be added or removed from groups, but doing that
is out of the scope of this course. This brief introduction to users and
groups is enough to go ahead and understand access permissions. 

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

Changing the permissions
------------------------

Now, it's not as if these permissions are set in stone. If you are the
owner of a file, you can change the permissions of a file, using the
``chmod`` command. 

Let's say, we wish to give the execute permissions for a file, to both the
user and the group, how do we go about doing it? To be more explicit, given
a file ``foo.sh``, with the permissions flags as ``-rw-r--r--``, change it
to ``-rwxr-xr--``. 

The following command does it for us, 

::

    $ chmod ug+x foo.sh
    $ ls -l foo.sh

As you can see, the permissions have been set to the required value. But
what did we exactly do? Let us try and understand. 

Symbolic modes
~~~~~~~~~~~~~~

In the command above, the parameter ``ug+x`` is the mode parameter to the
``chmod`` command. It specifies the changes that need to be made to the
permissions of the file ``foo.sh``. 

The ``u`` and ``g`` stand for the user and group, respectively. The ``x``
stands for the execute permission and the ``+`` stands for adding the
specified permission. So, essentially, we are asking ``chmod`` command to
add the execute permission for the user and group. The permission of others
will remain unchanged. 

The following three tables give the details of the class, the operator and
the permissions. 

+--------------+--------+---------------------------------------------+
| Reference    | Class  |                Description                  |
+==============+========+=============================================+
|      u       | user   | the owner of the file                       |
+--------------+--------+---------------------------------------------+
|      g       | group  | users who are members of the file's group   |
+--------------+--------+---------------------------------------------+
|      o       | others | users who are not hte owner of the file or  |
|              |        | members of the group                        |
+--------------+--------+---------------------------------------------+
|      a       | all    | all three of the above; is the same as *ugo*|
+--------------+--------+---------------------------------------------+

+--------------+------------------------------------------------------+
| Operator     |                      Description                     |
+==============+======================================================+
| +            | adds the specified modes to the specified classes    |
+--------------+------------------------------------------------------+
| -            | removes the specified modes from the specified       |
|              | classes                                              |
+--------------+------------------------------------------------------+
| =            | the modes specified are to be made the exact modes   |
|              | for the specified classes                            |
+--------------+------------------------------------------------------+

+-----+--------------+------------------------------------------------+
|Mode |    Name      |                 Description                    |
+=====+==============+================================================+
| r   | read         | read a file or list a directory's contents     |
+-----+--------------+------------------------------------------------+
| w   | write        | write to a file or directory                   |   
+-----+--------------+------------------------------------------------+
| x   | execute      | execute a file or recurse a directory tree     |
+-----+--------------+------------------------------------------------+

So, if we wished to add the execute permission to all the users, instead of
adding it to just the user and group, we would have instead said 

::

    $ chmod a+x foo.sh 

or 

::

    $ chmod ugo+x foo.sh


To change the permissions of a directory along with all of its
sub-directories and files, recursively, we use the ``-R`` option. 

For instance if we wished to remove the read permissions of a file from all
users except the owner of the file, we would say, 


::

    $ chmod go-r bar.txt

It is important to note that the permissions of a file can only be changed
by a user who is the owner of a file or the superuser. (We shall talk about
the superuser in the next section)


Changing Ownership of Files
---------------------------

What if we wish to change the ownership of a file? The ``chown`` command is
used to change the owner and group. 

By default, the owner of a file (or directory) object is the user that
created it. The group is a set of users that share the same access
permissions (i.e., read, write and execute). 

For instance, to change the user and the group of the file
``wonderland.txt`` to ``alice`` and ``users``, respectively, we say.

    $ chown alice:users wonderland.txt

What does it say? We get an error saying, the operation is not permitted.
We have attempted to change the ownership of a file that we own, to a
different user. Logically, this shouldn't be possible, because, this can
lead to problems, in a multi-user system. 

Only the superuser is allowed to change the ownership of a file from one
user to another. The superuser or the ``root`` user is the only user
empowered to a certain set of tasks and hence is called the superuser. The
command above would have worked, if you did login as the superuser and
then changed the ownership of the file. 

We shall end our discussion of the Linux hierarchy and file permissions
here. Let us look at working with text, files and the role of the command
shell in the next section. 

Looking at files
================

cat
---

The ``cat`` command is the most commonly used command to display the
contents of files. To view the contents of a file, say, ``foo.txt``, we
simply say, 

::

    $ cat foo.txt

The contents of the file are shown on the terminal. 

The cat command could also be used to concatenate the text of multiple
files. (It's name actually comes from there). Say, we have two files,
``foo.txt`` and ``bar.txt``, 

::

    $ cat foo.txt bar.txt

shows the output of both the files concatenated on the standard output. 

But if we had a long file, like ``wonderland.txt``, the ouptut of ``cat``
command is not convenient to read. Let's look at the ``less`` command which
turns out to be more useful in such a case. 


less
----

``less `` allows you to view the contents of a text file one screen at a
time. 

::

    $ less wonderland.txt

will give show us the file, one screen at a time. 

``less`` has a list of commands that it allows you to use, once you have
started viewing a file. A few of the common ones have been listed below. 

    * q: Quit.

    * [Arrows]/[Page Up]/[Page Down]/[Home]/[End]: Navigation.

    * ng: Jump to line number n. Default is the start of the file.

    * /pattern: Search for pattern. Regular expressions can be used.

    * h: Help.

wc
--

Often we just would like to get some statistical information about the
file, rather than viewing the contents of the file. The ``wc`` command
prints these details for a file. 

::

    $ wc wonderland.txt

The first number is the number of lines, the second is the number of words
and the third is the number of characters in the file. 

head & tail
-----------

Let us now look at a couple of commands that let you see parts of files,
instead of the whole file. ``head`` and ``tail`` let you see parts of
files, as their names suggest, the start and the end of a file,
respectively. 

::

    $ head wonderland.txt

will print the first 10 lines of the file. Similarly tail will print the
last 10 lines of the file. If we wish to change the number of lines that we
wish to view, we use the option ``-n``. 

::

    $ head -n 1 wonderland.txt

will print only the first line of the file. Similarly, we could print only
the last line of the file. 

The most common use of the tail command is to monitor a continuously
changing file, for instance a log file. Say you have a process running,
which is continuously logging it's information to a file, for instance the
logs of the system messages. 

::

	$ tail -f /var/log/dmesg

This will show the last 10 lines of the file as expected, but along with
that, start monitoring the file. Any new lines added at the end of the
file, will be shown. To interrupt, tail while it is monitoring, hit
``Ctrl-C``. Ctrl-C is used to stop any process that is running from your
current shell. 

cut & paste
-----------

We looked at a couple of functions that allow you to view a part of files,
line-wise. We shall now look at a couple of commands that allow you to look
at only certain sections of each line of a file and merge those parts.

Let's take the ``/etc/passwd`` file as our example file. It contains
information about each user of the system. 

::

    root:x:0:0:root:/root:/bin/bash
    bin:x:1:1:bin:/bin:/bin/false
    daemon:x:2:2:daemon:/sbin:/bin/false
    mail:x:8:12:mail:/var/spool/mail:/bin/false
    ftp:x:14:11:ftp:/srv/ftp:/bin/false
    http:x:33:33:http:/srv/http:/bin/false

Let us look at only the first, fifth, sixth and the last columns. The first
column is the user name, the fifth column is the user info, the sixth
column is the home folder and the last column is the path of the shell
program that the user uses. 

Let's say we wish to look at only the user names of all the users in the
file, how do we do it?

::
    
    $ cut -d : -f 1 /etc/passwd

gives us the required output. But what are we doing here? 

The first option ``-d`` specifies the delimiter between the various fields in
the file, in this case it is the semicolon. If no delimiter is specified,
the TAB character is assumed to be the delimiter. The ``-f`` option specifies,
the field number that we want to choose. 

You can print multiple fields, by separating the field numbers with a
comma. 

::
    
    $ cut -d : -f 1,5,7 /etc/passwd

prints only the first, fifth and the seventh fields. 

Instead of choosing by fields, ``cut`` also allows us to choose on the
basis of characters or bytes. For instance, we could get the first 4
characters of all the entries of the file, ``/etc/passwd`` 

::

    $ cut -c 1-4 /etc/passwd 

The end limits of the ranges can take sensible default values, if they are
left out. For example, 

::

    $ cut -c -4 /etc/passwd 

gives the same output as before. If the start position has not been
specified, it is assumed to be the start of the line. Similarly if the end
position is not specified, it is assumed to be the end of the line. 

::

    $ cut -c 10- /etc/passwd 

will print all the characters from the 10th character up to the end of the
line. 

Let us now solve the inverse problem. Let's say we have two columns of data
in two different files, and we wish to view them side by side. 

For instance, given a file containing the names of students in a file, and
another file with the marks of the students, we wish to view the contents,
side by side. ``paste`` command allows us to do that. 

Contents of students.txt

::
     
     Hussain
     Dilbert
     Anne
     Raul
     Sven    

Contents of marks.txt

::

     89 92 85
     98 47 67
     67 82 76
     78 97 60
     67 68 69

::

    $ paste students.txt marks.txt

    $ paste -s students.txt marks.txt


The first command gives us the output of the two files, next to each other
and the second command gives us the output one below the other. 

Now, this problem is a bit unrealistic because, we wouldn't have the marks
of students in a file, without any information about the student to which
they belong. Let's say our marks file had the first column as the roll
number of the student, followed by the marks of the students. What would we
then do, to get the same output that we got before? 

Essentially we need to use both, the ``cut`` and ``paste`` commands, but
how do we do that? That brings us to the topic of Redirection and Piping. 

The Command Shell
=================

Redirection and Piping
----------------------

Let's say the contents of ``marks.txt`` are as follows, 

::

     5 89 92 85
     4 98 47 67
     1 67 82 76
     2 78 97 60
     3 67 68 69

The solution would be as below

::

    $ cut -d " " -f 2- marks.txt | paste -d " " students.txt -

or 

::

    $ cut -d " " -f 2- marks.txt > /tmp/m_tmp.txt
    $ paste -d " " students.txt m_tmp.txt


Let's first try to understand the second solution, which is a two step
solution. Later, we shall look at the first solution. 

Redirecting
~~~~~~~~~~~

The standard output (stdout), in general, streams (or goes) to the display.
Hence, the output of the commands that we type, come out to the display.
This may not always be what we require. 

For instance, in the solution above, we use the cut command and get only
the required columns of the file and write the output to a new temporary
file. The ``>`` character is used to state that we wish to redirect the
output, and it is followed by the location to which we wish to redirect. 

::

    $ command > file1

In general, this creates a new file at the specified location, to which the
output is written. But, if we wish to append the output to an existing
file, we use ``>>``.

Similarly, the standard input (stdin) is assumed to be from the keyboard.
Instead we could redirect the input from a file. 

::

    $ command < file1

The input and the output redirection could be combined in a single command. 

::

    $ command < infile > outfile


There is actually a third kind of standard stream, called the Standard
error (stderr). Any error messages that you get, are coming through this
stream. Like ``stdout``, ``stderr`` also streams to the display, by default
but it could be redirected to a file, as well. 

For instance, let's introduce an error into the ``cut`` command used
before. We change the ``-f`` option to ``-c`` 

::

    $ cut -d " " -c 2- marks.txt > /tmp/m_tmp.txt

This prints an error that says the delimiter option should be used with the
fields option only, and you can verify that the ``m_tmp.txt`` file is
empty.  We can now, redirect the ``stderr`` also to a file, instead of
showing it on the display. 

::

    $ cut -d " " -f 2- marks.txt 1> /tmp/m_tmp.txt 2> /tmp/m_err.txt

The above command redirects all the errors to the ``m_err.txt`` file
and the output to the ``m_tmp.txt`` file. When redirecting, 1 stands
for ``stdout`` and 2 stands for ``stderr``. That brings us to the end of
the discussion on redirecting. 

The second command in the solution of the problem is trivial to understand. 
::

    $ paste -d " " students.txt m_tmp.txt

So, in two steps we solved the problem of getting rid of the roll numbers
from the marks file and displaying the marks along with the names of the
students. Now, that we know how to redirect output, we could choose to
write the output to a file, instead of showing on the display. 

Piping
~~~~~~

Let us now look at the first solution. 

::

    $ cut -d " " -f 2- marks.txt | paste -d " " students.txt -

First of all, the hyphen at the end is to ask the paste command to read the
standard input, instead of looking for a FILE. The ``man`` page of ``paste``
command gives us this information. 

Now, what is happening with the ``cut`` command. It is a normal ``cut`` 
command, if we looked at the command only up to the ``|`` character. So,
the ``|`` seems to be joining the commands in some way. 

Essentially, what we are doing is, to redirect the output of the first
command to the ``stdin`` and the second command takes input from the
``stdin``. 

More generally, 

::

    $ command1 | command2

executes ``command1`` and sends it's output to the ``stdin``, which is then
used as the input for the ``command2``. This activity is commonly called
piping, and the character ``|`` is called a pipe. 

This is roughly equivalent to using two redirects and a temporary file 

::

    $ command1 > tempfile
    $ command2 < tempfile
    $ rm tempfile

Also, given that a pipe is just a way to send the output of the command to
the ``stdin``, it should be obvious, to you that we can use a chain of
pipes. Any number of commands can be piped together and you need not be
restricted to two commands. 

Using piping and redirection, we can do a whole bunch of complex tasks
combined with the commands we have already looked at, and other commands
that we are going to look at. 

Features of the Shell
---------------------

The Bash shell has some nice features, that make our job of using the shell
easier and much more pleasant. We shall look at a few of them, here. 

Tab-completion
~~~~~~~~~~~~~~

Bash provides the feature of tab completion. What does tab completion mean?
When you are trying to type a word, bash can complete the word for you,
if you have entered enough portion of the word (to complete it
unambiguously) and then hit the tab key. 

If on hitting the tab key, the word doesn't get completed, either the word
doesn't exist or the word cannot be decided unambiguously. If the case is
the latter one, hitting the tab key a second time, will list the
possibilities. 

Bash provides tab completion for the following. 

  1. File Names
  2. Directory Names
  3. Executable Names
  4. User Names (when they are prefixed with a ~)
  5. Host Names (when they are prefixed with a @)
  6. Variable Names (when they are prefixed with a $) 

For example, 

::

    $ pas<TAB>
    $ $PA<TAB>
    $ ~/<TAB><TAB>

History
~~~~~~~

Bash also saves the history of the commands you have typed. So, you can go
back to a previously typed command. Use the up and down arrow keys to
navigate in your bash history. 

::

    $ <UP-ARROW>

You can also search incrementally, for commands in your bash history.
``Ctrl-r`` search for the commands that you have typed before. But, note
that the number of commands saved in the history is limited, generally upto
a 1000 commands. 

::

   $ <Ctrl-r> pas


Shell Meta Characters
~~~~~~~~~~~~~~~~~~~~~

Unix recognizes certain special characters, called "meta characters," as
command directives. The shell meta characters are recognized anywhere they
appear in the command line, even if they are not surrounded by blank space.
For that reason, it is safest to only use the characters A-Z, a-z, 0-9, and
the period, dash, and underscore characters when naming files and
directories on Unix. If your file or directory has a shell meta character
in the name, you will find it difficult to use the name in a shell command.

The shell meta characters include:

\ / < > ! $ % ^ & * | { } [ ] " ' ` ~ ; 


As an example,

::

    $ ls file.*

run on a directory containing the files file, file.c, file.lst, and myfile
would list the files file.c and file.lst. However,

::

    $ ls file.?

run on the same directory would only list file.c because the ? only matches
one character, no more, no less. This can save you a great deal of typing
time. 

For example, if there is a file called
california_cornish_hens_with_wild_rice and no other files whose names begin
with 'c', you could view the file without typing the whole name by typing
this

::

    $ more c*

because the c* matches that long file name.

File-names containing metacharacters can pose many problems and should
never be intentionally created.

More text processing
====================

``sort``
--------

Let's continue with the previous problem of the students and their marks,
that we had. Let's say we wish to sort the output in the alphabetical order
of the names of the files. We can use the ``sort`` command for this
purpose.

We just pipe the previous output to the ``sort`` command. 

::

    $ cut -d " " -f 2- marks.txt | paste -d " " students.txt -| sort

Let's say we wished to sort the names, based on the marks in the first
subject (first column after the name). ``sort`` command also allows us to
specify the delimiter between the fields and sort the data on a particular
field. ``-t`` option is used to specify the delimiter and the ``-k`` option
is used to specify the field. 

::

    $ cut -d " " -f 2- marks.txt | paste -d " " students.txt -| sort -t " " -k 2

The above command give us a sorted output as required. But, it would be
nicer to have the output sorted in the reverse order. ``-r`` option allows
the output to be sorted in the reverse order and the ``-n`` option is used
to choose a numerical sorting. 

::

    $ cut -d " " -f 2- marks.txt | paste -d " " students.txt -| sort -t " " -k 2 -rn    

``grep``
--------

While you are compiling the student marklist, Anne walks up to you and
wants to know her marks. You, being the kind person that you are, oblige.
But you do not wish to her to see the marks that others have scored. What
do you do? The ``grep`` command comes to your rescue. 

``grep`` is a command line text search utility. You can use it to search
for Anne and show her, what she scored. ``grep`` allows you to search for a
search string in files. But you could, like any other command, pipe the
output of other commands to it. So, we shall use the previous combination
of cut and paste that we had, to get the marks of students along with their
names and search for Anne in that. 

::

    $ cut -d " " -f 2- marks.txt | paste -d " " students.txt - | grep Anne 

This will give you only the line containing the word Anne as the output.
The grep command is by default case-sensitive. So, you wouldn't have got
the result if you had searched for anne instead of Anne. But, what if you
didn't know, whether the name was capitalized or not? ``grep`` allows you
to do case-insensitive searches by using the ``-i`` option. 

::

    $ cut -d " " -f 2- marks.txt | paste -d " " students.txt - | grep -i Anne 

Now, in another scenario, if you wished to print all the lines, which do
not contain the word Anne, you could use the ``-v`` option. 

::

    $ cut -d " " -f 2- marks.txt | paste -d " " students.txt - | grep -iv Anne

Grep allows you to do more complex searches, for instance searching for
sentences starting or ending with a particular pattern and regular
expression based searches. You shall learn about these, as a part of your
lab exercises. 

``tr``
------

``tr`` is a command that takes as parameters two sets of characters, and
replaces occurrences of the characters in the first set with the
corresponding elements from the other set. It reads from the standard
output and writes to the standard output. 

For instance if you wished to replace all the lower case letters in the
students file with upper case, 

::

    $ cat students.txt | tr a-z A-Z

A common task is to remove empty newlines from a file. The ``-s`` flag
causes ``tr`` to compress sequences of identical adjacent characters in its
output to a single token. For example,

::

    $ tr -s '\n' '\n'

replaces sequences of one or more newline characters with a single newline.

The ``-d`` flag causes ``tr`` to delete all tokens of the specified set of
characters from its input. In this case, only a single character set
argument is used. The following command removes carriage return characters,
thereby converting a file in DOS/Windows format to the Unix format. 

::

    $ cat foo.txt | tr -d '\r' > bar.txt

The ``-c`` flag complements the first set of characters.

::

    $ tr -cd '[:alnum:]' 

therefore removes all non-alphanumeric characters.

``uniq``
--------

Suppose we have a list of items, say books, and we wish to obtain a list which names of all the books only once, without any duplicates. We use the ``uniq`` command to achieve this. 

::

  Programming Pearls
  The C Programming Language
  The Mythical Man Month: Essays on Software Engineering 
  Programming Pearls
  The C Programming Language
  Structure and Interpretation of Computer Programs
  Programming Pearls
  Compilers: Principles, Techniques, and Tools
  The C Programming Language
  The Art of UNIX Programming
  Programming Pearls
  The Art of Computer Programming
  Introduction to Algorithms
  The Art of UNIX Programming
  The Pragmatic Programmer: From Journeyman to Master
  Programming Pearls
  Unix Power Tools
  The Art of UNIX Programming

Let us try and get rid of the duplicate lines from this file using the ``uniq`` command. 

::

  $ uniq items.txt 
  Programming Pearls
  The C Programming Language
  The Mythical Man Month: Essays on Software Engineering 
  Programming Pearls
  The C Programming Language
  Structure and Interpretation of Computer Programs
  Programming Pearls
  Compilers: Principles, Techniques, and Tools
  The C Programming Language
  The Art of UNIX Programming
  Programming Pearls
  The Art of Computer Programming
  Introduction to Algorithms
  The Art of UNIX Programming
  The Pragmatic Programmer: From Journeyman to Master
  Programming Pearls
  Unix Power Tools
  The Art of UNIX Programming

Nothing happens! Why? The ``uniq`` command removes duplicate lines only when they are next to each other. So, we get a sorted file from the original file and work with that file, henceforth. 

::

  $ sort items.txt | uniq
  Compilers: Principles, Techniques, and Tools
  Introduction to Algorithms
  Programming Pearls
  Structure and Interpretation of Computer Programs
  The Art of Computer Programming
  The Art of UNIX Programming
  The C Programming Language
  The Mythical Man Month: Essays on Software Engineering 
  The Pragmatic Programmer: From Journeyman to Master
  Unix Power Tools

``uniq -u`` command gives the lines which are unique and do not have any duplicates in the file. ``uniq -d`` outputs only those lines which have duplicates. The ``-c`` option displays the number of times each line occurs in the file. 

::

  $ uniq -u items-sorted.txt 
  Compilers: Principles, Techniques, and Tools
  Introduction to Algorithms
  Structure and Interpretation of Computer Programs
  The Art of Computer Programming
  The Mythical Man Month: Essays on Software Engineering 
  The Pragmatic Programmer: From Journeyman to Master
  Unix Power Tools

  $ uniq -dc items-sorted.txt      
  5 Programming Pearls
  3 The Art of UNIX Programming
  3 The C Programming Language

That brings us to the end of our discussion on text processing. Text
processing is an art and there is a lot more to it, than could have been
covered in this short introduction. But, we hope that the tools you learned
to use here, will help you solve a great deal of problems. 

Basic editing and editors
=========================

vim
---

Vim is a very powerful editor. It has a lot of commands, and all of them
cannot be explained here. We shall try and look at a few, so that you can
find your way around in vim.

To open a file in vim, we pass the filename as a parameter to the ``vim``
command. If a file with that filename does not exist, a new file is
created. 

::

    $ vim first.txt

To start inserting text into the new file that we have opened, we need to
press the ``i`` key. This will take us into the *insert* mode from the
*command* mode. Hitting the ``esc`` key, will bring us back to the
*command* mode. There is also another mode of vim, called the *visual* mode
which will be discussed later in the course.

In general, it is good to spend as little time as possible in the insert
mode and extensively use the command mode to achieve various tasks.

To save the file, use ``:w`` in the command mode. From here on, it is
understood that we are in the command mode, whenever we are issuing any
command to vim.

To save a file and continue editing, use ``:w FILENAME`` The file name is
optional. If you do not specify a filename, it is saved in the same file
that you opened. If a file name different from the one you opened is
specified, the text is saved with the new name, but you continue editing
the file that you opened. The next time you save it without specifying a
name, it gets saved with the name of the file that you initially opened.

To save file with a new name and continue editing the new file, use ``:saveas FILENAME``

To save and quit, use ``:wq``

To quit, use ``:q``

To quit without saving, use ``:q!``

Moving around
~~~~~~~~~~~~~

While you are typing in a file, it is in-convenient to keep moving your
fingers from the standard position for typing to the arrow keys. Vim,
therefore, provides alternate keys for moving in the document. Note again
that, you should be in the command mode, when issuing any commands to vim.

The basic cursor movement can be achieved using the keys, ``h`` (left),
``l`` (right), ``k`` (up) and ``j`` (down).

::
 
             ^
             k              
       < h       l >        
             j              
             v

Note: Most commands can be prefixed with a number, to repeat the command.
For instance, ``10j`` will move the cursor down 10 lines.

Moving within a line
++++++++++++++++++++

+----------------------------------------+---------+
| Cursor Movement                        | Command | 
+========================================+=========+
| Beginning of line                      | ``0``   |
+----------------------------------------+---------+
| First non-space character of line      | ``^``   |
+----------------------------------------+---------+
| End of line                            | ``$``   |
+----------------------------------------+---------+
| Last non-space character of line       | ``g_``  |
+----------------------------------------+---------+

Moving by words and sentences
+++++++++++++++++++++++++++++

+------------------------------+---------+
| Cursor Movement              | Command |
+==============================+=========+
| Forward, word beginning      | ``w``   |
+------------------------------+---------+
| Backward, word beginning     | ``b``   |
+------------------------------+---------+
| Forward, word end            | ``e``   |
+------------------------------+---------+
| Backward, word end           | ``ge``  |
+------------------------------+---------+
| Forward, sentence beginning  | ``)``   |
+------------------------------+---------+
| Backward, sentence beginning | ``(``   |
+------------------------------+---------+
| Forward, paragraph beginning | ``}``   |
+------------------------------+---------+
| Backward, paragraph beginning| ``{``   |
+------------------------------+---------+

More movement commands
++++++++++++++++++++++

+---------------------------------+------------+
| Cursor Movement                 | Command    |
+=================================+============+
| Forward by a screenful of text  | ``C-f``    |
+---------------------------------+------------+
| Backward by a screenful of text | ``C-b``    |
+---------------------------------+------------+
| Beginning of the screen         | ``H``      |
+---------------------------------+------------+
| Middle of the screen            | ``M``      |
+---------------------------------+------------+
| End of the screen               | ``L``      |
+---------------------------------+------------+
| End of file                     | ``G``      |
+---------------------------------+------------+
| Line number ``num``             | ``[num]G`` |
+---------------------------------+------------+
| Beginning of file               | ``gg``     |
+---------------------------------+------------+
| Next occurrence of the text     | ``*``      |
| under the cursor                |            |
+---------------------------------+------------+
| Previous occurrence of the text | ``#``      |
| under the cursor                |            |
+---------------------------------+------------+

Note: ``C-x`` is ``Ctrl`` + ``x``

The visual mode
~~~~~~~~~~~~~~~

The visual mode is a special mode that is not present in the original vi
editor. It allows us to highlight text and perform actions on it. All the
movement commands that have been discussed till now work in the visual mode
also. The editing commands that will be discussed in the future work on the
visual blocks selected, too.

Editing commands
~~~~~~~~~~~~~~~~

The editing commands usually take the movements as arguments. A movement is
equivalent to a selection in the visual mode. The cursor is assumed to have
moved over the text in between the initial and the final points of the
movement. The motion or the visual block that's been highlighted can be
passed as arguments to the editing commands.

+-------------------------+---------+
| Editing effect          | Command |
+=========================+=========+
| Cutting text            | ``d``   |
+-------------------------+---------+
| Copying/Yanking text    | ``y``   |
+-------------------------+---------+
| Pasting copied/cut text | ``p``   |
+-------------------------+---------+

The cut and copy commands take the motions or visual blocks as arguments
and act on them. For instance, if you wish to delete the text from the
current text position to the beginning of the next word, type ``dw``. If
you wish to copy the text from the current position to the end of this
sentence, type ``y)``.

Apart from the above commands, that take any motion or visual block as an
argument, there are additional special commands.

+----------------------------------------+---------+
| Editing effect                         | Command | 
+========================================+=========+
| Cut the character under the cursor     | ``x``   |
+----------------------------------------+---------+
| Replace the character under the        | ``ra``  |
| cursor with ``a``                      |         |
+----------------------------------------+---------+
| Cut an entire line                     | ``dd``  |
+----------------------------------------+---------+
| Copy/yank an entire line               | ``yy``  |
+----------------------------------------+---------+

Note: You can prefix numbers to any of the commands, to repeat them.

Undo and Redo
~~~~~~~~~~~~~
You can undo almost anything using ``u``. 

To undo the undo command type ``C-r``

Searching and Replacing
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------+---------+
| Finding                                 | Command |
+=========================================+=========+
| Next occurrence of ``text``, forward    |``\text``|
+-----------------------------------------+---------+
| Next occurrence of ``text``, backward   |``?text``|
+-----------------------------------------+---------+
| Search again in the same direction      | ``n``   |
+-----------------------------------------+---------+
| Search again in the opposite direction  | ``N``   |
+-----------------------------------------+---------+
| Next occurrence of ``x`` in the line    | ``fx``  |
+-----------------------------------------+---------+
| Previous occurrence of ``x`` in the line| ``Fx``  |
+-----------------------------------------+---------+

+---------------------------------------+------------------+
| Finding and Replacing                 |  Command         |
+=======================================+==================+
| Replace the first instance of ``old`` |``:s/old/new``    |
| with ``new`` in the current line.     |                  |
+---------------------------------------+------------------+
| Replace all instances of ``old``      |``:s/old/new/g``  |
| with ``new`` in the current line.     |                  |
+---------------------------------------+------------------+
| Replace all instances of ``old``      |``:s/old/new/gc`` |
| with ``new`` in the current line,     |                  |
| but ask for confirmation each time.   |                  |
+---------------------------------------+------------------+
| Replace the first instance of ``old`` |``:%s/old/new``   |
| with ``new`` in the entire file.      |                  |
+---------------------------------------+------------------+
| Replace all instances of ``old``      |``:%s/old/new/g`` |
| with ``new`` in the entire file.      |                  |
+---------------------------------------+------------------+
| Replace all instances of ``old`` with |``:%s/old/new/gc``|
| ``new`` in the entire file but ask    |                  |
| for confirmation each time.           |                  |
+---------------------------------------+------------------+

SciTE
-----

SciTE is a *source code* editor, that has a feel similar to the commonly
used GUI text editors. It has a wide range of features that are extremely
useful for a programmer, editing code. Also it aims to keep configuration
simple, and the user needs to edit a text file to configure SciTE to
his/her liking.

Opening, Saving, Editing files with SciTE is extremely simple and trivial.
Knowledge of using a text editor will suffice.

SciTE can syntax highlight code in various languages. It also has
auto-indentation, code-folding and other such features which are useful
when editing code.

SciTE also gives you the option to (compile and) run your code, from within
the editor.

Simple Shell Scripts
====================

A shell script is simply a sequence of commands, that are put into a file,
instead of entering them one by one onto the shell. The script can then be
run, to run the sequence of commands in a single shot instead of manually
running, each of the individual commands. 

For instance, let's say we wish to create a directory called ``marks`` in the
home folder and save the results of the students into a file
``results.txt``. 

We open our editor and save the following text to ``results.sh``

::

    #!/bin/bash
    mkdir ~/marks
    cut -d " " -f 2- marks.txt | paste -d " " students.txt - | sort > ~/marks/results.txt

We can now run the script, 

::

    $ ./results.sh

We get an error saying, Permission denied! Why? Can you think of the
reason? (Hint: ``ls -l``). Yes, the file doesn't have execute permissions.
We make the file executable and then run it. 

::

    $ chmod u+x results.sh
    $ ./results.sh

We get back the prompt. We can check the contents of the file
``results.txt`` to see if the script has run. 

So, here, we have our first shell script. We understand almost all of it,
except for the first line of the file. The first line is used to specify
the interpreter or shell which should be used to execute the script. In
this case, we are asking it to use the bash shell. 

Once, the script has run, we got back the prompt. We had to manually check,
if the contents of the file are correct, to see if the script has run. It
would be useful to have our script print out messages. For this, we can use
the ``echo`` command. We can edit our ``results.sh`` script, as follows. 

::

    #!/bin/bash
    mkdir ~/marks
    cut -d " " -f 2- marks.txt | paste -d " " students.txt - | sort > ~/marks/results.txt
    echo "Results generated."

Now, on running the script, we get a message on the screen informing us,
when the script has run. 

Let's now say, that we wish to let the user decide the file to which the
results should be written to. The results file, should be specifiable by an
argument in the command line. We can do so, by editing the file, as below. 

::

    #!/bin/bash
    mkdir ~/marks
    cut -d " " -f 2- marks.txt | paste -d " " students.txt - | sort > ~/marks/$1
    echo "Results generated."


The ``$1`` above, corresponds to the first command line argument to the
script. So, we can run the script as shown below, to save the results to
``grades.txt``. 

::

    $ ./results.sh grades.txt    

When we run the ``results.sh`` file, we are specifying the location of the
script by using ``./``. But for any of the other commands (even if they may
not be shell scripts), we didn't have to specify their locations. Why? The
shell has a set of locations where it searches, for the command that we are
trying to run. These set of locations are saved in an "environment"
variable called PATH. We shall look at environment variables, again, later.
But, let us look at what the value of the PATH variable is. To view the
values of variables, we can use the echo command.

::

    $ echo $PATH

So, these are all the paths that are searched, when looking to execute a
command. If we put the results.sh script in one of these locations, we
could simply run it, without using the ``./`` at the beginning. 

Control structures and Operators
================================

We can have if-else constructs, for and while loops in bash. Let us look at
how to write them, in this section. 

To write an if, or an if-else construct, we need to check or test for a
condition. ``test`` command allows us to test for conditions. ``test`` has
a whole range of tests that can be performed. The man page of ``test``
gives a listing of various types of tests that can be performed with it. 

Let's write a simple script with an ``if`` condition that tests whether a
directory with a particular name, is present or not.

``if``
------

Let's save the following code to the script ``dir-test.sh``

::

    #!/bin/bash
    if test -d $1
    then
      echo "Yes, the directory" $1 "is present"
    fi

When the script is run with an argument, it prints a message, if a
directory with that name exists in the current working directory. 

``if`` - ``else``
-----------------

Let's write a simple script which returns back whether the argument passed
is negative or not

::

   #!/bin/bash
   if test $1 -lt 0
   then
     echo "number is negative"
   else
     echo "number is non-negative"
   fi

We can run the file with a set of different inputs and see if it works. 

::

   $ ./sign.sh -11

Instead of using the ``test`` command, square brackets can also be used. 

::

   #!/bin/bash
   if [ $1 -lt 0 ]
   then
     echo "number is negative"
   else
     echo "number is non-negative"
   fi

Note that the spacing is important, when using the square brackets. ``[``
should be followed by a space and ``]`` should be preceded by a space. 

Let's create something interesting using the if-else clause. Let's write a
script, that greets the user, based on the time. 

::

   #!/bin/sh
   # Script to greet the user according to time of day
   hour=`date | cut -c12-13`
   now=`date +"%A, %d of %B, %Y (%r)"`
   if [ $hour -lt 12 ]
   then
     mess="Good Morning $LOGNAME, Have a nice day!"
   fi

   if [ $hour -gt 12 -a $hour -le 16 ]
   then
     mess="Good Afternoon $LOGNAME"
   fi

   if [ $hour -gt 16 -a $hour -le 18 ]
   then
     mess="Good Evening $LOGNAME"
   fi
   echo -e "$mess\nIt is $now"

There a couple of new things, in this script. ``$LOGNAME`` is another
environment variable, which has the login name of the user. The variables
``hour`` and ``now`` are actually taking the output of the commands that
are placed in the back quotes. 

Let us now see how to run loops in bash. We shall look at the ``for`` and
the ``while`` loops. 

``for``
-------

Suppose we have a set of files, that have names beginning with numbers
followed by their names - ``08 - Society.mp3``. We would like to rename
these files to remove the numbering. How would we go about doing that? 

It is clear from the problem statement that we could loop over the list of
files and rename each of the files. 

Let's first look at a simple ``for`` loop, to understand how it works. 

::

  for animal in rat cat dog man
  do 
    echo $animal
  done

We just wrote a list of animals, each animal's name separated by a space
and printed each name on a separate line. The variable ``animal`` is a
dummy or a loop variable. It can then be used to refer to the element of
the list that is currently being dealt with. We could, obviously, use
something as lame as ``i`` in place of ``animal``.

Now, we use a ``for`` loop to list the files that we are interested in.

::

  for i in `ls *.mp3`
  do
    echo "$i"
  done

If the file-names contain spaces, ``for`` assumes each space separated word
to be a single item in the list and prints it in a separate line. We could
change the script slightly to overcome this problem.

::

  for i in *.mp3
  do
    echo "$i"
  done

Now, we have each file name printed on a separate line. The file names are
in the form ``dd - Name.mp3`` and it has to be changed to the format
``Name.mp3``. Also, if the name has spaces, we wish to replace it with
hyphens. 

::

  for i in *.mp3
  do 
    echo $f|tr -s " " "-"|cut -d - -f 2-
  done

Now we just replace the echo command with a ``mv``  command. 

::

  for i in *.mp3
  do 
    mv $i `echo $f|tr -s " " "-"|cut -d - -f 2-`
  done

``while``
---------

The ``while`` command allows us to continuously execute a block of commands
until the command that is controlling the loop is executing successfully.

Let's start with the lamest example of a while loop.

::

  while true
  do
    echo "True"
  done

This, as you can see, is an infinite loop that prints the ``True``. 

Say we wish to write a simple program that takes user input and prints it
back, until the input is ``quit``, which quits the program. 

::

  while [ "$variable" != "quit" ]
  do
    read variable
    echo "Input - $variable"
  done
  exit 0

Environment Variables
---------------------

Environment variables are way of passing information from the shell to the
programs that are run in it. Programs are often made to look "in the
environment" for particular variables and behave differently based on what
their values are. 

Standard UNIX variables are split into two categories, environment
variables and shell variables. In broad terms, shell variables apply only
to the current instance of the shell and are used to set short-term working
conditions; environment variables have a farther reaching significance, and
those set at login are valid for the duration of the session. By
convention, environment variables have UPPER CASE and shell variables have
lower case names.

Here are a few examples of environment variables, 

::

   $ echo $OSTYPE 
   linux-gnu
   $ echo $HOME
   /home/user 

To see all the variables and their values, we could use any of the
following,  

::

   $ printenv | less
   $ env

We have looked at the PATH variable, in the previous section. We shall now
use the ``export`` command to change it's value.  

::

   $ export PATH=$PATH:$HOME/bin

See the difference in value of PATH variable before and after modifying it.

``export`` command is used to export a variable to the environment of all
the processes that are started from that shell. 

Miscellaneous Tools
===================

Finally, here are a bunch of tools, that will prove to be handy in your day
to day work. These tools will help you quickly perform tasks like searching
for files, comparing files and checking if they are the same, viewing the
exact differences between them. 

find
----

The ``find`` command lets you find files in a directory hierarchy. It
offers a very complex feature set allowing you to search for files with a
wide range of restrictions. We shall only look at some of the most
frequently used ones. You should look at the man page, for more. 

To find all files, which end with an extension, ``.pdf``, in the current
folder and all it's subfolders, 

::

    $ find . -name "*.pdf"

To list all the directory and sub-directory names, 

::

    $ find . -type d 

``find`` allows you to set limits on file-size, modification time and whole
lot of other things. 

``cmp``
-------

To compare two files, whether they are identical or not, we can use the
``cmp`` command. Let us consider some situation, we run ``find`` to locate
some file, and it turns out that we have a file with same name in different
location. 

If we are unsure, whether both the files are the same, we can use the
``cmp`` command to check if the files are identical. 

::

   $ find . -name quick.c
   ./Desktop/programs/quick.c
   ./c-folder/quick.c
   $ cmp Desktop/programs/quick.c c-folder/quick.c

If the cmp command doesn't return any output, it means that both files are
exactly identical. If there are any differences in the file, it gives you
the exact byte location at which the first difference occurred. 

Here is the output, after we made a small change to one of the files.

::

   $ cmp Desktop/programs/quick.c c-folder/quick.c
   Desktop/programs/quick.c c-folder/quick.c differ: byte 339, line 24
 

``diff``
--------

Now, we may not be happy with just the knowledge that the files are
different. We may want to see the exact differences between the files.
The ``diff`` command can be used to find the exact differences between the
files. 

::

   $ diff Desktop/programs/quick.c c-folder/quick.c

We get back a line by line difference between the two files. The ``>`` mark
indicates the content that has been added to the second file, and was not
present in the first file. The ``<`` mark indicates the lines that were
present in the first file, but are not existent in the second file. 

``tar``
-------

You would often come across (archive) files which are called *tarballs*. A
tar ball is essentially a collection of files, which may or may not be
compressed. Essentially, it eases the job of storing, backing up and
transporting multiple files, at once. 

Extracting an archive
~~~~~~~~~~~~~~~~~~~~~

The following command extracts the contents of the ``allfiles.tar`` tarball
to the directory extract. 

::

   $ mkdir extract
   $ cp allfiles.tar extract/
   $ cd extract
   $ tar -xvf allfiles.tar 

The option, ``x`` tells ``tar`` to extract the files in the archive file
specified by the ``f`` option. The ``v`` option tells ``tar`` to give out a
verbose output. 

Creating an archive
~~~~~~~~~~~~~~~~~~~

Similarly, if we wish to create a ``tar`` archive, we use the ``c`` option
instead of the ``x`` option. For instance, the command below creates an
archive from all the files with the ``.txt`` extension. 

::

    $ tar -cvf newarchive.tar *.txt


Compressed archives
~~~~~~~~~~~~~~~~~~~

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


So, if we wished to create a gzip archive in the previous command, we
change it to the following

::

    $ tar -cvzf newarchive.tar.gz *.txt

Customizing your shell
----------------------

What would you do, if you want bash to execute a particular command each
time you start it up? For instance, say you want the current directory to
be your Desktop instead of your home folder, each time bash starts up. How
would you achieve this? Bash reads and executes commands in a whole bunch
of files called start-up files, when it starts up.

When bash starts up as an interactive login shell, it reads the files
``/etc/profile``, ``~/.bash_profile``, ``~/.bash_login``, and
``~/.profile`` in that order.

When it is a shell that is not a login shell, ``~/.bashrc`` is read and the
commands in it are executed. This can be prevented using the ``--norc``
option. To force bash to use another file, instead of the ``~/.bashrc``
file on start-up, the ``--rcfile`` option may be used.

Now, you know what you should do, to change the current directory to you
Desktop. Just put a ``cd ~/Desktop`` into your ``~/.bashrc`` and you are
set!

This example is quite a simple and lame one. The start-up files are used
for a lot more complex things than this. You could set (or unset) aliases
and a whole bunch of environment variables in the ``.bashrc``, like
changing environment variables etc. 

.. 
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: nil
   fill-column: 75
   End:
