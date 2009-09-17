Introduction to the Course
==========================

Engineering students use computers for a large number of curricular
tasks – mostly computation centred. However, they do not see this as coding or programming tasks and usually are not even aware of the tools and
techniques that will help them to handle these tasks better. This results
in less than optimal use of their time and resources. This also causes
difficulties when it comes tocollaboration and building on other people’s
work. This course is intended to train such students in good software
practices and tools for producing code and documentation.

After successfully completing the program, the participants will be able to:

- understand how software tools work together and how they can be used in tandem to carry out tasks,        
                             
- use unix command line tools to carry out common (mostly text processing tasks,
                                                            
- to generate professional documents,                                

- use version control effectively – for both code and documents,       

- automate tasks by writing shell scripts and python scripts,        

- realise the impact of coding style and readbility on quality,      

- write mid-sized programs that carry out typical engineering / numerical computations such as those that involve (basic) manipulation of large arrays in an efficient manner,                                      

- generate 2D and simple 3D plots,                                   

- debug programs using a standardised approach,

- understand the importance of tests and the philosophy of Test Driven Development,

- write unit tests and improve the quality of code.

Introducing Linux
=================

(Attribution : A significant chunk of the content under this section is based on data from Wikipedia and the Linux Documentation Project)

Linux (usually pronounced ˈlɪnəks') is a generic term referring to Unix-like computer operating systems based on the Linux kernel. The development of the Linux OS is considered the basis for Free and Open Source Software (FOSS) collaboration since typically the underlying source code can be used, modified freely, and redistributed by anyone under the terms of the GNU Global Public License (GPL) and other free software licences.

Linux is installed on a variety of computer hardware, that include mobile phones, embedded devices and supercomputers, but is infamous for its use in servers.

The name "Linux"  comes from the Linux kernel, originally written in 1991 by Linus Torvalds. The rest of the system usually comprises components such as the Apache HTTP Server, the X Window System, the GNOME and KDE desktop environments, and utilities and libraries from the GNU Project (announced in 1983 by Richard Stallman). Commonly-used applications with desktop Linux systems include the Mozilla Firefox web-browser and the OpenOffice.org office application suite. The GNU contribution is the basis for the Free Software Foundation's preferred name GNU/Linux. The kernel's mascot is a penguin named "Tux".

Historical Background
----------------------

Events leading to the creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- The Unix operating system was conceived and implemented in the 1960s and first released in 1970. Its availability and portability caused it to be widely adopted, copied and modified by academic institutions and businesses. Its design became influential to authors of other systems.

- In 1983, Richard Stallman started the GNU project with the goal of creating a free UNIX-like operating system. As part of this work, he wrote the GNU General Public License (GPL). By the early 1990s there was almost enough available software to create a full operating system. However, the GNU kernel, called Hurd, failed to attract enough attention from developers leaving GNU incomplete.

- Another free operating system project in the 1980s was the Berkeley Software Distribution (BSD). This was developed by UC Berkeley from the 6th edition of Unix from AT&T. Since BSD contained Unix code that AT&T owned, AT&T filed a lawsuit (USL v. BSDi) in the early 1990s against the University of California. This strongly limited the development and adoption of BSD.

- MINIX, a Unix-like system intended for academic use, was released by Andrew S. Tanenbaum in 1987. While source code for the system was available, modification and redistribution were restricted. In addition, MINIX's 16-bit design was not well adapted to the 32-bit features of the increasingly cheap and popular Intel 386 architecture for personal computers.

- These factors of a lack of a widely-adopted, free kernel provided the impetus for Torvalds's starting his project. He has stated that if either the GNU or 386BSD kernels were available at the time, he likely would not have written his own.

The Creation of Linux
~~~~~~~~~~~~~~~~~~~~~~
In 1991, in Helsinki, Linus Torvalds began a project that later became the Linux kernel. It was initially a terminal emulator, which Torvalds used to access the large UNIX servers of the university. He wrote the program specifically for the hardware he was using and independent of an operating system because he wanted to use the functions of his new PC with an 80386 processor. Development was done on Minix using the GNU C compiler. This application is still the main choice for compiling Linux today (although the code can be built with other compilers, such as the Intel C Compiler).

Torvalds continues to direct the development of the kernel. Stallman heads the Free Software Foundation, which in turn supports the GNU components. Finally, individuals and corporations develop third-party non-GNU components. These third-party components comprise a vast body of work and may include both kernel modules and user applications and libraries. Linux vendors and communities combine and distribute the kernel, GNU components, and non-GNU components, with additional package management software in the form of Linux distributions.


Design and Implications
------------------------

A Linux-based system is a modular Unix-like operating system. It derives much of its basic design from principles established in Unix during the 1970s and 1980s. Such a system uses a monolithic kernel, the Linux kernel, which handles process control, networking, and peripheral and file system access. Device drivers are integrated directly with the kernel.

Separate projects that interface with the kernel provide much of the system's higher-level functionality. The GNU userland is an important part of most Linux-based systems, providing the most common implementation of the C library, a popular shell, and many of the common Unix tools which carry out many basic operating system tasks. The graphical user interface (or GUI) used by most Linux systems is based on the X Window System.

User Interface
~~~~~~~~~~~~~~
Users can control a Linux-based system through a command line interface (or CLI), a graphical user interface (or GUI), or through controls attached to the associated hardware (this is common for embedded systems). For desktop systems, the default mode is usually graphical user interface (or GUI).

On desktop machines, KDE, GNOME and Xfce are the most popular user interfaces,[36] though a variety of additional user interfaces exist. Most popular user interfaces run on top of the X Window System (or X), which provides network transparency, enabling a graphical application running on one machine to be displayed and controlled from another.

Other GUIs include X window managers such as FVWM, Enlightenment and Window Maker. The window manager provides a means to control the placement and appearance of individual application windows, and interacts with the X window system. This is a more minimalist goal than KDE, GNOME et al., which are termed desktop environments.

A Linux system typically provides a CLI of some sort through a shell, which is the traditional way of interacting with a Unix system. A Linux distribution specialized for servers may use the CLI as its only interface. A “headless system” run without even a monitor can be controlled by the command line via a remote-control protocol such as SSH or telnet.

Most low-level Linux components, including the GNU Userland, use the CLI exclusively. The CLI is particularly suited for automation of repetitive or delayed tasks, and provides very simple inter-process communication. A graphical terminal emulator program is often used to access the CLI from a Linux desktop.

Development
~~~~~~~~~~~
The primary difference between Linux and many other popular contemporary operating systems is that the Linux kernel and other components are free and open source software. Linux is not the only such operating system, although it is by far the most widely used. Some free and open source software licenses are based on the principle of copyleft, a kind of reciprocity: any work derived from a copyleft piece of software must also be copyleft itself. The most common free software license, the GNU GPL, is a form of copyleft, and is used for the Linux kernel and many of the components from the GNU project.

Linux based distributions are intended by developers for interoperability with other operating systems and established computing standards. Linux systems adhere to POSIX, SUS, ISO and ANSI standards where possible, although to date only one Linux distribution has been POSIX.1 certified, Linux-FT.

Free software projects, although developed in a collaborative fashion, are often produced independently of each other. The fact that the software licenses explicitly permit redistribution, however, provides a basis for larger scale projects that collect the software produced by stand-alone projects and make it available all at once in the form of a Linux distribution.

A Linux distribution, commonly called a "distro", is a project that manages a remote collection of system software and application software packages available for download and installation through a network connection. This allows the user to adapt the operating system to his/her specific needs. Distributions are maintained by individuals, loose-knit teams, volunteer organizations, and commercial entities. A distribution can be installed using a CD that contains distribution-specific software for initial system installation and configuration. A package manager such as Synaptic or YAST allows later package upgrades and installations. A distribution is responsible for the default configuration of the installed Linux kernel, general system security, and more generally integration of the different software packages into a coherent whole.

Community
~~~~~~~~~
A distribution is largely driven by its developer and user communities. Some vendors develop and fund their distributions on a volunteer basis, Debian being a well-known example. Others maintain a community version of their commercial distributions, as Red Hat does with Fedora.

In many cities and regions, local associations known as Linux Users Groups (LUGs) seek to promote their preferred distribution and by extension free software. They hold meetings and provide free demonstrations, training, technical support, and operating system installation to new users. Many Internet communities also provide support to Linux users and developers. Most distributions and free software / open source projects have IRC chatrooms or newsgroups. Online forums are another means for support, with notable examples being LinuxQuestions.org and the Gentoo forums. Linux distributions host mailing lists; commonly there will be a specific topic such as usage or development for a given list.

There are several technology websites with a Linux focus. Print magazines on Linux often include cover disks including software or even complete Linux distributions.

Although Linux distributions are generally available without charge, several large corporations sell, support, and contribute to the development of the components of the system and of free software. These include Dell, IBM, HP, Oracle, Sun Microsystems, Novell, Nokia. A number of corporations, notably Red Hat, have built their entire business around Linux distributions.

The free software licenses, on which the various software packages of a distribution built on the Linux kernel are based, explicitly accommodate and encourage commercialization; the relationship between a Linux distribution as a whole and individual vendors may be seen as symbiotic. One common business model of commercial suppliers is charging for support, especially for business users. A number of companies also offer a specialized business version of their distribution, which adds proprietary support packages and tools to administer higher numbers of installations or to simplify administrative tasks. Another business model is to give away the software in order to sell hardware.

Programming on Linux
~~~~~~~~~~~~~~~~~~~~
Most Linux distributions support dozens of programming languages. The most common collection of utilities for building both Linux applications and operating system programs is found within the GNU toolchain, which includes the GNU Compiler Collection (GCC) and the GNU build system. Amongst others, GCC provides compilers for Ada, C, C++, Java, and Fortran. The Linux kernel itself is written to be compiled with GCC. Proprietary compilers for Linux include the Intel C++ Compiler, Sun Studio, and IBM XL C/C++ Compiler.

Most distributions also include support for PHP, Perl, Ruby, Python and other dynamic languages. Examples of languages that are less common, but still supported, are C# via the Mono project, sponsored by Novell, and Scheme. A number of Java Virtual Machines and development kits run on Linux, including the original Sun Microsystems JVM (HotSpot), and IBM's J2SE RE, as well as many open-source projects like Kaffe.

The two main frameworks for developing graphical applications are those of GNOME and KDE. These projects are based on the GTK+ and Qt widget toolkits, respectively, which can also be used independently of the larger framework. Both support a wide variety of languages. There are a number of Integrated development environments available including Anjuta, Code::Blocks, Eclipse, KDevelop, Lazarus, MonoDevelop, NetBeans, and Omnis Studio while the long-established editors Vim and Emacs remain popular.

Reasons for Using Linux
-----------------------
- Linux is free:

As in free beer, they say. If you want to spend absolutely nothing, you don't even have to pay the price of a CD. Linux can be downloaded in its entirety from the Internet completely for free. No registration fees, no costs per user, free updates, and freely available source code in case you want to change the behavior of your system.
Most of all, Linux is free as in free speech:
The license commonly used is the GNU Public License (GPL). The license says that anybody who may want to do so, has the right to change Linux and eventually to redistribute a changed version, on the one condition that the code is still available after redistribution. In practice, you are free to grab a kernel image, for instance to add support for teletransportation machines or time travel and sell your new code, as long as your customers 
can still have a copy of that code.

- Linux is portable to any hardware platform:

A vendor who wants to sell a new type of computer and who doesn't know what kind of OS his new machine will run (say the CPU in your car or washing machine), can take a Linux kernel and make it work on his hardware, because documentation related to this activity is freely available.

- Linux was made to keep on running:

As with UNIX, a Linux system expects to run without rebooting all the time. That is why a lot of tasks are being executed at night or scheduled automatically for other calm moments, resulting in higher availability during busier periods and a more balanced use of the hardware. This property allows for Linux to be applicable also in environments where people don't have the time or the possibility to control their systems night and day.

- Linux is secure and versatile:

The security model used in Linux is based on the UNIX idea of security, which is known to be robust and of proven quality. But Linux is not only fit for use as a fort against enemy attacks from the Internet: it will adapt equally to other situations, utilizing the same high standards for security. Your development machine or control station will be as secure as you firewall.

- Linux is scalable:

From a Palmtop with 2 MB of memory to a petabyte storage cluster with hundreds of nodes: add or remove the appropriate packages and Linux fits all. You don't need a supercomputer anymore,because you can use Linux to do big things using the building blocks provided with the system. If you want to do little things, such as making an operating system for an embedded processor or just recycling your old 486, Linux will do that as well.

- The Linux OS and Linux applications have very short debug−times:

Because Linux has been developed and tested by thousands of people, both errors and people to fix them are found very quickly. It often happens that there are only a couple of hours between discovery and fixing of a bug.

Getting Started
================

Logging in, activating the user interface and logging out
----------------------------------------------------------
In order to work on a Linux system directly, you will need to provide a user name and password. You always need to authenticate to the system. Most PC−based Linux systems have two basic modes for a system to run in: either quick and sober in text console mode, which looks like DOS with mouse, multitasking and multi−user features, or in graphical console mode, which
looks better but eats more system resources.

Graphical Mode
~~~~~~~~~~~~~~
This is the default nowadays on most desktop computers. You know you will connect to the system using graphical mode when you are first asked for your user name, and then, in a new window, to type your password.

To log in, make sure the mouse pointer is in the login window, provide your user name and password to the system and click *OK* or press *Enter*.
It is generally considered a bad idea to connect (graphically) using the root user name, the system adminstrator's account, since the use of graphics includes running a lot of extra programs, in root's case with a lot of extra permissions. To keep all risks as low as possible, use a normal user account to connect graphically. But there are enough risks to keep this in mind as a general advice, for all use of the root account: only log in as root when extra privileges are required.

After entering your user name/password combination, it can take a little while before the graphical environment is started, depending on the CPU speed of your computer, on the software you use and on your personal settings.

To continue, you will need to open a *terminal window* or *xterm* for short (X being the name for the underlying software supporting the graphical environment). This program can be found in the *Applications−>Utilities,
System Tools* or *Internet menu*, depending on what window manager you are using. There might be icons that you can use as a shortcut to get an xterm window as well, and clicking the right mouse button on the desktop background will usually present you with a menu containing a terminal window application.

While browsing the menus, you will notice that a lot of things can be done without entering commands via the keyboard. For most users, the good old point−'n'−click method of dealing with the computer will do. But this
guide is for future network and system administrators, who will need to meddle with the heart of the system.

They need a stronger tool than a mouse to handle all the tasks they will face. This tool is the shell, and when in graphical mode, we activate our shell by opening a terminal window.

The terminal window is your control panel for the system. Almost everything that follows is done using this simple but powerful text tool. A terminal window should always show a command prompt when you open one. This terminal shows a standard prompt, which displays the user's login name, and the current working directory, represented by the twiddle (~)

Another common form for a prompt is this one:
[user@host dir]

In the above example, *user* will be your login name, *hosts* the name of the machine you are working on, and *dir* an indication of your current location in the file system.Prompts can display all kinds of information, but that they are not part of the commands you are giving to your system. To disconnect from the system in graphical mode, you need to close all terminal windows and other applications. After that, hit the logout icon or find Log Out in the menu. Closing everything is not really
necessary, and the system can do this for you, but session management might put all currently open applications back on your screen when you connect again, which takes longer and is not always the desired effect. However, this behavior is configurable.

When you see the login screen again, asking to enter user name and password, logout was successful.

Text Mode
~~~~~~~~~
You know you're in text mode when the whole screen is black, showing (in most cases white) characters. A text mode login screen typically shows some information about the machine you are working on, the name of the machine and a prompt waiting for you to log in.

The login is different from a graphical login, in that you have to hit the *Enter* key after providing your user name, because there are no buttons on the screen that you can click with the mouse. Then you should type
your password, followed by another *Enter*. You won't see any indication that you are entering something, not even an asterisk, and you won't see the cursor move. But this is normal on Linux and is done for security
reasons.

When the system has accepted you as a valid user, you may get some more information, called the *message of the day*, which can be anything. Additionally, it is popular on UNIX systems to display a fortune cookie,
which contains some general wise or unwise (this is up to you) thoughts. After that, you will be given a shell, indicated with the same prompt that you would get in graphical mode.

Also in text mode: log in as root only to do setup and configuration that absolutely requires administrator privileges, such as adding users, installing software packages, and performing network and other system configuration. Once you are finished, immediately leave the special account and resume your work as a non−privileged user.

Logging out is done by entering the logout command, followed by Enter. You are successfully disconnected from the system when you see the login screen again.Don't power−off the computer after logging out. It is not meant to be shut off without application of the proper procedures for halting the system. Powering it off without going through the halting process might cause severe damage!

Basic Commands
===============

1.ls
----

When invoked without any arguments, *ls* lists the files in the current working directory. A directory that is not the current working directory can be specified and ls will list the files there. The user also may specify any list of files and directories. In this case, all files and all contents of specified directories will be listed. The name *ls* is derived from *list segments* which was used in earlier systems.

Files whose names start with "." are not listed, unless the *-a* flag is specified or the files are specified explicitly.

Without options, *ls* displays files in a bare format. This bare format however makes it difficult to establish the type, permissions, and size of the files. The most common options to reveal this information or change the list of files are:

    * *-l* long format, displaying Unix file types, permissions, number of hard links, owner, group, size, date, and filename
    * *-F* appends a character revealing the nature of a file, for example, * for an executable, or / for a directory. Regular files have no suffix.
    * *-a* lists all files in the given directory, including those whose names start with "." (which are hidden files in Unix). By default, these files are excluded from the list.
    * *-R* recursively lists subdirectories. The command ls -R / would therefore list all files.
    * *-d* shows information about a symbolic link or directory, rather than about the link's target or listing the contents of a directory.
    * *-t* sort the list of files by modification time.
    * *-h* print sizes in human readable format. (e.g., 1K, 234M, 2G, etc.)

In some environments, providing the option *--color* (for GNU ls) or *-G* (FreeBSD ls) causes ls to highlight different types of files with different colors, instead of with characters as *-F* would. To determine what color to use for a file, GNU *ls* checks the Unix file type, the file permissions, and the file extension, while FreeBSD *ls* checks only the Unix file type and file permissions.::

	$ ls
	jeeves.rst psmith.html blandings.html
	$ ls -l
	drwxr--r--   1 plum  editors   4096  jeeves
	-rw-r--r--   1 plum  editors  30405  psmith
	-r-xr-xr-x   1 plum  plum      8460  blandings


2.date
-------

The Unix date command displays the time and date. The super-user can use it to set the system clock.

With no options, the date command displays the current date and time, including the abbreviated day name, abbreviated month name, day of the month, the time separated by colons, the timezone name, and the year. For example::

	$date
	Tue Sep  8 12:01:45 IST 2009

Options
~~~~~~~~

*-d, -de* : string display time described by string, not now.

*-e* : datefile like de once for each line of datefile

*-s, --set* : string set time described by string

*-n* : don't synchronize the clocks on groups of machines using the utility timed(8). By default, if timed is running, date will set the time on all of the machines in the local group. *-n* inhibites that.

*-u* : Display or set the date in UTC (universal) time.

*date [-u|--utc|--universal] [mmddHHMM[[cc]yy].SS* : The only valid option for the this form specifies Coordinated Universal Time.

*-u GMT* : example - Sat Feb 5 14:49:42 GMT 2005

*--utc, --universal* : Coordinated Universal Time, example - Tue Sep  8 07:05:54 UTC 2009

*-ITIMESPEC, --iso-8601* [=TIMESPEC] : output date/time in ISO 8601 format. TIMESPEC=date for date only, hours, minutes, or seconds for date and time to the indicated precision.

*--iso-8601* without TIMESPEC defaults to 'date'.

*-R*, *--rfc-822* outputs RFC-822 compliant date string,
example - Sat Feb 5 09:50:23 EST 2005

*--help*

The Single Unix Specification (SUS) mandates only one option: *-u*, where the date and time is printed as if the timezone was UTC+0. Other Unix and Unix-like systems provide extra options.

The XSI extension to the SUS specifies that the date command can also be used to set the date. The new date is specified as an option to date in the format MMddhhmm[[cc]yy], where MM specifies the two-digit numeric month, dd specifies the two-digit numeric day, hh specifies the two-digit numeric hour, mm specifies the two-digit numeric minutes. Optionally cc specifies the first two digits of the year, and yy specifies the last two digits of the year.

Other Unix and Unix-like systems may set different options or date formats for date, for example, on some systems to set the current date and time to September 8, 2004 01:22 you type::

	$date --set="20040908 01:22"

3.cd
-----

Change directory. Use “ cd ..” to go up one directory.

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

4.who
-----

The standard Unix command *who* displays a list of users who are currently logged into a computer.

The *who* command is related to the command *w*, which provides the same information but also displays additional data and statistics.::

	$who
	beeblebrox tty7         2009-09-08 10:50 (:0)
	beeblebrox pts/0        2009-09-08 11:25 (:0.0)
	dumbledore pts/1        2009-09-08 18:11 (potter.xyz.in)
	beeblebrox pts/2        2009-09-08 18:53 (:0.0)


The command can be invoked with the arguments am i or am I (so it is invoked as who am i or am I), showing information about the current terminal only (see the -m option below, of which this invocation is equivalent).

The Single Unix Specification (SUS) without extensions only specifies the following -m, -T, and -u options, all other options are specified in the XSI extension.

    -a, process the system database used for user information with the -b, -d, -l, -p, -r, -t, -T and -u.
    -b, show time when system was last rebooted
    -d, show zombie processes and details
    -H, show column headers
    -l, show terminals where a user can log in
    -m, show information about the current terminal only
    -p, show active processes
    -q, quick format, show only names and the number of all users logged on, disables all other options; equivalent to users command line utility
    -r, show runlevel of the init process.
    -s, (default) show only name, terminal, and time details
    -t, show when system clock was last changed
    -T, show details of each terminal in a standard format 
    -u, show idle time; XSI shows users logged in and displays information whether the terminal has been used recently or not 

5.mkdir
--------

Normal usage is as straightforward as follows::

	$mkdir name_of_directory

Where *name_of_directory* is the name of the directory one wants to create. When typed as above (ie. normal usage), the new directory would be created within the current directory. On Unix, multiple directories can be specified, and *mkdir* will try to create all of them.

Options
~~~~~~~

On Unix-like operating systems, *mkdir* takes options. Three of the most common options are:

    * *-p*: will also create all directories leading up to the given directory that do not exist already. If the given directory already exists, ignore the error.
    * *-v*: display each directory that mkdir creates. Most often used with -p.
    * *-m*: specify the octal permissions of directories created by mkdir.

*-p* is most often used when using mkdir to build up complex directory hierarchies, in case a necessary directory is missing or already there. -m is commonly used to lock down temporary directories used by shell scripts.

Examples
~~~~~~~~

An example of *-p* in action is::

	$mkdir -p /tmp/a/b/c

If */tmp/a* exists but */tmp/a/b* does not, mkdir will create */tmp/a/b* before creating */tmp/a/b/c*.

And an even more powerful command, creating a full tree at once (this however is a Shell extension, nothing mkdir does itself)::

	$mkdir -p tmpdir/{trunk/sources/{includes,docs},branches,tags}

This will create:

tmpdir 	- branches
	- tag
	- trunk	- sources - includes
			  - docs

Getting Help
============

1. apropos and whatis
----------------------

This is a command to search the manual pages files in Unix and Unix-like operating systems. ::

	$ apropos grep
	egrep       egrep (1)       Search a file for a pattern using full 		regular expressions
	fgrep       fgrep (1)       Search a file for a fixed-character 	string
	fmlgrep     fmlgrep (1)     Search a file for a pattern
	grep        grep (1)        Search a file for a pattern
	gzgrep      gzgrep (1)      Search a possibly compressed file for a 		regular expression
	nisgrep     nismatch (1)    Utilities for searching NIS+ tables
	pgrep       pgrep (1)       Find or signal a process by name or 	other attribute
	zgrep       zgrep (1)       Search a possibly compressed file for a 		regular expression

In this example, the user uses *apropos* to search for the string "grep", and apropos returns the indicated *man* pages that include the term "grep".

A short index of explanations for commands is available using the *whatis* command, like in the examples below::

	[your_prompt] whatis ls
	ls                   (1)  - list directory contents

This displays short information about a command, and the first section in the collection of man pages that contains an appropriate page.

If you don't know where to get started and which man page to read, *apropos* gives more information. Say that you don't know how to start a browser, then you could enter the following command::

	another prompt> apropos browser
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


2. man
-------

Man pages (short for "manual pages") are the extensive documentation that comes preinstalled with almost all substantial Unix and Unix-like operating systems. The Unix command used to display them is *man*. Each page is a self-contained document.

To read a manual page for a Unix command, one can use::

	$ man <command_name>

at a shell prompt; for example, "man ftp". In order to simplify navigation through the output, man generally uses the less terminal pager.

Pages are traditionally referred to using the notation "name(section)"; for example, ftp(1). The same page name may appear in more than one section of the manual, this can occur when the names of system calls, user commands, or macro packages coincide. Two examples are *man(1)* and *man(7)*, or *exit(2)* and *exit(3)*. The syntax for accessing the non-default manual section varies between different man implementations. On Linux and *BSD, for example, the syntax for reading *printf(3)* is::

	$ man 3 printf

Another example::

	yourname@yourcomp ~> man man


Layout
~~~~~~

All man pages follow a common layout that is optimized for presentation on a simple ASCII text display, possibly without any form of highlighting or font control. Sections present may include:

NAME
    The name of the command or function, followed by a one-line description of what it does.
SYNOPSIS
    In the case of a command, you get a formal description of how to run it and what command line options it takes. For program functions, a list of the parameters the function takes and which header file contains its definition. For experienced users, this may be all the documentation they need.
DESCRIPTION
    A textual description of the functioning of the command or function.
EXAMPLES
    Some examples of common usage.
SEE ALSO
    A list of related commands or functions.

Other sections may be present, but these are not well standardized across man pages. Common examples include: OPTIONS, EXIT STATUS, ENVIRONMENT, KNOWN BUGS, FILES, AUTHOR, REPORTING BUGS, HISTORY and COPYRIGHT.

History
~~~~~~~

The UNIX Programmer's Manual was first published on November 3, 1971. The first actual man pages were written by Dennis Ritchie and Ken Thompson at the insistence of Doug McIlroy in 1971. The *troff* macros used for man pages (-mm) were the general-purpose ones written by Ted Dolotta (later to be the first manager of USG and the principal author of the System III manual), with additions for the manuals. At the time, the availability of online documentation through the manual page system was regarded as a great advance. To this day, virtually every Unix command line application comes with its man page, and many Unix users perceive a lack of man pages as a sign of low quality; indeed, some projects, such as Debian, go out of their way to write man pages for programs lacking one. Few alternatives to man have enjoyed much popularity, with the possible exception of the GNU project's "info" system, an early and simple hypertext system.

However, the format of a single page for each application, the lack of classification within the sections and the relatively unsophisticated formatting facilities have motivated the development of alternative documentation systems, such as the previously mentioned info system.

Most Unix GUI applications (particularly those built using the GNOME and KDE development environments) now provide end-user documentation in HTML and include embedded HTML viewers such as yelp for reading the help within the application.

Usually the man pages are written in English. Translations into other languages can be also available on the system.

The default format of the man pages is troff, with either the macro package man (appearance oriented) or on some systems mdoc (semantic oriented). This makes it possible to typeset a man page to PostScript, PDF and various other formats for viewing or printing.

3. info
--------

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

4. --help
----------

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

1. cp
------

*cp* is the command entered in a Unix shell to copy a file from one place to another, possibly on a different filesystem. The original file remains unchanged, and the new file may have the same or a different name.

Usage
~~~~~

To copy a file to another file::

	$ cp [ -f ] [ -H ] [ -i ] [ -p ][ -- ] SourceFile TargetFile

To copy a file to a directory::

	$ cp [ -f ] [ -H ] [ -i ] [ -p ] [ -r | -R ] [ -- ] SourceFile ... 		TargetDirectory

To copy a directory to a directory::

	$ cp [ -f ] [ -H ] [ -i ] [ -p ] [ -- ] { -r | -R } 
	SourceDirectory ... TargetDirectory

Flags
~~~~~

*-f* (force) – specifies removal of the target file if it cannot be opened for write operations. The removal precedes any copying performed by the cp command.

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

To copy a specific set of files to another directory, enter::

    $ cp zaphod arthur ford /home/hhgg/clients

This copies the *zaphod*, *arthur*, and *ford* files in your current working directory to the /home/hhgg/clients directory.

To use pattern-matching characters to copy files, enter::

    $ cp programs/*.py .

This copies the files in the programs directory that end with *.py* to the current directory, signified by the single . (dot). You must type a space between the *py* and the final dot.

2. mv
-----

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
	$ mv myfile otherfilename    renames a file and deletes the existing 		file "myfile"
	$ mv myfile /myfile          moves 'myfile' from the current 		directory to the root directory
	$ mv myfile dir/myfile       moves 'myfile' to 'dir/myfile' relative 		to the current directory
	$ mv myfile dir              same as the previous command (the 		filename is implied to be the same)
	$ mv myfile dir/myfile2      moves 'myfile' to dir and renames it to 		'myfile2'
	$ mv foo bar baz dir         moves multiple files to directory dir
	$ mv --help                  shows a very concise help about the 		syntax of the command
	$ man mv                     prints an extensive user manual for 		'mv' in the terminal

In all cases, the file or files being moved or renamed can be a directory.

Note that when the command is called with two arguments (as *mv name1 name2* or *mv name1 /dir/name2*), it can have three different effects, depending on whether *name2* does not exist, is an existing file, or is an existing directory. If the user intends to refer to an existing directory, */.* (or in some Unix versions */* is sufficient) may be appended to the name to force the system to check this. To move a file to a new directory, the directory must be created first.

3. rm
------

*rm* (short for remove) is one of several basic Unix command lines that operates on files. It is used to delete files from a filesystem. The data is not actually destroyed. Only the index listing where the file is stored is destroyed, and the storage is made available for reuse. There are undelete utilities that will attempt to reconstruct the index and can bring the file back if the parts were not reused.

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

Usually, on most filesystems, deleting a file requires write permission on the parent directory (and execute permission, in order to enter the directory in the first place). (Note that, confusingly for beginners, permissions on the file itself are irrelevant. However, GNU rm asks for confirmation if a write-protected file is to be deleted, unless the -f option is used.)

To delete a directory (with rm -r), one must delete all of its contents recursively. This requires that one must have read and write and execute permission to that directory (if it's not empty) and all non-empty subdirectories recursively (if there are any). The read permissions are needed to list the contents of the directory in order to delete them. This sometimes leads to an odd situation where a non-empty directory cannot be deleted because one doesn't have write permission to it and so cannot delete its contents; but if the same directory were empty, one would be able to delete it.

If a file resides in a directory with the sticky bit set, then deleting the file requires one to be the owner of the file.


Command Line Arguments
=======================

In computer command line interfaces, a command line argument is an argument sent to a program being called. In general, a program can take any number of command line arguments, which may be necessary for the program to run, or may even be ignored, depending on the function of that program.

For example, in Unix and Unix-like environments, an example of a command-line argument is::

	rm file.s

"file.s" is a command line argument which tells the program rm to remove the file "file.s".

Programming languages such as C, C++ and Java allow a program to interpret the command line arguments by handling them as string parameters in the main function.

A command line option or simply option (also known as a command line parameter, flag, or a switch) is an indication by a user that a computer program should change its default output.

Long options are introduced via --, and are typically whole words. For example, *ls --long --classify --all*. Arguments to long options are provided with =, as *ls --block-size=1024*. Some Unix programs use long options with single dashes, for example MPlayer as in *mplayer -nosound*.

Linux also uses -- to terminate option lists. For example, an attempt to delete a file called *-file1* by using *rm -file1* may produce an error, since rm may interpret *-file1* as a command line switch. Using *rm -- -file1* removes ambiguity.

Basic Text Processing
======================

1. head
--------

*head* is a program on Unix and Unix-like systems used to display the first few lines of a text file or piped data. The command syntax is::

	$ head [options] <file_name>

By default, *head* will print the first 10 lines of its input to the standard output. The number of lines printed may be changed with a command line option. The following example shows the first 20 lines of filename::

	$ head -n 20 filename

This displays the first 5 lines of all files starting with *foo*::

	$ head -n 5 foo*

Some versions omit the n and just let you say -5.

Flags
~~~~~
::

	-c <x number of bytes> Copy first x number of bytes.

Other options: *sed*

Many early versions of Unix did not have this command, and so documentation and books had *sed* do this job::

	sed 5q foo

This says to print every line (implicit), and quit after the fifth.


2. tail
-------- 

*tail* is a program on Unix and Unix-like systems used to display the last few lines of a text file or piped data.

The command-syntax is::

	$ tail [options] <file_name>

By default, *tail* will print the last 10 lines of its input to the standard output. With command line options the number of lines printed and the printing units (lines, blocks or bytes) may be changed. The following example shows the last 20 lines of filename::

	$ tail -n 20 filename

This example shows the last 15 bytes of all files starting with *foo*::

	$ tail -c 15 foo*

This example shows all lines of filename from the second line onwards::

	$ tail -n +2 filename

Using an older syntax (still used in Sun Solaris as the -n option is not supported), the last 20 lines and the last 50 bytes of filename can be shown with the following command::

	$ tail -20 filename
	$ tail -50c filename

However this syntax is now obsolete and does not conform with the POSIX 1003.1-2001 standard. Even if still supported in current versions, when used with other options (like -f, see below), these switches could not work at all.

File monitoring
~~~~~~~~~~~~~~~

*tail* has a special command line option *-f* (follow) that allows a file to be monitored. Instead of displaying the last few lines and exiting, tail displays the lines and then monitors the file. As new lines are added to the file by another process, tail updates the display. This is particularly useful for monitoring log files. The following command will display the last 10 lines of messages and append new lines to the display as new lines are added to messages::

	$ tail -f /var/adm/messages

To interrupt tail while it is monitoring, break-in with *Ctrl+C*. This command can be run "in the background" with &, see job control.

If you have a command's result to monitor, you can use the *watch* command.


3. cut
-------

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

4. paste
---------

*paste* is a Unix command line utility which is used to join files horizontally (parallel merging) by outputting lines consisting of the sequentially corresponding lines of each file specified, separated by tabs, to the standard output. It is effectively the horizontal equivalent to the utility *cat* command which operates on the vertical plane of two or more files.

To paste several columns of data together into the file *www* from files *who*, *where*, and *when*::

	$ paste who where when > www

If the files contain:

+-----------+------------+------------+
|   who     |   where    |    when    |
+===========+============+============+
|  Sam      |  Detroit   | January 3  |
+-----------+------------+------------+	
|  Dave     | Edgewood   | February 4 |
+-----------+------------+------------+
|  Sue      |  Tampa     |  March 19  |
+-----------+------------+------------+	

This creates the file named *www* containing::

	Sam            Detroit         January 3
	Dave           Edgewood        February 4
	Sue            Tampa           March 19

Shell Meta Characters
======================

Unix recognizes certain special characters, called "meta characters," as command directives. The shell meta characters are recognized anywhere they appear in the command line, even if they are not surrounded by blank space. For that reason, it is safest to only use the characters A-Z, a-z, 0-9, and the period, dash, and underscore characters when naming files and directories on Unix. If your file or directory has a shell meta character in the name, you will find it difficult to use the name in a shell command.

The shell meta characters include:

\ / < > ! $ % ^ & * | { } [ ] " ' ` ~ ; 

Different shells may differ in the meta characters recognized.

As an example,
::

	$ ls file.*

run on a directory containing the files file, file.c, file.lst, and myfile would list the files file.c and file.lst. However,::

	$ ls file.?

run on the same directory would only list file.c because the ? only matches one character, no more, no less. This can save you a great deal of typing time. For example, if there is a file called california_cornish_hens_with_wild_rice and no other files whose names begin with 'c', you could view the file without typing the whole name by typing this::

	$ more c*

because the c* matches that long file name.

Filenames containing metacharacters can pose many problems and should never be intentionally created. If you do find that you've created a file with metacharacters, and you would like to remove it, you have three options. You may use wildcards to match metacharacter, use the \  to directly enter the filename, or put the command in double quotes (except in the case of double quotes within the file name, these must be captured with one of the first two methods). For example, deleting a file named `"``*`|more`"` can be accomplished with::

	$ rm ??more

or::

	$ rm $\backslash$*$\backslash$|more

or::

	$ rm ''*|more'' 


Looking At Files
================

1. cat
-------

The *cat* command is a standard Unix program used to concatenate and display files. The name is from "catenate", a synonym of *concatenate*.

The Single Unix Specification specifies the behavior that the contents of each of the files given in sequence as arguments will be written to the standard output in the same sequence, and mandates one option, -u, where each byte is printed as it is read.

If the filename is specified as -, then *cat* will read from standard input at that point in the sequence. If no files are specified, *cat* will read from standard input entered.

Extensions
~~~~~~~~~~

Both the BSD versions of *cat* (as per the OpenBSD manpage) and the GNU coreutils version of *cat* specify the following options:

    `*` -b (GNU only: --number-nonblank), number non-blank output lines

    `*` -n (GNU only: --number), number all output lines

    `*` -s (GNU only: --squeeze-blank), squeeze multiple adjacent blank lines

    `*` -v (GNU only: --show-nonprinting), displays nonprinting characters 		as if they were visible, except for tabs and the end of line 		character

    `*` -t on BSD, -T on GNU, implies -v but also display tabs as ^I

    `*` -e on BSD, -E on GNU, implies -v but also display end-of-line 		characters as $

Jargon File Definition
~~~~~~~~~~~~~~~~~~~~~~

The Jargon File version 4.4.7 lists this as the definition of *cat*::

   1. To spew an entire file to the screen or some other output sink without
 	pause (syn. blast).

   2. By extension, to dump large amounts of data at an unprepared target or
 	with no intention of browsing it carefully. Usage: considered silly.
 	Rare outside Unix sites. See also dd, BLT.

	Among Unix fans, *cat(1)* is considered an excellent example of
 	user-interface design, because it delivers the file contents without 
	such verbosity as spacing or headers between the files, and because 
	it does not require the files to consist of lines of text, but works 
	with any sort of data.

	Among Unix critics, *cat(1)* is considered the canonical example of 
	bad user-interface design, because of its woefully unobvious name. 
	It is far more often used to blast a single file to standard output 
	than to concatenate two or more files. The name cat for the former 
	operation is just as unintuitive as, say, LISP's cdr.

	Of such oppositions are holy wars made...

Useless Use of 'cat'
~~~~~~~~~~~~~~~~~~~~

UUOC (from comp.unix.shell on Usenet) stands for “Useless Use of cat”. As received wisdom on *comp.unix.shell* observes, “The purpose of cat is to concatenate (or 'catenate') files. If it's only one file, concatenating it with nothing at all is a waste of time, and costs you a process.”

Nevertheless one sees people doing::

	$ cat file | some_command and its args ...

instead of the equivalent and cheaper::

	<file some_command and its args ...

or (equivalently and more classically)::

	some_command and its args ... <file

Since 1995, occasional awards for UUOC have been given out, usually by Perl luminary Randal L. Schwartz. There is a web page devoted to this and other similar awards. In British hackerdom the activity of fixing instances of UUOC is sometimes called 'demoggification'.

Amongst many, it is still considered safer to use *cat* for such cases given that the < and > keys are next to each other in many popular keyboard mappings. While the risk might be low, the impact of using > instead of < can be high and prohibitive.

zcat
~~~~~

*zcat* is a Unix program similar to *cat*, that decompresses individual files and concatenates them to standard output. Traditionally *zcat* operated on files compressed by compress but today it is usually able to operate on *gzip* or even *bzip2* archives. On such systems, it is equivalent to *gunzip -c*

2. more
--------

In computing, *more* is a command to view (but not modify) the contents of a text file one screen at a time (terminal pager). It is available on Unix and Unix-like systems, DOS, OS/2 and Microsoft Windows. Programs of this sort are called pagers.

History
~~~~~~~

The *more* command was originally written by Daniel Halbert, a graduate student at the University of California, Berkeley, in 1978. It was first included in 3.0 BSD, and has since become a standard program in all Unix systems. *less*, a similar command with the extended capability of allowing both forward and backward navigation through the file was written by Mark Nudelman during 1983-85 and is now included in most Unix and Unix-like systems.

Usage
~~~~~

The command-syntax is::

	$ more [options] [file_name]

If no file name is provided, *more* looks for input from stdin.

Once *more* has obtained input, it displays as much as can fit on the current screen and waits for user input to advance, with the exception that a form feed (^L) will also cause *more* to wait at that line, regardless of the amount of text on the screen. In the lower-left corner of the screen is displayed the text "--More--" and a percentage, representing the percent of the file that *more* has paged through. (This percentage includes the text displayed on the current screen.) When *more* reaches the end of a file (100%) it exits. The most common methods of navigating through a file are *Enter*, which advances the output by one line, and *Space*, which advances the output by one screen.

There are also other commands that can be used while navigating through the document; consult *more*'s *man* page for more details.

Options
~~~~~~~

Options are typically entered before the file name, but can also be entered in the environment variable *$MORE*. Options entered in the actual command line will override those entered in the *$MORE* environment variable. Available options may vary between Unix systems, but a typical set of options is as follows:

    * -num: This option specifies an integer which is the screen size (in 	lines).

    * -d: more will prompt the user with the message "[Press space to 		  continue, 'q' to quit.]" and will display "[Press 'h' for 		  instructions.]" instead of ringing the bell when an illegal key is 		  pressed.

    * -l: more usually treats ^L (form feed) as a special character, and 	   will pause after any line that contains a form feed. The -l option 		  will prevent this behavior.

    * -f: Causes more to count logical, rather than screen lines (i.e., long 		  lines are not folded).

    * -p: Do not scroll. Instead, clear the whole screen and then display 		  the text.

    * -c: Do not scroll. Instead, paint each screen from the top, clearing 		  the remainder of each line as it is displayed.

    * -s: Squeeze multiple blank lines into one.

    * -u: Suppress underlining.

    * +/: The +/ option specifies a string that will be searched for before 		  each file is displayed. (Ex.: more +/Preamble gpl.txt)

    * +num: Start at line number num.


3. less
--------

*less* is a terminal pager program on Unix, Windows and Unix-like systems used to view (but not change) the contents of a text file one screen at a time. It is similar to *more*, but has the extended capability of allowing both forward and backward navigation through the file. Unlike most Unix text editors/viewers, *less* does not need to read the entire file before starting, resulting in faster load times with large files.

History
~~~~~~~~

*less* was initially written by Mark Nudelman during 1983-85, in the need of a version of more able to do backward scrolling of the displayed text. The name came from the joke of doing "backwards more." *less* is now part of the GNU project and it is included in most Unix systems.

Usage
~~~~~~

*less* can be invoked with options to change its behaviour, for example, the number of lines to display on the screen. A few options vary depending on the operating system. While *less* is displaying the file, various commands can be used to navigate through the file. These commands are based on those used by both *more* and *vi*. It is also possible to search for character patterns in the file.

By default, *less* displays the contents of the file to the standard output (one screen at a time). If the file name argument is omitted, it displays the contents from standard input (usually the output of another command through a pipe). If the output is redirected to anything other than a terminal, for example a pipe to another command, less behaves like cat.

The command-syntax is::

	$ less [options] file_name

Frequently Used Options
~~~~~~~~~~~~~~~~~~~~~~~

    * -g: Highlights just the current match of any searched string.

    * -I: Case-insensitive searches.

    * -M: Shows more detailed prompt, including file position.

    * -N: Shows line numbers (useful for source code viewing).

    * -S: Disables line wrap ("chop long lines"). Long lines can be seen by 		  side scrolling.

    * -?: Shows help.

Frequently Used Commands
~~~~~~~~~~~~~~~~~~~~~~~~

    * [Arrows]/[Page Up]/[Page Down]/[Home]/[End]: Navigation.

    * [Space bar]: Next page.

    * b: Previous page.

    * ng: Jump to line number n. Default is the start of the file.

    * nG: Jump to line number n. Default is the end of the file.

    * /pattern: Search for pattern. Regular expressions can be used.

    * n: Go to next match (after a successful search).

    * N: Go to previous match.

    * mletter: Mark the current position with letter.

    * 'letter: Return to position letter. [' = single quote]

    * '^ or g: Go to start of file.

    * '$ or G: Go to end of file.

    * s: Save current content (got from another program like grep) in a file.

    * =: File information.

    * F: continually read information from file and follow its end. Useful 	    for logs watching. Use Ctrl+C to exit this mode.

    * -option: Toggle command-line option -option.

    * h: Help.

    * q: Quit.

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

The majority of these directories exist in all UNIX operating systems and are generally used in much the same way; however, the descriptions here are those used specifically for the FHS, and are not considered authoritative for platforms other than Linux.

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


1. man hier
------------

This is the manual page on the UNIX filesystem. The syntax for this is::

	$ man hier

2. ls -l
---------

Shows you huge amounts of information (permissions, owners, size, and when last modified) for folders and files. The syntax is ::

	$ ls -l

This can be done after entering the required directory. 

Permissions and Ownership
=========================

1. chmod
---------

The *chmod* command (abbreviated from 'change mode') is a shell command and C language function in Unix and Unix-like environments. When executed, it can change file system modes of files and directories. The modes include permissions and special modes.A chmod command first appeared in AT&T Unix version 1, and is still used today on Unix-like machines.

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

Since the *setuid*, *setgid* and *sticky* bits are not set, this is equivalent to:
::

	$ chmod 0664 myfile

Special modes
+++++++++++++

The *chmod* command is also capable of changing the additional permissions or special modes of a file or directory. The symbolic modes use **s** to represent the *setuid* and *setgid* modes, and **t** to represent the sticky mode. The modes are only applied to the appropriate classes, regardless of whether or not other classes are specified.

Most operating systems support the specification of special modes using octal modes, but some do not. On these systems, only the symbolic modes can be used.

Redirection and Piping
=======================

In computing, *redirection* is a function common to most command-line interpreters, including the various Unix shells that can redirect standard streams to user-specified locations.

Programs do redirection with the *dup2(2)* system call, or its less-flexible but higher-level stdio analogues, *freopen(3)* and *popen(3)*.

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
A pipeline of three programs run on a text terminal::

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

In shells derived from *csh* (the C shell), the syntax instead appends the & character to the redirect characters, thus achieving a similar result.

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

1. grep
--------

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

In Perl, *grep* is a built-in function that finds elements in a list. In functional programming languages, this higher-order function is typically named "filter" instead.

The DOS, OS/2 and Microsoft Windows platforms provide the find command for simple string searches. Windows includes the "findstr" command which approximates much of the functionality of “grep”. Ports of grep (Cygwin and GnuWin32, for example) are also available for Windows.

Adobe added support for grep in the CS4 version of InDesign. Their support allow for finding and changing the formatting of text or the text itself in a document using *grep*.

2. tr
------

*tr* (abbreviated from *translate* or *transliterate*) is a command in Unix-like operating systems.

When executed, the program reads from the standard input and writes to the standard output. It takes as parameters two sets of characters, and replaces occurrences of the characters in the first set with the corresponding elements from the other set. For example,
::

	$ tr 'abcd' 'jkmn' 

maps 'a' to 'j', 'b' to 'k', 'c' to 'm', and 'd' to 'n'.

Sets of characters may be abbreviated by using character ranges. The previous example could be written:
::

	$ tr 'a-d' 'jkmn'

In POSIX compliant versions of *tr* the set represented by a character range depends on the locale's collating order, so it is safer to avoid character ranges in scripts that might be executed in a locale different from that in which they were written. Ranges can often be replaced with POSIX character sets such as [:alpha:].

The *-c* flag complements the first set of characters.
::

	$ tr -cd '[:alnum:]' 

therefore removes all non-alphanumeric characters.

The *-s* flag causes tr to compress sequences of identical adjacent characters in its output to a single token. For example,
::

	$ tr -s '\n' '\n'

replaces sequences of one or more newline characters with a single newline.

The *-d* flag causes tr to delete all tokens of the specified set of characters from its input. In this case, only a single character set argument is used. The following command removes carriage return characters, thereby converting a file in DOS/Windows format to one in Unix format.
::

	$ tr -d '\r'

Most versions of *tr*, including GNU *tr* and classic Unix *tr*, operate on single byte characters and are not Unicode compliant. An exception is the Heirloom Toolchest implementation, which provides basic Unicode support.

Ruby and Perl also have an internal *tr* operator, which operates analogously. Tcl's *string map* command is more general in that it maps strings to strings while *tr* maps characters to characters.

Elementary Regex
=================

In computing, regular expressions provide a concise and flexible means for identifying strings of text of interest, such as particular characters, words, or patterns of characters. A regular expression (often shortened to regex or regexp) is written in a formal language that can be interpreted by a regular expression processor, a program that either serves as a parser generator or examines text and identifies parts that match the provided specification.

Regular expressions are used by many text editors, utilities, and programming languages to search and manipulate text based on patterns. For example, Perl, Ruby and Tcl have a powerful regular expression engine built directly into their syntax. Several utilities provided by Unix distributions—including the editor *ed* and the filter *grep* — were the first to popularize the concept of regular expressions.

Traditional Unix regular expression syntax followed common conventions but often differed from tool to tool. The IEEE POSIX Basic Regular Expressions (BRE) standard (released alongside an alternative flavor called Extended Regular Expressions or ERE) was designed mostly for backward compatibility with the traditional (Simple Regular Expression) syntax but provided a common standard which has since been adopted as the default syntax of many Unix regular expression tools, though there is often some variation or additional features. Many such tools also provide support for ERE syntax with command line arguments.

In the BRE syntax, most characters are treated as literals — they match only themselves (i.e., a matches "a"). The exceptions, listed below, are called metacharacters or metasequences.

+-------------+------------------------------------------------------------+
|Metacharacter|                            Description                     |
+=============+============================================================+
| .           | Matches any single character (many applications exclude    | 
|             | newlines, and exactly which characters are considered      | 
|             | newlines is flavor, character encoding, and platform       |
|             | specific, but it is safe to assume that the line feed      |
|             | character is included). Within POSIX bracket expressions,  |
|             | the dot character matches a literal dot. For example, a.c  |
|             | matches abc, etc., but [a.c] matches only a, ., or         |
|             | c.                                                         |
+-------------+------------------------------------------------------------+
| [ ]         | A bracket expression. Matches a single character that is   | 
|             | contained within the brackets. For example, [abc] matches  |
|             | a, b, or c. [a-z] specifies a range which matches any      |
|             | lowercase letter from a to z. These forms can be mixed:    |
|             | [abcx-z] matches a, b, c, x, y, or z, as does              |
|             | [a-cx-z]. The - character is treated as a literal character|
|             | if it is the last or the first character within the        |
|             | brackets, or if it is escaped with a backslash: [abc-],    |
|             | [-abc], or [a\-bc].                                        |
+-------------+------------------------------------------------------------+
| [^ ]        | Matches a single character that is not contained within the|
|             | brackets. For example, [^abc] matches any character other  |
|             | than a, b, or c. [^a-z] matches any single character       |
|             | that is not a lowercase letter from a to z. As above,      |
|             | literal characters and ranges can be mixed.                |
+-------------+------------------------------------------------------------+
| ^           | Matches the starting position within the string. In        |
|             | line-based tools, it matches the starting position of any  |
|             | line.                                                      |
+-------------+------------------------------------------------------------+
| $           | Matches the ending position of the string or the position  |
|             | just before a string-ending newline. In line-based tools,  |
|             | it matches the ending position of any line.                |
+-------------+------------------------------------------------------------+
| `*`         | Matches the preceding element zero or more times. For      |
|             | example, ab*c matches "ac", "abc", "abbbc", etc. [xyz]*    |
|             | matches "", "x", "y", "z", "zx", "zyx", "xyzzy", and so on.|
|             | \(ab\)* matches "", "ab", "abab", "ababab", and so on.     |
+-------------+------------------------------------------------------------+
| ?           | Matches the preceding element zero or one time. For        |
|             | example, ba? matches "b" or "ba".                          |
+-------------+------------------------------------------------------------+
| `+`         | Matches the preceding element one or more times. For       |
|             | example, ba+ matches "ba", "baa", "baaa", and so on.       |
+-------------+------------------------------------------------------------+
| `|`         | The choice (aka alternation or set union) operator matches |
|             | either the expression before or the expression after the   |
|             | operator. For example, abc|def matches "abc" or "def".     |
+-------------+------------------------------------------------------------+

Lazy quantification
--------------------

The standard quantifiers in regular expressions are greedy, meaning they match as much as they can, only giving back as necessary to match the remainder of the regex. For example, someone new to regexes wishing to find the first instance of an item between < and > symbols in this example:
::

	Another whale explosion occurred on <January 26>, <2004>.

...would likely come up with the pattern <.*>, or similar. However, this pattern will actually return "<January 26>, <2004>" instead of the "<January 26>" which might be expected, because the `*` quantifier is greedy — it will consume as many characters as possible from the input, and "January 26>, <2004" has more characters than "January 26".

Though this problem can be avoided in a number of ways (e.g., by specifying the text that is not to be matched: <[^>]*>), modern regular expression tools allow a quantifier to be specified as lazy (also known as non-greedy, reluctant, minimal, or ungreedy) by putting a question mark after the quantifier (e.g., <.*?>), or by using a modifier which reverses the greediness of quantifiers (though changing the meaning of the standard quantifiers can be confusing). By using a lazy quantifier, the expression tries the minimal match first. Though in the previous example lazy matching is used to select one of many matching results, in some cases it can also be used to improve performance when greedy matching would require more backtracking.

One Liners
===========

A *one-liner* is textual input to the command-line of an operating system shell that performs some function in just one line of input.

The one liner can be

   1. An expression written in the language of the shell.
   2. The invocation of an interpreter together with program source for the  	   interpreter to run.
   3. The invocation of a compiler together with source to compile and 	  
      instructions for executing the compiled program.

Certain dynamic scripting languages such as AWK, sed, and perl have traditionally been adept at expressing one-liners. Specialist shell interpreters such as these Unix shells or the Windows PowerShell, allow for the construction of powerful one-liners.

The use of the phrase one-liner has been widened to also include program-source for any language that does something useful in one line.

The word *One-liner* has two references in the index of the book *The AWK Programming Language* (the book is often referred to by the abbreviation TAPL). It explains the programming language AWK, which is part of the Unix operating system. The authors explain the birth of the One-liner paradigm with their daily work on early Unix machines:
::

    “The 1977 version had only a few built-in variables and predefined functions. It was designed for writing short programs [...] Our model was that an invocation would be one or two lines long, typed in and used immediately. Defaults were chosen to match this style [...] We, being the authors, knew how the language was supposed to be used, and so we only wrote one-liners.”

Notice that this original definition of a One-liner implies immediate execution of the program without any compilation. So, in a strict sense, only source code for interpreted languages qualifies as a One-liner. But this strict understanding of a One-liner was broadened in 1985 when the IOCCC introduced the category of Best One Liner for C, which is a compiled language.

The TAPL book contains 20 examples of One-liners (A Handful of Useful awk One-Liners) at the end of the book's first chapter.

Here are the very first of them:

   1. Print the total number of input lines:

      END { print NR }

   2. Print the tenth input line:

      NR == 10

   3. Print the last field of every input line:

      { print $NF }

Here are examples in J:

   1. A function avg to return the average of a list of numbers:

      avg=: +/ % #

   2. Quicksort:

      quicksort=: (($:@(<#[) , (=#[) , $:@(>#[)) ({~ ?@#)) ^: (1<#)


Many one-liners are practical. For example, the following Perl one-liner will reverse all the bytes in a file:

	perl -0777e 'print scalar reverse <>' filename

One-liners are also used to show off the differential expressive power of programming languages. Frequently, one-liners are used to demonstrate programming ability. Contests are often held to see who can create the most exceptional one-liner.

The following example is a C program (a winning entry in the "Best one-liner" category of the IOCCC, here split to two lines for presentation).::
	
	main(int c,char**v){return!m(v[1],v[2]);}m(char*s,char*t){return
	*t-42?*s?63==*t|*s==*t&&m(s+1,t+1):!*t:m(s,t+1)||*s&&m(s+1,t);}

This one-liner program is a glob pattern matcher. It understands the glob characters '*' meaning 'zero or more characters' and '?' meaning exactly one character, just like most Unix shells.

Run it with two args, the string and the glob pattern. The exit status is 0 (shell true) when the pattern matches, 1 otherwise. The glob pattern must match the whole string, so you may want to use * at the beginning and end of the pattern if you are looking for something in the middle. Examples::

	$ prog foo 'f??'; echo $?

	$ prog 'best short program' '??st*o**p?*'; echo $?

Here is a one line shell script to show directories:

::

	$ ls -R | grep ":$" | sed -e 's/:$//' -e 's/[^-][^\/]*\//--/g' -e 's/^/   /' -e 's/-/|/' 


One liners in functional programming
-------------------------------------

The following Haskell program is a one-liner: it sorts its input lines asciibetically.
::

	 main = (mapM_ putStrLn . List.sort . lines) =<< getContents 

-- In ghci a qualified name like List.sort will work, although as a standalone executable you'd need to import List.

An even shorter version.
::
 
	main = interact (unlines . List.sort . lines) -- Ditto.

Python is well suited for writing one liners using lambda functions without yielding obfuscated code. Here is a one liner in Python that multiplies two matrices (represented as a list of lists)
::

	z = lambda x, y : [[ sum([x[i] [k]*y[k] [j] for k in 
	range(len(x[0]))]) for j in range(len(y[0]))] for i in range(len(x))]

Another, that prints all primes within the specified range [2, n] :
::

	z = lambda n : [x for x in range(2, n + 1) if len([i for i in 
	range(2, x) if x%i == 0]) == 0]

This performs a Discrete Time Convolution on two input lists and yields a new list
::

	z = lambda x, h : [sum((x[i - j] if i - j >= 0 and i - j < len(x) 	  else 0)*h[j]
 	 for j in range(len(h)))
 	 for i in range(len(x) + len(h) - 1)]


