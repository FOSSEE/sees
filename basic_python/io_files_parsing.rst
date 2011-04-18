I/O
===

Input and Output are used in almost every program, we write. We shall now
learn how to

 * Output data
 * Take input from the user

Let's start with printing a string. 

::
 
    a = "This is a string"
    a
    print a
     

``print a``, obviously, is printing the value of ``a``.

As you can see, even when you type just ``a``, the value of ``a`` is shown.
But there is a difference.

Typing ``a`` shows the value of ``a`` while ``print a`` prints the string.
This difference becomes more evident when we use strings with newlines in
them.

::

    b = "A line \n New line"
    b
    print b

As you can see, just typing ``b`` shows that ``b`` contains a newline
character. While typing ``print b`` prints the string and hence the newline.

Moreover when we type just ``a``, the value ``a`` is shown only in
interactive mode and does not have any effect on the program while running it
as a script.

We shall look at different ways of outputting the data.

``print`` statement in Python supports string formatting. Various arguments
can be passed to print using modifiers.

::

    x = 1.5
    y = 2
    z = "zed"
    print "x is %2.1f y is %d z is %s" %(x, y, z)

As you can see, the values of x, y and z are substituted in place of
``%2.1f``, ``%d`` and ``%s`` respectively. 

We can also see that ``print`` statement prints a new line character
at the end of the line, everytime it is called. This can be suppressed
by using a "," at the end ``print`` statement.

Let us see this by typing out following code on an editor as ``print_example.py``

Open an editor, like ``scite``, ``emacs`` or ``vim`` and type the following. 

::

    print "Hello"
    print "World"

    print "Hello",
    print "World"

Now we run the script using ``%run /home/fossee/print_example.py`` in the
interpreter. As we can see, the print statement when used with comma in the
end, prints a space instead of a new line.

Note that Python files are saved with an extension ``.py``. 

Now we shall look at taking input from the user. We will use the
``raw_input`` for this. 

Let's type 

::

    ip = raw_input()

The cursor is blinking indicating that it is waiting for input. We now type
some random input, 

::

    an input

and hit enter.

Now let us see what is the value of ip by typing.

::

    ip

We can see that it contains the string "an input"

Note that raw_input always gives us a string. For example


::

    c = raw_input()
    5.6
    c

Now let us see the type of c.

::

    type(c)

We see that c is a string. This implies that anything you enter as input,
will be taken as a string no matter what you enter.

``raw_input`` can also display a prompt to assist the user. 

::

    name = raw_input("Please enter your name: ")

prints the string given as argument and then waits for the user input.

Files
=====

We shall, now, learn to read files, and do some basic actions on the file,
like opening and reading a file, closing a file, iterating through the file
line-by-line, and appending the lines of a file to a list.

Let us first open the file, ``pendulum.txt`` present in ``/home/fossee/``.
The file can be opened using either the absolute path or relative path. In
all of these examples we shall assume that our present working directory is
``/home/fossee/`` and hence we only need to specify the file name. To check
the present working directory, we can use the ``pwd`` command and to change
our working directory we can use the ``cd`` command. 

::

    pwd
    cd /home/fossee

Now, to open the file

::

    f = open('pendulum.txt')

``f`` is called a file object. Let us type ``f`` on the terminal to
see what it is. 

::

  f

The file object shows, the file which is open and the mode (read or write) in
which it is open. Notice that it is open in read only mode, here.

We shall first learn to read the whole file into a single variable. Later, we
shall look at reading it line-by-line. We use the ``read`` method of ``f`` to
read, all the contents of the file into the variable ``pend``. 

::

  pend = f.read()

Now, let us see what is in ``pend``, by typing 

::

  print pend

We can see that ``pend`` has all the data of the file. Type just ``pend`` to
see more explicitly, what it contains.

::

  pend

We can split the variable ``pend`` into a list, ``pend_list``, of the lines
in the file. 

::

  pend_list = pend.splitlines()

  pend_list

Now, let us learn to read the file line-by-line. But, before that we will
have to close the file, since the file has already been read till the end.

Let us close the file opened into f.

::

  f.close()

Let us again type ``f`` on the prompt to see what it shows. 

::

  f

Notice, that it now says the file has been closed. It is a good programming
practice to close any file objects that we have opened, after their job is
done.

Let us, now move on to reading files line-by-line. 

To read the file line-by-line, we iterate over the file object line-by-line,
using the ``for`` command. Let us iterate over the file line-wise and print
each of the lines.

::

  for line in open('pendulum.txt'):
      print line

As we already know, ``line`` is a dummy variable, sometimes called the loop
variable, and it is not a keyword. We could have used any other variable
name, but ``line`` seems meaningful enough.

Instead of just printing the lines, let us append them to a list,
``line_list``. We first initialize an empty list, ``line_list``. 

::

  line_list = [ ]

Let us then read the file line-by-line and then append each of the lines, to
the list. We could, as usual close the file using ``f.close`` and re-open it.
But, this time, let's leave alone the file object ``f`` and directly open the
file within the for statement. This will save us the trouble of closing the
file, each time we open it.

::

  for line in open('pendulum.txt'):
      line_list.append(line)

Let us see what ``line_list`` contains. 

::

  line_list

Notice that ``line_list`` is a list of the lines in the file, along with the
newline characters. If you noticed, ``pend_list`` did not contain the newline
characters, because the string ``pend`` was split on the newline characters.

Let us now look at how to parse data, learn some string operations to parse
files and get data out of them, and data-type conversions. 

We have a file containing a huge number of records. Each record corresponds
to the information of a student.

::

    A;010002;ANAND R;058;037;42;35;40;212;P;;


Each record consists of fields seperated by a ";". The first record is region
code, then roll number, then name, marks of second language, first language,
maths, science and social, total marks, pass/fail indicatd by P or F and
finally W if withheld and empty otherwise.

Our job is to calculate the arithmetic mean of all the maths marks in the
region B.

Now what is parsing data.

From the input file, we can see that the data we have is in the form of text.
Parsing this data is all about reading it and converting it into a form which
can be used for computations -- in our case, sequence of numbers.

Let us learn about tokenizing strings or splitting a string into smaller
units or tokens. Let us define a string first. 

::

    line = "parse this           string"

We are now going to split this string on whitespace.

::

    line.split()

As you can see, we get a list of strings. Which means, when ``split`` is
called without any arguments, it splits on whitespace. In simple words, all
the spaces are treated as one big space.

``split`` also can split on a string of our choice. This is acheived by
passing that as an argument. But first lets define a sample record from the
file.

::

    record = "A;015163;JOSEPH RAJ S;083;042;47;AA;72;244;;;"
    record.split(';')

We can see that the string is split on ';' and we get each field seperately.
We can also observe that an empty string appears in the list since there are
two semi colons without anything in between.

To recap, ``split`` splits on whitespace if called without an argument and
splits on the given argument if it is called with an argument.

Now that we know how to split a string, we can split the record and retrieve
each field seperately. But there is one problem. The region code "B" and a
"B" surrounded by whitespace are treated as two different regions. We must
find a way to remove all the whitespace around a string so that "B" and a "B"
with white spaces are dealt as same.

This is possible by using the ``strip`` method of strings. Let us define a
string, 

::

    word = "     B    "
    word.strip()

We can see that strip removes all the whitespace around the sentence. 

The splitting and stripping operations are done on a string and their result
is also a string. Hence the marks that we have are still strings and
mathematical operations are not possible on them. We must convert them into
numbers (integers or floats), before we can perform mathematical operations
on them.

We have seen that, it is possible to convert float into integers using
``int``. We shall now convert strings into floats.

::

    mark_str = "1.25"
    mark = float(mark_str)
    type(mark_str)
    type(mark)

We can see that string, ``mark_str`` is converted to a ``float``. We can
perform mathematical operations on them now.

Now that we have all the machinery required to parse the file, let us solve
the problem. We first read the file line by line and parse each record. We
see if the region code is B and store the marks accordingly. 

::

    math_B = [] # an empty list to store the marks
    for line in open("sslc1.txt"):
        fields = line.split(";")

        reg_code = fields[0]
        reg_code_clean = reg_code.strip()

        math_mark_str = fields[5]
        math_mark = float(math_mark_str)

        if reg_code == "B":
            math_B.append(math_mark)


Now we have all the maths marks of region "B" in the list math_marks_B. To
get the mean, we just have to sum the marks and divide by the length.

::

    math_B_mean = sum(math_B) / len(math_B)
    math_B_mean

.. 
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: nil
   fill-column: 77
   End:


