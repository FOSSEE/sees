Interactive Plotting
====================

We have looked at the basics of Python. In this section we shall look at the
basics of plotting. 

Lets start our IPython interpreter, by

:: 

      $ ipython -pylab

Pylab is a python library which provides plotting functionality. It also
provides many other important mathematical and scientific functions. After
running ``ipython -pylab`` in your shell if at the top of the output, you see
something like

::
 
    `ERROR: matplotlib could NOT be imported! Starting normal IPython.`


Then you have to install ``python-matplotlib`` and run this command again.

Let us get started directly and try plotting a cosine curve in the range -pi
to pi.

::

    p = linspace(-pi,pi,100)
    plot(p, cos(p)) 

As you can see we have obtained a cosine curve in the required range. Let's
try and understand what we have done here. 

The variable ``p`` has a hundred points in the range -pi to pi. To see this,
check the documentation of the linspace command. 

::

    linspace?

As you can see, it returns ``num`` evenly spaced samples, calculated over the
interval start and stop.

You can verify this, by looking at the first and last points of ``p`` and the
length of ``p`` 

::

    print p[0], p[-1], len(p)

Now, let's clear the plot we obtained and plot a sine curve in the same
range. 

::

    clf()
    plot(p, sin(p))

``clf`` command clears the plot, and the plot command following it, plots the
required curve. 

Let's briefly explore the plot window and look at what features it has. 

Firstly, note that moving the mouse around gives us the point where mouse
points at.

Also we have some buttons the right most among them is for saving the file.

Left to the save button is the slider button to specify the margins.

Left to this is zoom button to zoom into the plot. Just specify the region to
zoom into.

The button left to it can be used to move the axes of the plot.  

The next two buttons with a left and right arrow icons change the state of
the plot and take it to the previous state it was in. It more or less acts
like a back and forward button in the browser.

The last one is 'home', which returns the plot to the original view. 

Embellishing Plots
==================

Now that we know how to make simple plots, let us look at embellishing the
plots. We shall look at how to modify the colour, thickness and line-style of
a plot. We shall then learn how to add title to a plot and then look at
adding labels to x and y axes. We shall also look at adding annotations to the plot and setting the limits on the axes.

Let us decorate the sine curve that we have already plotted. If you have closed that window or your IPython terminal, redo the plot. 

::

    p = linspace(-pi,pi,100)
    plot(p, sin(p)) 


As we can see, the default colour and the default thickness of the line is as
decided by pylab. Wouldn't it be nice if we could control these parameters in
the plot? This is possible by passing additional arguments to the plot
command.

The additional argument that we shall be passing in here now is the color
argument. We shall first clear the figure and plot the same in red color.

::

    clf()
    plot(p, sin(p), 'r')

As we can see we have the same plot but now in red color.

To alter the thickness of the line, we use the ``linewidth`` argument
in the plot command. 

::

    plot(p, cos(p), linewidth=2)

produces a plot with a thicker line, to be more precise plot with line
thickness 2.

Occasionally we would also want to alter the style of line. Sometimes all we
want is just a bunch of points not joined. This is possible by passing the
linestyle argument along with or instead of the colour argument.

::

    clf()
    plot(p, sin(p), '.')

produces a plot with only points.

To produce the same plot but now in blue colour, we do

::

    clf()
    plot(p, sin(p), 'b.')

Other available options can be seen in the documentation of plot.

::

    plot?

Now that we know how to produce a bare minimum plot with colour, style and
thickness of our interest, we shall look at decorating the plot.

Let us start with a plot of the function -x^2 + 4x - 5 in the range -2 to 4. 

::

    x = linspace(-2, 4, 50)
    plot(x, -x*x + 4*x - 5, 'r', linewidth=2)

We now have the plot in a colour and linewidth of our interest. As you can
see, the figure does not have any description describing the plot.

We will now add a title to the plot by using the ``title`` command.

::

    title("Parabolic function -x^2+4x-5") 

The figure now has a title which describes what the plot is. The ``title``
command as you can see, takes a string as an argument and sets the title
accordingly.

The formatting in title is messed and it does not look clean. You can imagine
what would be the situation if there were fractions and more complex
functions like log and exp. Wouldn't it be good if there was LaTeX like
formatting?

That is also possible by adding a $ sign before and after the part of the
string that should be in LaTeX style. For instance,

::

    title("Parabolic function $-x^2+4x-5$")

gives us the polynomial formatted properly.

Although we have title, the plot is not complete without labelling x and y
axes. Hence we shall label x-axis to "x" and y-axis to "f(x)" ::

    xlabel("x")

As you can see, ``xlabel`` command takes a string as an argument,
similar to the ``title`` command and sets it as the label to x-axis.

.. #[See the diff]

Similarly,

::

    ylabel("f(x)")

sets the name of the y-axis as "f(x)"

Let us now see how to name or annotate a point on the plot. For example the
point (2, -1) is the local maxima. We would like to name the point
accordingly. We can do this by using

::

    annotate("local maxima", xy=(2, -1))

As you can see, the first argument to ``annotate`` command is the name we
would like to mark the point as and the second argument is the co-ordinates
of the point at which the name should appear. It is a sequence containing two
numbers. The first is x co-ordinate and second is y co-ordinate.

As we can see, every annotate command makes a new annotation on the figure.

Now we have everything we need to decorate a plot. But, it would be nice to
change the limits of the plot area, so that it looks better. 

We shall look at how to get and set them from the script. We shall first get
the existing limits and then change them as required.

::

    xlim()
    ylim()

We see that ``xlim`` function returns the current x axis limits and ylim
function returns the current y-axis limits.

Let us look at how to set the limits.

::

    xlim(-4, 5)

We see the limits of x-axis are now set to -4 and 5.

Similarly

::

    ylim(-15, 2)

sets the limits of y-axis appropriately.

Saving to Scripts
=================

While we are at it, let's look at how to save all the things we typed into
our interpreter into scripts that can be used anytime we like. 

Let's now look at the history of the commands we have typed. The history can
be retreived by using ``%hist`` command.

::

    %hist


As you can see, it displays a list of recent commands that we typed. Every
command has a number in front, to specify in which order and when it was
typed.

Please note that there is a % sign before the hist command. This implies that
``%hist`` is a command that is specific to IPython and not available in the
vanilla Python interpreter. These type of commands are called as magic
commands.

Also note that, the ``%hist`` itself is a command and is displayed as the
most recent command. We should note that anything we type in is stored as
history, irrespective of whether it is a valid command or an error or an
IPython magic command.

If we want only the recent 5 commands to be displayed, we pass the number as
an argument to ``%hist`` command. 

::

    %hist 5 

displays the recent 5 commands, inclusive of the ``%hist`` command. The
default number is 40.

To list all the commands between 5 and 10, type

::

    %hist 5-10

Now that we have the history, we would like to save the required lines of
code from history to reproduce the plot of the parabolic function. This is
possible by using the ``%save`` command.

Before we do that, let us first look at history and identify what lines of
code we require.

::

    %hist

The first command is linspace. But second command is a command that gave us
an error. Hence we do not need second command. The commands from third to
sixth and eighth are required. 

::

    %save plot_script.py 1 3-6 8

The command saves first and then third to sixth and eighth lines of code into
the specified file.

The first argument to %save is the path of file to save the commands and the
arguments there after are the commands to be saved in the given order.

Now that we have the required lines of code in a file, let us learn how to
run the file as a python script. We use the IPython magic command ``%run`` to
do this. 

::

   %run -i plot_script.py

The script runs but we do not see the plot. This happens because when we are
running a script and we are not in interactive mode anymore.

Hence on your IPython terminal type

::

    show()

to show the plot.

The reason for including a ``-i`` after ``run`` is to tell the interpreter
that if any name is not found in script, search for it in the interpreter.
Hence all these ``sin``, ``plot``, ``pi`` and ``show`` which are not
available in script, are taken from the interpreter and used to run the
script.

Saving Plots
============

Let us now learn to save the plots, from the command line, in different
formats. 

Let us plot a sine curve from minus 3pi to 3pi. 

::

  x = linspace(-3*pi,3*pi,100)
  plot(x,sin(x))

As, you can see we now have a sine curve. Let's now see how to save the plot.

For saving the plot, we will use ``savefig()`` function, and it has to be
done with the plot window open. The statement is, ::

  savefig('sine.png')

Notice that ``savefig`` function takes one argument which is the filename.
The last 3 characters after the ``.`` in the filename is the extension or
type of the file which determines the format in which you want to save.

Also, note that we gave the full path or the absolute path to which we
want to save the file.

Here we have used an extension ``.png`` which means the plot gets saved as a
PNG image. 

You can check file which has been saved as ``sine.png`` 

``savefig`` can save the plot in many formats, such as pdf, ps, eps, svg and
png. 



Multiple Plots
==============

Let us now learn, how to draw more than one plot, how to add legends to each
plot to indicate what each plot represents. We will also learn how to switch
between the plots and create multiple plots with different regular axes which
are also called as subplots.

Let us first create set of points for our plot. For this we will use the
command called linspace::

  x = linspace(0, 50, 10)

As we know, x has 10 points in the interval between 0 and 50 both inclusive.

Now let us draw a plot simple sine plot using these points

::

  plot(x, sin(x))

This should give us a nice sine plot.

Oh! wait! It isn't as nice, as we expected. The curve isn't very smooth, why?
In the ``linspace`` command, we chose too few points in a large interval
between 0 and 50 for the curve to be smooth. So now let us use linspace again
to get 500 points between 0 and 50 and draw the sine plot

::

  y = linspace(0, 50, 500)
  plot(y, sin(y))

Now we see a smooth curve. We can also see that, we have two plots, one
overlaid upon another. Pylab overlays plots by default.

Since, we have two plots now overlaid upon each other we would like to have a
way to indicate what each plot represents to distinguish between them. This
is accomplished using legends. Equivalently, the legend command does this for
us

::

  legend(['sine-10 points', 'sine-500 points'])

Now we can see the legends being displayed for the respective plots. The
legend command takes a single list of parameters where each parameter is the
text indicating the plots in the order of their serial number.

Additionally, we could give the ``legend`` command an additional argument to
choose the location of the placement, manually. By default, ``pylab`` places
it in the location it thinks is the best. The example below, places it in the
center of the plot. Look at the doc-string of ``legend`` for other locations.

::

  legend(['sine-10 points', 'sine-500 points'], loc='center')

We now know how to draw multiple plots and use legends to indicate which plot
represents what function, but we would like to have more control over the
plots we draw. Like plot them in different windows, switch between them,
perform some operations or labeling on them individually and so on. Let us
see how to accomplish this. Before we move on, let us clear our screen.

::

  clf()

To accomplishing this, we use the figure command

::

  x = linspace(0, 50, 500)
  figure(1)
  plot(x, sin(x), 'b')
  figure(2)
  plot(x, cos(x), 'g')

Now we have two plots, a sine plot and a cosine plot in two different
figures.

The figure command takes an integer as an argument which is the serial number
of the plot. This selects the corresponding plot. All the plot commands we
run after this are applied to the selected plot. In this example figure 1 is
the sine plot and figure 2 is the cosine plot. We can, for example, save each
plot separately

::

  savefig('cosine.png')
  figure(1)
  title('sin(y)')
  savefig('sine.png')

We also titled our first plot as 'sin(y)' which we did not do for the second
plot.

Let us now do the following. Draw a line of the form y = x as one figure and
another line of the form y = 2x + 3. Switch back to the first figure,
annotate the x and y intercepts. Now switch to the second figure and annotate
its x and y intercepts. Save each of them.

To solve this problem we should first create the first figure using
the figure command. Before that, let us first run clf command to make
sure all the previous plots are cleared

::

  clf()
  figure(1)
  x = linspace(-5, 5, 100)
  plot(x, x)

Now we can use figure command to create second plotting area and plot
the figure

::

  figure(2)
  plot(x, ((2 * x) + 3))

Now to switch between the figures we can use figure command. So let us
switch to figure 1. We are asked to annotate x and y intercepts of the
figure 1 but since figure 1 passes through origin we will have to
annotate the origin. We will annotate the intercepts for the second
figure and save them as follows

::

  figure(1)
  annotate('Origin', xy=(0.0, 0.0)
  figure(2)
  annotate('x-intercept', xy=(0, 3))
  annotate('y-intercept', xy=(0, -1.5))
  savefig('plot2.png')
  figure(1)
  savefig('plot1.png')

We can close the figures from the terminal by using the ``close()`` command. 

::

    close()
    close()

The first ``close`` command closes figure 1, and the second one closes the
figure 2. We could have also use the ``close`` command with an argument
'all', to close all the figures. 

::

    close('all')

At times we run into situations where we want to compare two plots and in
such cases we want to draw both the plots in the same plotting area. The
situation is such that the two plots have different regular axes which means
we cannot draw overlaid plots. In such cases we can draw subplots.

We use subplot command to accomplish this

::

    subplot(2, 1, 1)

``subplot`` command takes three arguments, number of rows, number of columns
and the plot number, which specifies what subplot must be created now in the
order of the serial number. In this case we passed 1 as the argument, so the
first subplot that is top half is created. If we execute the subplot command
as

::

  subplot(2, 1, 2)

the lower subplot is created. Now we can draw plots in each of the subplot
area using the plot command.

::

  x = linspace(0, 50, 500)
  plot(x, cos(x))

  subplot(2, 1, 1)
  y = linspace(0, 5, 100)
  plot(y, y ** 2)

This created two plots one in each of the subplot area. The top subplot holds
a parabola and the bottom subplot holds a cosine curve.

As seen here we can use subplot command to switch between the subplot
as well, but we have to use the same arguments as we used to create
that subplot, otherwise the previous subplot at that place will be
automatically erased. It is clear from the two subplots that both have
different regular axes. For the cosine plot x-axis varies from 0 to
100 and y-axis varies from 0 to 1 where as for the parabolic plot the
x-axis varies from 0 to 10 and y-axis varies from 0 to 100

Plotting Data
=============

We often require to plot points obtained from experimental observations,
instead of the analytic functions that we have been plotting, until now. We
shall now learn to read data from files and read it into sequences that can
later be used to plot.

We shall use the ``loadtxt`` command to load data from files. We will be
looking at how to read a file with multiple columns of data and load each
column of data into a sequence.

Now, Let us begin with reading the file ``primes.txt``, which contains just a
list of primes listed in a column, using the loadtxt command. The file, in
our case, is present in ``primes.txt``.

Now let us read this list into the variable ``primes``.

::

  primes = loadtxt('primes.txt')

``primes`` is now a sequence of primes, that was listed in the file,
``primes.txt``.

We now type, ``print primes`` to see the sequence printed.

We observe that all of the numbers end with a period. This is so, because
these numbers are actually read as ``floats``. 

Now, let us use the ``loadtxt`` command to read a file that contains two
columns of data, ``pendulum.txt``. This file contains the length of the
pendulum in the first column and the corresponding time period in the second.
Note that ``loadtxt`` needs both the columns to have equal number of rows.

Let us, now, read the data into the variable ``pend``. Again, it is
assumed that the file is in our current working directory. 

::

  pend = loadtxt('pendulum.txt')

Let us now print the variable ``pend`` and see what's in it. 

::

  print pend

Notice that ``pend`` is not a simple sequence like ``primes``. It has a
sequence of items in which each item contains two values. Let us use an
additional argument of the ``loadtxt`` command, to read it into two separate,
simple sequences. We add the argument ``unpack=True`` to the ``loadtxt``
command. 

::

  L, T = loadtxt('pendulum.txt', unpack=True)

Let us now, print the variables L and T, to see what they contain.

::

  print L
  print T

Notice, that L and T now contain the first and second columns of data
from the data file, ``pendulum.txt``, and they are both simple
sequences. ``unpack=True`` has given us the two columns into two
separate sequences instead of one complex sequence. 

Now that we have the required data in sequences, let us see how to plot it. 

Since we already have the values of L and T as two different sequences, we
now need to calculate T squared. We shall be plotting L vs. T^2 values.

To obtain the square of sequence T we will use the function ``square`` 

::

   Tsq = square(T)

Now to plot L vs T^2 we will simply type 

::

  plot(L, Tsq, '.')

For any experimental data, there is always an error in measurements due to
instrumental and human constraints. Now we shall try and take into account
error into our plots. 

We shall read the read the error values from the file ``pendulum_error.txt``
along with the L and T values. 

::

    L, T, L_err, T_err = loadtxt('pendulum_error.txt', unpack=True)

  
Now to plot L vs T^2 with an error bar we use the function ``errorbar()``

::
    
    errorbar(L, Tsq , xerr=L_err, yerr=T_err, fmt='b.')

This gives a plot with error bar for x and y axis. The dots are of blue
color. The parameters ``xerr`` and ``yerr`` are error on x and y axis and
``fmt`` is the format of the plot.


You can explore other options of ``errorbar`` by looking at it's
documentation. 

::

   errorbar?


Other kinds of Plots
====================

We shall now briefly look at a few other kinds of plots, namely, the scatter
plot, the pie chart, the bar chart and the log-log plot.

Let us start with scatter plot. 

In a scatter plot, the data is displayed as a collection of points, each
having the value of one variable determining the position on the horizontal
axis and the value of the other variable determining the position on the
vertical axis. This kind of plot is also called a scatter chart, a scatter
diagram or a scatter graph.

Now, let us plot a scatter plot showing the percentage profit of a company A
from the year 2000-2010. The data for the same is available in the file
``company-a-data.txt``.

The data file has two lines with a set of values in each line, the first line
representing years and the second line representing the profit percentages.

To produce the scatter plot, we first need to load the data from the file
using ``loadtxt``. 

::

    year,profit = loadtxt('company-a-data.txt', dtype=int)

By default loadtxt converts the value to float. The ``dtype=type(int())``
argument in loadtxt converts the value to integer as we require the data as
integers.

In-order to generate the scatter graph we will use the function ``scatter()``

::

    scatter(year, profit)

Notice that we passed two arguments to ``scatter()`` function, first one the
values in x-coordinate, year, and the other the values in y-coordinate, the
profit percentage.

Now let plot a pie chart for the same data. A pie chart or a circle graph is
a circular chart divided into sectors, illustrating proportion.

Plot a pie chart representing the profit percentage of company A, with the
same data from file ``company-a-data.txt``.  We shall reuse the data we have
already read from the file. 

We can plot the pie chart using the function ``pie()``.

::

    pie(profit, labels=year)

Notice that we passed two arguments to the function ``pie()``. First one the
values and the next one the set of labels to be used in the pie chart.

Now let us move on to the bar charts. A bar chart or bar graph is a chart
with rectangular bars with lengths proportional to the values that they
represent.

Plot a bar chart representing the profit percentage of company A, with the
same data from file ``company-a-data.txt``.

We can plot the bar chart using the function ``bar()``.

::

    bar(year, profit)

Note that the function ``bar()`` needs at least two arguments one the values
in x-coordinate and the other values in y-coordinate which is used to
determine the height of the bars.

Now let us move on to the log-log plot. A log-log graph or a log-log plot is
a two-dimensional graph of numerical data that uses logarithmic scales on
both the horizontal and vertical axes. 

Due to the nonlinear scaling of the axes, a function of the form y = ax^b
will appear as a straight line on a log-log graph. 

Plot a ``log-log`` chart of y=5*x^3 for x from 1-20.

Before we actually plot let us calculate the points needed for that. 

::

    x = linspace(1,20,100)
    y = 5*x**3

Now we can plot the log-log chart using ``loglog()`` function,

::

    loglog(x, y)

For the sake of clarity, let us make a linear plot of x vs. y. 

::

    plot(x, y)

Observing the two plots together should give you some clarity about the
``loglog`` plot. 

Help about matplotlib can be obtained from
http://matplotlib.sourceforge.net/contents.html

That brings us to the end of the discussion on plots and matplotlib. We have
looked a making simple plots, embellishing plots, saving plots, making
multiple plots, plotting data from files, and a few varieties of plots. 

.. 
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: nil
   fill-column: 77
   End:


