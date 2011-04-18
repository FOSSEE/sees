In this section we shall look at using scipy to do various common
scientific computation tasks. We shall be looking at solving equations
(linear and non-linear) and solving ODEs. We shall also briefly look at
FFTs. 

Solving Equations
=================

Let us begin with solving equations, specifically linear equations. 

Consider the set of equations,
::

    3x + 2y -z = 1, 
    2x-2y + 4z = -2, 
    -x+ 1/2 y-z = 0

We shall use the ``solve`` function, to solve the given system of linear
equations. ``solve`` requires the coefficients and the constants to be in
the form of matrices, of the form ``Ax = b`` to solve the system. 

We begin by entering the coefficients and the constants as matrices.

::

    A = array([[3,2,-1], 
               [2,-2,4],
               [-1, 0.5, -1]])

A is a 3X3 matrix of the coefficients of x, y and z

::

    b = array([1, -2, 0])

Now, we can use the solve function to solve the given system. 

::
    
    x = solve(A, b)

Type x, to look at the solution obtained. 

The equation is of the form ``Ax = b``, so we verify the solution by
obtaining a matrix product of ``A`` and ``x``, and comparing it with ``b``.
As we have seen earlier, we should use the dot function, for a matrix
product and not the * operator.

::

    Ax = dot(A, x)
    Ax

The result ``Ax``, doesn't look exactly like ``b``, but if we carefully
observe, we will see that it is the same as ``b``. To save ourself all this
trouble, we can use the ``allclose`` function.

``allclose`` checks if two matrices are close enough to each other (with-in
the specified tolerance level). Here we shall use the default tolerance
level of the function.

::
    allclose(Ax, b)

The function returns ``True``, which implies that the product of ``A`` &
``x`` is very close to the value of ``b``. This validates our solution. 

Let's move to finding the roots of a polynomial. We shall use the ``roots``
function for this.

The function requires an array of the coefficients of the polynomial in the
descending order of powers. Consider the polynomial x^2-5x+6 = 0

::
    
    coeffs = [1, -5, 6]
    roots(coeffs)

As we can see, roots returns the result in an array. It even works for
polynomials with imaginary roots.

::

    roots([1, 1, 1])

As you can see, the roots of that equation are complex. 

What if, we want the solution of non linear equations?

For that we shall use the ``fsolve`` function. We shall use the equation
sin(x)+cos^2(x), as an example. ``fsolve`` is not part of the pylab package
which we imported at the beginning, so we will have to import it. It is
part of ``scipy`` package. Let's import it,

::

    from scipy.optimize import fsolve

We shall look at the details of importing, later.

Now, let's look at the documentation of fsolve by typing fsolve?    

::
    
    fsolve?

As mentioned in documentation the first argument, ``func``, is a python
function that takes atleast one argument. The second argument, ``x0``, is
the initial estimate of the roots of the function. Based on this initial
guess, ``fsolve`` returns a root.

Let's define a function called f, that returns the value of
``(sin(x)+cos^2(x))`` evaluated at the input value ``x``. 

::

    def f(x):
        return sin(x)+cos(x)*cos(x)

We can test our function, by calling it with an argument for which the
output value is known, say x = 0. We can see that 

Let's check our function definition, by calling it with 0 as an argument.

::

    f(0)


We can see that the output is 1 as expected, since sin(x) + cos^2(x) has a
value of 1, when x = 0.

Now, that we have our function, we can use ``fsolve`` to obtain a root of
the expression sin(x)+cos^2(x). Let's use 0 as our initial guess.

::

    fsolve(f, 0)

fsolve has returned a root of sin(x)+cos^2(x) that is close to 0. 

That brings us to the end of our discussion on solving equations. We
discussed solution of linear equations, finding roots of polynomials and
non-linear equations. 


ODEs
====

Let's see how to solve Ordinary Differential Equations (ODEs), using
Python. Let's consider the classic problem of the spread of an epidemic in
a population, as an example. 

This is given by the ordinary differential equation ``dy/dt = ky(L-y)``
where L is the total population and k is an arbitrary constant. 

For our problem, let us use L=250000, k=0.00003. Let the boundary condition
be y(0)=250.

We shall use the ``odeint`` function to solve this ODE. As before, this
function resides in a submodule of SciPy and doesn't come along with Pylab.
We import it, 
::

    from scipy.integrate import odeint

We can represent the given ODE as a Python function. This function takes
the dependent variable y and the independent variable t as arguments and
returns the ODE.

::

    def epid(y, t):
        k = 0.00003
        L = 250000
        return k*y*(L-y)

Independent variable t can be assigned the values in the interval of 0 and
12 with 60 points using linspace:

    In []: t = linspace(0, 12, 60)

Now obtaining the solution of the ode we defined, is as simple as calling
the Python's ``odeint`` function which we just imported

::
    
    y = odeint(epid, 250, t)

We can plot the the values of y against t to get a graphical picture our ODE.

::

    plot(y, t)

Let's now try and solve an ODE of second order. Let's take the example of a
simple pendulum. 

The equations can be written as a system of two first order ODEs

    d(theta)/dt = omega
    
and

    d(omega)/dt = - g/L sin(theta)

Let us define the boundary conditions as: at t = 0, theta = theta-naught =
10 degrees and omega = 0

Let us first define our system of equations as a Python function,
``pend_int``. As in the earlier case of single ODE we shall use ``odeint``
function to solve this system of equations. 

::

    def pend_int(initial, t):
        theta = initial[0]
        omega = initial[1]
        g = 9.81
        L = 0.2
        f=[omega, -(g/L)*sin(theta)]
        return f
    
It takes two arguments. The first argument itself containing two dependent
variables in the system, theta and omega. The second argument is the
independent variable t.

In the function we assign the first and second values of the initial
argument to theta and omega respectively. Acceleration due to gravity, as
we know is 9.81 meter per second sqaure. Let the length of the the pendulum
be 0.2 meter.

We create a list, f, of two equations which corresponds to our two ODEs,
that is ``d(theta)/dt = omega`` and ``d(omega)/dt = - g/L sin(theta)``. We
return this list of equations f.

Now we can create a set of values for our time variable t over which we need
to integrate our system of ODEs. Let us say,

::

    t = linspace(0, 20, 100)

We shall assign the boundary conditions to the variable initial.

::

    initial = [10*2*pi/360, 0]

Now solving this system is just a matter of calling the odeint function with
the correct arguments.

::

    pend_sol = odeint(pend_int, initial,t)

    plot(pend_sol)

This gives us 2 plots, omega vs t and theta vs t.

That brings us to the end of our discussion on ODEs and solving them in
Python. 

.. 
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: nil
   fill-column: 75
   End:
