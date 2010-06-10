Classes and Objects
===================

In the previous sections we learnt about functions which provide certain level
of abstraction to our code by holding the code which performs one or more
specific functionality. We were able to use this function as many times as we
wanted. In addition to functions, Python also higher level of abstractions
through *Classes* and *Objects*. *Objects* can be loosely defined as a
collection of a set of data items and a set of methods. The data items can be
any valid Python variable or any Python object. Functions enclosed within a class
are called as *methods*. If you are thinking if methods are functions why is there
a distinction between the two? The answer to this will be given as we walk through
the concepts of *Classes* and *Objects*. *Classes* contain the definition for the
*Objects*. *Objects* are instances of *Classes*.

A class is defined using the keyword **class** followed by the class name, in
turn followed by a semicolon. The statements that a *Class* encloses are written
in a new block, i.e on the next indentation level::

  class Employee:
    def setName(self, name):
      self.name = name

    def getName(self):
      return self.name

In the above example, we defined a class with the name Employee. We also defined
two methods, setName and getName for this class. It is important to note the
differences between the normal Python functions and class methods defined above.
Each method of the class must take the same instance of the class(object) from
which it was called as the first argument. It is conventionally given the name,
*self*. Note that *self* is only a convention. You can use any other name, but
the first argument to the method will always be the same object of the class
from which the method was called. The data members that belong to the class are
called as *class attributes*. *Class attributes* are preceded by the object of
the class and a dot. In the above example, *name* is a class attribute since it
is preceded by the *self* object. *Class attributes* can be accessed from
anywhere within the class. 

We can create objects of a class outside the class definition by using the same
syntax we use to call a function with no parameters. We can assign this object
to a variable::

  emp = Employee()

In the above example, we create an object named *emp* of the class *Employee*.
All the attributes and methods of the class can be accessed by the object of the
class using the standard notation *object.attribute* or *object.method()*.
Although the first parameter of a class method is the self object, it must not
be passed as an argument when calling the method. The *self* object is implicitly
passed to the method by the Python interpreter. All other arguments passing rules
like default arguments, keyword arguments, argument packing and unpacking follow
the same rules as those for ordinary Python functions::

  >>> emp.setName('John')
  >>> name = emp.getName()
  >>> print name
  John
  >>> print emp.name
  John

If we at all try to access a class attribute before assigning a value to it, i.e
before creating it, Python raises the same error as it would raise for the
accessing undefined variable::

  >>> emp = Employee()
  >>> emp.name
  Traceback (most recent call last):
    File "class.py", line 10, in <module>
      print e.name
  AttributeError: Employee instance has no attribute 'name'

It is also possible to assign values to the attributes using the above notation::

  >>> emp = Employee()
  >>> emp.name = 'John'
  >>> print emp.name
  John

Magic methods
-------------

Python reserves a number of names starting and ending with **__**. Note that it
is a double underscore. We must not invent names of this kind in our programs.
These methods are generally referred to as *Magic methods* or sometimes called
as *Special Methods*. Each *Magic method* performs a specific function. One such
magic method we will discuss now is **__init__** method. If you are from C++
background, the **__init__** method is analogous to the class constructor. This
method is called a constructor because, it is implicitly called everytime a new
instance of the class is created. So effectively **__init__** method constructs
the object from the class and sets up some initial values for the object. Other
than the above special properties, the **__init__** method is similar to any other
class method. The argument passing rules are same for **__init__** method. Although,
since **__init__** is called when the object is created we need to pass the
arguments to the class name we call while creating the object. It passes the
arguments to the **__init__** method::

  class Employee:
    def __init__(self, name):
      self.name = name

    def getName(self):
      return self.name

  >>> emp = Employee('John')
  >>> print emp.getName()
  John


Writing Object Oriented Code
----------------------------

Object oriented code mainly encompasses three components: Encapsulation, Inheritence and Polymorphism.
Lets briefly look at each of them with examples.
