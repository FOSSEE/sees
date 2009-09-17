More text processing
====================

``sort``
--------
Let's say we have a file which lists a few of the stalwarts of the open source community and a few details about them, like their "other" name, their homepage address, and what they are well known for or their claim to fame. 

::

  Richard Stallman%rms%GNU Project
  Eric Raymond%ESR%Jargon File
  Ian Murdock% %Debian
  Lawrence Lessig% %Creative Commons
  Linus Torvalds% %Linux Kernel
  Guido van Rossum%BDFL%Python
  Larry Wall% %Perl


The sort command enables us to do this in a flash! Just running the sort command with the file name as a parameter sorts the lines of the file alphabetically and prints the output on the terminal. 
::

  $ sort stalwarts.txt 
  Eric Raymond%ESR%Jargon File
  Guido van Rossum%BDFL%Python
  Ian Murdock% %Debian
  Larry Wall% %Perl
  Lawrence Lessig% %Creative Commons
  Linus Torvalds% %Linux Kernel
  Richard Stallman%rms%GNU Project

If you wish to sort them reverse alphabetically, you just need to pass the ``-r`` option. Now, you might want to sort the lines, based on each person's claim to fame or their "other" name. What do we do in that case? 

Below is an example that sorts the file based on "other" names. 
::

  $ sort -t % -k 2,2  stalwarts.txt

  Ian Murdock% %Debian
  Larry Wall% %Perl
  Lawrence Lessig% %Creative Commons
  Linus Torvalds% %Linux Kernel
  Guido van Rossum%BDFL%Python
  Eric Raymond%ESR%Jargon File
  Richard Stallman%rms%GNU Project

Sort command assumes white space to be the default delimiter for columns in each line. The ``-t`` option specifies the delimiting character, which is ``%`` in this case. 

The ``-k`` option starts a key at position 2 and ends it at 2, essentially telling the sort command that it should sort based on the 2nd column, which is the other name. ``sort`` also supports conflict resolution using multiple columns for sorting. You can see that the first three lines have nothing in the "other" names column. We could resolve the conflict by sorting based on the project names (the 3rd column). 

::

  $ sort -t % -k 2,2 -k 3,3  stalwarts.txt
  
  Lawrence Lessig% %Creative Commons
  Ian Murdock% %Debian
  Linus Torvalds% %Linux Kernel
  Larry Wall% %Perl
  Guido van Rossum%BDFL%Python
  Eric Raymond%ESR%Jargon File
  Richard Stallman%rms%GNU Project

``sort`` also has a lot of other options like ignoring case differences, month sort(JAN<FEB<...), merging already sorted files. ``man sort`` would give you a lot of information. 


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

  $ sort items.txt > items-sorted.txt
  $ uniq items-sorted.txt
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


``join``
--------

Now suppose we had the file ``stalwarts1.txt``, which lists the home pages of all the people listed in ``stalwarts.txt``.
::

  Richard Stallman%http://www.stallman.org
  Eric Raymond%http://www.catb.org/~esr/
  Ian Murdock%http://ianmurdock.com/
  Lawrence Lessig%http://lessig.org
  Linus Torvalds%http://torvalds-family.blogspot.com/
  Guido van Rossum%http://www.python.org/~guido/
  Larry Wall%http://www.wall.org/~larry/

It would be nice to have a single file with the information in both the files. To achieve this we use the ``join`` command. 
::

  $ join stalwarts.txt stalwarts1.txt -t %
  Richard Stallman%rms%GNU Project%http://www.stallman.org
  Eric Raymond%ESR%Jargon File%http://www.catb.org/~esr/
  Ian Murdock% %Debian%http://ianmurdock.com/
  Lawrence Lessig% %Creative Commons%http://lessig.org
  Linus Torvalds% %Linux Kernel%http://torvalds-family.blogspot.com/
  Guido van Rossum%BDFL%Python%http://www.python.org/~guido/
  Larry Wall% %Perl%http://www.wall.org/~larry/

The ``join`` command joins the two files, based on the common field present in both the files, which is the name, in this case. 

The ``-t`` option again specifies the delimiting character. Unless that is specified, join assumes that the fields are separated by spaces. 

Note that, for ``join`` to work, the common field should be in the same order in both the files. If this is not so, you could use ``sort``, to sort the files on the common field and then join the files. In the above example, we have the common field to be the first column in both the files. If this is not the case we could use the ``-1`` and ``-2`` options to specify the field to be used for joining the files. 
::

  $ join -2 2 stalwarts.txt stalwarts2.txt -t %
  Richard Stallman%rms%GNU Project%http://www.stallman.org
  Eric Raymond%ESR%Jargon File%http://www.catb.org/~esr/
  Ian Murdock% %Debian%http://ianmurdock.com/
  Lawrence Lessig% %Creative Commons%http://lessig.org
  Linus Torvalds% %Linux Kernel%http://torvalds-family.blogspot.com/
  Guido van Rossum%BDFL%Python%http://www.python.org/~guido/
  Larry Wall% %Perl%http://www.wall.org/~larry/


Generating a word frequency list
================================

Now, let us use the tools we have learnt to use, to generate a word frequency list of a text file. We shall use the free text of Alice in Wonderland.

The basic steps to achieve this task would be -

1. Eliminate the punctuation and spaces from the document. 
2. Generate a list of words.
3. Count the words.

We first use ``grep`` and some elementary ``regex`` to eliminate the non-alpha-characters. 
::

  $ grep "[A-Za-z]*" alice-in-wonderland.txt

This outputs all the lines which has any alphabetic characters on it. This isn't of much use, since we haven't done anything with the code. We only require the alphabetic characters, without any of the other junk. ``man grep`` shows us the ``-o`` option for outputting only the text which matches the regular expression.
::

  $ grep "[A-Za-z]*" -o alice-in-wonderland.txt

Not very surprisingly, we have all the words, spit out in the form of a list! Now that we have a list of words, it is quite simple to count the occurrences of the words. You would've realized that we can make use of ``sort`` and ``uniq`` commands. We pipe the output from the ``grep`` to the ``sort`` and then pipe it's output to ``uniq``.
::
  
  $ grep "[A-Za-z]*" -o alice-in-wonderland.txt | sort | uniq -c 

Notice that you get the list of all words in the document in the alphabetical order, with it's frequency written next to it. But, you might have observed that Capitalized words and lower case words are being counted as different words. We therefore, replace all the Upper case characters with lower case ones, using the ``tr`` command. 
::

  $ grep  "[A-Za-z]*" -o alice-in-wonderland.txt | tr 'A-Z' 'a-z' | sort | uniq -c 

Now, it would also be nice to have the list ordered in the decreasing order of the frequency of the appearance of the words. We sort the output of the ``uniq`` command with ``-n`` and ``-r`` options, to get the desired output. 
::

  $ grep  "[A-Za-z]*" -o alice-in-wonderland.txt | tr 'A-Z' 'a-z' | sort | uniq -c | sort -nr

Basic editing and editors
=========================

vim
---
Vim is a very powerful editor. It has a lot of commands, and all of them cannot be explained here. We shall try and look at a few, so that you can find your way around in vim. 

To open a file in vim, we pass the filename as a parameter to the ``vim`` command. If a file with that filename does not exist, a new file is created. 
::

  $ vim first.txt

To start inserting text into the new file that we have opened, we need to press the ``i`` key. This will take us into the *insert* mode from the *command* mode. Hitting the ``esc`` key, will bring us back to the *command* mode. There is also another mode of vim, called the *visual* mode which will be discussed later in the course. 

In general, it is good to spend as little time as possible in the insert mode and extensively use the command mode to achieve various tasks. 

To save the file, use ``:w`` in the command mode. From here on, it is understood that we are in the command mode, whenever we are issuing any command to vim. 

To save a file and continue editing, use ``:w FILENAME``
The file name is optional. If you donot specify a filename, it is saved in the same file that you opened. If a file name different from the one you opened is specified, the text is saved with the new name, but you continue editing the file that you opened. The next time you save it without specifying a name, it gets saved with the name of the file that you initially opened. 

To save file with a new name and continue editing the new file, use ``:saveas FILENAME``

To save and quit, use ``:wq``

To quit, use ``:q``

To quit without saving, use ``:q!``

Moving around
~~~~~~~~~~~~~

While you are typing in a file, it is in-convenient to keep moving your fingers from the standard position for typing to the arrow keys. Vim, therefore, provides alternate keys for moving in the document. Note again that, you should be in the command mode, when issuing any commands to vim. 

The basic cursor movement can be achieved using the keys, ``h`` (left), ``l`` (right), ``k`` (up) and ``j`` (down). 
::
 
             ^
             k              
       < h       l >        
             j              
             v

Note: Most commands can be prefixed with a number, to repeat the command. For instance, ``10j`` will move the cursor down 10 lines. 

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
The visual mode is a special mode that is not present in the original vi editor. It allows us to highlight text and perform actions on it. All the movement commands that have been discussed till now work in the visual mode also. The editing commands that will be discussed in the future work on the visual blocks selected, too. 

Editing commands
~~~~~~~~~~~~~~~~

The editing commands usually take the movements as arguments. A movement is equivalent to a selection in the visual mode. The cursor is assumed to have moved over the text in between the initial and the final points of the movement. The motion or the visual block that's been highlighted can be passed as arguments to the editing commands. 

+-------------------------+---------+
| Editing effect          | Command |
+=========================+=========+
| Cutting text            | ``d``   |
+-------------------------+---------+
| Copying/Yanking text    | ``y``   |
+-------------------------+---------+
| Pasting copied/cut text | ``p``   |
+-------------------------+---------+

The cut and copy commands take the motions or visual blocks as arguments and act on them. For instance, if you wish to delete the text from the current text position to the beginning of the next word, type ``dw``. If you wish to copy the text from the current position to the end of this sentence, type ``y)``.

Apart from the above commands, that take any motion or visual block as an argument, there are additional special commands. 

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

+----------------------------------------+---------+
| Finding                                          |
+========================================+=========+
| Next occurence of ``text``, forward    |``\text``|
+----------------------------------------+---------+
| Next occurence of ``text``, backward   |``?text``|
+----------------------------------------+---------+
| Search again in the same direction     | ``n``   |
+----------------------------------------+---------+
| Search again in the opposite direction | ``N``   |
+----------------------------------------+---------+
| Next occurence of ``x`` in the line    | ``fx``  |
+----------------------------------------+---------+
| Previous occurence of ``x`` in the line| ``Fx``  |
+----------------------------------------+---------+

+---------------------------------------+------------------+
| Finding and Replacing                                    |
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


scite
-----


Personalizing your Environment
==============================

.bashrc
-------
What would you do, if you want bash to execute a particular command each time you start it up? For instance, say you want the current directory to be your Desktop instead of your home folder, each time bash starts up. How would you achieve this? Bash reads and executes commands in a whole bunch of files called startup files, when it starts up. 

When bash starts up as an interactive login shell, it reads the files ``/etc/profile``, ``~/.bash_profile``, ``~/.bash_login``, and ``~/.profile`` in that order. 

When it is a shell that is not a login shell, ``~/.bashrc`` is read and the commands in it are executed. This can be prevented using the ``--norc`` option. To force bash to use another file, instead of the ``~/.bashrc`` file on startup, the ``--rcfile`` option may be used. 

Now, you know what you should do, to change the current directory to you Desktop. Just put a ``cd ~/Desktop`` into your ``~/.bashrc`` and you are set!

This example is quite a simple and lame one. The startup files are used for a lot more complex things than this. You could set (or unset) aliases and a whole bunch of environment variables in the ``.bashrc``. We shall look at them, in the next section where we look at environment variables and ``set`` command.


.vimrc
------
``.vimrc`` is a file similar to ``.bashrc`` for vim. It is a startup file that vim reads and executes, each time it starts up. The options that you would like to be set every time you use vim, are placed in the ``.vimrc`` file, so that they are automatically set each time vim starts. The recommended place for having your ``.vimrc`` is also your home directory. 

The file ``/etc/vimrc`` is the global config file and shouldn't usually be edited. You can instead edit the ``~/.vimrc`` file that is present in your home folder. 

There are a whole bunch of variables that you could set in the ``.vimrc`` file. You can look at all the options available, using the ``:set all`` command in vim. You could use the ``:help option_name`` to get more information about the option that you want to set. Once you are comfortable with what you want to set a particular variable to, you could add it to ``.vimrc``. You should also look at ``:help vimrc`` for more info on the ``.vimrc`` file. If you already have a ``.vimrc`` file, you can edit it from within vim, using ``:e $MYVIMRC`` command. We shall look at some of the most commonly used options. 

+----------------------------------+-----------------------------------------------------------------------------------+
|Command                           | Vim action                                                                        |
+==================================+===================================================================================+
|``set nocompatible``              | Explicitly disable compatibility with vi                                          |
+----------------------------------+-----------------------------------------------------------------------------------+
|``set backspace=indent,eol,start``| In the insert mode, vim allows the backspace key to delete white spaces at the    |
|                                  | start of line, line breaks and the character before which insert mode started.    |
+----------------------------------+-----------------------------------------------------------------------------------+
|set autoindent                    | Vim indents a new line with the same indentation of the previous line.            |
+----------------------------------+-----------------------------------------------------------------------------------+
|set backup                        | Vim keeps a backup copy of a file when overwriting it.                            |
+----------------------------------+-----------------------------------------------------------------------------------+
|set history=50                    | Vim keeps 50 commands and 50 search patterns in the history.                      |
+----------------------------------+-----------------------------------------------------------------------------------+
|set ruler                         | Displays the current cursor position in the lower right corner of the vim window. |
+----------------------------------+-----------------------------------------------------------------------------------+
|set showcmd                       | Displays the incomplete command in the lower right corner.                        |
+----------------------------------+-----------------------------------------------------------------------------------+
|set incsearch                     | Turns on incremental searching. Displays search results while you type.           |
+----------------------------------+-----------------------------------------------------------------------------------+

You can see the effect of the changes made to your ``.vimrc`` file by restarting vim. If you want to see the changes that you made to your ``.vimrc`` file immediately, you could source the file from within vim.

If the ``.vimrc`` file has been sourced when this instance of vim was started, you could just resource the file again::
  :so $MYVIMRC

If you just created the ``.vimrc`` file or it was not sourced when you stared this instance of vim, just replace the ``$MYVIMRC`` variable above, with the location of the ``.vimrc`` file that you created/edited.

Subshells and ``source``
========================

A subshell is just a separate instance of the shell which is a child process of the shell that launches it. Bash creates a subshell in various circumstances. Creation of subshells allows the execution of various processes simultaneously.   

  * When an external command is executed, a new subshell is created. Any built-in commands of bash are executed with int the same shell, and no new subshell is started. When an external command is run, the bash shell copies itself (along with it's environment) creating a subshell and the process is changed to the external command executed. The subshell is a child process of this shell. 

  * Any pipes being used, create a subshell. The commands on the input and output ends of the pipe are run in different subshells. 

  * You could also, explicitly tell bash to start a subshell by enclosing a list of commands between parentheses. Each of the commands in the list is executed within a single new subshell.   

To avoid creating a subshell, when running a shell script, you could use the ``source`` command. 
::

  $ source script.sh

This will run the ``script.sh`` within the present shell without creating a subshell. The ``.`` command is an alias for the source command. ``. script.sh`` is therefore equivalent to ``source script.sh``. 
