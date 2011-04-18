Arrays
======

In this section, we shall learn about a very powerful data structure,
specially useful for scientific computations, the array. We shall look at
initialization of arrays, operations on arrays and a brief comparison with
lists. 

Arrays are homogeneous data structures, unlike lists which can be
heterogeneous. They can have only one type of data as their entries. 

Arrays of a given length are comparatively much faster in mathematical
operations than lists of the same length, because of the fact that they are
homogeneous. 

Now let us see how to create arrays.

To create an array we will use the function ``array()``,

::

    a1 = array([1,2,3,4])

Notice that we created a one dimensional array here. Also notice that we
passed a list as an argument, to create the array. 

We create two dimensional array by converting a list of lists to an array

::

    a2 = array([[1,2,3,4],[5,6,7,8]])

A two dimensional array has been created by passing a list of lists to the
array function. 

Now let us use ``arange()`` function to create the same arrays as before.

::

    ar1 = arange(1, 5)

The ``arange`` function is similar to the range function that we have already
looked at, in the basic Python section. 

To create the two dimensional array, we first obtain a 1D array with the
elements from 1 to 8 and then convert it to a 2D array. 

To obtain the 1D array, we use the ``arange`` function

::
    ar2 = arange(1, 9)
    print ar2

We use the shape method to change the shape of the array, into a 2D array. 

::

    ar2.shape = 2, 4
    print ar2

This gives us the required array.     

Instead of passing a list to the array function, we could also pass a list
variable. For, instance

::

    l1 = [1,2,3,4]
    a3 = array(l1)

We used the shape method to change the shape of the array. But it can also
be used to find out the shape of an array that we have. 

::
    a1.shape
    a2.shape

As, already stated, arrays are homogeneous. Let us try to create a new
array with a mix of elements and see what happens.

::

    a4 = array([1,2,3,'a string'])

We expect an error, but there wasn't one. What happened? Let's see what a4
has. 

::

    a4

There you go! The data type of the array has been set to a string of
length 8. All the elements have been implicitly type-casted as strings,
though our first three elements were meant to be integers. The dtype
specifies the data-type of the array. 

There some other special methods as well, to create special types of
arrays. We can create an 2 dimensional identity array, using the function
``identity()``. The function ``identity()`` takes an integer argument which
specifies the size of the diagonal of the array.

::

    identity(3)

As you can see the identity function returned a three by three array, with
all the diagonal elements as ones and the rest of the elements as zeros.

``zeros()`` function accepts a tuple, which is the shape of the array that
we want to create, and it generates an array with all elements as zeros.

Let us creates an array of the order four by five with all the elements
zero. We can do it using the method zeros, ::

    zeros((4,5))

Notice that we passed a tuple to the function zeros. Similarly, ``ones()``
gives us an array with all elements as ones. 

Also, ``zeros_like`` gives us an array with all elements as zeros, with a
shape similar to the array passed as the argument and the same data-type as
the argument array. 

::

    a = zeros_like([1.5, 1, 2, 3]
    print a, a.dtype

Similarly, the function ``ones_like``. 

Let us try out some basic operations with arrays, before we end this
section. 

Let's check the value of a1, by typing it out on the interpreter. 

::

    a1

``a1`` is a single dimensional array, array([1,2,3,4]). Now, try

::

    a1 * 2

We get back a new array, with all the elements multiplied by 2. Note that
the value of elements of ``a1`` remains the same. 

::

    a1

Similarly we can perform addition or subtraction or division. 

::

    a1 + 3
    a1 - 7
    a1 / 2.0

We can change the array, by simply assigning the newly returned array to
the old array. 

::

    a1 = a1 + 2

Notice the change in elements of a1,

::

    a1

We could also do the augmented assignment, but there's a small nuance here.
For instance, 

::

    a = arange(1, 5)
    b = arange(1, 5)

    print a, a.dtype
    print b, b.dtype

    a = a/2.0
    b /= 2.0

    print a, a.dtype
    print b, b.dtype

As you can see, ``b`` doesn't have the expected result because the
augmented assignment that we are doing, is an inplace operation. Given that
arrays are optimized to be very fast, by fixing their datatype and hence
the amount of memory they can occupy, the division by a float, when
performed inplace, fails to change the dtype of the array. So, be cautious,
when using in-place assignments. 

Now let us try operations between two arrays. 

::

    a1 + a1
    a1 * a2

Note that both the addition and the multiplication are element-wise. 

Accessing pieces of arrays
==========================

Now, that we know how to create arrays, let's see how to access individual
elements of arrays, get rows and columns and other chunks of arrays using
slicing and striding.

Let us have two arrays, A and C, as the sample arrays that we will use to
learn how to access parts of arrays.

::

  A = array([12, 23, 34, 45, 56])

  C = array([[11, 12, 13, 14, 15],
             [21, 22, 23, 24, 25],
             [31, 32, 33, 34, 35],
             [41, 42, 43, 44, 45],
             [51, 52, 53, 54, 55]])

Let us begin with the most elementary thing, accessing individual elements.
Also, let us first do it with the one-dimensional array A, and then do the
same thing with the two-dimensional array.

To access, the element 34 in A, we say, 

::

  A[2]

A of 2, note that we are using square brackets.

Like lists, indexing starts from 0 in arrays, too. So, 34, the third
element has the index 2.

Now, let us access the element 34 from C. To do this, we say

::

  C[2, 3]

C of 2,3.

34 is in the third row and the fourth column, and since indexing begins
from zero, the row index is 2 and column index is 3.

Now, that we have accessed one element of the array, let us change it. We
shall change the 34 to -34 in both A and C. To do this, we simply assign
the new value after accessing the element. 

::

  A[2] = -34
  C[2, 3] = -34

Now that we have accessed and changed a single element, let us access and
change more than one element at a time; first rows and then columns.

Let us access one row of C, say the third row. We do it by saying, 

::

  C[2] 

How do we access the last row of C? We could say,

::

  C[4] 

for the fifth row, or as with lists, use negative indexing and say

::

  C[-1]

Now, we could change the last row into all zeros, using either 

::

  C[-1] = [0, 0, 0, 0, 0]

or 

::
  
  C[-1] = 0

Now, how do we access one column of C? As with accessing individual
elements, the column is the second parameter to be specified (after the
comma). The first parameter, is replaced with a ``:``. This specifies that
we want all the elements of that dimension, instead of just one particular
element. We access the third column by

::
  
  C[:, 2]

So, we can change the last column of C to zeroes, by

::
  
  C[:, -1] = 0

Since A is one dimensional, rows and columns of A don't make much sense. It
has just one row and

::

  A[:] 

gives the whole of A. 

Now, that we know how to access, rows and columns of an array, we shall
learn how to access other, larger pieces of an array. For this purpose, we
will be using image arrays.

To read an image into an array, we use the ``imread`` command. We shall use
the image ``squares.png``. We shall first navigate to that path in the OS
and see what the image contains.

Let us now read the data in ``squares.png`` into the array ``I``. 

::

  I = imread('squares.png')

We can see the contents of the image, using the command ``imshow``. We say,

::

  imshow(I) 

to see what has been read into ``I``. We do not see white and black
because, ``pylab`` has mapped white and black to different colors. This can
be changed by using a different colormap.

To see that ``I`` is really, just an array, we say, 

::

  I 

at the prompt, and see that an array is displayed. 

To check the dimensions of any array, we can use ``.shape``. We say

::

  I.shape 

to get the dimensions of the image. As we can see, ``squares.png`` has the
dimensions of 300x300.

Our goal for now, is be to get the top-left quadrant of the image. To do
this, we need to access, a few of the rows and a few of the columns of the
array.

To access, the third column of C, we said, ``C[:, 2]``. Essentially, we are
accessing all the rows in column three of C. Now, let us modify this to
access only the first three rows, of column three of C.

We say, 

::

  C[0:3, 2]

to get the elements of rows indexed from 0 to 3, 3 not included and column
indexed 2. Note that, the index before the colon is included and the index
after it is not included in the slice that we have obtained. This is very
similar to the ``range`` function, where ``range`` returns a list, in which
the upper limit or stop value is not included.

Now, if we wish to access the elements of row with index 2, and in
columns indexed 0 to 2 (included), we say, 

::

  C[2, 0:3]

Note that when specifying ranges, if you are starting from the beginning or
going up-to the end, the corresponding element may be dropped. 

::

  C[2, :3]

also gives us the same elements, [31, 32, 33]

Now, we are ready to obtain the top left quarter of the image. How do we go
about doing it? Since, we know the shape of the image to be 300, we know
that we need to get the first 150 rows and first 150 columns. 

::

  I[:150, :150]

gives us the top-left corner of the image. 

We use the ``imshow`` command to see the slice we obtained in the
form of an image and confirm. 

::

  imshow(I[:150, :150])

How would we obtain the square in the center of the image?

::

  imshow(I[75:225, 75:225])

Our next goal is to compress the image, using a very simple technique to
reduce the space that the image takes on disk while not compromising too
heavily on the image quality. The idea is to drop alternate rows and
columns of the image and save it. This way we will be reducing the data to
a fourth of the original data but losing only so much of visual
information.

We shall first learn the idea of striding using the smaller array C.
Suppose we wish to access only the odd rows and columns (first, third,
fifth). We do this by, 

::

  C[0:5:2, 0:5:2]

if we wish to be explicit, or simply, 
::

  C[::2, ::2]

This is very similar to the step specified to the ``range`` function. It
specifies, the jump or step in which to move, while accessing the elements.
If no step is specified, a default value of 1 is assumed.

::

  C[1::2, ::2] 

gives the elements, [[21, 23, 0], [41, 43, 0]]

Now, that we know how to stride over an array, we can drop alternate rows
and columns out of the image in I.

::

  I[::2, ::2]

To see this image, we say, 
::

  imshow(I[::2, ::2])

This does not have much data to notice any real difference, but notice that
the scale has reduced to show that we have dropped alternate rows and
columns. If you notice carefully, you will be able to observe some blurring
near the edges. To notice this effect more clearly, increase the step to 4.

::

  imshow(I[::4, ::4])

That brings us to our discussion on accessing pieces of arrays. We shall
look at matrices, next. 

Matrices
========

In this course, we shall perform all matrix operations using the array
data-structure. We shall create a 2D array and treat it as a matrix. 

::

    m1 = array([[1,2,3,4]])
    m1.shape

As we already know, we can get a 2D array from a list of lists as well. 

::

    l1 = [[1,2,3,4],[5,6,7,8]]
    m2 = array(l1)
    m3 = array([[5,6,7,8],[9,10,11,12]])

We can do matrix addition and subtraction as,

::

    m3 + m2

does element by element addition, thus matrix addition.

Similarly,

::

    m3 - m2

it does matrix subtraction, that is element by element
subtraction. Now let us try,

::

    m3 * m2

Note that in arrays ``m3 * m2`` does element wise multiplication and not
matrix multiplication,

And matrix multiplication in matrices are done using the function ``dot()``

::

    dot(m3, m2)

but for matrix multiplication, we need arrays of compatible sizes and hence
the multiplication fails, in this case. 

To see an example of matrix multiplication, we choose a proper pair.

::

    m1.shape

m1 is of the shape one by four, let us create an array of the shape four by
two, 

::

    m4 = array([[1,2],[3,4],[5,6],[7,8]])
    dot(m1, m4)

Thus, the function ``dot()`` can be used for matrix multiplication.

We have already seen the special functions like  ``identity()``,
``zeros()``, ``ones()``, etc. to create special arrays. 

Let us now look at some Matrix specific operations. 

To find out the transpose, we use the ``.T`` method. 

::

    print m4
    print m4.T

Now let us try to find out the Frobenius norm of inverse of a 4 by 4
matrix, the matrix being,

::

    m5 = arange(1,17).reshape(4,4)
    print m5

The inverse of a matrix A, A raise to minus one is also called the
reciprocal matrix such that A multiplied by A inverse will give 1. 

::

    im5 = inv(m5)

The Frobenius norm of a matrix is defined as square root of sum of squares
of elements in the matrix. The Frobenius norm of ``im5`` can be found by,

::

    sqrt(sum(im5 * im5)) 

Now try to find out the infinity norm of the matrix im5. The infinity norm
is defined as the maximum value of sum of the absolute of elements in each
row. 

The solution for the problem is,

::

    max(sum(abs(im5), axis=1))

Well! to find the Frobenius norm and Infinity norm we have an even easier
method, and let us see that now.

The norm of a matrix can be found out using the method ``norm()``. In order
to find out the Frobenius norm of the im5, we do,

::

    norm(im5)

And to find out the Infinity norm of the matrix im5, we do,
::

    norm(im5,ord=inf)


The determinant of a square matrix can be obtained using the function
``det()`` and the determinant of m5 by,

::

    det(m5)

The eigen values and eigen vector of a square matrix can be computed
using the function ``eig()`` and ``eigvals()``.

Let us find out the eigen values and eigen vectors of the matrix
m5. We can do it as,

::

    eig(m5)


Note that it returned a tuple of two matrices. The first element in
the tuple are the eigen values and the second element in the tuple are
the eigen vectors. Thus the eigen values are,
::

    eig(m5)[0]

and the eigen vectors are,

::

    eig(m5)[1]

The eigen values can also be computed using the function ``eigvals()`` as,

::

    eigvals(m5)


We can also find the singular value decomposition or S V D of a matrix.

The SVD of ``m5`` can be found by

::

    svd(m5)

Notice that it returned a tuple of 3 elements. The first one U the
next one Sigma and the third one V star.
    
That brings us to our discussion of matrices and operations on them. But we
shall continue to use them in the next section on Least square fit. 

Least square fit
================

First let us have a look at the problem.

We have an input file generated from a simple pendulum experiment, which we
have already looked at. We shall find the least square fit of the plot
obtained by plotting l vs. t^2, where l is the length of the pendulum and t
is the corresponding time-period. 

::

    l, t = loadtxt("/home/fossee/pendulum.txt", unpack=True)
    l
    t

We can see that l and t are two sequences containing length and time values
correspondingly.

Let us first plot l vs t^2. Type
::

    tsq = t * t
    plot(l, tsq, 'bo')

We can see that there is a visible linear trend, but we do not get a
straight line connecting them. We shall, therefore, generate a least square
fit line.

We are first going to generate the two matrices ``tsq`` and A, the vander
monde matrix. Then we are going to use the ``lstsq`` function to find the
values of m and c.

Let us now generate the A matrix with l values. We shall first generate a 2
x 90 matrix with the first row as l values and the second row as ones. Then
take the transpose of it. Type 

::

    A = array((l, ones_like(l)))
    A

We see that we have intermediate matrix. Now we need the transpose. Type

::

    A = A.T
    A

Now we have both the matrices A and tsq. We only need to use the ``lstsq``

::

    result = lstsq(A, tsq)

The result is a sequence of values. The first item in this sequence, is the
matrix p i.e., the values of m and c. Hence,

::

    m, c = result[0]
    m
    c

Now that we have m and c, we need to generate the fitted values of t^2. Type

::

    tsq_fit = m * l + c
    plot(l, tsq, 'bo')
    plot(l, tsq_fit, 'r')

We get the least square fit of l vs t^2

That brings us to the end of our discussion on least square fit curve and
also our discussion of arrays. 

.. 
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: nil
   fill-column: 75
   End:
