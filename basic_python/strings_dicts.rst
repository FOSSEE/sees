=======
Strings
=======

Strings were briefly introduced previously in the introduction document. In this
section strings will be presented in greater detail. All the standard operations 
that can be performed on sequences such as indexing, slicing, multiplication, length
minimum and maximum can be performed on string variables as well. One thing to
be noted is that strings are immutable, which means that string variables are
unchangeable. Hence, all item and slice assignments on strings are illegal.
Let us look at a few example.

::

  >>> name = 'PythonFreak'
  >>> print name[3]
  h
  >>> print name[-1]
  k
  >>> print name[6:]
  Freak
  >>> name[6:0] = 'Maniac'
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: 'str' object does not support item assignment

This is quite expected, since string objects are immutable as already mentioned.
The error message is clear in mentioning that 'str' object does not support item
assignment.

String Formatting
=================

String formatting can be performed using the string formatting operator represented
as the percent (%) sign. The string placed before the % sign is formatted with 
the value placed to the right of it. Let us look at a simple example.

::

  >>> format = 'Hello %s, from PythonFreak'
  >>> str1 = 'world!'
  >>> print format % str1
  Hello world!, from PythonFreak

The %s parts of the format string are called the coversion specifiers. The coversion
specifiers mark the places where the formatting has to be performed in a string. 
In the example the %s is replaced by the value of str1. More than one value can 
also be formatted at a time by specifying the values to be formatted using tuples
and dictionaries (explained in later sections). Let us look at an example.

::

  >>> format = 'Hello %s, from %s'
  >>> values = ('world!', 'PythonFreak')
  >>> print format % values
  Hello world!, from PythonFreak

In this example it can be observed that the format string contains two conversion 
specifiers and they are formatted using the tuple of values as shown.

The s in %s specifies that the value to be replaced is of type string. Values of 
other types can be specified as well such as integers and floats. Integers are 
specified as %d and floats as %f. The precision with which the integer or the 
float values are to be represented can also be specified using a **.** (**dot**)
followed by the precision value.

String Methods
==============

Similar to list methods, strings also have a rich set of methods to perform various
operations on strings. Some of the most important and popular ones are presented
in this section.

**find**
~~~~~~~~

The **find** method is used to search for a substring within a given string. It 
returns the left most index of the first occurence of the substring. If the 
substring is not found in the string then it returns -1. Let us look at a few 
examples.

::

  >>> longstring = 'Hello world!, from PythonFreak'
  >>> longstring.find('Python')
  19
  >>> longstring.find('Perl')
  -1

**join**
~~~~~~~~

The **join** method is used to join the elements of a sequence. The sequence 
elements that are to be join ed should all be strings. Let us look at a few 
examples.

::
  
  >>> seq = ['With', 'great', 'power', 'comes', 'great', 'responsibility']
  >>> sep = ' '
  >>> sep.join(seq)
  'With great power comes great responsibility'
  >>> sep = ',!'
  >>> sep.join(seq)
  'With,!great,!power,!comes,!great,!responsibility'

*Try this yourself*

::

  >>> seq = [12,34,56,78]
  >>> sep.join(seq)

**lower**
~~~~~~~~~

The **lower** method, as the name indicates, converts the entire text of a string
to lower case. It is specially useful in cases where the programmers deal with case
insensitive data. Let us look at a few examples.

::

  >>> sometext = 'Hello world!, from PythonFreak'
  >>> sometext.lower()
  'hello world!, from pythonfreak'

**replace**
~~~~~~~~~~~

The **replace** method replaces a substring with another substring within
a given string and returns the new string. Let us look at an example.

::

  >>> sometext = 'Concise, precise and criticise is some of the words that end with ise'
  >>> sometext.replace('is', 'are')
  'Concaree, precaree and criticaree are some of the words that end with aree'

Observe here that all the occurences of the substring *is* have been replaced,
even the *is* in *concise*, *precise* and *criticise* have been replaced.

**split**
~~~~~~~~~

The **split** is one of the very important string methods. split is the opposite of the 
**join** method. It is used to split a string based on the argument passed as the
delimiter. It returns a list of strings. By default when no argument is passed it
splits with *space* (' ') as the delimiter. Let us look at an example.

::

  >>> grocerylist = 'butter, cucumber, beer(a grocery item??), wheatbread'
  >>> grocerylist.split(',')
  ['butter', ' cucumber', ' beer(a grocery item??)', ' wheatbread']
  >>> grocerylist.split()
  ['butter,', 'cucumber,', 'beer(a', 'grocery', 'item??),', 'wheatbread']

Observe here that in the second case when the delimiter argument was not set 
**split** was done with *space* as the delimiter.

**strip**
~~~~~~~~~

The **strip** method is used to remove or **strip** off any whitespaces that exist
to the left and right of a string, but not the whitespaces within a string. Let 
us look at an example.

::

  >>> spacedtext = "               Where's the text??                 "
  >>> spacedtext.strip()
  "Where's the text??"

Observe that the whitespaces between the words have not been removed.

::

  Note: Very important thing to note is that all the methods shown above do not
        transform the source string. The source string still remains the same.
	Remember that **strings are immutable**.

Introduction to the standard library
====================================

Python is often referred to as a "Batteries included!" language, mainly because 
of the Python Standard Library. The Python Standard Library provides an extensive
set of features some of which are available directly for use while some require to
import a few **modules**. The Standard Library provides various built-in functions
like:

    * **abs()**
    * **dict()**
    * **enumerate()**

The built-in constants like **True** and **False** are provided by the Standard Library.
More information about the Python Standard Library is available http://docs.python.org/library/


I/O: Reading and Writing Files
==============================

Files are very important aspects when it comes to computing and programming.
Up until now the focus has been on small programs that interacted with users
through **input()** and **raw_input()**. Generally, for computational purposes
it becomes necessary to handle files, which are usually large in size as well.
This section focuses on basics of file handling.

Opening Files
~~~~~~~~~~~~~

Files can be opened using the **open()** method. **open()** accepts 3 arguments
out of which 2 are optional. Let us look at the syntax of **open()**:

*f = open( filename, mode, buffering)*

The *filename* is a compulsory argument while the *mode* and *buffering* are 
optional. The *filename* should be a string and it should be the complete path
to the file to be opened (The path can be absolute or relative). Let us look at
an example.

::

  >>> f = open ('basic_python/interim_assessment.rst')
  
The *mode* argument specifies the mode in which the file has to be opened.
The following are the valid mode arguments:

**r** - Read mode
**w** - Write mode
**a** - Append mode
**b** - Binary mode
**+** - Read/Write mode

The read mode opens the file as a read-only document. The write mode opens the
file in the Write only mode. In the write mode, if the file existed prior to the
opening, the previous contents of the file are erased. The append mode opens the
file in the write mode but the previous contents of the file are not erased and
the current data is appended onto the file.
The binary and the read/write modes are special in the sense that they are added
onto other modes. The read/write mode opens the file in the reading and writing
mode combined. The binary mode can be used to open a files that do not contain 
text. Binary files such as images should be opened in the binary mode. Let us look
at a few examples.

::

  >>> f = open ('basic_python/interim_assessment.rst', 'r')
  >>> f = open ('armstrong.py', 'r+')

The third argument to the **open()** method is the *buffering* argument. This takes
a boolean value, *True* or *1* indicates that buffering has to be enabled on the file,
that is the file is loaded on to the main memory and the changes made to the file are 
not immediately written to the disk. If the *buffering* argument is *0* or *False* the 
changes are directly written on to the disk immediately.

Reading and Writing files
~~~~~~~~~~~~~~~~~~~~~~~~~

**write()**
-----------

**write()**, evidently, is used to write data onto a file. It takes the data to 
be written as the argument. The data can be a string, an integer, a float or any
other datatype. In order to be able to write data onto a file, the file has to
be opened in one of **w**, **a** or **+** modes.

**read()**
----------

**read()** is used to read data from a file. It takes the number of bytes of data
to be read as the argument. If nothing is specified by default it reads the entire 
contents from the current position to the end of file.

Let us look at a few examples:

::

  >>> f = open ('randomtextfile', 'w')
  >>> f.write('Hello all, this is PythonFreak. This is a random text file.')
  >>> f = open ('../randomtextfile', 'r')
  >>> f = open ('../randomtextfile', 'r')
  >>> f.read(5)
  'Hello'
  >>> f.read()
  ' all, this is PythonFreak. This is a random text file.'
  >>> f.close()

**readline()**
--------------

**readline()** is used to read a file line by line. **readline()** reads a line
of a file at a time. When an argument is passed to **readline()** it reads that
many bytes from the current line.

One other method to read a file line by line is using the **read()** and the 
**for** construct. Let us look at this block of code as an example.

::

  >>> f = open('../randomtextfile', 'r')
  >>> for line in f:
  ...     print line
  ... 
  Hello all!
  
  This is PythonFreak on the second line.
  
  This is a random text file on line 3

**close()**
-----------

One must always close all the files that have been opened. Although, files opened
will be closed automatically when the program ends. When files opened in read mode
are not closed it might lead to uselessly locked sometimes. In case of files
opened in the write mode it is more important to close the files. This is because,
Python maybe using the file in the buffering mode and when the file is not closed
the buffer maybe lost completely and the changes made to the file are lost forever.


Dictionaries
============

A dictionary in general, are designed to be able to look up meanings of words. 
Similarly, the Python dictionaries are also designed to look up for a specific
key and retrieve the corresponding value. Dictionaries are data structures that
provide key-value mappings. Dictionaries are similar to lists except that instead
of the values having integer indexes, dictionaries have keys or strings as indexes.
Let us look at an example of how to define dictionaries.

::

  >>> dct = { 'Sachin': 'Tendulkar', 'Rahul': 'Dravid', 'Anil': 'Kumble'}

The dictionary consists of pairs of strings, which are called *keys* and their
corresponding *values* separated by *:* and each of these *key-value* pairs are
comma(',') separated and the entire structure wrapped in a pair curly braces *{}*.

::

  Note: The data inside a dictionary is not ordered. The order in which you enter
  the key-value pairs is not the order in which they are stored in the dictionary.
  Python has an internal storage mechanism for that which is out of the purview 
  of this document.

**dict()**
~~~~~~~~~~

The **dict()** function is used to create dictionaries from other mappings or other
dictionaries. Let us look at an example.

::

  >>> diction = dict(mat = 133, avg = 52.53)

**String Formatting with Dictionaries:**

String formatting was discussed in the previous section and it was mentioned that
dictionaries can also be used for formatting more than one value. This section 
focuses on the formatting of strings using dictionaries. String formatting using
dictionaries is more appealing than doing the same with tuples. Here the *keyword*
can be used as a place holder and the *value* corresponding to it is replaced in
the formatted string. Let us look at an example.

::

  >>> player = { 'Name':'Rahul Dravid', 'Matches':133, 'Avg':52.53, '100s':26 }
  >>> strng = '%(Name)s has played %(Matches)d with an average of %(Avg).2f and has %(100s)d hundreds to his name.'
  >>> print strng % player
  Rahul Dravid has played 133 with an average of 52.53 and has 26 hundreds to his name.

Dictionary Methods
~~~~~~~~~~~~~~~~~~

**clear()**
-----------

The **clear()** method removes all the existing *key-value* pairs from a dictionary.
It returns *None* or rather does not return anything. It is a method that changes
the object. It has to be noted here that dictionaries are not immutable. Let us 
look at an example.

::
  
  >>> dct
  {'Anil': 'Kumble', 'Sachin': 'Tendulkar', 'Rahul': 'Dravid'}
  >>> dct.clear()
  >>> dct
  {}

**copy()**
----------

The **copy()** returns a copy of a given dictionary. Let us look at an example.

::

  >>> dct = {'Anil': 'Kumble', 'Sachin': 'Tendulkar', 'Rahul': 'Dravid'}
  >>> dctcopy = dct.copy()
  >>> dctcopy
  {'Anil': 'Kumble', 'Sachin': 'Tendulkar', 'Rahul': 'Dravid'}


**get()**
---------

**get()** returns the *value* for the *key* passed as the argument and if the
*key* does not exist in the dictionary, it returns *None*. Let us look at an
example.

::

  >>> print dctcopy.get('Saurav')
  None
  >>> print dctcopy.get('Anil')
  Kumble

**has_key()**
-------------

This method returns *True* if the given *key* is in the dictionary, else it returns 
*False*.

::

  >>> dctcopy.has_key('Saurav')
  False
  >>> dctcopy.has_key('Sachin')
  True

**pop()**
---------

This method is used to retrieve the *value* of a given *key* and subsequently 
remove the *key-value* pair from the dictionary. Let us look at an example.

::

  >>> print dctcopy.pop('Sachin')
  Tendulkar
  >>> dctcopy
  {'Anil': 'Kumble', 'Rahul': 'Dravid'}

**popitem()**
-------------

This method randomly pops a *key-value* pair from a dictionary and returns it.
The *key-value* pair returned is removed from the dictionary. Let us look at an
example.

::

  >>> print dctcopy.popitem()
  ('Anil', 'Kumble')
  >>> dctcopy
  {'Rahul': 'Dravid'}

  Note that the item chosen is completely random since dictionaries are unordered
  as mentioned earlier.

**update()**
------------

The **update()** method updates the contents of one dictionary with the contents
of another dictionary. For items with existing *keys* their *values* are updated,
and the rest of the items are added. Let us look at an example.

::

  >>> dctcopy.update(dct)
  >>> dct
  {'Anil': 'Kumble', 'Sachin': 'Tendulkar', 'Rahul': 'Dravid'}
  >>> dctcopy
  {'Anil': 'Kumble', 'Sachin': 'Tendulkar', 'Rahul': 'Dravid'}

