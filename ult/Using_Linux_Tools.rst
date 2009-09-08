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

ls
---

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


date
------

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

cd
----

Change directory. Use “ cd ..” to go up one directory.

One dot '.' represents the current directory while two dots '..' represent the parent directory.

“ cd -” will return you to the previous directory (a bit like an “undo”).

You can also use cd absolute path or cd relative path (see below):

Absolute paths

    An “ absolute path” is easily recognised from the leading forward slash, /. The / means that you start at the top level directory and continue down.

For example to get to /boot/grub you would type::

	$cd /boot/grub

This is an absolute path because you start at the top of the hierarchy and go downwards from there (it doesn't matter where in the filesystem you were when you typed the command).

Relative paths

    A “ relative path” doesn't have a preceding slash. Use a relative path when you start from a directory below the top level directory structure. This is dependent on where you are in the filesystem.

    For example if you are in root's home directory and want to get to /root/music, you type::

	$ cd music

Please note that there is no / using the above cd command. Using a / would cause this to be an absolute path, working from the top of the hierarchy downward.
