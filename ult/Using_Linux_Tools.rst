Introducing Linux
=================

We are here to welcome you to Linux. GNU/Linux is an operating system that is similar to the UNIX operating system, but is open source software. Being an open source program means that (if you wanted to) you could view the source code of the operating system and change it to suit your needs. 

The name "Linux" properly refers to an operating system "kernel", a single but key component of a complete operating system. In everyday use, the term "Linux" is frequently used to refer to a complete operating system which consists of the kernel and some of the thousands of other programs required to make an operating system useful. Much of the important system software that is typically installed on a Linux system comes from The GNU Project, a project to build an operating system made entirely of free software.
The first Linux kernel was created by Linus Torvalds. It was started as an x86-only, single processor operating system, but grew to become one of the most ported pieces of software. Other parts of a complete GNU/Linux system come from other projects such as the GNU project, and are integrated into a complete GNU/Linux OS by your supplier. Usually your supplier will assign their own version number to the integrated whole.This collection of the kernal and programs maintained by vendor is called distro or distribution.
The GNU Project is overseen by the Free Software Foundation. The Free Software Foundation was founded by Richard Stallman. Stallman believes that the people should use the term "GNU/Linux" to refer to such an operating system, because so many of the required programs were in fact, written as part of the GNU Project.



Design and Implications
------------------------

A Linux-based system is a modular Unix-like operating system, deriving much of its basic design from principles established in Unix earlier. Such a system uses a monolithic kernel, called the Linux kernel, which handles process control, networking, and peripheral and file system access. Device drivers are integrated directly with the kernel. Separate projects that interface with the kernel provide much of the system's higher-level functionality. The GNU userland is an important part of most Linux-based systems, providing the most common implementation of the C library, a popular shell, and many of the common Unix tools which carry out many basic operating system tasks. The graphical user interface (or GUI) used by most Linux systems is based on the "X Window System".





Reasons for Using Linux
-----------------------
- Linux is free:

As in "free beer". Linux can be downloaded in its entirety from the Internet completely for free. No registration fees, no costs per user, free updates, and freely available source code in case you want to change the behavior of your system.
Most of all, Linux is free as in "free speech":


- Linux is portable to any hardware platform:

A vendor, who wants to sell a new type of computer and who does not know what kind of OS his/her new machine will run, can take a Linux kernel and make it work on his/her hardware, because documentation related to this activity is freely available.

- Linux was made to keep on running:

As with UNIX, a Linux system expects to run without rebooting all the time. That is why a lot of tasks are being executed at night or scheduled automatically for other times, resulting in higher availability during busier periods and a more balanced use of the hardware. This property allows for Linux to be applicable to environments where people do not have the time or the possibility to control their systems constantly.

- Linux is secure and versatile:

The security model used in Linux is based on the UNIX idea of security, which is known to be robust and of proven quality. But Linux is not only safe from attacks from the Internet: it will adapt equally to other situations, utilizing the same high standards for security.

- Linux is scalable:

From a Palmtop with 2 MB of memory to a petabyte storage cluster with hundreds of nodes: add or remove the appropriate packages and Linux fits all. 



Getting Started
================

Logging in, activating the user interface and logging out
----------------------------------------------------------
In order to work on a Linux system directly, one needs to provide a user name and password. You always need to authenticate to the system. Most PC−based Linux systems have two basic modes for a system to run in: either quick and clean in text console mode,which includes with mouse, multitasking and multi−user features, or in graphical console mode.



When you see the login screen again, asking to enter user name and password, logout was successful.


Basic Commands
===============

ls
---

*ls* lists the files in the current working directory. A directory that is not the current working directory can be specified and ls will list the files there.::


	$ ls
	jeeves.rst psmith.html blandings.html

cd
---

This stands for "change directory". When one wants to change the directory .

       $cd Music 

One dot '.' represents the current directory while two dots '..' represent the parent directory.

“ cd -” will return you to the previous directory (a bit like an “undo”).

You can also use cd absolute path or cd relative path (see below):

Absolute paths:

    An “ absolute path” is easily recognised from the leading forward slash, /. The / means that you start at the top level directory and continue down.

For example to get to /boot/grub you would type::

	$cd /boot/grub

This is an absolute path because you start at the top of the hierarchy and go downwards from there (it doesn't matter where in the filesystem you were when you typed the command).

Relative paths:

    A “ relative path” doesn't have a preceding slash. Use a relative path when you start from a directory below the top level directory structure. This is dependent on where you are in the filesystem.

    For example if you are in root's home directory and want to get to /root/music, you type::

	$ cd music

Please note that there is no / using the above cd command. Using a / would cause this to be an absolute path, working from the top of the hierarchy downward.

who
----

The standard Unix command *who* displays a list of users who are currently logged into a computer.

The *who* command is related to the command *w*, which provides the same information but also displays additional data and statistics.::

	$who
	beeblebrox tty7         2009-09-08 10:50 (:0)
	beeblebrox pts/0        2009-09-08 11:25 (:0.0)
	dumbledore pts/1        2009-09-08 18:11 (potter.xyz.in)
	beeblebrox pts/2        2009-09-08 18:53 (:0.0)


The command can be invoked with the arguments *am i* or *am I* (so it is invoked as *who am i* or * who am I*), showing information about the current terminal only (see the *-m* option below, of which this invocation is equivalent).



mkdir
-----

This command is used to make a new directory. Normal usage is as straightforward as follows::

	$mkdir name_of_directory

Where *name_of_directory* is the name of the directory one wants to create. When typed as above (ie. normal usage), the new directory would be created within the current directory. On Unix, multiple directories can be specified, and *mkdir* will try to create all of them.




pwd
----
pwd is a Linux / Unix command which prints the current working directory. If you wish to know the full path of the  directory in which you are in from the Linux console, then the pwd command will come to your rescue. pwd stands for Print Working Directory.

pwd have one option called -P, which lists the current working directory with all the links resolved.

Usage of pwd command

I have a directory called "Examples/" on my machine which is actually a soft link to the directory /usr/share/example-content/. 

I move into the "Examples" directory and run the pwd command to get the following output.

$ cd Examples
$ pwd
/home/laf/Examples


FLAGS
~~~~~
The standard commands in Linux have a lot of options also called flags to change or provide some additional functionality to the command For example ::
      
       $ls -l 
       
       * *ls with flag -l* displays the result in long format, displaying Unix file types, permissions, number of hard links, owner, group, size, date, and filename



Getting Help
============

apropos and whatis
-------------------

This is a command to search the manual pages files in Unix and Unix-like operating systems. ::

	$ apropos grep
	egrep       egrep (1)       Search a file for a pattern using full regular expressions
	fgrep       fgrep (1)       Search a file for a fixed-character	string
	fmlgrep     fmlgrep (1)     Search a file for a pattern
	grep        grep (1)        Search a file for a pattern
	gzgrep      gzgrep (1)      Search a possibly compressed file for a regular expression
	nisgrep     nismatch (1)    Utilities for searching NIS+ tables
	pgrep       pgrep (1)       Find or signal a process by name or other attribute
	zgrep       zgrep (1)       Search a possibly compressed file for a regular expression
	...

In this example, the user uses *apropos* to search for the string "grep", and apropos returns the indicated *man* pages that include the term "grep".

A short index of explanations for commands is available using the *whatis* command, like in the examples below::

	$whatis ls
	ls (1) 		 - list directory contents

This displays short information about a command, and the first section in the collection of man pages that contains an appropriate page.

If you don't know where to get started and which man page to read, *apropos* gives more information. Say that you do not know how to start a browser, then you could enter the following command::

	$apropos browser
	gmusicbrowser (1)    - Jukebox for large collections of audio files
	infobrowser (1)      - read Info documents
	libsmbclient (7)     - An extension library for browsers and that 		can be used...
	opera (1)            - a standards-compliant graphical Web browser
	sensible-browser (1) - sensible editing, paging, and web browsing
	smbtree (1)          - A text based smb network browser
	tvtk_doc (1)         - A GUI based TVTK documentation search browser.
	viewres (1)          - graphical class browser for Xt
	w3m (1)              - a text based Web browser and pager
	www-browser (1)      - a text based Web browser and pager
	...

man
----

Man pages (short for "manual pages") are the extensive documentation that comes preinstalled with almost all substantial Unix and Unix-like operating systems. The Unix command used to display them is *man*. Each page is a self-contained document.

To read a manual page for a Unix command, one can use::

	$ man <command_name>

at a shell prompt; for example, "man ftp". In order to simplify navigation through the output, *man* generally uses the less terminal pager.

To see the manual on man itself do::

	$man man

The previous example will take you to the "Manual" page entry about manual pages!


info
-----

*info* is a software utility which forms a hypertextual, multipage documentation and help viewer working on a command line interface, useful when there is no GUI available.

The syntax is ::
	
	$ info <command_name>

*info* processes info files, which are Texinfo formatted files, and presents the documentation as a tree, with simple commands to traverse the tree and to follow cross references. For instance

    - *n* goes to the next page.
    - *p* goes to the previous page.
    - *u* goes to the upper page.
    - *l* goes to the last(visited) node
    - To follow a cross reference, the cursor can be moved over a link (a word preceded by a `*`) and enter pressed.

info was initially written for use with GNU/Linux and then ported to other Unix-like operating systems.

--help
-------

Most GNU commands support the --help, which gives a short explanation about how to use the command and a list of available options. Below is the output of this option with the *cat* command::

	$ userprompt@host: cat --help
	Usage: cat [OPTION] [FILE]...
	Concatenate FILE(s), or standard input, to standard output.

	  -A, --show-all           equivalent to -vET
	  -b, --number-nonblank    number nonempty output lines
	  -e                       equivalent to -vE
	  -E, --show-ends          display $ at end of each line
	  -n, --number             number all output lines
	  -s, --squeeze-blank      suppress repeated empty output lines
	  -t                       equivalent to -vT
	  -T, --show-tabs          display TAB characters as ^I
	  -u                       (ignored)
	  -v, --show-nonprinting   use ^ and M- notation, except for LFD and 		  TAB
	  --help     display this help and exit
      	  --version  output version information and exit

	With no FILE, or when FILE is -, read standard input.

	Examples:
	  cat f - g  Output f's contents, then standard input, then g's 	  contents.
	  cat        Copy standard input to standard output.

	Report bugs to <bug-coreutils@gnu.org>.



Basic file handling
===================

cp
---

*cp* is the command entered in a Unix shell to copy a file from one place to another, possibly on a different filesystem. The original file remains unchanged, and the new file may have the same or a different name.

Usage
~~~~~

To copy a file to another file::

	$ cp  SourceFile TargetFile

To copy a file to a directory::

	$ cp  SourceFile  TargetDirectory
 
To copy a directory to a directory::

	$ cp  -r SourceDirectory  TargetDirectory

Flags
~~~~~


*-P* – makes the cp command copy symbolic links. The default is to follow symbolic links, that is, to copy files to which symbolic links point.

*-i* (interactive) – prompts you with the name of a file to be overwritten. This occurs if the TargetDirectory or TargetFile parameter contains a file with the same name as a file specified in the SourceFile or SourceDirectory parameter. If you enter y or the locale's equivalent of y, the cp command continues. Any other answer prevents the cp command from overwriting the file.

*-p* (preserve) – duplicates the following characteristics of each SourceFile/SourceDirectory in the corresponding TargetFile and/or TargetDirectory:

    * The time of the last data modification and the time of the last access.
    * The user ID and group ID (only if it has permissions to do this)
    * The file permission bits and the SUID and SGID bits.

*-R* (recursive) – copy directories (recursively copying all the contents)

Examples
~~~~~~~~

To make a copy of a file in the current directory, enter::

    $ cp prog.c prog.bak

This copies prog.c to prog.bak. If the prog.bak file does not already exist, the cp command creates it. If it does exist, the cp command replaces it with a copy of the prog.c file.

To copy a file in your current directory into another directory, enter::

    $ cp zaphod /home/books/hhgg

This copies the jones file to /home/books/hhgg/zaphod.

To copy a file to a new file and preserve the modification date, time, and access control list associated with the source file, enter::

    $ cp -p martin_luther_king martin_luther_king.jr

This copies the *martin_luther_king* file to the *martin_luther_king.jr* file. Instead of creating the file with the current date and time stamp, the system gives the *martin_luther_king.jr* file the same date and time as the *martin_luther_king* file. The *martin_luther_king.jr* file also inherits the *martin_luther_king* file's access control protection.

To copy all the files in a directory to a new directory, enter::

    $ cp /home/galactica/clients/* /home/hhgg/customers

This copies only the files in the clients directory to the customers directory.

To copy a directory, including all its files and subdirectories, to another directory, enter:

    $ cp -R /home/hhgg/clients /home/hhgg/customers

This copies the clients directory, including all its files, subdirectories, and the files in those subdirectories, to the customers/clients directory.

To copy a specific set of files of any extension to another directory, enter::

    $ cp zaphod arthur ford /home/hhgg/clients

This copies the *zaphod*, *arthur*, and *ford* files in your current working directory to the /home/hhgg/clients directory.

To use pattern-matching characters to copy files, enter::

    $ cp programs/*.py .

This copies the files in the programs directory that end with *.py* to the current directory, signified by the single "." (dot). You must type a space between the *py* and the final dot.

mv
---

*mv* (short for move) is a Unix command that moves one or more files or directories from one place to another. The original file is deleted, and the new file may have the same or a different name. If possible (i.e. when the original and new files are on the same file system), *mv* will rename the file instead. Write permission is required on all directories being modified.

Conflicting existing file
~~~~~~~~~~~~~~~~~~~~~~~~~~

In all cases, when a file is moved to have the name of an existing file (in the same directory), the existing file is deleted. If the existing file is not writable but is in a directory that is writable, then the mv command asks for confirmation if possible (i.e. if run from a terminal) before proceeding, unless the -f (force) option is used.

Differences with copy and delete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note that, usually, when moving files within the same volume, moving (and/or renaming) is not the same as simply copying and then deleting the original. When moving a file, the link is simply removed from the old parent directory and added to the new parent directory. However, the file itself is untouched (i.e. it has the same inodes and resides at the same place on the disk). For example, you cannot copy a file you cannot read, but you can move (and/or rename) it (provided you have write permission to its old and new parent directories). Also, suppose there is a non-empty directory you do not have write permission to. You cannot delete this directory (since you cannot delete its contents); but you can move (and/or rename) it. Also, since moving between filenames on a single volume does not involve copying, it is faster and does not place strain of lots of reads and writes on the disk. Moving files across different volumes, however, does necessitate copying and deleting.

Examples
~~~~~~~~
::

	$ mv myfile mynewfilename    renames a file
	$ mv myfile /myfile          moves 'myfile' from the current 		directory to the root directory
	$ mv myfile dir/myfile       moves 'myfile' to 'dir/myfile' relative 		to the current directory
	$ mv myfile dir              same as the previous command (the 		filename is implied to be the same)
	$ mv myfile dir/myfile2      moves 'myfile' to dir and renames it to 		'myfile2'
	$ mv foo bar baz dir         moves multiple files to directory dir
	$ mv --help                  shows a very concise help about the 		syntax of the command
	$ man mv                     prints an extensive user manual for 		'mv' in the terminal

In all cases, the file or files being moved or renamed can be a directory.

Note that when the command is called with two arguments (as *mv name1 name2* or *mv name1 /dir/name2*), it can have three different effects, depending on whether *name2* does not exist, is an existing file, or is an existing directory. If the user intends to refer to an existing directory, */.* (or in some Unix versions */* is sufficient) may be appended to the name to force the system to check this. To move a file to a new directory, the directory must be created first.

rm
---

*rm* (short for "remove") is one of several basic Unix command lines that operates on files. It is used to delete files from a filesystem. The data is not actually destroyed. Only the index listing where the file is stored is destroyed, and the storage is made available for reuse. There are undelete utilities that will attempt to reconstruct the index and can bring the file back if the parts were not reused.

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

*rm* is often aliased to "rm -i" so as to avoid accidental deletion of files. If a user still wishes to delete a large number of files without confirmation, they can manually cancel out the -i argument by adding the -f option (as the option specified later on the expanded command line "rm -i -f" takes precedence).

*rm -rf* (variously, rm -rf /, rm -rf `*`, and others) is frequently used in jokes and anecdotes about Unix disasters. The rm -rf variant of the command, if run by a superuser on the root directory, would cause the contents of every writable mounted filesystem on the computer to be deleted.

*rm* is often used in conjunction with xargs to supply a list of files to delete::

	xargs rm < filelist

When *rm* is used on a symbolic link, it deletes the link, but does not affect the target of the link.

Permissions
~~~~~~~~~~~
Linux is a proper multi-user environment. In a multi-user environment, security of user and system data is very important. Access should be given only to users who need to access the data. Since Linux is essentially a server OS, good and efficient file security is built right . The permissions are based on whether one is allowed to read, write or execute a file.

Usually, on most filesystems, deleting a file requires write permission on the parent directory (and execute permission, in order to enter the directory in the first place). (Note that, confusingly for beginners, permissions on the file itself are irrelevant. However, GNU rm asks for confirmation if a write-protected file is to be deleted, unless the -f option is used.)

To delete a directory (with rm -r), one must delete all of its contents recursively. This requires that one must have read and write and execute permission to that directory (if it's not empty) and all non-empty subdirectories recursively (if there are any).





Basic Text Processing
======================

head
-----

*head* is a program on Unix and Unix-like systems used to display the first few lines of a text file or piped data. The command syntax is::

	$ head [options] <file_name>

By default, *head* will print the first 10 lines of its input to the standard output. The number of lines printed may be changed with a command line option. The following example shows the first 20 lines of filename::

	$ head -n 20 filename

This displays the first 5 lines of all files starting with *foo*::

	$ head -n 5 foo*



Flags
~~~~~
::

	-c <x number of bytes> Copy first x number of bytes.


tail
----

*tail* is a program on Unix and Unix-like systems used to display the last few lines of a text file or piped data.

The command-syntax is::

	$ tail [options] <file_name>

By default, *tail* will print the last 10 lines of its input to the standard output. With command line options the number of lines printed and the printing units (lines, blocks or bytes) may be changed. The following example shows the last 20 lines of filename::

	$ tail -n 20 filename

This example shows the last 15 bytes of all files starting with *foo*::

	$ tail -c 15 foo*

This example shows all lines of filename from the second line onwards::

	$ tail -n +2 filename



File monitoring
~~~~~~~~~~~~~~~

*tail* has a special command line option *-f* (follow) that allows a file to be monitored. Instead of displaying the last few lines and exiting, tail displays the lines and then monitors the file. As new lines are added to the file by another process, tail updates the display. This is particularly useful for monitoring log files. The following command will display the last 10 lines of messages and append new lines to the display as new lines are added to messages::

	$ tail -f /var/adm/messages

To interrupt tail while it is monitoring, break-in with *Ctrl+C*. This command can be run "in the background" with &, see job control.

If you have a command's result to monitor, you can use the *watch* command.


cut
----

In computing, *cut* is a Unix command line utility which is used to extract sections from each line of input — usually from a file.

Extraction of line segments can typically be done by *bytes (-b), characters (-c)*, or *fields (-f)* separated by a *delimiter (-d — the tab character by default)*. A range must be provided in each case which consists of one of N, N-M, N- (N to the end of the line), or -M (beginning of the line to M), where N and M are counted from 1 (there is no zeroth value). Since version 6, an error is thrown if you include a zeroth value. Prior to this the value was ignored and assumed to be 1.

Assuming a file named file containing the lines::

	foo:bar:baz:qux:quux
	one:two:three:four:five:six:seven
	alpha:beta:gamma:delta:epsilon:zeta:eta:teta:iota:kappa:lambda:mu

To output the fourth through tenth characters of each line::

	$ cut -c 4-10 file

This gives the output::

	:bar:ba
	:two:th
	ha:beta

To output the fifth field through the end of the line of each line using the colon character as the field delimiter::

	$ cut -d : -f 5- file

This gives the output::

	quux
	five:six:seven
	epsilon:zeta:eta:teta:iota:kappa:lambda:mu

paste
------

*paste* is a Unix command line utility which is used to join files horizontally (parallel merging) by outputting lines consisting of the sequentially corresponding lines of each file specified, separated by tabs, to the standard output. It is effectively the horizontal equivalent to the utility *cat* command which operates on the vertical plane of two or more files.

To paste several columns of data together into the file *www* from files *who*, *where*, and *when*::

	$ paste who where when > www

If the files contain:

+-----------+------------+------------+
|   who     |   where    |    when    |
+===========+============+============+
|  Batman   | GothamCity | January 3  |
+-----------+------------+------------+	
| Trillian  | Andromeda  | February 4 |
+-----------+------------+------------+
|  Jeeves   | London     |  March 19  |
+-----------+------------+------------+	

This creates the file named *www* containing ::

	Batman            GothamCity       January 3
	Trillian          Andromeda        February 4
	Jeeves            London           March 19

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

Filenames containing metacharacters can pose many problems and should never be intentionally created.


Looking At Files
================

cat
---

The *cat* command is a standard Unix program used to concatenate and display files. The name is from "catenate", a synonym of *concatenate*.

The Single Unix Specification specifies the behavior that the contents of each of the files given in sequence as arguments will be written to the standard output in the same sequence, and mandates one option, -u, where each byte is printed as it is read.

If the filename is specified as -, then *cat* will read from standard input at that point in the sequence. If no files are specified, *cat* will read from standard input entered.

Usage ::
        $ cat foo boo
	This is file foo
	
	This is file boo.



more
-----

In computing, *more* is a command to view (but not modify) the contents of a text file one screen at a time (terminal pager). It is available on Unix and Unix-like systems, DOS, OS/2 and Microsoft Windows. Programs of this sort are called pagers.

Usage
~~~~~

The command-syntax is::

	$ more [options] [file_name]

If no file name is provided, *more* looks for input from stdin.

Once *more* has obtained input, it displays as much as can fit on the current screen and waits for user input to advance, with the exception that a form feed (^L) will also cause *more* to wait at that line, regardless of the amount of text on the screen. In the lower-left corner of the screen is displayed the text "--More--" and a percentage, representing the percent of the file that *more* has paged through. (This percentage includes the text displayed on the current screen.) When *more* reaches the end of a file (100%) it exits. The most common methods of navigating through a file are *Enter*, which advances the output by one line, and *Space*, which advances the output by one screen.

There are also other commands that can be used while navigating through the document; consult *more*'s *man* page for more details.



less
-----

*less* is a terminal pager program on Unix, Windows and Unix-like systems used to view (but not change) the contents of a text file one screen at a time. It is similar to *more*, but has the extended capability of allowing both forward and backward navigation through the file. Unlike most Unix text editors/viewers, *less* does not need to read the entire file before starting, resulting in faster load times with large files.

Usage
~~~~~~

*less* can be invoked with options to change its behaviour, for example, the number of lines to display on the screen. A few options vary depending on the operating system. While *less* is displaying the file, various commands can be used to navigate through the file. These commands are based on those used by both *more* and *vi*. It is also possible to search for character patterns in the file.

By default, *less* displays the contents of the file to the standard output (one screen at a time). If the file name argument is omitted, it displays the contents from standard input (usually the output of another command through a pipe). If the output is redirected to anything other than a terminal, for example a pipe to another command, less behaves like cat.

The command-syntax is ::

	$ less [options] file_name

Frequently Used Options
~~~~~~~~~~~~~~~~~~~~~~~

    * -g: Highlights just the current match of any searched string.

    * -I: Case-insensitive searches.

    * -M: Shows more detailed prompt, including file position.

    * -N: Shows line numbers (useful for source code viewing).

    * -S: Disables line wrap ("chop long lines"). Long lines can be seen by side scrolling.

    * -?: Shows help.

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

    * s: Save current content (got from another program like grep) in a file.

    * =: File information.

    * h: Help.

    * q: Quit.



-------------------------------------------------------------------

Examples 
~~~~~~~~~
::

	$ less -M readme.txt                     #Read "readme.txt."
	$ less +F /var/log/mail.log              #Follow mode for log
	$ file * | less                          #Easier file analysis.
	$ grep -i void *.c | less -I -p void     #Case insensitive search 		                                          for "void" in all .c files

Directory Structure
====================

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

ls -l
-----

Shows you huge amounts of information (permissions, owners, size, and when last modified) for folders and files. The syntax is ::

	$ ls -l

This can be done after entering the required directory. 

Permissions and Ownership
=========================

let's check out the file permissions. File permissions are defined
for users, groups and others. User would be the username that you are
logging in as. Further more, users can be organized into groups for better
administration and control. Each user will belong to at least one default
group. Others includes anyone the above categories exclude.

Given below is the result of an 'ls -l'

drwxr-x--- 2 user group 4096 Dec 28 04:09 tmp
-rw-r--r-- 1 user group 969 Dec 21 02:32 foo
-rwxr-xr-x 1 user group 345 Sep 1 04:12 somefile

Relevant information in the first column here is the file type followed by the file permissions. The third and the fourth column show the owner of the file and the group that the file belongs to.The fifth column is no bytes and sixth modification date .The first entry here is tmp. The first character in the first column is 'd', which means the tmp is a directory. The other entries here are files,as indicated by the '-'.

d rwx r-x ---
file type users group others

The next 9 characters define the file permissions. These permissions are given in groups of 3 each. The first 3 characters are the permissions for the owner of the file or directory. The next 3 are permissions for the group that the file is owned by and the final 3 characters define the access permissions for everyone not part of the group. There are 3 possible attributes that make up file access permissions.

r - Read permission. Whether the file may be read. In the case of a directory, this would mean the ability to list the contents of the directory.

w - Write permission. Whether the file may be written to or modified. For a directory, this defines whether you can make any changes to the contents
of the directory. If write permission is not set then you will not be able
to delete, rename or create a file.

x - Execute permission. Whether the file may be executed. In the case of a directory, this attribute decides whether you have permission to enter,run a search through that directory or execute some program from that directory.




chmod
------

The *chmod* command (abbreviated from 'change mode') is a shell command and C language function in Unix and Unix-like environments. When executed, it can change file system modes of files and directories. The modes include permissions and special modes.

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
| X   | special      | which is not a permission in itself but rather |
|     | execute      | can be used instead of 'x'. It applies execute |
|     |              | permissions to directories regardless of their |
|     |              | current permissions and applies execute        |
|     |              | permissions to a file which already has at     |
|     |              | least 1 execute permission bit already set     |
|     |              | (either user, group or other). It is only      |
|     |              | really useful when used with '+' and usually   |
|     |              | in combination with the *-R* option for giving |
|     |              | group or other access to a big directory tree  |
|     |              | without setting execute permission on normal   |
|     |              | files (such as text files), which would        |
|     |              | normally happen if one just used 'chmod -R     |
|     |              | a+rx .', whereas with 'X' one can do 'chmod -R |
|     |              | a+rX .' instead.                               |
+-----+--------------+------------------------------------------------+
| s   | setuid/gid   | are Unix access rights flags that allow users  |
|     |              | to run an executable with the permissions of   |
|     |              | the executable's owner or group.They are often |
|     |              | used to allow users on a computer system to run| 
|     |              | programs with temporarily elevated privileges  | 
|     |              | in order to perform a specific task. While the |
|     |              | assumed user id or group id privileges provided|
|     |              | are not always elevated, at a minimum they are | 
|     |              | specific.They are needed for tasks that require|
|     |              | higher privileges than those which a common    |
|     |              | user has, such as changing his or her login    |  
|     |              | password.                                      |
+-----+--------------+------------------------------------------------+
| t   | sticky       | The most common use of the sticky bit today is |
|     |              | on directories, where, when set, items inside  |
|     |              | the directory can be renamed or deleted only by|
|     |              | the item's owner, the directory's owner, or the| 
|     |              | superuser; without the sticky bit set, any user|
|     |              | with write and execute permissions for the     |
|     |              | directory can rename or delete contained files,| 
|     |              | regardless of owner.                           |
+-----+--------------+------------------------------------------------+

The combination of these three components produces a string that is understood by the chmod command. Multiple changes can be specified by separating multiple symbolic modes with commas.

Symbolic examples
+++++++++++++++++

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

Set the permissions for the *u*ser and the *g*roup to read and execute only (no write permission) on *mydir*.
::

	$ chmod ug=rx mydir
	$ ls -ld mydir
	dr-xr-x---   2 starwars  yoda 96 Dec 8 12:53 mydir

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



Since the *setuid*, *setgid* and *sticky* bits are not set, this is equivalent to:
::

	$ chmod 0664 myfile


chown
~~~~~
The chown command is used to change the owner and group of files, directories and links.

By default, the owner of a filesystem object is the user that created it. The group is a set of users that share the same access permissions (i.e., read, write and execute) for that object.

The basic syntax for using chown to change owners is

    chown -v alice wonderland.txt





Redirection and Piping
=======================

In computing, *redirection* is a function common to most command-line interpreters, including the various Unix shells that can redirect standard streams to user-specified locations.



Redirecting standard input and standard output
-----------------------------------------------

Redirection is usually implemented by placing certain characters between commands. Typically, the syntax of these characters is as follows::

	$ command1 > file1

executes *command1*, placing the output in file1. Note that this will truncate any existing data in *file1*. To append output to the end of the file, use the >> operator.::

	$ command1 < file1

executes *command1*, using *file1* as the source of input (as opposed to the keyboard).::

	$ command1 < infile > outfile

combines the two capabilities: *command1* reads from *infile* and writes to *outfile*

Piping
-------

Programs can be run together such that one program reads the output from another with no need for an explicit intermediate file:
A pipeline of two programs run on a text terminal::

	$ command1 | command2

executes *command1*, using its output as the input for *command2* (commonly called piping, since the "|" character is known as a "pipe").

This is equivalent to using two redirects and a temporary file::

	$ command1 > tempfile
	$ command2 < tempfile
	$ rm tempfile

A good example for command piping is combining *echo* with another command to achieve something interactive in a non-interactive shell, e.g.::

	$ echo -e "user\npass" | ftp localhost

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



Another useful capability is to redirect one standard file handle to another. The most popular variation is to merge standard error into standard output so error messages can be processed together with (or alternately to) the usual output. Example:
::

	$ find / -name .profile > results 2>&1

will try to find all files named *.profile*. Executed without redirection, it will output hits to *stdout* and errors (e.g. for lack of privilege to traverse protected directories) to *stderr*. If standard output is directed to file results, error messages appear on the console. To see both hits and error messages in file results, merge *stderr* (handle 2) into *stdout* (handle 1) using 2>&1 .

It's possible use 2>&1 before ">" but it doesn't work. In fact, when the interpreter reads 2>&1, it doesn't know yet where standard output is redirected and then standard error isn't merged.

If the merged output is to be piped into another program, the file merge sequence 2>&1 must precede the pipe symbol, thus:
::

	$ find / -name .profile 2>&1 | less

A simplified form of the command:
::

	$ command > file 2>&1

is:
::

	$ command &>file

or:
::

	$command >&file

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

More Text Processing
====================

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



