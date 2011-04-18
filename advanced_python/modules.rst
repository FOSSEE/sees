Using Python modules
====================

We shall, in this section, see how to run Python scripts from the command
line, and more details about importing modules. 

Let us create a simple python script to print hello world. Open your text
editor and type the following, and save the script as ``hello.py``. 

::

    print "Hello world!"

Until now we have been running scripts from inside IPython, using

::

    %run -i hello.py

But, as we know, IPython is just an advanced interpreter and it is not
mandatory that every one who wants to run your program has IPython
installed. 

So, the right method to run the script, would be to run it using the Python
interpreter. Open the terminal and navigate to the directory where
``hello.py`` is saved. 

Then run the script by saying, 
::

    python hello.py

The script is executed and the string ``Hello World!`` has been printed. 

Now let us run a script that plots a simple sine curve in the range -2pi to
2pi, using Python, instead of running it from within IPython. 

Type the following lines and save it in ``sine_plot.py`` file. 

::

    x = linspace(-2*pi, 2*pi, 100)
    plot(x, sin(x))
    show()

Now let us run sine_plot.py as a python script.

::

    python sine_plot.py

Do we get the plot? No! All we get is error messages. Python complains that
``linspace`` isn't defined. What happened? Let us try to run the same
script from within IPython. Start IPython, with the ``-pylab`` argument and
run the script. It works!

What is going on, here? IPython when started with the ``-pylab`` option, is
importing a whole set of functionality for us to work with, without
bothering about importing etc. 

Let us now try to fix the problem by importing ``linspace``. 

Let's add the following line as the first line in the script. 

::

    from scipy import *

Now let us run the script again,

::

    python sine_plot.py

Now we get an error, that says ``plot`` is not defined. Let's edit the file
and import this from pylab. Let's add the following line, as the second
line of our script. 

::

    from pylab import *

And run the script,

::

    python sine_plot.py

Yes! it worked. So what did we do?

We actually imported the required functions and keywords, using ``import``.
By using the *, we are asking python to import everything from the
``scipy`` and ``pylab`` modules. This isn't a good practice, as 
  1. it imports a lot of unnecessary things
  2. the two modules may have functions with the same name, which would
  cause a conflict. 

One of the ways out is to import only the stuff that we need, explicitly. 

Let us modify sine_plot.py by replacing the import statements with the
following lines. 

::

    from scipy import linspace, pi, sin
    from pylab import plot, show

Now let us try running the code again as,

::

    python show_plot.py

As expected, this works. But, once the number of functions that you need to
import increases, this is slightly inconvenient. Also, you cannot use
functions with the same name, from different modules. To overcome this,
there's another method. 

We could just import the modules as it is, and use the functions or other
objects as a part of those modules. Change the import lines, to the
following. 

::

    import scipy
    import pylab

Now, replace ``pi`` with ``scipy.pi``. Similarly, for ``sin`` and
``linspace``. Replace ``plot`` and ``show`` with ``pylab.plot`` and
``pylab.show``, respectively. 

Now, run the file and see that we get the output, as expected. 

We have learned how to import from modules, but what exactly is a module?
How is one written? 

A module is simply a Python script containing the definitions and
statements, which can be imported. So, it is very easy to create your own
modules. You just need to stick in all your definitions into your python
file and put the file in your current directory. 

When importing, Python searches the locations present in a variable called
the Python path. So, our module file should be present in one of the
locations in the Python path. The first location to be searched is the
current directory of the script being run. So, having our module file in
the current working directory, is the simplest way to allow it to be used
as a module and import things from it. 

Python has a very rich standard library of modules. It is very extensive,
offering a wide range of facilities. Some of the standard modules are,

for Math: math, random
for Internet access: urllib2, smtplib
for System, Command line arguments: sys
for Operating system interface: os
for regular expressions: re
for compression: gzip, zipfile, tarfile
And there are lot more.

Find more information at Python Library reference,
``http://docs.python.org/library/``

There are a lot of other modules like pylab, scipy, Mayavi, etc which
are not part of the standard Python library.

This brings us to the end of our discussion on modules and running scripts
from the command line. 

Writing modules
===============

In this section we shall look at writing modules, in some more detail.
Often we will have to reuse the code that we have previously written. We do
that by writing functions. Functions can then be put into modules, and
imported as and when required. 

Let us first write a function that computes the gcd of two numbers and save
it in a script.

::

    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a

Now, we shall write a test function in the script that tests the gcd
function, to see if it works. 

::

    if gcd(40, 12) == 4 and gcd(12, 13) == 1:
        print "Everything OK"
    else:
        print "The GCD function is wrong"

Let us save the file as gcd_script.py in ``/home/fossee/gcd_script.py`` and
run it. 

::

    $ python /home/fossee/gcd_script.py

We can see that the script is executed and everything is fine.

What if we want to use the gcd function in some of our other scripts. This
is also possible since every python file can be used as a module.

But first, we shall understand what happens when you import a module.

Open IPython and type

::

    import sys
    sys.path

This is a list of locations where python searches for a module when it
encounters an import statement. Hence, when we just did ``import sys``,
python searches for a file named ``sys.py`` or a folder named ``sys`` in
all these locations one by one, until it finds one. We can place our script
in any one of these locations and import it.

The first item in the list is an empty string which means the current
working directory is also searched.

Alternatively, we can also import the module if we are working in same
directory where the script exists.

Since we are in /home/fossee, we can simply do

::

    import gcd_script
    
We can see that the gcd_script is imported. But the test code that we added
at the end of the file is also executed.

But we want the test code to be executed only when the file is run as a
python script and not when it is imported.

This is possible by using ``__name__`` variable.


Go to the file and add

::

    if __name__ == "__main__":
        
before the test code and indent the test code.

Let us first run the code.

::

    $ python gcd_script.py

We can see that the test runs successfully.

Now we shall import the file

::
    
    import gcd_script

We see that now the test code is not executed.

The ``__name__`` variable is local to every module and it is equal to
``__main__`` only when the file is run as a script. Hence, all the code
that goes in to the if block, ``if __name__ == "__main__":`` is executed
only when the file is run as a python script.

.. 
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: nil
   fill-column: 75
   End:
