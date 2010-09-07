Introducing Linux
=================

GNU/Linux is an  operating system that uses the Linux Kernel. It is similar to the Unix operating system. It is an open source operating system which basically means you can view and change the code.  

The Linux Kernel written by Linus Torvalds in 1991. Although written only for x86 architecture , it was ported to many other architectures.The whole operating system contains the kernel and several other system and application software contributed by many different projects. A major contributor has been the GNU project. GNU project was started by Richard Stallman in 1983. Richard Stallman wrote the GNU General Public License which gave the first impetus to the free software movement leading up do development of the family of Linux operating systems that we see today . 

Design and Implications
------------------------

Linux is a modular operating system, deriving much of its basic design from principles established in Unix earlier. The kernel  manages the systems resources like process control, networking, peripherals and file system access. Application Software written on top of it gives higher level functionality. 

Reasons for Using Linux
-----------------------
- Linux is free:

As in "free beer". Linux can be downloaded in its entirety from the Internet completely for free. No registration fees, no costs per user, free updates, and freely available source code in case you want to change the behavior of your system.

- Linux can be deployed easily on clusters for parallel and distributed computing 

There are many distributions of Linux meant for clusters. One of the popular ones is Rocks Cluster Distribution.   

- Linux was made to keep on running:

As with UNIX, a Linux system expects to run without rebooting all the time. That is why a lot of tasks are being executed at night or scheduled automatically for other times, resulting in higher availability during busier periods and a more balanced use of the hardware. This property allows for Linux to be applicable to environments where people do not have the time or the possibility to control their systems constantly.

- Linux is secure and versatile:

The security model used in Linux is based on the UNIX idea of security, which is known to be robust and of proven quality. 

- Linux contains a tools for scientific computing

Linux contains many tools like latex for reading and writing scientific text. It also contains many softwares like scilab , python and fortran used for scientific computing needs. 



Getting Started
================

Logging in, activating the user interface and logging out
----------------------------------------------------------
Linux supports multiple users on a machine. Each user must log in with his or her username and password.

In order to work on a Linux system directly, one needs to provide a username and password. You always need to authenticate to the system. After booting , you will see a login screen/prompt asking for username and password , enter the username and password , if it is correct you will be logged in . One can logout by typing logout on the prompt or navigating to logout button if using Graphical User Interface . 


When you see the login screen again, asking to enter username and password, logout was successful.


Basic Commands
===============

What files do I have on my computer?
-------------------------------------

All content in Linux  is kept on data structure called files.We can list those files to know what all is there.
*ls* lists the files in the current working directory. A directory that is not the current working directory can be specified and ls will list the files there.::


	$ ls
	jeeves.rst psmith.html blandings.html Music

How do I move around the file system?
-------------------------------------

This stands for "change directory". When one wants to change the directory .

       $cd Music 

One dot '.' represents the current directory while two dots '..' represent the parent directory.

“ cd -” will return you to the previous directory.

You can also use cd [absolute path] or cd [relative path] (see below):

Absolute paths:

Absolute Path is the path of the directory from root i.e / . / is the top most level in file system.

For example to get to /var/www you would type::

	$cd /var/www

This is an absolute path because you start at the top of the hierarchy and go downwards from there (it doesn't matter where in the filesystem you were when you typed the command).

Relative paths:

   Releative Path is path in relation to your current location . 

    For example if you are in Music directory and want to get to Rock directory inside Music, you type::

	Music$ cd Rock

Please note that there is no / using the above cd command. Using a / would cause this to be an absolute path, working from the top of the hierarchy downward.

Linux is multiuser system so *who* all are using my system now?
--------------------------------------------------------

The standard Unix command *who* displays a list of users who are currently logged into a computer.::



	$who
	user       tty7         2009-09-08 10:50 (:0)
	harry      pts/0        2009-09-08 11:25 (:0.0)
	dumbledore pts/1        2009-09-08 18:11 (potter.xyz.in)

The columns represent user, current terminal , date and time of login and the host from which he is logged in respectively. 
The command can be invoked with the arguments *am i* or *am I* (so it is invoked as *who am i* or * who am I*), showing information about the current terminal only (see the *-m* option below, of which this invocation is equivalent).



How do I organize my files?
---------------------------

This command is used to make a new directory. Normal usage is as straightforward as follows::

	$mkdir name_of_directory

Where *name_of_directory* is the name of the directory one wants to create. When typed as above (ie. normal usage), the new directory would be created within the current directory. On Unix, multiple directories can be specified, and *mkdir* will try to create all of them.




Where am I now on the filesystem?
--------------
pwd is a Linux / Unix command which prints the current working directory. If you wish to know the full path of the  directory in which you are in from the Linux console, then the pwd command will come to your rescue. pwd stands for Print Working Directory.

Usage of pwd command::

      $ cd Examples
      $ pwd
      /home/user/Examples



 I wish some commads were a bit smarter ? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The standard commands in Linux have a lot of options also called flags to change or provide some additional functionality to the command For example ::
      
       $ls -l 
       
       * *ls with flag -l* displays the result in long format, displaying Unix file types, permissions, number of hard links, owner, group, size, date, and filename ::

       $ls ­a 
       * *ls with flag -a*  lists all files including hidden files


Similarly, mkdir with -p option automatically creates parent directory even if it does not exist.::

	   $mkdir -p this/path/never/existed/earlier/
	    



Getting Help
============

How do I find what a command does?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A short index of explanations for commands is available using the *whatis* command, like in the examples below::

	$whatis ls
	ls (1) 		 - list directory contents

This displays short information about a command, and the first section in the collection of man pages that contains an appropriate page.

More extensive Documentation
----------------------------

Man pages (short for "manual pages") are the extensive documentation that comes preinstalled with almost all substantial Unix and Unix-like operating systems. The Unix command used to display them is *man*. Each page is a self-contained document.

To read a manual page for a Unix command, one can use::

	$ man <command_name>

To see the manual on man itself do::

	$man man

The previous example will take you to the "Manual" page entry about manual pages!

Looking at man pages is a very good way to actually check flags and other help related to a command. 

--help
-------

Most GNU commands support the --help, which gives a short explanation about how to use the command and a list of available options. Below is the output of this option with the *mkdir* command::

	$ mkdir --help
	
	Usage: mkdir [OPTION]... DIRECTORY...
        Create the DIRECTORY(ies), if they do not already exist.

        Mandatory arguments to long options are mandatory for short options too.
          -m, --mode=MODE   set file mode (as in chmod), not a=rwx - umask
          -p, --parents     no error if existing, make parent directories as needed
          -v, --verbose     print a message for each created directory
          -Z, --context=CTX  set the SELinux security context of each created
                            directory to CTX
          --help     display this help and exit
          --version  output version information and exit

        Report mkdir bugs to bug-coreutils@gnu.org
        GNU coreutils home page: <http://www.gnu.org/software/coreutils/>
        General help using GNU software: <http://www.gnu.org/gethelp/>
        Report mkdir translation bugs to <http://translationproject.org/team/>



Working with Files
===================

Copying Files
-------------

*cp* is the command to copy a file from one place to another including different file system(#change? ellaborate). The original file remains unchanged, and the new file may have the same or a different name.

Usage
~~~~~

To copy a file to another file ::

	$ cp  SourceFile TargetFile

To copy a file to a directory::

	$ cp  SourceFile  TargetDirectory
 
To copy a directory to a directory::

	$ cp  -r SourceDirectory  TargetDirectory

In case target Directory has a file of the same name::
   	
	TargetDirectory$ls
	jeeves.rst psmith.html

	SourceDirectory$ls
	jeeves.rst index.html
	
	$cp -i 	jeeves.rst TargetDirectory/
	cp: overwrite 'TargetDirectory/jeeves.rst'? 

-i option is for interactive usage.


Flags
~~~~~
*-i* (interactive) – prompts you with the name of a file to be overwritten. This occurs if the TargetDirectory or TargetFile parameter contains a file with the same name as a file specified in the SourceFile or SourceDirectory parameter. If you enter y or the locale's equivalent of y, the cp command continues. Any other answer prevents the cp command from overwriting the file.


*-r* (recursive) – copy directories (recursively copying all the contents)


Moving Files
------------

*mv* (short for move) is a Unix command that moves one or more files or directories from one place to another. The original file is deleted, and the new file may have the same or a different name.An interesting usage of mv is actualy to rename it by moving it in same directory under a different name. 



Usage
~~~~~~~~


To rename a file ::

   $ mv myfile mynewfilename  

To move to a different directory ::
   $ mv myfile otherdir/     

To move a directory ::
   
   $mv mydir otherdir


Using -i to avoid overwrite(just like cp)::
   
   $mv -i mydir otherdir
   mv: overwrite `otherdir/mydir'?


Removing files
--------------

*rm*  is used to delete files from a filesystem. 

Here's example to remove a file named "foo" from a directory, here shown with the -i option::

  	$ rm -i foo
    	remove foo? y

Options
~~~~~~~

Common options that rm accepts include:

    * *-r*, which removes directories, removing the contents recursively beforehand (so as not to leave files without a directory to reside in) ("recursive")
    * *-i*, which asks for every deletion to be confirmed ("interactive")
    * *-f*, which ignores non-existent files and overrides any confirmation prompts ("force")
    * *-v*, which shows what is being removed as it happens ("verbose")

*rm* is often aliased to "rm -i" so as to avoid accidental deletion of files. 

*rm -rf* (variously, rm -rf /, rm -rf `*`, and others) is frequently used in jokes and anecdotes about Unix disasters. The rm -rf variant of the command, if run by a superuser on the root directory, would cause the contents of every writable mounted filesystem on the computer to be deleted.





Permissions
~~~~~~~~~~~
Linux is a proper multi-user environment. In a multi-user environment, security of user and system data is very important. Access should be given only to users who need to access the data. Since Linux is essentially a server OS, good and efficient file security is built right . The permissions are based on whether one is allowed to read, write or execute a file.

Usually, on most filesystems, deleting a file requires write permission on the parent directory (and execute permission, in order to enter the directory in the first place). (Note that, confusingly for beginners, permissions on the file itself are irrelevant. However, GNU rm asks for confirmation if a write-protected file is to be deleted, unless the -f option is used.)

To delete a directory (with rm -r), one must delete all of its contents recursively. This requires that one must have read and write and execute permission to that directory (if it's not empty) and all non-empty subdirectories recursively (if there are any).


Is there a default organization system of files and Directories that Linux follows
==================================================================================

In the File Hierarchy Standard (FHS) all files and directories appear under the root directory "/", even if they are stored on different physical devices. Note however that some of these directories may or may not be present on a Unix system depending on whether certain subsystems, such as the X Window System, are installed.

The majority of these directories exist in all UNIX operating systems and are generally used in much the same way; however, the descriptions here are those used specifically for the FHS, and are not considered authoritative for platforms other thanmajor Linux distros.

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


man hier
---------

This is the manual page on the UNIX filesystem. The syntax for this is::

	$ man hier






Permissions and Ownership
=========================

drwxr-x--- 2 user group 4096 Dec 28 04:09 tmp
-rw-r--r-- 1 user group 969 Dec 21 02:32 foo
-rwxr-xr-x 1 user group 345 Sep 1 04:12 somefile

d - The file is a directory.

r - Read permission. The file may be read. In the case of a directory, this would mean the ability to list the contents of the directory.

w - Write permission.For a directory, this defines whether you can make any changes to the contents
of the directory. If write permission is not set then you will not be able to delete, rename or create a file.

x - Execute permission. Whether the file may be executed. In the case of a directory, this attribute decides whether you have permission to enter,run a search through that directory or execute some program from that directory.

The Permission are read in the following manner::

    | User | Group | Others |
    |------+-------+--------|
    | drwx | rwx   | rwx    |


Problem: Given a file with only read permission, add execute permission to User, Group and Others.
--------------------------------------------------------------------------------------------------

Solution::
	
	$chmod a+x executablefile
   	$ls -l executablefile

Thats it .


chmod
------

The *chmod* command changes the  file system modes of files and directories. The modes include permissions and special modes.
 
Usage
~~~~~

The *chmod* command options are specified like this:
::

	$ chmod [options] mode[,mode] file1 [file2 ...]

To view what the permissions currently are, type:
::

	$ ls -l file

Command line options
~~~~~~~~~~~~~~~~~~~~

The *chmod* command has a number of command line options that affect its behavior. The most common options are:

    * -R: Changes the modes of directories and files recursively

    * -v: Verbose mode; lists all files as they are being processed

Symbolic modes
+++++++++++++++

To the *chmod* utility, all permissions and special modes are represented by its mode parameter. One way to adjust the mode of files or directories is to specify a symbolic mode. The symbolic mode is composed of three components, which are combined to form a single string of text:
::

	$ chmod [references][operator][modes] file1 ...

The references (or classes) are used to distinguish the users to whom the permissions apply. If no references are specified it defaults to “all” but modifies only the permissions allowed by the umask. The references are represented by one or more of the following letters:

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

The *chmod* program uses an operator to specify how the modes of a file should be adjusted. The following operators are accepted:

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

The modes indicate which permissions are to be granted or taken away from the specified classes. There are three basic modes which correspond to the basic permissions:

+-----+--------------+------------------------------------------------+
|Mode |    Name      |                 Description                    |
+=====+==============+================================================+
| r   | read         | read a file or list a directory's contents     |
+-----+--------------+------------------------------------------------+
| w   | write        | write to a file or directory                   |   
+-----+--------------+------------------------------------------------+
| x   | execute      | execute a file or recurse a directory tree     |
+-----+--------------+------------------------------------------------+

Examples
+++++++++

Add the 'read' and 'write' permissions to the 'user' and 'group' classes of a directory:
::

	$ chmod ug+rw mydir
	$ ls -ld mydir
	drw-rw----   2 starwars  yoda  96 Dec 8 12:53 mydir

For a file, remove *write* permissions for all classes:
::

	$ chmod a-w myfile
	$ ls -l myfile
	-r-xr-xr-x   2 starwars  yoda 96 Dec 8 12:53 myfile

Octal numbers
+++++++++++++

The *chmod* command also accepts three and four-digit octal numbers representing modes. Using a three-digit octal number to set the modes of a file named myfile :
::

	$ chmod 664 myfile
	$ ls -l myfile
	-rw-rw-r--  1   57 Jul  3 10:13  myfile

Foe each one, you define the right like that :

    * a read right correspond to 4
    * a write right correspond to 2
    * an execute right correspond to 1

You want the user to have all the rights? : 4 + 2 + 1 = 7

you want the group to have read and write rights : 4 + 2 = 6


Changing Ownership of Files
===========================


chown
~~~~~
The chown command is used to change the owner and group of files, directories and links.

By default, the owner of a filesystem object is the user that created it. The group is a set of users that share the same access permissions (i.e., read, write and execute) for that object.

The basic syntax for using chown to change owners is::

    $chown -v alice wonderland.txt

-v - For verbose Mode
 
alice - Username of new owner 





Working with text
=================

How do I look into a file?
~~~~~~~~~~~~~~~~~~~~~~~~~~

more
-----

In computing, *more* is a command to view  contents of a text file one screen at a time 

Usage
~~~~~

The command-syntax is::

	$ more [options] [file_name]

Traversing the pages ::


     SPACE       Display next k lines of text.  Defaults to current screen
                 size.


     RETURN      Display next k lines of text.  Defaults to 1.  Argument
                 becomes new default.
	       
     /pattern    Search for kth occurrence of regular expression.  Defaults to
                 1 .



less
-----

*less*  is similar to *more* in the sense that it is used to view files , but has the extended capability of allowing both forward and backward navigation through the file. Unlike most Unix text editors/viewers, *less* does not need to read the entire file before starting, resulting in faster load times with large files.

Usage
~~~~~~

*less* can be invoked with options to change its behaviour, for example, the number of lines to display on the screen. A few options vary depending on the operating system. While *less* is displaying the file, various commands can be used to navigate through the file. These commands are based on those used by both *more* and *vi*. It is also possible to search for character patterns in the file.

By default, *less* displays the contents of the file to the standard output (one screen at a time). If the file name argument is omitted, it displays the contents from standard input (usually the output of another command through a pipe). If the output is redirected to anything other than a terminal, for example a pipe to another command, less behaves like cat.

The command-syntax is ::

	$ less [options] file_name



Frequently Used Commands
~~~~~~~~~~~~~~~~~~~~~~~~

    * [Arrows]/[Page Up]/[Page Down]/[Home]/[End]: Navigation.

    * [Space bar]: Next page.

    * b: Previous page.

    * ng: Jump to line number n. Default is the start of the file.

    * nG: Jump to line number n. Default is the end of the file.

    * /pattern: Search for pattern. Regular expressions can be used.

    * '^ or g: Go to start of file.

    * '$ or G: Go to end of file.

    * =: File information.

    * h: Help.

    * q: Quit.


cat
---

The *cat* command is a standard Unix program used to concatenate and display files. The name is from "catenate", a synonym of *concatenate*.

The Single Unix Specification specifies the behavior that the contents of each of the files given in sequence as arguments will be written to the standard output in the same sequence, and mandates one option, -u, where each byte is printed as it is read.

If the filename is specified as -, then *cat* will read from standard input at that point in the sequence. If no files are specified, *cat* will read from standard input entered.

Usage ::
        $ cat foo boo
	This is file foo
	
	This is file boo.

Text Processing 
---------------


How do look at part of a file?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

head
-----

*head* is a program on Unix and Unix-like systems used to display the first few lines of a text file or piped data. The command syntax is::

	$ head [options] <file_name>

By default, *head* will print the first 10 lines of its input to the standard output. The number of lines printed may be changed with a command line option. The following example shows the first 20 lines of somefile::

	$ head -n 20 somefile




tail
----

*tail* is a program on Unix and Unix-like systems used to display the last few lines of a text file or piped data.

The command-syntax is::

	$ tail [options] <file_name>

By default, *tail* will print the last 10 lines of its input to the standard output. With command line options the number of lines printed and the printing units (lines, blocks or bytes) may be changed. The following example shows the last 20 lines of somefile::

	$ tail -n 20 somefile



This example shows all lines of somefile from the second line onwards::

	$ tail -n +2 somefile



Monitoring a continously changing file(example: A log file) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*tail* has a special command line option *-f* (follow) that allows a file to be monitored. Instead of displaying the last few lines and exiting, tail displays the lines and then monitors the file. As new lines are added to the file by another process, tail updates the display. This is particularly useful for monitoring log files. The following command will display the last 10 lines of messages and append new lines to the display as new lines are added to messages::

	$ tail -f /var/log/dmesg

To interrupt tail while it is monitoring, break-in with *Ctrl+C*. This command can be run "in the background" with &, see job control.

More serious Text Processing:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Problem1. Get the names of people in the following file
-----------------------------------------------------
::

	Foot in Mouth:Bully:Fat:Peter
	Rich:Simple:Peabrain:Lois
	Self-concious:Wannabe:Adolescent:Meg
	Dim-witted:Fat:evil-monkey:Chris
	Matricidal:Over-Ambitious:Infant:Stewy
	Anthropomorphic:Democrat:Sensible:Brian

Soulution::
 	$cut -d : -f 4- file
	
	Peter
	Lois
	Meg
	Chris
	Stewy
	Brian


		



cut
----

In computing, *cut* is a Unix command line utility which is used to extract sections from each line of input — usually from a file.

Extraction of line segments can typically be done by  a *delimiter (-d — the tab character by default)*. A range must be provided in which consists of one of N, N-M, N- (N to the end of the line), or -M (beginning of the line to M), where N and M are counted from 1 (there is no zeroth value). 


Options
-------
::

	-b   select on the basis of bytes

        -c   select on the basis of characters
			
			
	-f  select on  the basis of fields,also print any line that contains no delimiter character

Problem2.Given two files of student name and marks merge them
-------------------------------------------------------------

File of students(students.txt) ::
     
     Hussain
     Dilbert
     Alex
     Raul
     Sven

File of marks(marks.txt)::
     

     89
     98
     67
     78
     67

Solution::

	$paste students.txt marks.txt
	Hussain	89
	Dilbert	98
 	Alex	67
 	Raul	78
 	Sven	67


	$paste -d : students.txt marks.txt
	
	Hussain:89
	Dilbert:98
	Alex:67
 	Raul:78
 	Sven:67

	
	$paste -s students.txt marks.txt

	Hussain	  	 Dilbert	 Alex	 Raul	 Sven	
	89		 98		 67	 78	 67




paste
------

*paste* is a Unix command line utility which is used to join files horizontally (parallel merging) by outputting lines consisting of the sequentially corresponding lines of each file specified, separated by tabs, to the standard output. 


Some frequently used Text Processing tools
==========================================

Given a file with names US presidents  . Sort the file  on the names . The contents of the file are mentioned below
::
      
       
       John%Kennedy
       Bill%Clinton
       Bill%Clinton
       Franklin%Rosevelt
       George%Bush 
       Abraham%Lincoln
       Abraham%Lincoln
       George%Washington
       George%Washington
       


Solution:: 
	
	 $sort presidents.txt

       Abraham%Lincoln
       Abraham%Lincoln
       Bill%Clinton
       Bill%Clinton       
       Franklin%Rosevelt
       George%Bush 
       George%Washington
       George%Washington
       John%Kennedy


Sort
====
sort command with the file name as a parameter sorts the lines of the file alphabetically and prints the output on the terminal.	


To sort the same file using the last names     
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

	$sort -t % -k 2 presidents.txt
	
	George%Bush 
        Bill%Clinton
        Bill%Clinton       
        John%Kennedy
        Abraham%Lincoln
        Abraham%Lincoln
        Franklin%Rosevelt
        George%Washington
        George%Washington



	-t - specify the delimiter 
	-k - specify the column 

There are other options like -r to sort on reverse order etc ..



Problem:Given a file remove all the duplicate lines in it ?
===========================================================

File ::
     
       Abraham%Lincoln
       Abraham%Lincoln
       Bill%Clinton
       Bill%Clinton       
       Franklin%Rosevelt
       George%Bush 
       George%Washington
       George%Washington
       John%Kennedy

Solution::
      
      $uniq -c sortpresidents.txt


      2 Abraham%Lincoln       
      2 Bill%Clinton
      1 Franklin%Rosevelt
      1 George%Bush 
      2 George%Washington
      1 John%Kennedy


uniq
====


``uniq`` command removes duplicate lines next to each other.

-c - also gives the no. of repetitions .


Redirection and Piping
=======================

In computing, *redirection* is a function common to most command-line interpreters, including the various Unix shells that can redirect standard streams to user-specified locations.



Problem: Get a sorted list of all xml file in directory ?

Soulition::
	$ls | grep '.xml$' > xmllist


This problem introduced a lot of concepts we shall look at them one by one .


Redirecting standard input and standard output
-----------------------------------------------

Redirection refers to redirecting standard Input or output to a command or file .

Ex::

	$ command > file1

This command executes *command1*, placing the output in file1. Note that this will truncate any existing data in *file1*. To append output to the end of the file, use the >> operator like this
     	$ command >> file1
	
Ex2::
	


	$ command < file1

executes *command1*, using *file1* as the source of input (as opposed to the keyboard).::

	$ command1 < infile > outfile

combines the two capabilities: *command1* reads from *infile* and writes to *outfile*


In this example we see redirection in the end ::

   $(some commands) > xmllist 




Piping
-------

Programs can be run together such that one program reads the output from another with no need for an explicit intermediate file:
A pipeline of two programs run on a text terminal::

	$ command1 | command2

executes *command1*, using its output as the input for *command2* (commonly called piping, since the '|' character is known as a "pipe").

This is equivalent to using two redirects and a temporary file ::

	$ command1 > tempfile
	$ command2 < tempfile
	$ rm tempfile

In the above example we used piping in the following manner ::

	$ echo

This runs the ftp client with input user, press return, then pass.

Redirecting to and from the standard file handles
--------------------------------------------------

In Unix shells derived from the original Bourne shell, the first two actions can be further modified by placing a number (the file descriptor) immediately before the character; this will affect which stream is used for the redirection. The Unix standard I/O streams are:

+------------+-------------+------------------------+
|   Handle   |    Name     |      Description       |
+============+=============+========================+
| 0          |   stdin     |    Standard input      |
+------------+-------------+------------------------+
| 1          |   stdout    |    Standard output     |
+------------+-------------+------------------------+
| 2          |   stderr    |    Standard error      |
+------------+-------------+------------------------+

For example:
::

	$ command1 2> file1

executes *command1*, directing the standard error stream to *file1*. 



	$ find / -name .profile 2>&1 | less



Chained pipelines
------------------

The redirection and piping tokens can be chained together to create complex commands. For example:
::

	$ ls | grep '\.sh' | sort > shlist

lists the contents of the current directory, where this output is filtered to only contain lines which contain *.sh*, sort this resultant output lexicographically, and place the final output in *shlist*. This type of construction is used very commonly in shell scripts and batch files.

Redirect to multiple outputs
-----------------------------

The standard command *tee* can redirect output from a command to several destinations.
::

	$ ls -lrt | tee xyz

This directs the file list output to both standard output as well as to the file *xyz*.



Shell Meta Characters
======================

Unix recognizes certain special characters, called "meta characters," as command directives. The shell meta characters are recognized anywhere they appear in the command line, even if they are not surrounded by blank space. For that reason, it is safest to only use the characters A-Z, a-z, 0-9, and the period, dash, and underscore characters when naming files and directories on Unix. If your file or directory has a shell meta character in the name, you will find it difficult to use the name in a shell command.

The shell meta characters include:

\ / < > ! $ % ^ & * | { } [ ] " ' ` ~ ; 


As an example,
::

	$ ls file.*

run on a directory containing the files file, file.c, file.lst, and myfile would list the files file.c and file.lst. However,::

	$ ls file.?

run on the same directory would only list file.c because the ? only matches one character, no more, no less. This can save you a great deal of typing time. For example, if there is a file called california_cornish_hens_with_wild_rice and no other files whose names begin with 'c', you could view the file without typing the whole name by typing this::

	$ more c*

because the c* matches that long file name.

filenames containing metacharacters can pose many problems and should never be intentionally created.




grep
-----

*grep* is a command line text search utility originally written for Unix. The name is taken from the first letters in *global / regular expression / print*, a series of instructions for the *ed* text editor. The *grep* command searches files or standard input globally for lines matching a given regular expression, and prints them to the program's standard output.

Usage
~~~~~~

This is an example of a common *grep* usage:
::

	$ grep apple fruitlist.txt

In this case, *grep* prints all lines containing 'apple' from the file *fruitlist.txt*, regardless of word boundaries; therefore lines containing 'pineapple' or 'apples' are also printed. The *grep* command is case sensitive by default, so this example's output does not include lines containing 'Apple' (with a capital A) unless they also contain 'apple'.

Like most Unix commands, *grep* accepts command line arguments to change this and many other behaviors. For example:
::

	$ grep -i apple fruitlist.txt

This prints all lines containing 'apple' regardless of capitalization. The '-i' argument tells *grep* to be case insensitive, or to ignore case.

To print all lines containing 'apple' as a word ('pineapple' and 'apples' will not match):
::

	$ grep -w apple fruitlist.txt

Regular expressions can be used to match more complicated queries.

Variations
+++++++++++

There are countless implementations and derivatives of *grep* available for many operating systems. Early variants of *grep* included *egrep* and *fgrep*. The former applies an extended regular expression syntax that was added to Unix after Ken Thompson's original regular expression implementation. The latter searches for any of a list of 'fixed' strings using the Aho-Corasick algorithm. These variants are embodied in most modern *grep* implementations as command-line switches (and standardized as -E and -F in POSIX). In such combined implementations, *grep* may also behave differently depending on the name by which it is invoked, allowing *fgrep*, *egrep*, and *grep* to be links to the same program.

*pcregrep* is an implementation of *grep* that uses Perl regular expression syntax.

Other commands contain the word 'grep' to indicate that they search (usually for regular expression matches). The *pgrep* utility, for instance, displays the processes whose names match a given regular expression.


Elementary Regex
=================

In computing, regular expressions provide a concise and flexible means for identifying strings of text of interest, such as particular characters, words, or patterns of characters. A regular expression (often shortened to regex or regexp) is written in a formal language that can be interpreted by a regular expression processor, a program that either serves as a parser generator or examines text and identifies parts that match the provided specification.

Regular expressions are used by many text editors, utilities, and programming languages to search and manipulate text based on patterns. For example, Perl, Ruby and Tcl have a powerful regular expression engine built directly into their syntax. Several utilities provided by Unix distributions—including the editor *ed* and the filter *grep* — were the first to popularize the concept of regular expressions.


Regular Expressions are a feature of UNIX. They describe a pattern to match, a sequence of characters, not words, within a line of text. Here is a quick summary of the special characters used in the grep tool and their meaning: 

* ^ (Caret)        =    match expression at the start of a line, as in ^A.
* $ (Question)     =    match expression at the end of a line, as in A$.
* \ (Back Slash)   =    turn off the special meaning of the next character, as in \^.
* [ ] (Brackets)   =    match any one of the enclosed characters, as in [aeiou].
                      Use Hyphen "-" for a range, as in [0-9].
* [^ ]             =    match any one character except those enclosed in [ ], as in [^0-9].
* . (Period)       =    match a single character of any value, except end of line.
* * (Asterisk)     =    match zero or more of the preceding character or expression.
* \{x,y\}          =    match x to y occurrences of the preceding.
* \{x\}            =    match exactly x occurrences of the preceding.
* \{x,\}           =    match x or more occurrences of the preceding.



Here are some examples using grep:

*    grep smug files         {search files for lines with 'smug'}
*    grep '^smug' files      {'smug' at the start of a line}
*    grep 'smug$' files      {'smug' at the end of a line}
*    grep '^smug$' files     {lines containing only 'smug'}
*    grep '\^s' files        {lines starting with '^s', "\" escapes the ^}
*    grep '[Ss]mug' files    {search for 'Smug' or 'smug'}
*    grep 'B[oO][bB]' files  {search for BOB, Bob, BOb or BoB }
*    grep '^$' files         {search for blank lines}
*   grep '[0-9][0-9]' file  {search for pairs of numeric digits}




Lazy quantification
--------------------

The standard quantifiers in regular expressions are greedy, meaning they match as much as they can, only giving back as necessary to match the remainder of the regex. For example, someone new to regexes wishing to find the first instance of an item between < and > symbols in this example:
::

	Another whale explosion occurred on <January 26>, <2004>.

...would likely come up with the pattern <.*>, or similar. However, this pattern will actually return "<January 26>, <2004>" instead of the "<January 26>" which might be expected, because the `*` quantifier is greedy — it will consume as many characters as possible from the input, and "January 26>, <2004" has more characters than "January 26".

Though this problem can be avoided in a number of ways (e.g., by specifying the text that is not to be matched: <[^>]*>), modern regular expression tools allow a quantifier to be specified as *lazy* (also known as non-greedy, reluctant, minimal, or ungreedy) by putting a question mark after the quantifier (e.g., <.*?>), or by using a modifier which reverses the greediness of quantifiers (though changing the meaning of the standard quantifiers can be confusing). By using a lazy quantifier, the expression tries the minimal match first. Though in the previous example lazy matching is used to select one of many matching results, in some cases it can also be used to improve performance when greedy matching would require more backtracking.

One Liners
===========

A *one-liner* is textual input to the command-line of an operating system shell that performs some function in just one line of input.

The one liner can be

   1. An expression written in the language of the shell.
   2. The invocation of an interpreter together with program source for the interpreter to run.
   3. The invocation of a compiler together with source to compile and 	  
      instructions for executing the compiled program.

Certain dynamic scripting languages such as AWK, sed, and perl have traditionally been adept at expressing one-liners. Specialist shell interpreters such as these Unix shells or the Windows PowerShell, allow for the construction of powerful one-liners.

The use of the phrase one-liner has been widened to also include program-source for any language that does something useful in one line.



Here is a one line shell script to show directories:

::

      $grep user * | cut -d":"  -f1|uniq

This returns list of all files which has the word user in it .


Environment Variables:
======================

These variables like HOME, OSTYPE,Variables are a way of passing information from the shell to programs when you run them. Programs look "in the environment" for particular variables and if they are found will use the values stored. Standard UNIX variables are split into two categories, environment variables and shell variables. In broad terms, shell variables apply only to the current instance of the shell and are used to set short-term working conditions; environment variables have a farther reaching significance, and those set at login are valid for the duration of the session.By convention, environment variables have UPPER CASE and shell variables have lower case names.  

Some of examples of Environment variables are: ::

   $ echo $OSTYPE 
   linux-gnu
   $ echo $HOME
   /home/user 

To see all the variables and there values use any of following commands: ::

   $ printenv | less
   $ env

The most commonly used environment variable is "PATH", it defines a list of directories to search through when looking for a command to execute. If you decide to put your own programs in a bin directory under your home directory, you'll have to modify the path to include that directory, or the system will never find your programs (unless you happen to be in that directory when you enter the command). Here's how to change your PATH variable so it includes your personal bin directory: ::

   $ set PATH=$PATH:$HOME/bin

See the difference in value of PATH variable before and after modifying it. One can also create its own variable to make things easier: ::

   $ set repo = $HOME/Desktop/random/code
   $ cd $repo

*set* command is used to define a variable for the current shell. Try opening a new shell and use the above mentioned command, it wont work as expected. The other child process wont be able to see these variables unless we *export* them. Repeat the above mentioned activity with *export* command. Now with all new shells, *$repo* will work.





Shell Scripting:
================

Basics:
-------

Shell program or shell script,a sequence of commands to a text file and tell the shell to execute the text file instead of entering the commands. The first *"Hello World"* sample for shell scripting is as easy as it sounds: ::

   $ echo '#!/bin/sh' > my-script.sh
   $ echo 'clear' >> my-script.sh   
   $ echo 'echo Hello World' >> my-script.sh
   $ chmod 755 my-script.sh
   $ ./my-script.sh
   Hello World

The #! syntax(also known as shebang) is used in scripts to indicate an interpreter for execution under UNIX / Linux operating systems. The chmod is required to make the script executable. This script will just execute two commands, *clear* and *echo* one after another. One can also do the same task using a one liner command *clear; echo 'Hello World';* but as number of lines grows using a script file is helpful. 

So lets create a script which gives us all the filenames for given initial alphabet or string in a directory. Let the name of script be *initial.sh*, open it with text editor, and write: ::

   #!/bin/sh
   ls > temp
   grep ^$1 < temp
   rm temp
   $ chmod a+x initial.sh
   $ ./initial.sh s

The $1 in the script is pertaining to command line argument. All arguments passed via command line are accessed via *$#* with name of script being first member, that is $0. Now lets write a script for finding a file, and then checking when was it last modified: ::

   #!/bin/sh
   name=`find . -name $1 -print`
   echo $name
   last_modified=`stat -c %y $name| cut -f 1 -d " "`
   echo "Last modified: $last_modified"    
   $ ./search.sh fname

Try giving some file you want to search in place of fname. Please note in second line *`* its a back-quote(other key mapped with tilda), it is specifically used to get the output of one command into a variable. In this particular case name is a User defined variables  which stores the value. We access value stored in any variable using *$* symbol before name of variable.



Shell Arithmetic:
-----------------

Shell also provides support for basic arithmetic operations. The syntax is: ::

   $ expr op1 math-operator op2

Some of example which can be tried handily: ::
   
   $ expr -3 + 5
   2
   $ expr 10 % 3
   1

These spaces in between operator and operands is important, without them shell interpreter will raise the syntax error. ::

   $ expr 2*3
   expr: syntax error
   
One can use back-quotes(`) also to get value of expr. ::

   $ echo `expr 6 + 3`
   9
   $ result=`expr 6 + 3`
   $ echo $result
   9

Shell uses three kinds of quotes. Double quotes("), anything enclosed among them except from variable trailing after $, and characters after \ would be printed as it is. Single quotes('), anything enclosed within them is just same, no formulation/interpretation. Back quotes(`), anything inclosed is considered as command, or is executed. ::

   $ echo "Today is date"
   Today is date
   $ echo "Today is `date`"
   Today is Wed Sep 16 17:32:22 IST 2009
   $ echo 'Today is `date`'
   Today is `date`
   $ echo "Today is \n `date`"
   Today is \n Wed Sep 16 17:40:13 IST 2009
   $ echo -e "Today is \n `date`"
   Today is 
    Wed Sep 16 17:41:13 IST 2009 

if else construct:
------------------

One can have simple *if else if* constructs in shell scripts to check conditions. Lets take simple example of writing a script which returns back whether the argument passed is positive or not: ::

   #!/bin/sh
   if test $1 -gt 0
   then
     echo "number is positive"
   else
     echo "number is negative"
   fi
   $ ./sign.sh -11
   number is negative

This script will compare the first value passed as argument with 0 *if test var -gt val*, var being $1 and val being 0, gt meaning greater then. Now this program has some flaw, it will give same result for following input: (-11) and (-1, 5), as we are checking just $1 which is first argument and hence the result. For handling such situation we can include *if-else* clause which will warn user of correct usage of script. ::

   #this is the case when no argument is passed  
   if [ $# -eq 0 ]
   then
     echo "$0 : You must give/supply one integers"
     exit 1
   else 
     if [ $# -gt 1 ]
     then
       echo "$0 : You must give one integer"
       exit 1
     fi
   fi

One important thing to note in shell script is spacing, with many comparison and evaluation operation a wrongly placed space will spoil all the fun. So in previous example the expression *[ $# -eq 0 ]* will work properly, but if we remove those leading or trailing spaces like *[ $# -eq 0]*, it wont work as expected, or rather throw a warning. Both *test* and *[]* do the same task of testing a expression and returning true or false.

Lets create something interesting using these if-else clause. Now we will create a script which will greet the user when he opens the shell. We will create the script, change the permission to make it executable and append the *.bashrc* file with *./greet.sh* line and we are done. The script is: ::

   #!/bin/sh
   #Script to greet the user according to time of day
   temph=`date | cut -c12-13`
   dat=`date +"%A %d in %B of %Y (%r)"`
   if [ $temph -lt 12 ]
   then
     mess="Good Morning $LOGNAME, Have a nice day!"
   fi

   if [ $temph -gt 12 -a $temph -le 16 ]
   then
     mess="Good Afternoon $LOGNAME"
   fi

   if [ $temph -gt 16 -a $temph -le 18 ]
   then
     mess="Good Evening $LOGNAME"
   fi
   echo -e "$mess\nThis is $dat"

For me when I open the shell the output is something like: ::

   Good Morning user, Have a nice day!
   This is Wednesday 16 in September of 2009 (11:54:47 AM IST) 

Loops
-----

Bash has three different commands for looping -- ``for``, ``while`` and ``until``. 

``for`` loop
~~~~~~~~~~~~

Suppose we have a set of files, that have names beginning with numbers followed by their names - ``08 - Society.mp3``. We would like to rename these files to remove the numbering. How would we go about doing that? It is clear from the problem statement that we could use a ``for`` loop, to loop through the list of files and rename each of the files.  

Let's first look at a simple ``for`` loop, to understand how it works. 
::

  for animal in rat cat dog man
  do 
    echo $animal
  done

We just wrote a list of animals, each animal's name separated by a space and printed each name on a separate line. The variable ``animal`` is a dummy variable and has no significance. You could use something as lame as ``i`` in place of ``animal``.  

Now, we use a simple ``for`` loop to list the files that we are interested in. 
::

  ls *.mp3 > list
  for i in `cat list`
  do
    echo "$i"
  done

If your filenames contain spaces, ``for`` assumes each space separated word to be a single item in the list and prints it in a separate line. We could change the script slightly to overcome this problem. 
::

  for i in *.mp3
  do
    echo "$i"
  done

Now, we have each file printed on a separate line. Depending on the files that we have we could use grep to get the relevant portion of the filenames and rename the files. 
::

  for i in *.mp3
  do 
    j=$(echo "$i"|grep -o "[A-Za-z'&. ]*.mp3")
    echo "$i -> $j"
  done

Now we just replace the echo command with a ``mv``  command. 
::

  for i in *.mp3
  do 
    j=$(echo "$i"|grep -o "[A-Za-z'&. ]*.mp3")
    mv "$i" "$j"
  done



``while``
~~~~~~~~~

The ``while`` command allows us to continuously execute a block of commands until the command that is controlling the loop is executing successfully. 

Let's start with the lamest example of a while loop.
::

  while true
  do
    echo "True"
  done

This, as you can see, is an infinite loop that prints the ``True``. 

Say we wish to write a simple program that takes user input and prints it back, until the input is ``quit``, which quits the program. 
::

  while [ "$variable" != "quit" ]
  do
    read variable
    echo "Input - $variable"
  done
  exit 0

``until``
~~~~~~~~~

The ``until`` loop is similar to the ``while`` loop, except that it executes until the conditional command does not execute properly. 

The infinite loop changes to the following, when ``until`` is used.
::

  until false
  do
    echo "True"
  done

Now lets try and use these above mentioned options provided by shell to write a utility. Until now, when we try find or locate it looks through directories and files for result. But they wont search through tar archives and zipped files. Lets create a shell script for especially looking through these files
::

  #!/bin/sh

  #To check number of arguments being passed.
  if [ $# -eq 0 ] ; then
  echo "Correct usage: $0 tar-archive filename \nOr $0 filename"
  exit 1
  else
    if [ $# -eq 1 ] ; then
      tar_archive=`find $PWD -name "*.tar*"`
    else
      tar_archive=`find $PWD -name $1`
    fi
  fi

  #Search of particular file inside archives.
  for archive in $tar_archive
  do
    echo $archive
    variable=`tar -tf $archive`
    for word in $variable
    do
      if [ $# -eq 1 ] ; then
        echo "$word" | grep -q ".*$1"
      else
	echo "$word" | grep -q ".*$2"
      fi
    if [ $? -eq 0 ] ; then 
      echo "File present in $archive!" 
    fi  
    done
  done


Functions
---------

When a group of commands are repeatedly being used within a script, it is convenient to group them as a function. This saves a lot of time and you can avoid retyping the code again and again. Also, it will help you maintain your code easily. Let's see how we can define a simple function, ``hello-world``. Function can be defined by using function name followed by a pair of parentheses. 
::

  
  hello-world () {
    echo "Hello, World.";
  }

  $ hello-world
  Hello, World.

Passing parameters to functions is similar to passing them to scripts. 
::


  #! /bin/bash

  hello-name()
  {
     echo  "hello ". $1
        
  }

  hello-name $1


  #!usr/bin/bash
  hello-name
  { 
  echo "Hello, $1."; 
  }

  hello-name $1

  save this in a file helloscipt.sh and give it execute permission
  

  $ ./helloscipt 9
  Hello, 9.

Any variables that you define within a function, will be added to the global namespace. If you wish to define variables that are restricted to the scope of the function, define a variable using the ``local`` built-in command of bash.

  
We shall now write a function for the word frequency generating script that we had looked at in the previous session. 

::

  word_frequency() {
    if [ $# -ne 1 ]
    then
      echo "Usage: $0 file_name"
      exit 1
    else 
      if [ -f "$1" ]
      then
        grep  "[A-Za-z]*" -o "$1" | tr 'A-Z' 'a-z' | sort | uniq -c | sort -nr | less
      fi
    fi
  }

 word_frequency  $1



	

