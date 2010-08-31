LaTeX
=====

Introduction
------------
LaTeX is a typesetting program that produces excellently typeset documents. Typesetting is placing text onto a page with all the style formatting defined, so that content looks as intended. It is extensively used for producing high quality scientific and mathematical documents. It is also used for producing other kinds of documents, ranging from simple one page articles or letters to books. LaTeX is based on the TeX typesetting language. 

TeX
~~~

TeX is a typesetting system designed and developed by Donald E. Knuth, the renowned Computer Scientist and Emeritus professor at Stanford University.

It was designed with two goals in mind-

1. To allow anybody to produce high-quality books using a reasonable amount of effort. 
2. To provide a system that would give the exact same results on all computers, now and in the future

TeX is well known for it's stability and portability. TeX is known to be virtually bug free. 

The current version of TeX is 3.1415926 and is converging to π.

LaTeX
~~~~~

LaTeX is an extension of TeX, consisting of TeX macros and a program to parse the LaTeX files. It is supposed to be an easier to use language than TeX, but producing the same quality of output. It was developed by Leslie Lamport in the early 1980s and is now being maintained and developed by the LaTeX3 Project.

LaTeX is pronounced either as "Lah-tech" or "Lay-tech"

Why should you use it?
~~~~~~~~~~~~~~~~~~~~~~

A few reasons for using LaTeX - 

  * It produces documents with excellent visual quality. 
  * It does the typesetting for you, leaving you - the author - to focus on writing the content.
  * It makes writing math just as easy as writing simple text.
  * It's renowned for it's stability and a virtually bug free code base. 
  * It is light on your resources as compared to most of the word processors available today. 
  * It uses plain text files as input and can give output in a variety of formats including PDFs and html making it platform independent.
  * It is free software (free as in freedom) and gratis too.
  * It is widely used and has a large user community. 

First Document
--------------

Let's begin by writing a simple LaTeX, Hello World, document. The following code is typed out into a text editor. 

::

  %hello.tex - The Hello World of LaTeX
  \documentclass{article}

  \begin{document}
    Hello, World!
  \end{document}

Save the file as ``hello.tex`` and open up a terminal to compile your ``tex`` file to get the output in a ``pdf`` format. 

Compiling & Output
~~~~~~~~~~~~~~~~~~

::

  $pdflatex hello.tex

  Output written on hello.pdf (1 page, 5733 bytes).
  Transcript written on hello.log.

Open the ``hello.pdf`` to see the output as shown. 

Note: The command ``latex`` is often used to get the ``dvi`` output. But, throughout this course, we shall use pdflatex to compile our documents. 

What does it mean? - Understanding the source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``%hello.tex - First LaTeX document``

  The first line is a comment. It is meant only for human readers and LaTeX simply ignores that line. Anything following a ``%`` symbol, until the end of the line, is ignored by LaTeX. 

``\documentclass{article}``

  This line is a command and sets the ``documentclass`` of the document to ``article``. LaTeX has other classes like ``report``, ``book``, ``letter``, etc. The typesetting of the document varies, depending on the ``documentclass`` of the document. 


``\begin{document}``

  This line informs LaTeX that this is the beginning of the content of the document. The command, technically speaking, marks the beginning of the ``document`` environment. 

``Hello, World!``

  This is the actual text displayed in the document. 

``\end{document}``

  The end command marks the end of the ``document`` environment. It tells LaTeX that the document is complete and LaTeX will simply ignore anything written after this line.

Some Basics
~~~~~~~~~~~

LaTeX treats multiple empty spaces (or lines) as a single space (or line). An empty line between two lines of text is considered as a change of paragraphs. 

In order to explicitly instruct LaTeX to start a new-line, ``\\`` or ``\newline`` command is used. Appending ``*`` to ``\\``,  instructs LaTeX to create a new line, without creating a new page at that point. 

As already mentioned, ``%`` symbol marks the beginning of a comment. How would we then use it in our document's text? ``%`` is one of the many special characters and is used by escaping it with a backslash, as shown. Other special characters are  ``~ # $ ^ & _ { } \``. All of them, except the backslash character, can be inserted in the document by escaping them with a ``\`` character. To insert the ``\`` character, ``\textbackslash`` must be used. 

::

  %hello.tex - First LaTeX document
  \documentclass{article}
  \begin{document}
  Hello,       World!
  This will not start a new line. 

  But, this will start a new paragraph. 
  Again no new line. \% what follows isn't a comment. 
  \end{document}
  This is text that is ignored. 

Basic Structure
---------------

``\documentclass``
~~~~~~~~~~~~~~~~~~
As already stated, the ``documentclass`` command tells LaTeX, the type of the document that you intend to create. Each class has a few differences in how the content of the document is typeset. 

Some of the available LaTeX classes are, article, proc, report, book, slides, letter. 

The ``documentclass`` command also accepts a few optional parameters. For example::
  \documentclass[12pt,a4paper,oneside,draft]{report}

``12pt`` specifies the size of the main font in the document. The relative sizes of the various fonts is maintained, when the font size is changed. If no size is specified, ``10pt`` is assumed by default. 

``a4paper`` specifies the size of the paper to be used for the document. 

``oneside`` specifies that the document will be printed only on one side of the paper. The ``article`` and ``report`` classes are ``oneside`` by default and the ``book`` class is ``twoside``.

``draft`` marks the hyphenation and justification problems in the document with a small square in the right hand margin of the document, so that they can be easily spotted. 

Note: Everything written in between the ``\documentclass`` command and the ``\begin{document}`` command is called the Preamble. 


Top Matter
~~~~~~~~~~

The information about the document such as it's title, the date, the author(s) information etc, is collectively known as the topmatter. The term topmatter is frequently used in LaTeX documentation. 

Let us add top matter to our document, now. 
::

  \title{LaTeX - A How-to}
  \author{The FOSSEE Team}
  \date

The  commands ``\title`` and  ``\author`` are self explanatory. 
The ``\date`` command automatically puts in today's date into the document. Now let us compile and look at the result. 

To put a specific date, you can specify it as below

:: 

  \date{June 1, 2010}

These details do not appear in the document until we use the ``\maketitle`` command with the document environment to instruct LaTeX to place the top matter information into the document. 

Sectioning Commands
~~~~~~~~~~~~~~~~~~~

Documents are often divided into parts, chapters, sections and subsections. LaTeX provides an intuitive mechanism to use them in your documents. 

+-------------------+-------+------------------------+
| command           | level | comments               |
+-------------------+-------+------------------------+
| ``part``          |    -1 | not in letters         |
+-------------------+-------+------------------------+
| ``chapter``       |     0 | only books and reports |
+-------------------+-------+------------------------+
| ``section``       |     1 | not in letters         |
+-------------------+-------+------------------------+
| ``subsection``    |     2 | not in letters         |
+-------------------+-------+------------------------+
| ``subsubsection`` |     3 | not in letters         |
+-------------------+-------+------------------------+
| ``paragraph``     |     4 | not in letters         |
+-------------------+-------+------------------------+
| ``subparagraph``  |     5 | not in letters         |
+-------------------+-------+------------------------+

LaTeX has seven levels of sectioning commands, as shown above. 

Text of a block or a section of the document need not be enclosed within ``\begin`` and ``\end`` commands. LaTeX starts a new block each time it finds a sectioning command. 
::

  \section[Short Title]{This is a very long title and the Short Title will appear in the Table of Contents.}

The short title appears in the table of contents, if at all one is generated. 

Section Numbering
+++++++++++++++++

As you may have observed, numbering is done automatically in LaTeX. Parts are numbered using roman numerals; Chapters and sections are numbered using decimal numbers. When a table of contents is inserted into the document, all the numbered headings automatically appear in it.

A sectioning command appended with an asterisk gives an unnumbered heading that is not included in the table of contents.
::

  \section*{Introduction}

By default, levels up to 2, are numbered, i.e, parts, chapters, sections and subsections. This can be changed by setting the ``secnumdepth`` counter using the ``\setcounter`` command. The following command removes numbering of the subsections. Only parts, chapters and sections will be numbered. 
::

  \setcounter{secnumdepth}{1}


Appendices
~~~~~~~~~~

LaTeX allows for separate numbering for appendices. ``\appendix`` command indicates that the sections following it, are to be included in the appendix. 
::

  \appendix
  \chapter{First Appendix}

Abstract
~~~~~~~~
LaTeX provides an ``abstract`` environment, to place an abstract in a document. The abstract appears in the document after the topmatter but before the main body of the document. 
::

  \begin{abstract}
    The abstract abstract.
  \end{abstract}

By default LaTeX uses the word "Abstract" as a title for the abstract. This can be changed using the ``\renewcommand``. 
::

  \renewcommand{\abstractname}{Summary}



Table of Contents
~~~~~~~~~~~~~~~~~

Parts, chapters or sections that have been auto numbered by LaTeX automatically appear in the Table of Contents (ToC). ``\tableofcontents`` command places the ToC at the location, where the command has been issued. 

The counter ``tocdepth`` specifies the depth up to which headings appear in the ToC. It can be set using the ``\setcounter`` command as shown below. 
::

  \setcounter{tocdepth}{3}

Unnumbered sections can be placed in the table of contents using the ``\addcontentsline`` command as shown below.
::

  \section*{Preface}
  \addcontentsline{toc}{section}{Preface}

Note: To get the correct entries in your table of contents, you will need to run one extra compilation, each time. This is because, the entries of the table of contents are collected during each compilation of the document and utilized during the next compilation. 

Typesetting Text
----------------

Text formatting
~~~~~~~~~~~~~~~

Font Styles and Size
++++++++++++++++++++

LaTeX has three font families:

 1. roman ``\textrm{your text here}``
 2. serif ``\textsf{your text here}``
 3. monospace ``\texttt{your text here}``

For emphasizing text, *italics* are generally used. The ``\emph`` command is used to emphasize text. 
``\textbf`` gives  **bold face** text. Underlines can be made using the ``\uline`` command and ``\sout`` strikes out text. For small caps, ``\textsc`` command is to be used. 

LaTeX provides a series of commands to change the size of text. The table below shows the commands and the size of text, they produce. 

+-------------------+----------------+-------------+-------------+
| size              | 10pt (default) | 11pt option | 12pt option |
+===================+================+=============+=============+
| ``\tiny``         | 5pt            | 6pt         | 6pt         |
+-------------------+----------------+-------------+-------------+
| ``\scriptsize``   | 7pt            | 8pt         | 8pt         |
+-------------------+----------------+-------------+-------------+
| ``\footnotesize`` | 8pt            | 9pt         | 10pt        |
+-------------------+----------------+-------------+-------------+
| ``\small``        | 9pt            | 10pt        | 11pt        |
+-------------------+----------------+-------------+-------------+
| ``\normalsize``   | 10pt           | 11pt        | 12pt        |
+-------------------+----------------+-------------+-------------+
| ``\large``        | 12pt           | 12pt        | 14pt        |
+-------------------+----------------+-------------+-------------+
| ``\Large``        | 14pt           | 14pt        | 17pt        |
+-------------------+----------------+-------------+-------------+
| ``\LARGE``        | 17pt           | 17pt        | 20pt        |
+-------------------+----------------+-------------+-------------+
| ``\huge``         | 20pt           | 20pt        | 25pt        |
+-------------------+----------------+-------------+-------------+
| ``\Huge``         | 25pt           | 25pt        | 25pt        |
+-------------------+----------------+-------------+-------------+


Superscript and Subscript
+++++++++++++++++++++++++

For superscripting text in the text mode, LaTeX provides the ``\textsuperscript`` command. 
::

  This is how you super\textsuperscript{script} text. 

LaTeX does not provide any command for subscripting text in the text mode. The math mode needs to be used to obtain subscripts. 

::

  This is sub_{script}

Quotation Marks
+++++++++++++++

When typing in LaTeX, the double quotation mark ``"`` character shouldn't be used. The grave accent ````` character produces the left quote and the apostrophe ``'`` character produces the right quote. To obtain double quotes they are, each, used twice. 
::

  `` Here is an example of putting `text' in quotes ''

Dashes and Hyphens
++++++++++++++++++

LaTeX has four dashes of different lengths. Three of them can be produces with different number of consecutive dashes. The short dashes are used for hyphens, slightly longer ones for number ranges and the longest ones for comments. The fourth one is a mathematical symbol, the minus sign. 
::

  The names of these dashes are: `-' hyphen, `--' en-dash, `---' em-dash and `$-$' minus sign.

The names for these dashes are: ‘‐’ hyphen, ‘–’ en-dash, ‘—’ em-dash and ‘−’ minus sign.

Lists - Itemize, Enumerate, and Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
LaTeX has three different environments for producing lists. Itemize, Enumerate and Description allow you to produce lists of various types in LaTeX. 

Itemize is used to produce unnumbered lists. The bullets of the list can be easily changed to use any character. Enumerate environment allows you to produce auto-numbered lists. The description environment, allows you to produce a list of definitions. These environments can be nested within each other, easily. 

::

  \begin{itemize}
    \item Now we move onto some elementary \emph{Text Typesetting}.
    \item How do we get \emph{emphasized or italic text}?
    \item \emph{Did you wonder what happens when we try \emph{emphasizing text} within \emph{emphasized text}}?
    \item ``Beautiful is better than ugly.''
  \end{itemize}
  
  \begin{description}
    \item[Description] This list is a description list. 
    \item[Enumerate] Numbered lists are often useful.
      \begin{enumerate}
      \item First
      \item Second
      \item Third
      \item \ldots
      \end{enumerate}
    \item[Itemize] The list above this description list is an itemize list.
  \end{description}
  
Special Paragraphs
~~~~~~~~~~~~~~~~~~

Footnotes
+++++++++

With the command::

  \footnote{footnote text}

a footnote is printed at the foot of the current page. Footnotes should always be put after the word or sentence they refer to. Footnotes referring to a sentence or part of it should therefore be put after the comma or period.

Quotes
++++++

LaTeX provides a ``quote`` environment that can be used for quoting, highlighting important material, etc. 
::

  The Zen of Python
  \begin{quote}
    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
  \end{quote}

LaTeX provides two other similar environments, the quotation and the verse environments. 

Verbatim
++++++++
The verbatim environment allows us to insert pre-formatted text in a LaTeX document. It is useful for inserting code samples within the document. The verbatim text needs to be enclosed between ``\begin{verbatim}`` and ``\end{verbatim}``. 
::

  \begin{verbatim}
  from numpy import *
  a = linspace(0, 5, 50, endpoint = False)
  \end{verbatim}

  from numpy import *
  a = linspace(0, 5, 50, endpoint = False)

To insert verbatim text in-line, the ``\verb`` command can be used. 
::
  
 The verb command allows placing \verb|verbatim text| in-line. 

The | is just an example of a delimiter character. You can use any character except letters, * or space.

Including Code
++++++++++++++

The ``listings`` package can be used to embed source code into your LaTeX document. We shall briefly explore inserting python code into our document. 

Obviously, you first need to tell LaTeX that you want it to use the ``listings`` package, using the ``\usepackage`` command. 
::

  \usepackage{listings}

Then, we tell LaTeX that we are going to embed Python code into this document. A simple code highlighting for Python code can be achieved using this. 
::

  \lstset{language=Python,
          showstringspaces=false,
         }

You might want to customize the code highlighting further using other variables like ``basicstyle``, ``commentstyle``, ``stringstyle``, ``keywordstyle`` etc. For detailed information on all this, you should look at the ``listings`` package documentation. 

You include a block of code into your document by enclosing it within the ``lstlisting`` environment. 
::

  \begin{lstlisting}
  string="Hello, World! "
  for i in range(10):
      print string*i
  \end{lstlisting} 

You can also include source code files directly into your latex document, using the ``lstinputlisting`` command. 
::

  \lstinputlisting[lastline=20]{lstexample.py}

This command includes the first 20 lines of the file ``lstexample.py`` into out LaTeX document. 

Tables, Figures, Floats, & Referencing
--------------------------------------

Tables
~~~~~~

The ``tabular`` environment allows typesetting tables in LaTeX. Like any other environment it starts with ``\begin`` command and ends with ``\end``. 

It takes an optional argument, ``pos`` that specifies the vertical position of the table relative to the baseline of the surroundging text. It takes values of ``t`` for top, ``b`` for bottom, or ``c`` for center. 

The ``col fmt`` argument specifies the formatting of the columns of the table. Following are the possible arguments to the tabular environment. 

+---------------+------------------------------------+
| ``l``         | left justified column content      |
+---------------+------------------------------------+
| ``r``         | right justified column content     |
+---------------+------------------------------------+
| ``c``         | centered column content            |
+---------------+------------------------------------+
| ``*{n}{col}`` | produces ``n`` columns with the    |
|               | ``col`` type of formatting         |
|               | ``*{3}{c}`` is the same as {c c c} |
+---------------+------------------------------------+
| ``|``         | produces a vertical line.          |
+---------------+------------------------------------+

Each row in a table is separated by ``\\`` command and each column entry of a row is separated by ``&``. 

The ``\hline`` command allows you to draw horizontal lines between two rows of the table. But it does not allow you do draw partial lines. ``\cline{a-b}`` draws a horizontal line from column ``a`` to column ``b``.
::

  \begin{tabular}{|c|c|}
    \hline
    \verb+l+ & left justified column content\\ 
    \hline
    \verb+r+ & right justified column content\\ 
    \hline
    \verb+c+ & centered column content\\ 
    \hline
    \verb+*{n}{col}+ & produces \verb+n+ columns with the\\
                   & \verb+col+ type of formatting\\
    \cline{2-2}
                   &\verb+*{3}{c}+ is the same as \verb+{c c c}+ \\
    \hline
    \verb+|+ & produces a vertical line\\ 
    \hline
  \end{tabular}


Figures
~~~~~~~

To include images in LaTeX, we require to use an additional package known as ``graphicx``.  To load a package, we use the ``\usepackage`` directive in the preamble of the document.
::

  \usepackage{graphicx}

When compiling with ``pdflatex`` command,  **jpg**, **png**, **gif** and **pdf** images can be inserted. 

::

  \includegraphics[optional arguments]{imagename}

A few ``optional arguments``:

  ``width=x``, ``height=x``
    If only the height or width is specified, the image is scaled, maintaining the aspect ratio.

  ``keepaspectratio``
    This parameter can either be set to true or false. When set to true, the image is scaled according to both width and height, without changing the aspect ratio, so that it does not exceed both the width and the height dimensions. 

  ``scale=x``
    Scale the image by a factor of ``x``. For example, ``scale=2``, will double the image size. 

  ``angle=x``
    This option can be used to rotate the image by ``x`` degrees, counter-clockwise. 

::

  \includegraphics[scale=0.8, angle=30]{lion_orig.png}


Floats
~~~~~~

Tables and Figures need to be treated in a special manner, since they cannot be split over pages, and they are referred to as floats in LaTeX. 

When there is not enough space on a page, to fit in a table or figure, it is floated over to the next page filling up the current page with text. LaTeX has float environments called ``table`` and ``figure`` for tables and figures, respectively.

Anything enclosed within the table or figure environments will be treated as floats.
::

  \begin{figure}[pos] or 
  \begin{table}[pos]

The ``pos`` parameter specifies the placement of the float. The possible values it can take are as follows. 

+-----------+-------------------------------------------------------------------+
| Specifier | Permission                                                        |
+===========+===================================================================+
|   h       |  at approximately the same place where it occurs in the source    |
+-----------+-------------------------------------------------------------------+
|   t       |  at the top of the page.                                          |
+-----------+-------------------------------------------------------------------+
|   b       |  at the bottom of the page.                                       |
+-----------+-------------------------------------------------------------------+
|   p       |  on a special page for floats only.                               |
+-----------+-------------------------------------------------------------------+
|   !       |  Override LaTeX's internal parameters for good positions          |
+-----------+-------------------------------------------------------------------+
|   H       |  nearly equivalent to h!                                          |
+-----------+-------------------------------------------------------------------+

Examples::

  \begin{figure}[h]
  \centering
  \includegraphics[scale=0.8, angle=30]{lion_orig.png}
  \end{figure}


Captions
++++++++

The ``\caption{text}`` command allows you to add captions to floats. Similar to section numbering, LaTeX automatically numbers floats too. The caption appears below or on top of the image (or table), depending on whether you place it after or before the ``importgraphics`` (or ``tabular``) command. 

::

  \begin{figure}[h]
  \centering
  \includegraphics[scale=0.8]{lion_orig.png}
  \caption{CTAN lion drawing by Duane Bibby; thanks to www.ctan.org}
  \end{figure}

The caption command also, like the section command, has the short caption optional parameter. The short caption will appear in the list of tables or figures. 

List of Figures, Tables
+++++++++++++++++++++++

LaTeX can automatically generate a List of Tables or Figures, with the table or figure numbers, the captions and page numbers on which they appear. They can be added to the document using the ``\listoftables`` or ``\listoffigures`` commands. 

Note: Just like table of contents, these lists also require an extra compilation. 

Cross References
~~~~~~~~~~~~~~~~

LaTeX has a very efficient mechanism of inserting cross-references in documents. 

The command ``\label{name}`` is used to label figures, tables or blocks of text, like chapters, sections etc. ``\ref{name}`` refers to the object marked by the ``name`` by it's numbering (figure, table, section etc.) ``\pageref{name}`` gives the page number of the object which has been labeled with ``name``. 

Note: Cross referencing also requires an extra compilation, like table of contents. 

Typesetting Math
----------------

In general, it is advised to use the AMS-LaTeX bundle to typeset mathematics in LaTeX. AMS-LaTeX is a collection of packages and classes for mathematical typesetting. 

We load ``amsmath`` by issuing the ``\usepackage{amsmath}`` in the preamble. Through out this section, it is assumed that the ``amsmath`` package has been loaded. 


Styles or Modes
~~~~~~~~~~~~~~~

LaTeX has two styles of inserting mathematical equations. They can either be inserted in-line within a paragraph (*text style*), or the paragraph can be broken to typeset them separately (*display style*). 

Inline formulas are typeset by placing them in two ``$`` symbols or in between ``\(`` and ``\)``. 

Displayed equations or equations that are set apart from the paragraph text are typeset by using ``\[`` and ``\]`` or ``\begin{equation*}`` and ``\end{equation*}`` for unnumbered equations or ``\begin{equation}`` and ``\end{equation}`` for numbered equations. 

LaTeX provides several environments for handling equation groups and multi-line equations. ``multiline``, ``gather`` and ``align`` are a few. We shall look at ``align`` environment here. You could try out the others, in the lab. 

``align`` numbers each of the lines in the environment, and ``align*`` as expected, does not number any of them.  The ``&`` is used to align the equations vertically and the ``\\`` command is used to break the lines. Line numbering can be skipped for a particular line in the ``align`` environment by placing a ``\nonumber`` before the line break.

::

  \begin{align}
  a^2 + b^2 &= c^2 \\
  a + b &> c \nonumber\\
  b + c &> a \nonumber\\
  c + a &> b \\
  \end{align}

Basic Elements
~~~~~~~~~~~~~~

Greek Letters can are entered as ``\alpha, \beta, \gamma, \delta, ...`` for lowercase letters and ``\Alpha, \Beta, \Gamma, ...`` for uppercase ones. 

Exponents and subscripts can be typeset using the carat ``^`` and the underscore ``_`` respectively. Most of the math mode commands act only on the next character. If you want a command to affect several characters, they need to be enclosed in curly braces. 

The ``\sqrt`` command is used to typeset the square root symbol. LaTeX of the root sign is determined automatically. The nth root is generated with ``\sqrt[n]``. 

