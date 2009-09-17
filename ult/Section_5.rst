Module Objectives:
==================

After successfully completing this module a participant will be able to: ::

  - Understand
    * What are archives and zipped files                              U
    * What are environment variables				      U
    * What are Shell Scripts					      U
  - Able to use file comparison commands like 			      Ap
    diff, cmp, comm
  - Create and extract archives(.tar files) and zipped files(.gz)     Ap
  - Set/Modify environment as per need	    	                      Ap
  - Create shell scripts to autmoate tasks.			      Ap

tar:
====

Introduction:
-------------

In world of Linux based distribution, *tarballs* is the term which pops up very often. It is part of the GNU project and comes as part of every distribution of GNU/Linux. Tarball is like defacto standard for releasing source code for free software. Some of common use of *tar* archives is to: *Store, backup, and transport*.

GNU tar creates and manipulates archives which are actually collections of many other files; the program provides users with an organized and systematic method for controlling a large amount of data. It is basically form of creating archive by concatenating one or more files. 

Getting Started(go go go!):
---------------------------

As mentioned previously and if not, *The best way to get started with any command line tool of Linux is to use "man".* ::

   $ man tar

or try these commands(the output may vary with different installations): ::

   $ tar --version
   tar (GNU tar) 1.20
   Copyright (C) 2008 Free Software Foundation, Inc.
   License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
   This is free software: you are free to change and redistribute it.
   There is NO WARRANTY, to the extent permitted by law.

   Written by John Gilmore and Jay Fenlason.

   $ tar --help
   Usage: tar [OPTION...] [FILE]...
   GNU `tar' saves many files together into a single tape or disk archive, and can
   restore individual files from the archive.
   Examples:
   tar -cf archive.tar foo bar  # Create archive.tar from files foo and bar.
   tar -tvf archive.tar         # List all files in archive.tar verbosely.
   tar -xf archive.tar          # Extract all files from archive.tar.  
   ____________

Creating a tar archive: 
~~~~~~~~~~~~~~~~~~~~~~~

We will do some off-the road activity for this exercise. We will use an interesting command *fortune* for creating our practice files and then performing archives of those files and directories. Content of the files would vary for users, as fortune works like that. ::

   $ mkdir fortune-files 
   $ cd fortune-files/
   $ fortune > first.txt
   $ cat first.txt 
   Expect the worst, it's the least you can do.
   $ fortune > second.txt
   $ fortune > third.txt
   $ ls
   first.txt  second.txt  third.txt

By now we have three txt files, with some random fortune content. To create a tar archive of these files we can use any of following commands according to ones convenience: ::

   $ tar --create --verbose --file=allfiles.tar first.txt second.txt third.txt
   first.txt
   second.txt
   third.txt
   $ ls
   allfiles.tar  first.txt  second.txt  third.txt

allfiles.tar is our required tar archive of all the rest of files(or archive of files mentioned in command line). Other form of the previous command are: ::

   $ tar -c -v -f allfiles.tar first.txt second.txt third.txt

or ::

   $ tar -cvf allfiles.tar first.txt second.txt third.txt
   
The general format for creating a tar archive is: ::
   
   tar [OPTION...] [FILE]... 

For our command are using these options:

   * -c to Create the archive.
   * -v for Verbose mode, to get the names of the files as they are archived.
   * -f mentioning the file name of the resulting tar archive.

To create archive of folder itself try this: ::
   
   $ tar -cvf fortune.tar fortune/

To add files to existing tar archive, option *`r`* is used: ::

   $ fortune > fourth.txt
   $ tar -r fourth.txt -vf allfiles.tar
   fourth.txt

There are other options too available for explicitly mentioning the position of archive, use *tar --help* for getting all the details.

Similarly to remove file from archive use *--delete* option: ::

   $ tar --delete second.txt -f allfiles.tar
   $ tar -tf allfiles.tar
   first.txt
   third.txt
   fourth.txt

Listing the files of archive:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once files are archived, tar command have the *`t`* option, for Listing all files in the tar file: ::

   $ tar tf allfiles.tar
   first.txt
   second.txt
   third.txt

**//this is not working for me in some cases :(**

To locate a particular file among the archive mention its name after *t* option. ::

   $ tar t second.txt allfiles.tar
   second.txt

one can also use elementary regex for locating the file, so in previous case even second.* will also return the same result.

Extracting files from archive:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To extract the content from a archive, use *`x`* option: ::

   $ mkdir extract
   $ cp allfiles.tar extract/
   $ cd extract
   $ tar -xvf allfiles.tar 
   first.txt
   second.txt
   third.txt

To extract any particular file from archive, mention the name of file after *x* option: ::

   $ tar -x second.txt -vf allfiles.tar 
   second.txt
   
    
Further Reading for this section:
---------------------------------	
	
	* http://en.wikipedia.org/wiki/Tar_(file_format)
	* http://www.gnu.org/software/tar/manual/tar.html 
	* http://linuxreviews.org/beginner/

GZip:
=====

Tar creates archives but it does not compress data by itself unless specified explicitly. Hence all the archive we create using tar command, is simply of the size of total size of all individual files. With Linux there is a compression tool known as *gzip* which is used to reduce the size of files mentioned. Whenever possible, each file is replaced by one with the extension `.gz', so unlike `tar` this command would *replace the existing file*.

Get going:
----------

As usual first commands to check out with gzip are *man* and *help*, ::

    $ man gzip
    $ gzip --help

Creating a zip of a bunch of files is fairly trivial, it can be done simply via: ::

    $ gzip [OPTION]... [FILE]...
    
Creating zip files:
~~~~~~~~~~~~~~~~~~~

Continuing from previous set of files and setup, we will like to zip them and hence the command would be: ::

    $ gzip first.txt fourth.txt second.txt third.txt
    $ ls
    allfiles.tar  first.txt.gz  fourth.txt.gz  second.txt.gz  third.txt.gz  zipped.tar.gz

Hence, as mentioned above, all original files are replaced by .gz extension. The above task can also be restated and made easy with help of some common regex expression: ::

    $ gzip *.txt

Similar to *tar* command, one can also use *`-v`* option here to see the output in *verbose* form. For the previous example, if we enable this option the result would be something like this: ::

    $ gzip -v *.txt
    first.txt:	  4.4% -- replaced with first.txt.gz
    fourth.txt:	 -7.1% -- replaced with fourth.txt.gz
    second.txt:	 -4.8% -- replaced with second.txt.gz
    third.txt:	  3.8% -- replaced with third.txt.gz    

For files of very small sizes and some other cases, one might end up with a zipped file whose size is greater then original file, but compression is always performed(so don't be disheartened in the above case, as files are larger :P). So unlike tar, here all files are zipped separately by default, to make them part of one single chunk one can use some *pipes* and *redirections* ::

    $ gzip -c *.txt > all.gz 

Now in this case, all files would be zipped, concatenated and then the output would be written to a file all.gz leaving back all the original files. In the command above *`-c`* option states to print the output to standard output(stdout) and following *`>`* would redirect the output to file all.gz. So when we decompress this file, we will get a single file named 'all' with all the content of each files concatenated one after the another. 

For creating a zip archive of a complete directory, one has to use *`-r`* options which means recursive, it makes gzip to traverse through all directory tree/structure. By default it will create zip files of each file inside the directory, that is even with the -r flag, gzip still compresses one file at a time : ::

    $ gzip -r fortune-files/
    $ gzip -rv .
    ./first.txt:	  4.4% -- replaced with ./first.txt.gz
    ./second.txt:	 -4.8% -- replaced with ./second.txt.gz
    ./third.txt:	  3.8% -- replaced with ./third.txt.gz
    ./allfiles.tar:	 96.6% -- replaced with ./allfiles.tar.gz
    ./fourth.txt:	 -7.1% -- replaced with ./fourth.txt.gz

Hence one always sees files like xxxxx.tar.gz, to create a zip of whole directory in a single file, first archive everything inside a folder and then use gzip on that. For zipping the files using tar itself, one has to use the option *`g`*. ::

    $ tar -cvzf zipped.tar.gz *.txt 
    first.txt
    fourth.txt
    second.txt
    third.txt

*Thats why gzip is designed as a complement to tar, not as a replacement.*

gzip command comes with a option *`-l`* to view the compressed file contents: ::

    $ gzip -l zipped.tar.gz
             compressed        uncompressed  ratio uncompressed_name
                332               10240      97.0% zipped.tar

Other feature of gzip is option for mentioning the kind of compression one wants. There is a option of *`-n`* where *n varies from 0 to 9* which regulate the speed/quality of compression. With *`-1`* or *`--fast`* option it means the fastest compression method (less compression) and *`--best`* or *`-9`* indicates the slowest compression method, default compression level is *`-6`*.

To decompress a already compressed file there are two options, either use *`gunzip`* command or use *`-d`* option with gzip command: ::

    $ gzip -dv *.gz 
    all.gz:	-440.4% -- replaced with all
    first.txt.gz:	  4.4% -- replaced with first.txt
    fourth.txt.gz:	 -7.1% -- replaced with fourth.txt
    second.txt.gz:	 -4.8% -- replaced with second.txt
    third.txt.gz:	  3.8% -- replaced with third.txt
    zipped.tar.gz:	 97.0% -- replaced with zipped.tar

or: ::
    
    $ gunzip -v *.gz

Both of those commands will give the same result. So here one can notice the content of file "all" which we created earlier, it will have content of all the rest of four files concatenated one after another, but "zipped.tar.gz" is zip of tar of all files, will effectively have zip of archives of all files separately, and hence the usage and importance of *tar*.

Further Reading for this section:
---------------------------------

	* http://linuxreviews.org/beginner/
	* http://lowfatlinux.com/linux-gzip-gunzip.html
	* http://www.gnu.org/software/gzip/manual/gzip.html
	* http://en.wikipedia.org/wiki/ZIP_(file_format)


File Comparisons:
=================

Linux based distributions also have some utilities for checking the content of files, comparing them very quickly to other files. These operations can be looking for differences/similarities. Some of the commands which prove handy are: 

cmp:
----

If one wants to compare two files whether they are same or not, one can use this handy tool. Let us consider some situation, we run find/locate command to locate some file, and it turns out that we have a file with same name in different location, and in case we want to run a quick check on there content, cmp is the right tool. For my system I perform these tasks to illustrate the use of this command: ::

   $ find . -name quick.c
   ./Desktop/programs/quick.c
   ./c-folder/quick.c
   $ cmp Desktop/programs/quick.c c-folder/quick.c
   $

For me it returns nothing, hence that means both the files are exact copy of each other, by default, cmp is silent if the files are the same. Make some changes in one of the file and rerun the command. For me it works like this: ::

   $ cmp Desktop/programs/quick.c c-folder/quick.c
   Desktop/programs/quick.c c-folder/quick.c differ: byte 339, line 24

That is, if files differ, the byte and line number at which the first difference occurred is reported. 
 
diff:
-----

Now there are situations when one wants to exactly know the differences among two files, for them, GNU diff can show whether files are different without detailing the differences. For simple and basic usage of this programs, consider following example: ::

    $ echo -e "quick\nbrown\nfox\njumped\nover\nthe\nlazy\ndog" > allcharacters.txt
    $ echo -e "quick\nbrown\nfox\njmuped\nover\nteh\nlzay\ndog" > problem.txt
    $ diff problem.txt allcharacters.txt 
    4c4
    < jmuped
    ---
    > jumped
    6,7c6,7
    < teh
    < lzay
    ---
    > the
    > lazy

Looking at results above mentioned it is very trivial to deduce that, diff if used on two separate text files will result in line by line results for all the lines which are different. So most common use case scenario can be, got some files in various location of system with same name and size, just run diff through them and remove all the redundant files. Other similar command which one can find more effective for this can be *sdiff*, for the same files using sdiff will result in: ::

    $ sdiff problem.txt allcharacters.txt 
    quick								quick
    brown								brown
    fox									fox
    jmuped							      |	jumped
    over								over
    teh								      |	the
    lzay							      |	lazy
    dog								      	dog   

Some exercise for a change:
 
     * Try using diff for any binary file, does it work? 
     * What are other equivalent for diff command based on needs/requirements?
     * Can we use diff to compare two directories? If yes how?

comm:
-----

This is one more command which proves handy at times, the short and sweet man page states "compare two sorted files line by line". Or this it compares sorted files and selects or rejects lines common to two files. For ex: ::

   $ sort allcharacters.txt>sortedcharac.txt; sort problem.txt>sortedprob.txt
   $ comm sortedcharac.txt sortedprob.txt 
		brown
		dog
		fox
	jmuped
   jumped
   lazy
	lzay
		over
		quick
	teh
   the

Environment Variables:
======================

These variables like HOME, OSTYPE,Variables are a way of passing information from the shell to programs when you run them. Programs look "in the environment" for particular variables and if they are found will use the values stored. Standard UNIX variables are split into two categories, environment variables and shell variables. In broad terms, shell variables apply only to the current instance of the shell and are used to set short-term working conditions; environment variables have a farther reaching significance, and those set at login are valid for the duration of the session.By convention, environment variables have UPPER CASE and shell variables have lower case names.  

Some of examples of Environment variables are(result may vary!): ::

   $ echo $OSTYPE 
   linux-gnu
   $ echo $HOME
   /home/baali 

To see all the variables and there values use any of following commands: ::

   $ printenv | less
   $ env

The most commonly used environment variable is "PATH", it defines a list of directories to search through when looking for a command to execute. If you decide to put your own programs in a bin directory under your home directory, you'll have to modify the path to include that directory, or the system will never find your programs (unless you happen to be in that directory when you enter the command). Here's how to change your PATH variable so it includes your personal bin directory: ::

   $ set PATH=$PATH:$HOME/bin

See the difference in value of PATH variable before and after modifying it. One can also create its own variable to make things easier: ::

   $ set repo = $HOME/Desktop/random/code
   $ cd $repo

*set* command is used to define a variable for the current shell. Try opening a new shell and use the above mentioned command, it wont work as expected. The other child process wont be able to see these variables unless we *export* them. Repeat the above mentioned activity with *export* command. Now with all new shells, *$repo* will work.

Again these changes are limited to current session. To make them permanent or get loaded each time you log in, just add those lines to *.bashrc* file. 

Further Reading:
----------------

	* http://lowfatlinux.com/linux-environment-variables.html
	* http://www.codecoffee.com/tipsforlinux/articles/030.html
	* http://www.ee.surrey.ac.uk/Teaching/Unix/unix8.html
	* http://en.wikipedia.org/wiki/Environment_variable	


Shell Scripting:
================

Basics:
-------

Shell program or shell script,a sequence of commands to a text file and tell the shell to execute the text file instead of entering the commands. The first *"Hello World"* sample for shell scripting is as easy as it sounds: ::

   $ echo '#!/bin/sh' > my-script.sh
   $ clear >> my-script.sh   
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

Try giving some file you want to search in place of fname. Please note in second line *`* its a back-quote(other key mapped with tilda), it is specifically used to get the output of one command into a variable. In this particular case name is a User defined variables (UDV) which stores the value. We access value stored in any variable using *$* symbol before name of variable.

naming conventions for variables?? do we need them??

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
   
One can use backquotes(`) also to get value of expr. ::

   $ echo `expr 6 + 3`
   9
   $ result=`expr 6 + 3`
   $ echo $result
   9

Shell uses three kinds of quotes. Double quotes("), anything enclosed among them except from variable trailing after $, and characters after \ would be printed as it is. Single quotes('), anything enclsed within them is just same, no formulation/interpretaion. Back quotes(`), anything inclosed is considered as command, or is executed. ::

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

if construct:
-------------

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

One important thing to not in shell script is spacing, with many comparison and evaluation operation a wrongly placed space will spoil all the fun. So in previous example the expression *[ $# -eq 0 ]* will work properly, but if we remove those leading or trailing spaces like *[ $# -eq 0]*, it wont work as expected, or rather throw a warning. Both *test* and *[]* do the same task of testing a expression and returning true or false.

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

   Good Morning baali, Have a nice day!
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

Now we just replace the echo command with a ``mv`` or a ``cp`` command. 
::

  for i in *.mp3
  do 
    j=$(echo "$i"|grep -o "[A-Za-z'&. ]*.mp3")
    cp "$i" "$j"
  done

As an exercise, you could try sorting the files in reverse alphabetical order and then prefix numbers to each of the filenames.  

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


Further Reading:
---------------- 
	* http://www.freeos.com/guides/lsst/ 
	* http://www.freeos.com/guides/lsst/ch02sec01.html
	* http://bash.cyberciti.biz/guide/Main_Page
	
