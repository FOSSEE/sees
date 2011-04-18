Sage notebook
=============

In this section, we will learn what Sage is, what is Sage notebook, how to
start and use the sage notebook. In the notebook we will be specifically
learning how to execute our code, how to write annotations and other
content, typesetting the content and how to use the offline help available.

To start with, What is Sage? Sage is a free, open-source mathematical
software. Sage can do a lot of math stuff for you including, but not
limited to, algebra, calculus, geometry, cryptography, graph theory among
other things. It can also be used as aid in teaching and research in any of
the areas that Sage supports. So let us start Sage now

We are assuming that you have Sage installed on your computer now. If not
please visit the page
http://sagemath.org/doc/tutorial/introduction.html#installation for the
tutorial on how to install Sage.


Let us now learn how to start Sage. On the terminal type

::

  sage

This should start a new Sage shell with the prompt sage: which looks like
this

::

    sage:

So now we can type all the commands that Sage supports here. But Sage comes
bundled with a much more elegant tool called Sage Notebook. It provides a
web based user interface to use Sage. So once we have a Sage notebook
server up and running, all we need is a browser to access the Sage
functionality.

We could also use a server run by somebody, else like the official instance
of the Sage server at http://sagenb.org. So all we need is just a browser,
a modern browser, to use Sage and nothing else! The Sage notebook also
provides a convenient way of sharing and publishing our work, which is very
handy for research and teaching.

However we can also run our own instances of Sage notebook servers on all
the computers we have a local installation of Sage. To start the notebook
server just type

::

  notebook()

on the Sage prompt. This will start the Sage Notebook server. If we are
starting the notebook server for the first time, we are prompted to enter
the password for the admin. Type the password and make a note of it. After
this Sage automatically starts a browser page, with the notebook opened.

If it doesn't automatically start a browser page check if the Notebook
server started and there were no problems. If so open your browser and in
the address bar type the URL shown in the instructions upon running the
notebook command on the sage prompt.

If you are not logged in yet, it shows the Notebook home page and textboxes
to type the username and the password. You can use the username 'admin' and
the password you gave while starting the notebook server for the first
time. There are also links to recover forgotten password and to create new
accounts.

Once we are logged in with the admin account we can see the notebook admin
page. A notebook can contain a collection of Sage Notebook worksheets.

Worksheet is basically a working area. This is where we enter all the Sage
commands on the notebook.

The admin page lists all the worksheets created. On the topmost part of
this page we have the links to various pages.

The home link takes us to the admin home page. The published link takes us
to the page which lists all the published worksheets. The log link has the
complete log of all the actions we did on the notebook. We have the
settings link where we can configure our notebook, the notebook server,
create and mangage accounts. We have a link to help upon clicking opens a
new window with the complete help of Sage. The entire documentation of Sage
is supplied with Sage for offline reference and the help link is the way to
get into it. Then we can report bugs about Sage by clicking on Report a
Problem link and there is a link to sign out of the notebook.

We can create a new worksheet by clicking New Worksheet link

Sage prompts you for a name for the worksheet. Let us name the worksheet as
nbtutorial. Now we have our first worksheet which is empty.

A worksheet will contain a collection of cells. Every Sage command must be
entered in this cell. Cell is equivalent to the prompt on console. When we
create a new worksheet, to start with we will have one empty cell. Let us
try out some math here

::

  2 + 2
  57.1 ^ 100

The hat operator is used for exponentiation. We can observe that only the
output of the last command is displayed. By default each cell displays the
result of only the last operation. We have to use print statement to
display all the results we want to be displayed.

Now to perform more operations we want more cells. So how do we create a
new cell? It is very simple. As we hover our mouse above or below the
existing cells we see a blue line, by clicking on this new line we can
create a new cell.

We have a cell, we have typed some commands in it, but how do we evaluate
that cell? Pressing Shift along with Enter evaluates the cell.
Alternatively we can also click on the evaluate link to evaluate the cell

::

  matrix([[1,2], [3,4]])^(-1)

After we create many cells, we may want to move between the cells. To move
between the cells use Up and Down arrow keys. Also clicking on the cell
will let you edit that particular cell.

To delete a cell, clear the contents of the cell and hit backspace. 

If you want to add annotations in the worksheet itself on the blue line
that appears on hovering the mouse around the cell, Hold Shift and click on
the line. This creates a *What You See Is What You Get* cell.

We can make our text here rich text. We can make it bold, Italics, we can
create bulleted and enumerated lists in this area

::

  This text contains both the **bold** text and also *italicised*
  text.
  It also contains bulleted list:
  * Item 1
  * Item 2
  It also contains enumerate list:
  1. Item 1
  2. Item 2

In the same cell we can display typeset math using the LaTeX like syntax

::

  $\int_0^\infty e^{-x} \, dx$

We enclose the math to be typeset within $ and $ or $$ and $$ as in LaTeX.

We can also obtain help for a particular Sage command or function within
the worksheet itself by using a question mark following the command

::

  sin?

Evaluating this cell gives me the entire help for the sin function inline
on the worksheet itself. Similarly we can also look at the source code of
each command or function using double question mark

::

  matrix??

Sage notebook also provides the feature for autocompletion. To auto-complete
a command type first few unique characters and hit tab key

::

  sudo<tab>

To see all the commands starting with a specific name type those characters
and hit tab

::

  plo<tab>

To list all the methods that are available for a certain variable or a
data-type we can use the variable name followed by the dot to access the
methods available on it and then hit tab

::

  s = 'Hello'
  s.rep<tab>

The output produced by each cell can be one of the three states. It can be
either the full output, or truncated output or hidden output. The output
area will display the error if the Sage code we wrote in the cell did not
successfully execute

::

  a, b = 10

The default output we obtained now is a truncated output. Clicking at the
left of the output area when the mouse pointer turns to hand gives us the
full output, clicking again makes the output hidden and it cycles.

Lastly, Sage supports a variety of languages and each cell on the worksheet
can contain code written in a specific language. It is possible to instruct
Sage to interpret the code in the language we have written. This can be
done by putting percentage sign(%) followed by the name of the language.
For example, to interpret the cell as Python code we put

::

  %python

as the first line in the cell. Similarly we have: %sh for shell scripting,
%fortran for Fortran, %gap for GAP and so on. Let us see how this works.
Say we have an integer. The type of the integer in default Sage mode is 

::

  a = 1
  type(a)

  Output: <type 'sage.rings.integer.Integer'>

We see that Integers are Sage Integers. Now let us put %python as the first
line of the cell and execute the same code snippet

::

  %python
  a = 1
  type(a)

  Output: <type 'int'>

Now we see that the integer is a Python integer. Why? Because now we
instructed Sage to interpret that cell as Python code.

This brings us to the end of the section on using Sage. 

Symbolics
=========

In this section, we shall learn to define symbolic expressions in Sage, use
built-in constants and functions, perform integration and differentiation
using Sage, define matrices and symbolic functions and simplify and solve
them. 

In addtion to a lot of other things, Sage can do Symbolic Math and we shall
start with defining symbolic expressions in Sage.

On the sage notebook type

::
   
    sin(y)

It raises a name error saying that ``y`` is not defined. We need to declare
``y`` as a symbol. We do it using the ``var`` function.

::

    var('y')
   
Now if you type

::

    sin(y)

Sage simply returns the expression.

Sage treats ``sin(y)`` as a symbolic expression. We can use this to do
symbolic math using Sage's built-in constants and expressions.

Let us try out a few examples. 

::
   
   var('x, alpha, y, beta') 
   (x^2/alpha^2)+(y^2/beta^2)

We have defined 4 variables, ``x``, ``y``, ``alpha`` and ``beta`` and
have defined a symbolic expression using them.
 
Here is an expression in ``theta``  

::
   
   var('theta')
   sin(theta)*sin(theta)+cos(theta)*cos(theta)

Sage also provides built-in constants which are commonly used in
mathematics, for instance pi, e, infinity. The function ``n`` gives the
numerical values of all these constants.

::

    n(pi) 
    n(e) 
    n(oo)
   
If you look into the documentation of function ``n`` by doing

::

   n?

You will see what all arguments it takes and what it returns. It will be
very helpful if you look at the documentation of all functions introduced,
in this section. 

Also we can define the number of digits we wish to have in the constants.
For this we have to pass an argument -- digits. 

::

   n(pi, digits = 10)

Apart from the constants Sage also has a lot of built-in functions like
``sin``, ``cos``, ``log``, ``factorial``, ``gamma``, ``exp``, ``arcsin``
etc ...

Lets try some of them out on the Sage notebook.

::
     
   sin(pi/2)
   
   arctan(oo)
     
   log(e,e)

Given that we have defined variables like x, y etc., we can define an
arbitrary function with desired name

::

    var('x') 
    function('f',x)

Here f is the name of the function and x is the independent variable .
Now we can define f(x) to be 

::

    f(x) = x/2 + sin(x)

Evaluating this function f for the value x=pi returns pi/2.

::
	   
    f(pi)

We can also define functions that are not continuous but defined piece-wise.
Let us define a function which is a parabola between 0 to 1 and a constant
from 1 to 2 . 

::
      

      var('x') 
      h(x)=x^2 
      g(x)=1 

      f=Piecewise([[(0,1),h(x)],[(1,2),g(x)]],x) 
      f

We can also define functions convergent series and other series.

We first define a function f(n) in the way discussed above.

::

   var('n') 
   function('f', n)


To sum the function for a range of discrete values of n, we use the
sage function sum.

For a convergent series , f(n)=1/n^2 we can say 

::
   
   var('n') 
   function('f', n)
   f(n) = 1/n^2
   sum(f(n), n, 1, oo)

 
Lets us now try another series 

::


    f(n) = (-1)^(n-1)*1/(2*n - 1)
    sum(f(n), n, 1, oo)

This series converges to pi/4. 

Let's now look at some calculus. 

::

    diff(x**2 + sin(x), x) 

The diff function differentiates an expression or a function. It's first
argument is expression or function and second argument is the independent
variable.

We have already tried an expression now lets try a function 

::

   f = exp(x^2) + arcsin(x) 
   diff(f(x), x)

To get a higher order differential we need to add an extra third argument
for order 

::
 
   diff(f(x), x, 3)

in this case it is 3.

Just like differentiation of expression you can also integrate them 

::

    x = var('x') 
    s = integral(1/(1 + (tan(x))**2),x) 
    s

Many a times we need to find factors of an expression, we can use the
"factor" function

::

    y = (x^100 - x^70)*(cos(x)^2 + cos(x)^2*tan(x)^2) 
    f = factor(y)

One can simplify complicated expression 

::
    
    f.simplify_full()

This simplifies the expression fully. We can also do simplification of
just the algebraic part and the trigonometric part 

::

    f.simplify_exp() 
    f.simplify_trig()
    
One can also find roots of an equation by using ``find_root`` function

::

    phi = var('phi') 
    find_root(cos(phi)==sin(phi),0,pi/2)

Let's substitute this solution into the equation and see we were
correct 

::

     var('phi') 
     f(phi)=cos(phi)-sin(phi)
     root=find_root(f(phi)==0,0,pi/2) 
     f.substitute(phi=root)

as we can see when we substitute the value the answer is almost = 0 showing 
the solution we got was correct.

Lets us now try some matrix algebra symbolically ::

   var('a,b,c,d') 
   A=matrix([[a,1,0],[0,b,0],[0,c,d]]) 
   A

Now lets do some of the matrix operations on this matrix

::
    A.det() 
    A.inverse()


That brings us to the end of our discussion on symbolics. 

Plotting using Sage
===================

In this section we shall look at 
 
 * 2D plotting in SAGE
 * 3D plotting in SAGE

We shall first create a symbolic variable ``x``

::

    x = var('x')

We shall plot the function ``sin(x) - cos(x) ^ 2`` in the range (-5, 5).

::

    plot(sin(x) - cos(x) ^ 2, (x, -5, 5))

As we can see, the plot is shown.

``plot`` command takes the symbolic function as the first argument and the
range as the second argument.

We have seen that plot command plots the given function on a linear range.

What if the x and y values are functions of another variable. For instance,
lets plot the trajectory of a projectile.

A projectile was thrown at 50 m/s^2 and at an angle of 45 degrees from the
ground. We shall plot the trajectory of the particle for 5 seconds.

These types of plots can be drawn using the parametric_plot function. We
first define the time variable.

::

    t = var('t')

Then we define the x and y as functions of t.

::

    f_x = 50 * cos(pi/4)
    f_y = 50 * sin(pi/4) * t - 1/2 * 9.81 * t^2 )

We then call the ``parametric_plot`` function as

::

    parametric_plot((f_x, f_y), (t, 0, 5))

And we can see the trajectory of the projectile.

The ``parametric_plot`` funciton takes a tuple of two functions as the
first argument and the range over which the independent variable varies as
the second argument.

Now we shall look at how to plot a set of points.

We have the ``line`` function to achieve this.

We shall plot sin(x) at few points and join them.

First we need the set of points.

::

    points = [ (x, sin(x)) for x in srange(-2*float(pi), 2*float(pi), 0.75) ]

``srange`` takes a start, a stop and a step argument and returns a list of
point. We generate list of tuples in which the first value is ``x`` and
second is ``sin(x)``.

::

    line(points)

plots the points and joins them with a line.

The ``line`` function behaves like the plot command in matplotlib. The
difference is that ``plot`` command takes two sequences while line command
expects a sequence of co-ordinates.

As we can see, the axes limits are set by SAGE. Often we would want to set
them ourselves. Moreover, the plot is shown here since the last command
that is executed produces a plot.

Let us try this example

::

    plot(cos(x), (x,0,2*pi))
    # Does the plot show up??

As we can see here, the plot is not shown since the last command does not
produce a plot.

The actual way of showing a plot is to use the ``show`` command.

::

    p1 = plot(cos(x), (x,0,2*pi))
    show(p1)
    # What happens now??

As we can see the plot is shown since we used it with ``show`` command.

``show`` command is also used set the axes limits.

::

    p1 = plot(cos(x), (x,0,2*pi))
    show(p1, xmin=0, xmax=2*pi, ymin=-1.2, ymax=1.2)

As we can see, we just have to pass the right keyword arguments to the
``show`` command to set the axes limits.

The ``show`` command can also be used to show multiple plots.

::

    p1 = plot(cos(x), (x, 0, 2*pi))
    p2 = plot(sin(x), (x, 0, 2*pi))
    show(p1+p2)

As we can see, we can add the plots and use them in the ``show`` command.

Now we shall look at 3D plotting in SAGE.

We have the ``plot3d`` function that takes a function in terms of two
independent variables and the range over which they vary.

::

    x, y = var('x y')
    plot3d(x^2 + y^2, (x, 0, 2), (y, 0, 2))

We get a 3D plot which can be rotated and zoomed using the mouse.

``parametric_plot3d`` function plots the surface in which x, y and z are
functions of another variable.

::

   u, v = var("u v")
   f_x = u
   f_y = v
   f_z = u^2 + v^2
   parametric_plot3d((f_x, f_y, f_z), (u, 0, 2), (v, 0, 2))

Using Sage
==========

In this section we shall quickly look at a few examples of using Sage for
Linear Algebra, Calculus, Graph Theory and Number theory.

Let us begin with Calculus. We shall be looking at limits, differentiation,
integration, and Taylor polynomial.

To find the limit of the function x*sin(1/x), at x=0, we say

::

   lim(x*sin(1/x), x=0)

We get the limit to be 0, as expected. 

It is also possible to the limit at a point from one direction. For
example, let us find the limit of 1/x at x=0, when approaching from the
positive side. 

::

    lim(1/x, x=0, dir='above')

To find the limit from the negative side, we say,

::

    lim(1/x, x=0, dir='below')   

Let us now see how to differentiate, using Sage. We shall find the
differential of the expression ``exp(sin(x^2))/x`` w.r.t ``x``. We shall
first define the expression, and then use the ``diff`` function to obtain
the differential of the expression.

::

    var('x')
    f = exp(sin(x^2))/x

    diff(f, x)

We can also obtain the partial differentiation of an expression w.r.t one
of the variables. Let us differentiate the expression ``exp(sin(y -
x^2))/x`` w.r.t x and y.

::

    var('x y')
    f = exp(sin(y - x^2))/x

    diff(f, x)

    diff(f, y)

Now, let us look at integration. We shall use the expression obtained from
the differentiation that we did before, ``diff(f, y)`` --- ``e^(sin(-x^2 +
y))*cos(-x^2 + y)/x``. The ``integrate`` command is used to obtain the
integral of an expression or function.

::

    integrate(e^(sin(-x^2 + y))*cos(-x^2 + y)/x, y)

We get back the correct expression. The minus sign being inside or outside
the ``sin`` function doesn't change much.

Now, let us find the value of the integral between the limits 0 and pi/2.

::

    integral(e^(sin(-x^2 + y))*cos(-x^2 + y)/x, y, 0, pi/2)

Let us now see how to obtain the Taylor expansion of an expression using
sage. Let us obtain the Taylor expansion of ``(x + 1)^n`` up to degree 4
about 0.

::

    var('x n')
    taylor((x+1)^n, x, 0, 4)

This brings us to the end of the features of Sage for Calculus, that we
will be looking at. For more, look at the Calculus quick-ref from the Sage
Wiki.

Next let us move on to Matrix Algebra. 

Let us begin with solving the equation ``Ax = v``, where A is the matrix
``matrix([[1,2],[3,4]])`` and v is the vector ``vector([1,2])``.

To solve the equation, ``Ax = v`` we simply say

::

    x = solve_right(A, v)

To solve the equation, ``xA = v`` we simply say

::

    x = solve_left(A, v)

The left and right here, denote the position of ``A``, relative to x. 

Now, let us look at Graph Theory in Sage. 

We shall look at some ways to create graphs and some of the graph families
available in Sage.

The simplest way to define an arbitrary graph is to use a dictionary of
lists. We create a simple graph by

::

    G = Graph({0:[1,2,3], 2:[4]})

We say 

::

    G.show()

to view the visualization of the graph. 

Similarly, we can obtain a directed graph using the ``DiGraph`` function.

::

    G = DiGraph({0:[1,2,3], 2:[4]})


Sage also provides a lot of graph families which can be viewed by typing
``graph.<tab>``. Let us obtain a complete graph with 5 vertices and then
show the graph.

::

    G = graphs.CompleteGraph(5)

    G.show()

Sage provides other functions for Number theory and Combinatorics. Let's
have a glimpse of a few of them.

::

    prime_range(100, 200)

gives primes in the range 100 to 200. 

::

    is_prime(1999) 

checks if 1999 is a prime number or not. 

::

    factor(2001)

gives the factorized form of 2001. 

::

    C = Permutations([1, 2, 3, 4])
    C.list()

gives the permutations of ``[1, 2, 3, 4]``

::

    C = Combinations([1, 2, 3, 4])
    C.list()

gives all the combinations of ``[1, 2, 3, 4]``
  
That brings us to the end of this session showing various features
available in Sage. 

Using Sage to Teach
===================

In this section, we shall look at

 * How to use the "@interact" feature of SAGE for better demonstration
 * How to use SAGE for collaborative learning

Let us look at a typical example of demonstrating a damped oscillation.

::

    t = var('t')
    p1 = plot( e^(-t) * sin(2*t), (t, 0, 15))
    show(p1)

Now let us reduce the damping factor

::

    t = var('t')
    p1 = plot(e^(-t/2) * sin(2*t), (t, 0, 15))
    show(p1)

Now if we want to reduce the damping factor even more, we would be using
e^(-t/3). We can observe that every time we have to change, all we do is
change something very small and re evaluate the cell.

This process can be simplified, using the ``@interact`` feature of SAGE.

::

    @interact
    def plot_damped(n=1):
        t = var('t')
        p1 = plot( e^(-t/n) * sin(2*t), (t, 0, 20))
        show(p1)

We can see that the function is evaluated and the plot is shown. We can
also see that there is a field to enter the value of ``n`` and it is
currently set to ``1``. Let us change it to 2 and hit enter.

We see that the new plot with reduced damping factor is shown. Similarly we
can change ``n`` to any desired value and hit enter and the function will
be evaluated.

This is a very handy tool while demonstrating or teaching.

Often we would want to vary a parameter over range instead of taking it as
an input from the user. For instance we do not want the user to give ``n``
as 0 for the damping oscillation we discussed. In such cases we use a range
of values as the default argument. 

::

    @interact
    def plot_damped(n=(1..10)):
        t = var('t')
        p1 = plot( e^(-t/n) * sin(2*t), (t, 0, 20))
        show(p1)

We get similar plot but the only difference is the input widget. Here it is
a slider unlike an input field. We can see that as the slider is moved, the
function is evaluated and plotted accordingly.

Sometimes we want the user to have only a given set of options. We use a
list of items as the default argument in such situations.

::

    @interact
    def str_shift(s="STRING", shift=(0..8), direction=["Left", "Right"]):
        shift_len = shift % len(s)
        chars = list(s)
        if direction == "Right":
            shifted_chars = chars[-shift_len:] + chars[:-shift_len]
        else:
            shifted_chars = chars[shift_len:] + chars[:shift_len]
        print "Actual String:", s
        print "Shifted String:", "".join(shifted_chars)

We can see that buttons are displayed which enables us to select from a
given set of options.

We have learnt how to use the ``@interact`` feature of SAGE for better
demonstration. We shall look at how to use SAGE worksheets for
collaborative learning.

The first feature we shall see is the ``publish`` feature. Open a worksheet
and in the top right, we can see a button called ``publish``. Click on that
and we get a confirmation page with an option for re publishing.

For now lets forget that option and simply publish by clicking ``yes``. The
worksheet is now published.

Now lets sign out and go to the sage notebook home. We see link to browse
published worksheets. Lets click on it and we can see the worksheet. This
does not require login and anyone can view the worksheet.

Alternatively, if one wants to edit the sheet, there is a link on top left
corner that enables the user to download a copy of the sheet onto their
home. This way they can edit a copy of the worksheet.

We have learnt how to publish the worksheets to enable users to edit a
copy. Next, we shall look at how to enable users to edit the actual
worksheet itself.

Let us open the worksheet and we see a link called ``share`` on the top
right corner of the worksheet. Click the link and we get a box where we can
type the usernames of users whom we want to share the worksheet with. We
can even specify multiple users by seperating their names using commas.
Once we have shared the worksheet, the worksheet appears on the home of
shared users.

.. 
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: nil
   fill-column: 75
   End:
