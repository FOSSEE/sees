Lists and Tuples
================

Python provides an intuitive way to represent a group items, called *Lists*. The
items of a *List* are called its elements. Unlike C/C++, elements can be of any
type. A *List* is represented as a list of comma-sepated elements with paren-
thesis around them::

  >>> a = [10, 'Python programming', 20.3523, 23, 3534534L]
  >>> a
  [10, 'Python programming', 20.3523, 23, 3534534L]


Common List Operations
----------------------


Indexing
~~~~~~~~

Individual elements of a *List* can be accessed using an index to the element.
The indices start at 0. One can also access the elements of the *List* in reverse
using negative indices.::

  >>> a[1]
  'Python programming'
  >>> a[-1]
  3534534L

It is important to note here that the last element of the *List* has an index of
-1.


Concatenating
~~~~~~~~~~~~~

Two or more *Lists* can be concatenated using the + operator::

  >>> a + ['foo', 12, 23.3432, 54]
  [10, 'Python programming', 20.3523, 'foo', 12, 23.3432, 54]
  >>> [54, 75, 23] + ['write', 67, 'read']
  [54, 75, 23, 'write', 67, 'read']
  

Slicing
~~~~~~~

A *List* can be sliced off to contain a subset of elements of the *List*. Slicing
can be done by using two indices separated by a colon, where the first index is
inclusive and the second index is exclusive. The resulting slice is also a *List*.::

  >>> num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  >>> num[3:6]
  [4, 5, 6]
  >>> num[0:1]
  [1]
  >>> num[7:10]
  [7, 8, 9]

The last example showed how to access last 3 elements of the *List*. There is a 
small catch here. The second index 10 actually refers to the 11th element of the
*List* which is still valid, even though it doesn't exist because the second 
index is exclusive and tells the Python interpreter to get the last element of
the *List*. But this can also be done in a much easier way using negative indices::

  >>> num[-3:-1]
  [7, 8, 9]

Excluding the first index implies that the slice must start at the beginning of 
the *List*, while excluding the second index includes all the elements till the
end of the *List*. A third parameter to a slice, which is implicitly taken as 1
is the step of the slice. It is specified as a value which follows a colon after
the second index::

  >>> num[:4]
  [1, 2, 3, 4]
  >>> num[7:]
  [8, 9]
  >>> num[-3:]
  [7, 8, 9]
  >>> num[:]
  [1, 2, 3, 4, 5, 6, 7, 8, 9]
  >>> num[4:9:3]
  [5, 8]
  >>> num[3::2]
  [4, 6, 8]
  >>> num[::4]
  [1, 5, 9]


Multiplication
~~~~~~~~~~~~~~

A *List* can be multiplied with an integer to repeat itself::

  >>> [20] * 5
  [20, 20, 20, 20, 20]
  >>> [42, 'Python', 54] * 3
  [42, 'Python', 54, 42, 'Python', 54, 42, 'Python', 54]


Membership
~~~~~~~~~~

**in** operator is used to find whether an element is part of the *List*. It
returns **True** if the element is present in the *List* or **False** if it is not 
present. Since this operator returns a Boolean value it is called a Boolean
operator::

  >>> names = ['Guido', 'Alex', 'Tim']
  >>> 'Tim' in names
  True
  >>> 'Adam' in names
  False


Length, Maximum and Minimum
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Length of a *List* can be found out using the len function. The max function
returns the element with the largest value and the min function returns the 
element with the smallest value::

  >>> num = [4, 1, 32, 12, 67, 34, 65]
  >>> len(num)
  7
  >>> max(num)
  67
  >>> min(num)
  1


Changing Elements
~~~~~~~~~~~~~~~~~

Unlike Strings *Lists* are mutable, i.e. elements of a *List* can be manipulated::

  >>> a = [1, 3, 5, 7]
  >>> a[2] = 9
  >>> a
  [1, 3, 9, 7]


Deleting Elements
~~~~~~~~~~~~~~~~~

An element or a slice of a *List* can be deleted by using the **del** statement::

  >>> a = [1, 3, 5, 7, 9, 11]
  >>> del a[-2:]
  >>> a
  [1, 3, 5, 7]
  >>> del a[1]
  >>> a
  [1, 5, 7]


Assign to Slices
~~~~~~~~~~~~~~~~

In the same way, values can be assigned to individual elements of the *List*, 
a *List* of elements can be assigned to a slice::

  >>> a = [2, 3, 4, 5]
  >>> a[:2] = [0, 1]
  [0, 1, 4, 5]
  >>> a[2:2] = [2, 3]
  >>> a
  [0, 1, 2, 3, 4, 5]
  >>> a[2:4] = []
  >>> a
  [0, 1, 4, 5]

The last two examples should be particularly noted carefully. The last but one
example insert elements or a list of elements into a *List* and the last example
deletes a list of elements from the *List*.


None, Empty Lists, and Initialization
-------------------------------------

An *Empty List* is a *List* with no elements and is simply represented as
[]. A *None List* is one with all elements in it being **None**. It serves
the purpose having a container list of some fixed number of elements with
no value::

  >>> a = []
  >>> a
  []
  >>> n = [None] * 10
  >>> n
  [None, None, None, None, None, None, None, None, None, None]


Nested Lists
------------

As mentioned earlier, a List can contain elements of any data type. This also
implies a *List* can have a *Lists* themselves as its elements. These are 
called as *Nested Lists*. There is no limit on the depth of the *Nested Lists*::

  >>> a = [1, [1, 2, 3], 3, [1, [1, 2, 3]], 7]


List Methods
------------

A method is a function that is coupled to an object. More about objects
and its methods are discussed in Advanced Python module. In general, a
method is called like::

  object.method(arguments)

For now, it is enough to know that a list of elements is an object and
so *List* methods can be called upon them. Also some of the methods change
the *List* in-place, meaning it modifies the existing list instead of creating
a new one, while other methods don't. It must be noted as we run through
the *List* methods.

Some of the most commonly used *List* methods are as follows:


append
~~~~~~

The *append* method is used to append an object at the end of the list::

  >>> prime = [2, 3, 5]
  >>> prime.append(7)
  >>> prime
  [2, 3, 5, 7]

It is important to note that append changes the *List* in-place.


count
~~~~~

The *count* method returns the number of occurences of a particular element
in a list::

  >>> [1, 4, 4, 9, 9, 9].count(9)
  3
  >>> tlst = ['Python', 'is', 'a', 'beautiful', 'language']
  >>> tlst.count('Python')
  1


extend
~~~~~~

The *extend* method extends the list on which it is called by the list supplied
as argument to it::

  >>> a = [1, 2, 3]
  >>> b = [4, 5, 6]
  >>> a.extend(b)
  [1, 2, 3, 4, 5, 6]

This is an in-place method. This method is equivalent to using the + operator, but
using the + operator returns a new list.


index
~~~~~

The *index* method returns the index position of the element in the list 
specified as argument::

  >>> a = [1, 2, 3, ,4, 5]
  >>> a.index(4)
  3


insert
~~~~~~

The *insert* method is used to insert an element specified as the second 
argument to the list at the position specified by the first argument::

  >>> a = ['Python', 'is', 'cool']
  >>> a.insert(2, 'so')
  >>> a
  ['Python', 'is', 'so', 'cool']

The *insert* method changes the *List* in-place.


pop
~~~

The *pop* method removes an element from the list. The index position
of the element to be removed can be specified as an argument to the
*pop* method, if not it removes the last element by default::

  >>> a = [1, 2, 3, 4, 5]
  >>> a.pop()
  >>> a
  5
  >>> a.pop(2)
  >>> a
  3

The *pop* method changes the *List* in-place.


remove
~~~~~~

The *remove* method removes the first occurence of an element supplied as a
parameter::

  >>> a = [1, 2, 3, 4, 2, 5, 2]
  >>> a.remove(2)
  >>> a
  [1, 3, 4, 2, 5, 2]


reverse
~~~~~~~

The *reverse* method reverses elements in the list. It is important to note
here that *reverse* method changes the list in-place and doesn't return any
thing::

  >>> a = ['guido', 'alex', 'tim']
  >>> a.reverse()
  >>> a
  ['tim', 'alex', 'guido']


sort
~~~~

The *sort* method is used to sort the elements of the list. The *sort* method
also sorts in-place and does not return anything::

  >>> a = [5, 1, 3, 7, 4]
  >>> a.sort()
  >>> a
  [1, 3, 4, 5, 7]

In addition to the sort method on a *List* object we can also use the built-in
**sorted** function. This function takes the *List* as a parameter and returns
a sorted copy of the list. However the original list is left intact::

  >>> a = [5, 1, 3, 7, 4]
  >>> b = sorted(a)
  >>> b
  [1, 3, 4, 5, 7]
  >>> a
  [5, 1, 3, 7, 4]

