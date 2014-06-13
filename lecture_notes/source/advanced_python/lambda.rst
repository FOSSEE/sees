Functional programming
======================

In this section, we shall look at a different style of programming called
Functional programming, which is supported by Python. 

The fundamental idea behind functional programming is that the output of a
function, should not depend on the state of the program. It should only
depend on the inputs to the program and should return the same output,
whenever the function is called with the same arguments. Essentially, the
functions of our code, behave like mathematical functions, where the output
is dependent only on the variables on which the function depends. There is
no "state" associated with the program. 

Let's look at some of the functionality that Python provides for writing
code in the Functional approach.

List Comprehensions
-------------------

Let's take a very simple problem to illustrate how list comprehensions
work. Let's say, we are given a list of weights of people, and we need to
calculate the corresponding weights on the moon. Essentially, return a new
list, with each of the values divided by 6.0. 

It's a simple problem, and let's first solve it using a ``for`` loop. We
shall initialize a new empty, list and keep appending the new weights
calculated

::

    weights = [30, 45.5, 78, 81, 55.5, 62.5]
    
    weights_moon = []

    for w in weights:
        weights_moon.append(w/6.0)

    print weights_moon

We had to initialize an empty list, and write a ``for`` loop that appends
each of the values to the new list. List comprehensions provide a way of
writing a one liner, that does the same thing, without resorting to
initializing a new empty list. Here's how we would do it, using list
comprehensions

::

    [ w/6.0 for w in weights ]
    
As we can see, we have the same list, that we obtained previously, using
the ``for`` loop. 

Let's now look at a slightly more complex example, where we wish to
calculate the weights on the moon, only if the weight on the earth is
greater than 50. 

::

    weights = [30, 45.5, 78, 81, 55.5, 62.5]
    weights_moon = []
    for w in weights:
        if w > 50:
            weights_moon.append(w/6.0)

    print weights_moon

The ``for`` loop above can be translated to a list comprehension as shown

::

    [ w/6.0 for w in weights if w>50 ]

Now, let's change the problem again. Say, we wish to give the weight on the
moon (divide by 6), when the weight is greater than 50, otherwise triple
the weight.

::

    weights = [30, 45.5, 78, 81, 55.5, 62.5]
    weights_migrate = []
    for w in weights:
        if w > 50:
            weights_migrate.append(w/6.0)
        else:
            weights_migrate.append(w * 3.0)

    print weights_migrate

This problem, however, cannot be translated into a list comprehension. We
shall use the  ``map`` built-in, to solve the problem in a functional
style. 

``map``
-------

But before getting to the more complex problem, let's solve the easier
problem of returning the weight on moon for all the weights. 

The ``map`` function essentially allows us to apply a function to all the
elements of a list, and returns a new list that consists of the outputs
from each of the call. So, to use ``map`` we need to define a function,
that takes an input and returns a sixth of it.

::
    
    def moonize(weight):
        return weight/6.0

Now, that we have our ``moonize`` function, we can pass the function and the
list of weights as an argument to ``map`` and get the required list. 

::

    map(moonize, weights)

Let's define a new function, that compares the weight value with 50 and
returns a new value based on the condition. 

::

    def migrate(weight):
        if weight < 50:
            return weight*3.0
        else:
            return weight/6.0

Now, we can use ``map`` to obtain the new weight values

::

    map(migrate, weights)

As you can see, we obtained the result, that we obtained before. 

But, defining such functions each time, is slightly inconvenient. We are
not going to use these functions at any later point, in our code. So, it is
slightly wasteful to define functions for this. Wouldn't it be nice to
write them, without actually defining functions? Enter ``lambda``!

``lambda``
----------

Essentially, lambda allows us to define small functions anonymously. The
first example that uses the ``moonize`` function can now be re-written as
below, using the lambda function. 

::

    map(lambda x: x/6.0, weights)

``lambda`` above is defining a function, which takes one argument ``x`` and
returns a sixth of that argument. The ``lambda`` actually returns a
function object which we could in fact assign to a name and use later. 

::

    l_moonize = lambda x: x/6.0

The ``l_moonize`` function, now behaves similarly to the ``moonize``
function. 

The ``migrate`` function can be written using a lambda function as below

::

    l_migrate = lambda x: x*3.0 if x < 50 else x/6.0


If you observed, we have carefully avoided the discussion of the example
where only the weights that were above 50 were calculated and returned.
This is because, this cannot be done using ``map``. We may return ``None``
instead of calculating a sixth of the element, but we cannot ensure that
the element is not present in the new list. 

This can be done using ``filter`` and ``map`` in conjunction. 

``filter``
----------

The ``filter`` function, like the ``map`` takes two arguments, a function
and a sequence and calls the function for each element of the sequence. The
output of ``filter`` is a sequence consisting of elements for which the
function returned ``True`` 

The problem of returning a sixth of only those weights which are more than
50, can be solved as below

::

    map(lambda x: x/6.0, filter(lambda x: x > 50, weights))

The ``filter`` function returns a list containing only the values which are
greater than 50. 

::

    filter(lambda x: x > 50, weights)


``reduce``
----------

As, the name suggests, ``reduce`` reduces a sequence to a single object.
``reduce`` takes two arguments, a function and a sequence, but the function
should take two arguments as input. 

``reduce`` initially passes the first two elements as arguments, and
continues iterating of the sequence and passes the output of the previous
call with the current element, as the arguments to the function. The final
result therefore, is just a single element. 

::

    reduce(lambda x,y: x*y, [1, 2, 3, 4])

multiplies all the elements of the list and returns ``24``. 

.. 
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: nil
   fill-column: 75
   End:
