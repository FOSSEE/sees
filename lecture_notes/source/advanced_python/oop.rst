Object Oriented Programming
===========================

At the end of this section, you will be able to - 

- Understand the differences between Object Oriented Programming and
  Procedural Programming
- Appreciate the need for Object Oriented Programming
- Read and understand Object Oriented Programs
- Write simple Object Oriented Programs

Suppose we have a list of talks, to be presented at a conference. How would
we store the details of the talks? We could possibly have a dictionary for
each talk, that contains keys and values for Speaker, Title and Tags of the
talk. Also, say we would like to get the first name of the speaker and the
tags of the talk as a list, when required. We could do it, as below.

::

    talk = {'Speaker': 'Guido van Rossum', 
            'Title': 'The History of Python'
            'Tags': 'python,history,C,advanced'} 
            
    def get_first_name(talk):
        return talk['Speaker'].split()[0]

    def get_tags(talk):
        return talk['Tags'].split(',')

This is fine, when we have a small number of talks and a small number of
operations that we wish to perform. But, as the number of talks increases,
this gets inconvenient. Say, you are writing another function in some other
module, that uses this ``talk`` dictionary, you will also need to pass the
functions that act on ``talk`` to that function. This gets quite messy,
when you have a lot of functions and objects. 

This is where Objects come in handy. Objects, essentially, group data with
the methods that act on the data into a single block/object. 

Objects and Methods
-------------------

The idea of objects and object oriented programming is being introduced,
now, but this doesn't mean that we haven't come across objects. Everything
in Python is an object. We have been dealing with objects all the while.
Strings, lists, functions and even modules are objects in Python. As we
have seen, objects combine data along with functions that act upon the
data and we have been seeing this since the beginning. The functions that
are tied to an object are called methods. We have seen various methods,
until now. 

::

    s = "Hello World"
    s.lower()

    l = [1, 2, 3, 4, 5]
    l.append(6)

``lower`` is a string method and is being called upon ``s``, which is a
string object. Similarly, ``append`` is a list method, which is being
called on the list object ``l``. 

Functions are also objects and they can be passed to and returned from
functions, as we have seen in the SciPy section. 

Objects are also useful, because the provide a similar interface, without
us needing to bother about which exact type of object we are dealing with.
For example, we can iterate over the items in a sequence, as shown below
without really worrying about whether it's a list or a dictionary or a
file-object. 

::

    for element in (1, 2, 3):
        print element
    for key in {'one':1, 'two':2}:
        print key
    for char in "123":
        print char
    for line in open("myfile.txt"):
        print line
    for line in urllib2.urlopen('http://site.com'):
        print line
          
All objects providing a similar inteface can be used the same way.

Classes
-------

When we created a string ``s``, we obtained an object of ``type`` string. 

::

    s = "Hello World"
    type(s)
    
``s`` already comes with all the methods of strings. So, it suggests that
there should be some template, based on which the object ``s`` is built.
This template or blueprint to build an object is the Class. The class
definition gives the blueprint for building objects of that kind, and each
``object`` is an *instance* of that ``class``. 

As you would've expected, we can define our own classes in Python. Let us
define a simple Talk class for the example that we started this section
with. 

::

    class Talk:
        """A class for the Talks."""

        def __init__(self, speaker, title, tags):
            self.speaker = speaker
            self.title = title
            self.tags = tags

        def get_speaker_firstname(self):
            return self.speaker.split()[0]

        def get_tags(self):
            return self.tags.split(',')

The above example introduces a lot of new things. Let us look at it, piece
by piece. 

A class is defined using a ``class`` block -- the keyword ``class``
followed by the class name, in turn followed by a semicolon. All the
statements within the ``class`` are enclosed in it's block. Here, we have
defined a class named ``Talk``. 

Our class has the same two functions that we had defined before, to get the
speaker firstname and the tags. But along with that, we have a new function
``__init__``. We will see, what it is, in a short while. By the way, the
functions inside a class are called methods, as you already know. By
design, each method of a class requires to have the same instance of the
class, (i.e., the object) from which it was called as the first argument.
This argument is generally defined using ``self``.

``self.speaker``, ``self.title`` and ``self.tags`` are variables that
contain the respective data. So, as you can see, we have combined the data
and the methods operating on it, into a single entity, an object. 

Let's now initialize a ``Talk`` which is equivalent to the example of the
talk, that we started with. Initializing an object is similar to calling a
function. 

::

    bdfl = Talk('Guido van Rossum', 
                'The History of Python', 
                'python,history,C,advanced')

We pass the arguments of the ``__init__`` function to the class name. We
are creating an object ``bdfl``, that is an instance of the class ``Talk``
and represents the talk by Guido van Rossum on the History of Python. We
can now use the methods of the class, using the dot notation, that we have
been doing all the while. 

::

    bdfl.get_tags()
    bdfl.get_speaker_firstname()

The ``__init__`` method is a special method, that is called, each time an
object is created from a class, i.e., an instance of a class is created. 

::

    print bdfl.speaker
    print bdfl.tags
    print bdfl.title

As you can see, the ``__init__`` method was called and the variables of the
``bdfl`` object have been set. object have been set. Also notice that, the
``__init__`` function takes 4 arguments, but we have passed only three. The
first argument ``self`` as we have already seen, is a reference to the
object itself.


Inheritance
-----------

Now assume that we have a different category for Tutorials. They are almost
like talks, except that they can be hands-on or not. Now, we do not wish to
re-write the whole code that we wrote for the ``Talk`` class. Here, the
idea of inheritance comes in handy. We "inherit" the ``Talk`` class and
modify it to suit our needs. 

::

    class Tutorial(Talk):
        """A class for the tutorials."""

        def __init__(self, speaker, title, tags, handson=True):
            Talk.__init__(self, speaker, title, tags)
            self.handson = handson

        def is_handson(self):
            return self.handson

We have now derived the ``Tutorial`` class from the ``Talk`` class. The
``Tutorial`` class, has a different ``__init__`` method, and a new
``is_handson`` method. But, since it is derived from the ``Talk`` method it
also has the methods, ``get_tags`` and ``get_speaker_firstname``. This
concept of inheriting methods and values is called inheritance. 

::

    numpy = Tutorial('Travis Oliphant', 'Numpy Basics', 'numpy,python,beginner')
    numpy.is_handson()
    numpy.get_speaker_firstname()

As you can see, it has saved a lot of code duplication and effort.

That brings us to the end of the section on Object Oriented Programming. In
this section we have learnt, 

- the fundamental difference in paradigm, between Object Oriented
  Programming and Procedural Programming
- to write our own classes
- to write new classes that inherit from existing classes

.. 
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: nil
   fill-column: 75
   End:
