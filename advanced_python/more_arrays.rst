More Arrays
===========

In this section, we shall explore arrays a bit more, since they are the
fundamental building block of all the computation work we wish to do. 

Arrays were introduced, stating that they are very fast as compared to
lists, owing to their homogeneity. They are definitely a lot more
convenient than a list of lists for doing element-wise operations. Let's
now look at the speed difference, quantitatively. 

Arrays vs. Lists
----------------

Let us create a large array with, say a million elements and see how long
it takes to get a new sequence that contains the ``sin`` of each of these
elements.

::

    a = linspace(0, 2*pi, 1000000)

    sin(a)

    b = []
    for i in a: b.append(sin(i))

There is a visible difference in the run-time of the two ways of doing it.
But, let's look at it quantitatively using the ``%timeit`` magic command of
IPython to get a quantitative difference between doing is using a ``for``
loop and using the array way of doing it.

::

    %timeit sin(a)

    b = []
    %timeit for i in a: b.append(sin(i))

The first method turns out to be around 70 times faster on my machine. So,
as you can see, the homogeneity. The speed gains due to homogeneity are
because, the loops are run in C, rather than in Python and Python loops are
comparatively much slower than C loops. 

Fancy Indexing
--------------

We have looked at slicing and striding to get pieces of arrays. But they
only allow us to do so much. 

For instance, let's say, we have an array a of length 40 with some random
elements. We wish to get a new array which is obtained by dropping every
element that is at a position that is a multiple of 8, i.e., we wish to
drop the elements 0, 8, 16, 24, 32. How do we go about doing this?
Essentially, we wish to drop the elements a[::8]. We shall use something
called Boolean arrays to solve this problem. 

Let's look at a small example before solving this problem. 

::

    p = array([1, 2, 3])
    q = array([True, False, True])

    p[q]

``q`` is called a Boolean array and can be used to index another array.
Only the elements at positions corresponding to ``True`` values in q, will
be returned. 

Now, to solve the problem of dropping the elements a[::8] from a, we need
to create a Boolean array, with those elements as ``False`` and the rest as
``True``. There could be multiple ways of doing that. Here's one

::

    b = arange(len(a))
    b%8!=0
    
    a[b%8!=0]

Checking if the elements of ``b`` are not multiples of 8, returns a Boolean
array, which we are then using to index ``a``. 

Numpy arrays can also be indexed using arrays of indices. Let's solve the
same problem using arrays with indices. Let's look at the same small
example that we looked at, for Boolean arrays, before solving the actual
problem. 

::

    p = array([1, 2, 3])
    q = array([0, 2])

    p[q]

The array ``q`` has the indices of the elements that we wish to pick out of
the array ``p``. The order in which the indices are present, doesn't
matter. The returned array, will contain the elements of ``p`` in the order
in which they have been indexed. They can even be repeated, if we wish to
get the same element out of ``p``.

::

    r = array([2, 0])
    p[r]
    
    s = array([1, 1])
    p[s]

Now, to solve the problem of dropping all the elements of ``p`` whose
indices are a multiple of 8, we need to generate an array, which doesn't
have these elements. 

::

    q = array([i for i in range(40) if i%8])
    p[q]

Copies and Views
----------------

Simple assignment of mutable objects, do not make copies in Python. For
instance, 

::

    a = array([1, 2, 3])
    b = a

Here, ``b`` and ``a`` are not copies of each other, but different names for
the same object. If one of them is changed, it reflects in the other one,
as well. By the way, if you recall, this behaviour is similar with lists as
well. 

::

    a[0] = 1
    print a, b


Slicing an array, returns a view of it. Assigning the slice of an object to
a new variable, means the new variable references a portion of the data of
the original object. Hence, changing the data of the new variable, changes
the original variable, as well. 

::

    a = arange(10)
    b = a[5:]
    
    b[:] = 5
    print b, a 

If we require a complete (or deep) copy of the data of an array, we should
use the ``copy()`` method.

::

    a = arange(10)
    b = a[5:].copy()

    b[:] = 5
    print b, a 

Broadcasting
------------

Let's now look at a more advanced concept called Broadcasting. The
broadcasting rules help us understand how Numpy deals with arrays of
different dimensions. 

We know that array operations are element-wise, and for them to work, the
two arrays should be of the same shape. 

For instance,

::

    a = array([1, 2, 3, 4])
    b = array([2, 4, 6, 8])
    
    a * b

works, but, 

::

    a = array([1, 2, 3, 4])
    c = array([6, 8, 10])
    
    a * c

does not work, which is expected. But, surprisingly (or may be not so
surprisingly, since we have seen it before) multiplication of a vector with
a scalar works. 

::

    a = array([1, 2, 3, 4])
    c = 6
    
    a * c

The above multiplication works, thanks to Broadcasting. Let us look at
another example of Broadcasting before looking at the general rules of
broadcasting. 

::

    x = array([1, 2, 3])
    y = array([4, 5, 6])
    x+y

    y.shape = 3, 1
    print x, y
    x+y

When we are operating on two arrays, Numpy broadcasts the arrays, so that
the shape of the two arrays becomes the same. Then the required operation
is performed on the two arrays. 

The procedure of broadcasting is as follows. 

1. When operating on two arrays, the arrays with the smaller number of
   dimensions, has 1s prepended to it's shape, so that the number of
   dimensions of both the arrays becomes the same.
2. The size in each dimension of the output shape is the maximum of all the
   input shapes in that dimension.
3. An input can be used in the calculation if its shape in a particular
   dimension either matches the output shape or has value exactly 1.
4. If an input has a dimension size of 1 in its shape, the first data entry
   in that dimension will be used for all

Let's look at the example of adding ``x`` and ``y`` to each other, step by
step. 

::

    x.shape
    y.shape

``x.shape`` is (3,) and ``y.shape`` is (3,1). Now, ``x`` has the smaller
dimensions of the two. 1 is prepended to the shape of x, until both the
arrays have the same dimension. ``x.shape`` becomes (1, 3). 

Now, by rule 2, we know that the output shape is the maximum of all the
input shapes, in each of the dimensions. So, the shape of the output is
expect to be (3, 3)

The condition 3 satisfies, for both ``x`` and ``y``. So, this is a valid
operation on ``x`` and ``y``.

To see how the last step works, we use the ``broadcast_arrays`` command. 

::

    broadcast_arrays(x, y)

The values of ``x`` are broadcasted or copied, in the dimension where it's
size was 1. Similarly, for ``y``. 

Let's look at another example, before ending our discussion on
Broadcasting. Let's say we have the co-ordinates of a set of points, and we
wish to calculate the distance of a new point from each of these points. 

::

    x = array([[ 2.,  2.],
               [ 6.,  9.],
               [ 6.,  6.],
               [ 9.,  0.]])

    y = array([4., 3.])

We shall use broadcasting to calculate the difference between ``y`` and each of
the points in ``x``. 

::

    x - y

The array ``y`` has been broadcast and the difference has been obtained.
The following commands, will now give us the required distances. 

::

    (x-y)**2
    sqrt(sum((x-y)**2, axis=1))

As you can see, broadcasting makes the code much simpler. Also, the
operation of subtracting ``y`` from each of the elements of ``x`` is
performed using iterations in the underlying C language, rather than us
writing ``for`` loops in Python. This turns out to be much faster, as long
as the array sizes are small. 

But this may turn out to be slower, when the number of objects gets larger.
This discussion is not in the scope of this course. Look at
`EricsBroadcastingDoc<http://www.scipy.org/EricsBroadcastingDoc>`_ for more
detail.



.. 
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: nil
   fill-column: 75
   End:
