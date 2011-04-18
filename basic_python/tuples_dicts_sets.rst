We shall now look at a few more datatypes available in Python, namely,
tuples, dictionaries and sets. Let us start with tuples. 

Tuples
======

We shall learn

 * what are tuples
 * their similarities and dissimilarities with lists
 * why are they needed

Let's get started by defining a tuple. A tuple is defined by enclosing
parentheses around a sequence of items seperated by commas. It is similar to
defining a list except that parentheses are used instead of square brackets.

::

    t = (1, 2.5, "hello", -4, "world", 1.24, 5)
    t

defines a tuple. 

It is not always necessary to use parenthesis around a ``tuple``

::
    a = 1, 2, 3
    a
    (1, 2, 3)

    b = 1, 
    b
    (1,)

The items in the tuple are indexed using numbers and can be accessed by using
their position.

::

    t[3]

prints -4 which is the fourth item of the tuple.

::

    t[1:5:2]

prints the corresponding slice

This is the behaviour similar as to lists. But the difference can be seen
when we try to change an element in the tuple.

::

    t[2] = "Hello"

We can see that, it raises an error saying tuple does not support item
assignment. Tuples are immutable, and cannot be changed after creation.

Then, what's the use of tuples?

We shall understand that soon. But let us look at a simple problem of
swapping values.

``a = 5`` and ``b = 7``. swap the values of a and b

We define the two values

::

    a = 5
    b = 7

    a
    b

Traditionally, we swap them using a temporary variable. 

::

    temp = a
    a = b
    b = temp

    a
    b

The Python way, would be 

::

    a
    b

    a, b = b, a

    a
    b

We see that the values are swapped. This idiom works for different data-types
also.

::

    a = 2.5
    b = "hello"

    a
    b

Moreover this type of behaviour is something that feels natural and you'd
expect to happen.

This is possible because of the immutability of tuples. This process is
called tuple packing and unpacking.

Let us first see what is tuple packing. Type

::

    5,

What we see is a tuple with one element.

::

    5, "hello", 2.5

Now it is a tuple with three elements.

So when we are actually typing two or more elements seperated by commas,
those elements are packed into a tuple.

When you type
::

    a, b = b, a

First the values of b and a are packed into a tuple on the right side and then
unpacked into the variables a and b.

Immutability of tuples ensures that the values are not changed during the
packing and unpacking.

That brings us to the end of our discussion of tuples. Let us now look at
dictionaries. 

Dictionaries
============

A dictionary in general, are designed to be able to look up meanings of
words. Similarly, the Python dictionaries are also designed to look up for a
specific key and retrieve the corresponding value. Dictionaries are data
structures that provide key-value mappings. Dictionaries are similar to lists
except that instead of the values having integer indexes, dictionaries have
keys or strings as indexes. 

We shall now look at creating dictionaries, accessing elements of
dictionaries, checking for presence of elements and iterating over the
elements. 

Let us start by creating an empty dictionary, type the following in
your IPython interpreter.

::

    mt_dict = {}    

Notice that curly braces are used define dictionaries.

Now let us see how to create a non-empty dictionary,

::

    extensions = {'jpg' : 'JPEG Image', 
                  'py' : 'Python script', 
                  'html' : 'Html document', 
                  'pdf' : 'Portable Document Format'}

Notice that each key-value pair is separated by a comma, and each key and
value are separated using a colon.

Here, we defined four entries in the dictionary extensions. The keys are
``jpg``, ``py``, ``html``, and ``pdf``.

Simply type,

::

    extensions

in the interpreter to see the content of the dictionary. Notice that in
dictionaries the order cannot be predicted and you can see that the values
are not in the order that we entered in.

Like in lists, the elements in a dictionary can be accessed using the
index, here the index is the key. Try,

::

    print extensions['jpg']

It printed JPEG Image. And now try,

::

    print extensions['zip']

As expected it gave us an error. Obviously, our dictionary didn't have any
key 'zip', and that's what the error message says.

Well that was about creating dictionaries, now how do we add or delete items.

::

    extensions['cpp'] = 'C++ code'

Adds a new key value pair, ``cpp : C++ code``

We delete items using the ``del`` keyword

::

    del extension['pdf']

Let us check the content of the dictionary now,

::

    extensions

So the changes have been made. Now let us try one more thing,

::

    extensions['cpp'] = 'C++ source code'
    extensions

As you can see, it neither added a new thing nor gave an error, but it
simply replaced the existing value with the new one.

Now let us learn how to check if a particular key is present in the
dictionary. For that we can use ``in``,

::

    'py' in extensions
    'odt' in extensions

It will return ``True`` if the key is found in the dictionary, and
will return ``False`` if key is not present. Note that we can check
only for container-ship of keys in dictionaries and not values.

Now let us see how to retrieve the keys and values. We can use the
method ``keys()`` for getting a list of the keys in a particular
dictionary and the method ``values()`` for getting a list of
values. Let us try them,

::

    extensions.keys()

It returned the ``list`` of keys in the dictionary extensions. And now
the values, 

::

    extensions.values()

It returned the ``list`` of values in the dictionary.

Now let us print the data in the dictionary. We can use ``for`` loop to
iterate.

::

    for each in extensions.keys():
        print each, "-->", extensions[each]


This brings us to the end of our discussion on dictionaries. Let us now look
at sets. 

Sets
====

We shall look at, 

 * sets 
 * operations on sets

Sets are collections of unique elements. ``set`` datastructure in Python
provides an implementation of this. 

Lets look at how to input sets.

::
 
    a_list = [1, 2, 1, 4, 5, 6, 2]
    a = set(a_list)
    a
     
We can see that duplicates are removed and the set contains only unique
elements.

::

    f10 = set([1, 2, 3, 5, 8])
    p10 = set([2, 3, 5, 7])

* f10 is the set of fibonacci numbers from 1 to 10.
* p10 is the set of prime numbers from 1 to 10.

Various operations that we do on sets are possible here also.

The | (pipe) character stands for union

::

    f10 | p10

gives us the union of f10 and p10

The & (ampersand) character stands for intersection.

::

    f10 & p10

gives the intersection

similarly,

::

    f10 - p10

gives all the elements that are in f10 but not in p10

::

    f10 ^ p10

is all the elements in f10 union p10 but not in f10 intersection p10. In
mathematical terms, it gives the symmectric difference.

Sets also support checking of subsets.

::

    b = set([1, 2])
    b < f10

gives a ``True`` since b is a proper subset of f10.

Similarly,
::

    f10 < f10

gives a ``False`` since f10 is not a proper subset.

Where as, 

::

    f10 <= f10

gives ``True`` since every set is a subset of itself.

Sets can be iterated upon just like lists and tuples. 

::

    for i in f10:
        print i,

prints the elements of f10.

The length and containership check on sets is similar as in lists and tuples.

::

    len(f10)

shows 5. And

::
    
    1 in f10
    4 in f10

prints ``True`` and ``False`` respectively

The order in which elements are organised in a set is not to be relied upon.
There is no ordering of elements of a set. Sets do not support indexing and
hence slicing and striding do not make sense, either. 

Here's an example that shows the use of sets. 

Given a list of marks, marks = [20, 23, 22, 23, 20, 21, 23] list all the
duplicates

Duplicates marks are the marks left out when we remove each element of the 
list exactly one time.

::

    marks = [20, 23, 22, 23, 20, 21, 23] 
    marks_set = set(marks)
    for mark in marks_set:
        marks.remove(mark)

    # we are now left with only duplicates in the list marks
    duplicates = set(marks)

This brings us to the end of our discussion on sets. 
.. 
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: nil
   fill-column: 77
   End:


