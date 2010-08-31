LaTeX
=====

Introduction
------------

LaTeX is a typesetting program that produces excellently typeset
documents. Typesetting is placing text onto a page with all the style
formatting defined, so that content looks as intended. It is
extensively used for producing high quality scientific and
mathematical documents. It is also used for producing other kinds of
documents, ranging from simple one page articles or letters to
books. LaTeX is based on the TeX typesetting language.

LaTeX is pronounced either as "Lah-tech" or "Lay-tech"

In this course, we shall use the sample document, ``sample.pdf``, as a
tool to learn various commands of LaTeX. By the end of the sessions on
LaTeX, we will have produced a copy of that document, starting from
scratch.

A Look at the Sample Document
-----------------------------

Let's first look at the basic structure of the sample document.

Slides with screen shots of

  * Title, Author, Date
  * Abstract
  * Sections
  * Subsections
  * Appendix
  * References/Bibliography
  * Tables
  * Figures
  * Math

Writing the source & compiling it
---------------------------------

Let's begin with a simple hello world, to see how to write a LaTeX
document and compile it.  Write the following code into the file
``draft.tex``.  ::

  \documentclass{article}
  \begin{document}
  SciPy is open-source software for mathematics, science, and engineering.   
  \end{document}

To compile the document, do the following in your terminal::

  $ pdfLaTeX draft.tex

This produces the output file ``draft.pdf``

Note: The ``LaTeX`` command is often used, instead of ``pdfLaTeX`` to
get the ``dvi`` output. But, throughout this course, we shall use
pdfLaTeX to compile our documents.

``\documentclass``
------------------

The documentclass command, defines the structure and formatting of our
document. LaTeX typsets the document, based on the documentclass.

LaTeX is a document based markup language. 

First of all, a markup language is a system of annotating text or
adding in extra information to the text that specifies it's structure
or presentation.

LaTeX is a document based markup and not an element based one. You
generally don't have to worry about typesetting each of the elements
of your document. Choosing an appropriate documentclass, gives you a
suitable typesetting. You as an author can worry about the content of
the document, rather than the appearance or presentation of the
document.

Why should you use it?
~~~~~~~~~~~~~~~~~~~~~~

A few reasons for using LaTeX - 

  * It produces documents with excellent visual quality.
  * It does the typesetting for you, leaving you - the author - to
    focus on writing the content.
  * It makes writing math just as easy as writing simple text.
  * It's renowned for it's stability and a virtually bug free code
    base.
  * It is light on your resources as compared to most of the word
    processors available today.
  * It uses plain text files as input and can give output in a variety
    of formats including PDFs and html making it platform independent.
  * It is free software (free as in freedom) and gratis too.
  * It is widely used and has a large user community. 


``\begin`` and ``\end`` commands define environments. In our document,
we have the document environment, which defines the beginning and end
of the content of the document. We place all the content of the
document within this environment.

Also, as you may have noticed, all the commands in LaTeX begin with a
``\``. Note that they are case sensitive. Command names in LaTeX
usually have only alpha characters. Any characters other than alpha
characters, terminate the command name. Parameters to commands are
passed in ``{ }``.


Top Matter
----------

Let us begin with adding the Title, Author's name and the date to the
document.

::

  \documentclass{article}
  \title{A Glimpse at Scipy}
  \author{FOSSEE}
  \date{June 2010}
  \begin{document}
  \maketitle
  SciPy is open-source software for mathematics, science, and engineering.   
  \end{document}

We add the title, the author and the date to the document before the
``\begin{document}`` directive. We compile the document to see if the
details appear in the document, but they donot. These details do not
appear in the document until we use the ``\maketitle`` command with
the document environment to instruct LaTeX to place the top matter
information into the document. Now the document has these details, on
compiling again.

If no date is specified, LaTeX automatically inserts the current date.

Abstract
--------

Next we shall add an abstract to our document. LaTeX provides an
environment, for adding an abstract to the document.  ::

  \documentclass{article}

  \title{A Glimpse at Scipy}
  \author{FOSSEE}
  \date{June 2010}

  \begin{document}

  \maketitle

  \begin{abstract}
  This document shows a glimpse of the features of Scipy that will be explored during this course.
  \end{abstract}

  SciPy is open-source software for mathematics, science, and engineering.   
  \end{document}

The abstract environment is placed at the location where we wish it to
appear in the document.

Sections
--------

Now let's look at how to add (chapters,) sections and sub-sections to
our document. Let's add the section headings and sub headings present
in our sample document to the working copy of our document.

``\section``, ``\subsection``, ``\subsubsection``

On compiling, we can see that the headings of the sections and the
sub-sections appear in the document.

You may have noticed that LaTeX automatically numbers the sections. To
prevent a section from getting numbered, an asterix is appended to the
corresponding sectioning command.

If the document was a longer document, we could have used a report or
a book class. (Note: Books donot have the abstract environment.) Let's
look at what happens to the document, when we change it to the report
class.

The numbering strangely begins from zero, now. This is because,
chapters have an additional sectioning command called
``\chapter``. The chapter is one level above a section and since, our
document does not have a ``\chapter`` command, the sections are
numbered from 0. To change this, we add a chapter command before the
first section. We say::

  \chapter{One}

Now, observe that we now have a chapter title appearing and the
numbering starting from 1.

Also, note that the subsubsections donot get a numbering now. This is
controlled by a variable called the secnumdepth. By default it is set
to 2. We can now, change it to 3 and get numbering for subsubsections
also.  ::

  \setcounter{secnumdepth}{3}

What do you expect to happen if we changed the secnumdepth to 1? What
if it is 0? -1? {Lab excercise}


Appendix
--------

Notice that our document also has an appendix. Let's add an appendix
to our document.

::

  \appendix
  \section{Plotting using Pylab}

Table of Contents
-----------------

Our sample document is not long enough to warrant a table of contents,
but let us learn to add a table of contents to a LaTeX document. If
you ever tried adding a table of contents, to a document in a
wordprocessor, you would know how much of a trouble it is. In LaTeX,
it is a matter of just one command and placing the command at the
location where you would want to have the table of contents. Let's now
add a table of contents to our draft. Now, compile the document and
look at the output document. It does not have the table of contents!

On the first compilation only the "Contents" heading appears in the
document, but the actual table does not appear. You will need to
compile your document once more, for the actual table to appear in
your document. On the first run, LaTeX has gone through your document
and generated a temporary file (``.toc``), with the entries that
should go into the table of contents. These entries are made, when you
compile your document for the second time.

Note that any section/block that has been numbered automatically
appears in the table of contents. It is possible to get un-numbered
sections, for instance a Preface or a Foreword section to appear in
the Table of Contents.

Let's change our Introduction section to be an un-numbered one and try
to make it appear in the table-of-contents.  ::

  \section*{Introduction}
  \addcontentsline{toc}{section}{Intro}

We shall talk about adding and managing bibliographies, later in the
course.

Now, that we have the basic structure of the document, let's get into
the content and the details of it.

Typesetting Text
----------------

Let's begin with adding the second paragraph to the introduction
section. Let's place the text of the second para, after the first
line, that we already have. Now, compile the document. 

Notice, that the second para appears in continuation with the previous
line. To start a new paragraph in LaTeX, we need to insert an empty
line. Multiple empty lines are considered as a single empty line. To
start a new line, use the ``\newline`` or ``\\`` command. Notice the
difference (in the output), in starting a new paragraph and starting a
newline. A new paragraph is indented.

Quotation Marks
---------------

Look at the quotation marks around the text, Sigh Pie. They are not
formatted properly. To place quotation marks in LaTeX, you should use
````` character for the left quote & ``'`` character for the right
quote. For double quotes, they should be used twice.

Fonts
-----

The names of the software tools, Scilab, Matlab, etc. appear in
italics or emphasized as it is called in LaTeX. To emphasize text, the
``\emph`` command is used.

Let's also add the contents of the subsection "Sub-packages of
Scipy". We shall add the table as plain text, until we learn how to
edit tables.

Let's try and form a tabular structure by separating the left and
right columns using spaces. On compiling we find that LaTeX doesn't
add multiple spaces between words. Just like multiple empty lines,
multiple spaces are considered as a single space.

The names of the sub-packages appear in a fixed width font in the
sample document provided to us. The headings of the columns appear in
bold-face. Let's make changes to this effect.

``\textbf`` is used to change text to bold face and ``\texttt`` is
used to change text to fixed width font.

We could also change the separating - (hyphen) to an em-dash (or
en-dash) -- is em-dash and --- is an em-dash, to improve the
appearance of the document.

Lists
-----

The section on Use of Scipy in this course, contains lists. Let's now
add lists to our document. The ``enumerate`` environment adds numbered
lists to our document and the ``itemize`` environment adds un-numbered
lists. ``\item`` command adds a new entry to a list. Note, that LaTeX
can easily handle nested lists. In fact most environments can be
embedded within other environments, without any problems.

LaTeX also has a description list, which shall be looked at, during
the lab sessions.

Footnotes, Labels and References
--------------------------------

Let's now add the footnote to pylab. LaTeX provides a footnote command
to add a footnote.

We added the footnote with Appendix A, as plain text. But, in case we
added another Appendix before the section on using ``pylab``, the
footnote will have to be edited. To avoid this, LaTeX provides a handy
system of labels and referencing.

We first add a label to the section that we want to refer in this
footnote. Then, we change the footnote, and add the reference to this
label instead of the character A. If you look at the output after
compiling the document once, you will see that the footnote has
question marks instead of the section number.  You will have to
compile once again, for the section number to appear in the footnote.


Including code
--------------

In the footnote above, and in the table for the sub-packages list, we
used the ``\texttt`` command to get a fixed width font. But we could
instead use an environment provided by LaTeX to include pre-formatted
text or code. LaTeX by default provides the verbatim environment to
include pre-formatted text. You can try that out during the lab
session. We shall look at using the listings package, specifically
meant for including code in our document.

First of all you need to tell LaTeX, that you want to use the listings
package in your document. We add the directive
``\usepackage{listings}`` to the preamble of our document.

Then we set the language of the code that we are going to embed into
our document. For this we use the lstset command.  ::
 
  \lstset{language=Python,
          showstringspaces=false,}

The listings package allows you to use color and do a lot of things
with your embedded code, but all that during a lab exercise.

Now, to put a line of code, inline and not as a separate block, we use
the ``\lstinline`` command. We change the name pylab in the footnote
to use lstinline instead of the texttt. To embed a block of code, we
use the lstlisting environment (``\begin{lstlisting}`` and
``\end{lstlisting}``). For example, let's add the code to the Appendix
of our document.

Figures, Tables and Floats
--------------------------

Let's now add the figure, to the appendix.

To include graphics in a LaTeX document, we need to use the graphicx
package. Add the ``\usepackage{graphicx}`` directive to the preamble
of the document.

To add the graphic, use the ``includegraphics`` command. The relative
path of the image that we wish to include is passed as an argument to
includegraphics. It takes an optional argument of scaling the
image. We use a scale of 0.4 to scale our image.

It takes other optional arguments. 

  ``width=x``, ``height=x`` 
    If only the height or width is specified,
    the image is scaled, maintaining the aspect ratio.

  ``keepaspectratio``
    This parameter can either be set to true or false. When set to
    true, the image is scaled according to both width and height,
    without changing the aspect ratio, so that it does not exceed both
    the width and the height dimensions.

  ``angle=x``
    This option can be used to rotate the image by ``x`` degrees,
    counter-clockwise.

Figures (and tables) are treated specially because, they cannot be
broken across pages. They are "floated" across to the next page, if
they donot fit on the current page, filling the current page with
text.

To make our graphic into a float, we should enlose it within a figure
environment. For a table, the table environment should be used. We now
move our graphic into a figure environment. The figure environment
takes an additional parameter for the location of the
float. ``\begin{figure}[hbtp!]``. The specifiers ``htbp`` are
permissions to place the float at various locations. ``t`` for top of
page, ``b`` for bottom of page, ``p`` for a separate page for floats
and ``h`` for here, as in the same place where the command appears in
the source. ``!`` mark overrides a few of LaTeX's internal parameters
for good position of floats.

The figure environment also, allows us to add a caption to the graphic
using the ``\caption`` command.

To place the graphic in the center aligned in the page, we use the
center environment.

To label a figure, we just add a label with in the figure
environment. Note, that the label to a figure should be added after
the caption command. Also, note that tables are auto-numbered.

Let us finish the appendix, by adding the content present at the
beginning of the appendix. The bibliographic citations will be dealt
with later.

Tables
~~~~~~

Now, let us look at the other kind of floats - Tables. We shall
convert the list of sub-packages in the sub-packages section to a
table.

To begin a table, we use the tabular environment. And to make this a
float, it is enclosed in the table environment. The table environment
also allows us to add captions to the table and Tables are also auto
numbered.

The tabular environment takes as arguments the columns and the
formatting of each column. The possible arguments to the tabular
environment are

+---------------+------------------------------------+
| ``l``         | left justified column content      |
+---------------+------------------------------------+
| ``r``         | right justified column content     |
+---------------+------------------------------------+
| ``c``         | centered column content            |
+---------------+------------------------------------+
| ``|``         | produces a vertical line.          |
+---------------+------------------------------------+

It also takes an optional parameter that specifies the position of the
table; ``t`` for top, ``b`` for bottom, or ``c`` for center.

Each column of a table is separated by an ``&`` symbol and each row is
separated by a new line. The ``\hline`` command allows you to draw
horizontal lines between two rows of the table. But it does not allow
you do draw partial lines. ``\cline{a-b}`` draws a horizontal line
from column ``a`` to column ``b``.

We also add a label to the table and refer to it in the first line of
the section.

You could also add a listoftables or listoffigures to the document,
similar to the way we added table of contents.

Typesetting Math
----------------

Now we shall move to typesetting the Math in the sample document given
to us. We shall start with the Matrices subsection.

In general, it is advised to use the AMS-LaTeX bundle to typeset
mathematics in LaTeX. AMS-LaTeX is a collection of packages and
classes for mathematical typesetting.

We load ``amsmath`` by issuing the ``\usepackage{amsmath}`` in the
preamble. Through out this section, it is assumed that the ``amsmath``
package has been loaded.

Let's now typeset the matrix A.

To typeset math, we just have to enclose it within ``\(`` and ``\)``
or a pair of ``$`` signs.

To typeset the matrix A, we use the ``bmatrix`` environment. It works
similar to a tabular environment - ``&`` is used to demarcate columns
and ``\\`` is used to add a new row. ``bmatrix`` environment gives the
``[`` ``]`` as delimiters. There are 5 other matrix environments
giving matrices with other delimiters - ``matrix`` (none), ``pmatrix``
``(``, ``Bmatrix`` ``{``, ``vmatrix`` ``|`` and ``Vmatrix`` ``||``.

To write the name of the matrix A, a bold-faced A is used. This is
obtained by using the ``\mathbf`` command.

This subsection doesn't have much more math. The next section on
inverse doesn't have anything new except for writing inverse of A.

To typeset superscripts in LaTeX, the ``^`` character is used. The
carat operator just acts on the next character. To have multiple
characters as superscript they must be enclosed in ``{ }``. Similarly
for typesetting text as subscripts the ``_`` character is used.

To typeset the summation symbol, use the command ``\sum.`` The upper
and lower limits are specified using the ``^`` and ``_``
characters. Similarly, the integral symbol is obtained using the
``\int`` command.

Next, let us type in the equation present in the section on
Determinants. Note that it is different from all the math we've typed
until now, since it is not inline and is "displayed", in the LaTeX
lingo. LaTeX has a number of environments for displaying equations,
with minor subtle differences. In general use ``\[`` ``\]`` to typeset
displayed equations without numbering them. ``\begin{equation*}`` is
equivalent to it.  To obtain numbered equations use
``\begin{equation}``.

Next we wish to typeset a group of equations. The equation environment
does not accept ``\\`` to get a new line. For multiple equations
amsmath has a handful of environments with subtle differences. We
shall use the ``eqnarray`` environment. ``eqnarray*`` environment
gives unnumbered equations, as expected. The ``eqnarray`` environment
works similar to a table environment. The parts of the equation that
need to be aligned are indicated using an ``&`` symbol. The
``newline`` command is used to enter a every new equation after the
first one. We now typeset the equations in the section on linear
equations using the ``eqnarray`` environment. (The equations in the
determinants section use ``eqnarray*``)

We next typeset the math in the section on polynomials. To typeset
fractions use the ``\frac`` command. To typeset surds, we use the
``\sqrt`` command with the optional paramter of ``[n]``.

Inserting Greek letters into LaTeX is simple. ``\alpha``, ``\beta``,
``\gamma``, ... on for small letters and ``\Alpha``, ``\Beta``,
``\Gamma``, ... for capital.

Also, math environments do not give extra spaces using the space or
tab characters. The following commands are available to specify the
spacing required.

+---------+--------------------+---------+
| Abbrev. | Spelled out        | Example |
+---------+--------------------+---------+
| ``\,``  | ``\thinspace``     |         |
+---------+--------------------+---------+
| ``\:``  | ``\medspace``      |         |
+---------+--------------------+---------+
| ``\;``  | ``\thickspace``    |         |
+---------+--------------------+---------+
|         | ``\quad``          |         |
+---------+--------------------+---------+
|         | ``\qquad``         |         |
+---------+--------------------+---------+
| ``\!``  | ``\negthinspace``  |         |
+---------+--------------------+---------+
|         | ``\negmedspace``   |         |
+---------+--------------------+---------+
|         | ``\negthickspace`` |         |
+---------+--------------------+---------+

Bibliography
------------

Let's now look at how to write bibliography and cite references.

Writing bibliographies in LaTeX using the ``thebibliography``
environment is pretty easy. You simply have to list down all the
bibliography items within the bibliography environment.

Each entry of the bibliography begins with the command
``\bibitem[label]{name}``. The name is used to cite the bibliography
item within the document using ``\cite{name}``. The label option
replaces the numbers from the auto enumeration with the labels given.

The ``9`` passed as an argument to ``thebibliography`` command
indicates the maximum width of the label that the references will
have. In our sample document, we have less than 10 items in the
Bibliography and therefore we use 9.

Presentations with Beamer
-------------------------

Using beamer for you presentations is a good idea, since you can use
the LaTeX that you have used for the report/document for the
presentation as well.

To write a ``beamer`` presentation, it is recommended that we use one
of the templates that beamer provides. We shall use the
``speaker_introduction`` template to get started with beamer.

As you can see, the document begins with the ``documentclass`` being
set to beamer.

``\usetheme`` command sets the theme to be used in the presentation.

``\usecolortheme`` command sets the color theme of the presentation.

Notice that each slide is enclosed within ``\begin{frame}`` and
``\end{frame}`` commands. The ``\begin{frame}`` command can be passed
the Title and Subtitle of the slide as parameters.

The title page of the presentation can be set like any other LaTeX
document.

To do overlays, use the ``\pause`` command. It does sequential
overlays. Non sequential overlays can also be done. (Lab exercise.)

If you have fragile environments like ``verbatim`` or ``lstlisting``,
you need to give the frame an optional parameter ``[fragile]``.

To achieve more with beamer, it is highly recommended that you look at
the ``beameruserguide``.

