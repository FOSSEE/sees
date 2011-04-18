Exercises
=========

#. Consider the iteration :math:`$x_{n+1} = f(x_n)$` where
   :math:`$f(x) = kx(1-x)$`. Plot the successive iterates of this
   process.

#. Plot this using a cobweb plot as follows:

   #. Start at :math:`$(x_0, 0)$`
   #. Draw line to :math:`$(x_i, f(x_i))$`;
   #. Set :math:`$x_{i+1} = f(x_i)$`
   #. Draw line to :math:`$(x_i, x_i)$`
   #. Repeat from 2 for as long as you want

#. Plot the Koch snowflake. Write a function to generate the necessary
   points given the two points constituting a line.

   #. Split the line into 4 segments.
   #. The first and last segments are trivial.
   #. To rotate the point you can use complex numbers, recall that
      :math:`$z e^{j \theta}$` rotates a point :math:`$z$` in 2D by
      :math:`$\theta$`.
   #. Do this for all line segments till everything is done.

#. Show rate of convergence for a first and second order finite
   difference of sin(x)

#. Given, the position of a projectile in in ``pos.txt``, plot it's
   trajectory.

   -  Label both the axes.
   -  What kind of motion is this?
   -  Title the graph accordingly.
   -  Annotate the position where vertical velocity is zero.

#. Write a Program that plots a regular n-gon(Let n = 5).

#. Create a sequence of images in which the damped oscillator
   (:math:`$e^{-x/10}sin(x)$`) slowly evolves over time.

.. 
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: nil
   fill-column: 77
   End:

