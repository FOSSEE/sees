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