To explicitly show a multiplication a dot may be shown. ``\cdot`` could be used, which typesets the dot to the center. ``\cdots`` is three centered dots while ``\ldots`` sets the dots on the baseline. Besides that ``\vdots`` for vertical and ``\ddots`` can be used for diagonal dots.

A fraction can be typeset with the command ``\frac{..}{..}``

The integral operator is generated with ``\int``, the sum operator with ``\sum``, and the product operator with ``\prod``. The upper and lower limits are specified with ``^`` and ``_`` like subscripts and superscripts.

LaTeX provides all kinds of braces as delimiters. The round and square brackets can be produces using the keys on the keyboard and appending a backslash. Other delimiters can be produced using special commands of LaTeX. Placing ``\left`` in front of an opening delimiter and ``\right`` in front of a closing delimiter, instructs LaTeX to automatically take care of the sizes of the delimiters. 

Arrays and Matrices
~~~~~~~~~~~~~~~~~~~

To typeset arrays, use the ``array`` environment. It works similar to the ``tabular`` environment. The ``\\`` command is used to break the lines. 
::

  \begin{equation*}
  \mathbf{X} = \left(
   \begin{array}{ccc}
   a_1 & a_2 & \ldots \\
   b_1 & b_2 & \ldots \\
   \vdots & \vdots & \ddots
   \end{array} \right)
  \end{equation*}

The ``array`` environment can also be used to typeset piecewise functions by using a “.” as an invisible ``\right`` delimiter
::

  \begin{equation*}
  f(x) = \left\{
   \begin{array}{rl}
     0 & \text{if } x \le 0\\
     1 & \text{if } x > 0
   \end{array} \right.
   \end{equation*}

Six different types of matrix environments are available in the ``amsmath`` package for typesetting matrices.  They essentially have different delimiters: ``matrix`` (none), ``pmatrix`` (, ``bmatrix`` [, ``Bmatrix`` {, ``vmatrix`` | and ``Vmatrix`` ‖. In these matrix environments, the number of columns need not be specified, unlike the ``array`` environment.
::

  \begin{equation*}
    \begin{matrix}
    1 & 2 \\
    3 & 4
    \end{matrix} \qquad
 
    \begin{bmatrix}
    1 & 2 & 3 \\
    4 & 5 & 6 \\
    7 & 8 & 9
    \end{bmatrix}
  \end{equation*}

Spacing
~~~~~~~
+---------+----------------+---------+
| Abbrev. | Spelled out    | Example |
+---------+----------------+---------+
|         | no space       |         |
+---------+----------------+---------+
| \,      | \thinspace     |         |
+---------+----------------+---------+
| \:      | \medspace      |         |
+---------+----------------+---------+
| \;      | \thickspace    |         |
+---------+----------------+---------+
|         | \quad          |         |
+---------+----------------+---------+
|         | \qquad         |         |
+---------+----------------+---------+
| \!      | \negthinspace  |         |
+---------+----------------+---------+
|         | \negmedspace   |         |
+---------+----------------+---------+
|         | \negthickspace |         |
+---------+----------------+---------+



Referencing
~~~~~~~~~~~
Equations can also be cross referenced using the ``\label`` and ``\eqref`` commands. 


Bibliography
------------

Bibliography or references can be added to LaTeX documents in two ways - using the ``thebibliography`` environment, or using BibTeX. Let's first look at using the ``\thebibliography`` environment and then move on to BibTeX.

``thebibliography`` environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Writing bibliographies in LaTeX using the ``thebibliography`` environment is pretty easy. You simply have to list down all the bibliography items within the bibliography environment. 

Each entry of the bibliography begins with the command ``\bibitem[label]{name}``. The name is used to cite the bibliography item within the document using  ``\cite{name}``. The label option replaces the numbers from the auto enumeration with the labels given. 
::

  He used this lion in the illustrations for D Knuth's original TeXbook\cite{DKnuth}, for L Lamport's LaTeX book\cite{LLamport}

  \begin{thebibliography}{99}
    \bibitem{DKnuth} Donald E. Knuth (1984). \emph{The TeXbook} (Computers and Typesetting, Volume A). Reading, Massachusetts: Addison-Wesley. ISBN 0-201-13448-9.
  
    \bibitem{LLamport} Lamport, Leslie (1994). \emph{LaTeX: A document preparation system: User's guide and reference}.
     illustrations by Duane Bibby (2nd ed.). Reading, Mass: Addison-Wesley Professional. 
  \end{thebibliography}

The ``99`` in the example above indicates the maximum width of the label that the references may get. We here assume that the number of Bibliography items will be less than 100. If your document has less than 10 references, you may want to replace ``99`` with ``9``. 

BibTeX
~~~~~~

The previous section explained the process of listing references at the end of a document and embedding cross references. In this section let us explore the BibTeX environment for keeping track of references.

Using BibTeX is a very convenient method to use, when writing multiple documents in a single area or field. BibTeX allows you to create a database of all your references and use them as and when required. 

The BibTeX database is stored in a ``.bib`` file. The structure of the file is quite simple and an example is shown below. 
::

  @book{Lamport94,
  author    = "Leslie Lamport",
  title     = "A Document Preparation System: User's Guide and Reference",
  publisher = "Addison-Wesley Professional",
  year      = "1994",
  edition    = "second",
  note      = "illustrations by Duane Bibby"
  }

Each bibliography entry starts with a declaration of the type of the reference being mentioned. The reference is in the above example is of the book type. BibTeX has a wide range of reference types, for example, ``article, book, conference, manual, proceedings, unpublished``.

The type of reference is followed by a left curly brace, and immediately followed by the citation key. The citation key, ``Lamport94`` in the example above is used to cite this reference using the command ``\cite{Lamport94}``. 

This is followed by the relevant fields and their values, listed one by one. Each entry must be followed by a comma to delimit one field from the other. 

To get your LaTeX document to use the bibliography database, you just add the following lines to your LaTeX document. 
::

  \bibliographystyle{plain}
  \bibliography{LaTeX}

Bibliography styles are files that tell BibTeX how to format the information stored in the ``.bib`` database file. The style file for this example is ``plain.bst``. Note that you do not need to add the ``.bst`` extension to the filename.  If you wish to achieve a particular style of listing the bibliography items and citing them, you should use an appropriate style file. 

The ``bibliography`` command specifies the file that should be used as the database for references. The file used in this example is ``LaTeX.bib``

Compiling
+++++++++

Adding BibTeX based references, slightly complicates the process of compiling the document to obtain the desired output. The exact workings of LaTeX and BibTeX will not be explained here. The procedure for obtaining the output (without any explanations) is as follows:

1. Compile the ``.tex`` file using ``pdflatex`` - ``$pdflatex LaTeX(.tex)``
2. Compile the ``.bib`` file using ``bibtex`` -  ``$bibtex LaTeX(.bib)``
3. Compile the ``.tex`` file again. 
4. Compile the ``.tex`` file for one last time!

Beamer
~~~~~~

LaTeX has quite a few options to produce presentation slides. We shall look at the ``beamer`` class, which is well developed and easy to use. We shall only briefly look at some of the features of beamer. For the best documentation, look at the beamer user guide.

To write a ``beamer`` presentation, it is recommended that you use one of the templates that beamer provides. We shall use the ``speaker_introduction`` template to get started with beamer. 

As you can see, the document begins with the ``documentclass`` being set to beamer. 

The ``\setbeamertemplate`` command sets the template for various parameters. The ``background canvas``, ``headline`` and ``footline`` are being set using the command.

``\usetheme`` command sets the theme to be used in the presentation. 

Notice that each slide is enclosed within ``\begin{frame}`` and ``\end{frame}`` commands. The ``\begin{frame}`` command can be passed the Title and Subtitle of the slide as parameters. 

To achieve more with beamer, it is highly recommended that you look at the ``beameruserguide``.


Recommended Reading
-------------------

1. *LaTeX Wikibook*

2. *The Not So Short Introduction to LaTeX2e* by Tobias Oetikar et al.. 


