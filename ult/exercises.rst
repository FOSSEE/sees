Session-1
=========

1. Login to your machine from the CLI prompt, by pressing Ctrl+Alt+F1. 

#. Logout and re-login. 

#. What is your present working directory, once you login?

#. List all the files present in your current working directory. 

#. Navigate to the ``Desktop`` directory. If such a directory is not
 present create one.

#. Navigate back to the ``home`` directory. 

#. Create a directory called ``ult`` inside another directory called
 ``sees``. Create both the directories in a single command.

#. What would be your present working directory after doing the
 following?

   ::
   
       cd ~/sees/./../

#. Use the touch command to create a file with your name in the
 ``ult`` folder.

#. Remove the file you created in the previous step. 

#. Navigate to your home directory and remove the directory
 ``sees``. Use ``rm`` command.

#. Re-create the directories ``sees`` and ``ult`` again. Now, remove
 them using the ``rmdir`` command. Use ``man`` or ``--help``, if
 required.

#. Create a file with your first-name in your home directory and copy
 it to ``sees/ult``.

#. Copy the file again, but this time, ensure that ``cp`` checks if
 such a file doesn't already exist.

#. Copy the directory ``sees` to the directory ``sttp``. 

#. Rename directory ``sttp`` with your name.

#. Create a file ``test`` and modify its permission for user and group
   to ``execute``.

#. For the same ``test`` file, change mode to ``r,w,x`` for
   all(user,group,others).

#. Change ownership of the file ``test`` to some other user (if exists).

#. Count the number of files in a directory. 

#. Create a new file ``alice.txt`` by concatenating the first 30 lines
 and the last 40 lines of ``wonderland.txt``.

#. Show the lines from 10 to 20 of ``primes.txt`` 

#. Concatenate the content of ``foo.txt`` and ``bar.txt`` in a single
 ``foobar.txt`` but with the ``source:wikipedia`` line appearing only
 once, at the end of the file. 

Session-2
=========

0. Read through the section ``REGULAR EXPRESSIONS`` in ``man grep``

1. grep the marks of the students who scored above 75 in atleast one
subject. 

#. grep the marks of all the students whose names begin with an 's'

#. grep the marks of all the students whose names begin with
consonants. 

#. change the results.sh script to accept the input files also as
arguments. 

#. Write a shell script that will take a filename as input and check
if it is executable. 

#. Modify the script in the previous step, to remove the execute
permissions, if the file is executable. 

#. Write a shell script to remove all executable files from a
 directory, when a directory is given as argument. 

#. List all the years between 2001 and 2099 which have 5 Fridays,
 Saturdays and Sundays in the month of July. Hint: ``man cal``

#. Generate frequency list of all the commands you have used, and show
 the top 5 commands along with their count. (Hint: ``history`` command
 will give you a list of all commands used.)

#. generate a word frequency list for ``wonderland.txt``. Hint: use
``grep``, ``tr``, ``sort``, ``uniq`` (or anything else that you want)

#. **Print the middle line of a file**. 

