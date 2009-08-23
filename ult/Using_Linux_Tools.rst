1. Introduction to the Course
=============================

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

2. Introducing Linux
=====================

Linux (commonly pronounced ˈlɪnəks') is a generic term referring to Unix-like computer operating systems based on the Linux kernel. Their development is one of the most prominent examples of free and open source software collaboration; typically all the underlying source code can be used, freely modified, and redistributed by anyone under the terms of the GNU Global Public License (GPL) and other free software licences.

Linux is predominantly known for its use in servers, although it is installed on a wide variety of computer hardware, ranging from embedded devices and mobile phones to supercomputers. 

The name "Linux"  comes from the Linux kernel, originally written in 1991 by Linus Torvalds. The rest of the system usually comprises components such as the Apache HTTP Server, the X Window System, the GNOME and KDE desktop environments, and utilities and libraries from the GNU Project (announced in 1983 by Richard Stallman). Commonly-used applications with desktop Linux systems include the Mozilla Firefox web-browser and the OpenOffice.org office application suite. The GNU contribution is the basis for the Free Software Foundation's preferred name GNU/Linux

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

For the 2.6.29 release only, the kernel's mascot, a penguin named Tux, was temporarily replaced by Tuz in order to highlight efforts to save the Tasmanian Devil from extinction.

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
- The Linux operating system is free of charge. No user or server licenses are required.Sometimes, one cam find various Linux distributions on the shelf available for purchase, that cost is purely to cover the packaging and possible support available for the distribution.

\* The newer 'Advanced Linux Servers', now available from companies such as Redhat, actually charge a license fee because of the support and update services they provide for the operating system. These services can be considered rightly charged since they are aimed at businesses that will use their operating system in critical environments where downtime and immediate support is non-negotiable.

- Linux is developed by hundreds of thousands of people worldwide. Because of this community development mode there are very fresh ideas going into the operating system and many more people to find glitches and bugs in the software than any commercial company could ever afford.

- Runtime errors and crashes are quite rare on the Linux operating system due to the way its kernel is designed and the way processes are allowed to access it. No one can guarantee that your Linux desktop or server will not crash at all, because that would be a bit extreme, however, we can say that it happens a lot less frequently in comparison with other operating systems.


- There are almost no viruses for Linux and, because there are so many people working on Linux, whenever a bug is found, a fix is provided rather quickly. Linux is much more difficult for hackers to break into as it has been designed from the ground up with security in mind.


- Linux uses less system resources than other current operating systems. You don't need the latest, fastest computer to run Linux. In fact you can run a functional version of Linux from a floppy disk with a computer that is 5-6 years old!

- Linux has been designed to put power into the hands of the user so that you have total control of the operating system and not the other way around. 

- Linux is fully compatible with all other systems, apart from offering localization to a specific region or language, targeting of specific user groups, and support for real-time applications.
