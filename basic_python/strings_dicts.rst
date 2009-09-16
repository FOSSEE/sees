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

