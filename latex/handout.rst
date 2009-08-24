LaTeX
=====

Introduction
------------
LaTeX is a typesetting program that is excellent for producting scientific and mathematical documents of high typographical quality. It is also suitable for producing all sorts of other documents, from simple letters to complete books. LaTeX uses TeX as its formatting engine.


TeX & LaTeX
~~~~~~~~~~~

TeX
+++

TeX is a typesetting system designed and mostly written by Donald Knuth. It was designed with two goals in mind-
  
1. To allow anybody to produce high-quality books using a reasonable amount of effort. 
2. To provide a system that would give the exact same results on all computers, now and in the future

It’s also a Turing-complete programming language, in the sense that it supports the if-else construct, it can calculate (the calculations are performed while compiling the document), etc., but you would find it very hard to make anything else but typesetting with it. The fine control TeX offers makes it very powerful, but also difficult and time-consuming to use.

TeX is renowned for being extremely stable, for running on many different kinds of computers, and for being virtually bug free. 

The version number of TeX is converging to π and is now at 3.1415926.

The characters T, E, X in the name come from capital Greek letters tau, epsilon, and chi, as the name of TeX derives from the Greek: τέχνη (skill, art, technique); for this reason, TeX's creator Donald Knuth promotes a /tɛx/ pronunciation

LaTeX
+++++
LaTeX is a macro package based on TeX created by Leslie Lamport. It was intended to provide a high-level language that provides access to TeX. It essentially comprises a collection of TeX macros and a program to process LaTeX documents. For the end-users, it is much simpler to use than TeX. It has become the dominant method for using TeX (relatively few people write in TeX anymore).

LaTeX is pronounced either as "Lah-tech" or "Lay-tech"

WYSIWG vs. WYSIWM
~~~~~~~~~~~~~~~~~
The Advantages-

  * It is free (both as in free-beer and free-speech)
  * It is platform independent. 
  * It is very stable. 
  * LaTeX is ASCII and any text editor of your choice can be used to view and edit the source.
  * The typesetting is better, especially the maths.
  * It encourages Authors to write well-structured texts, since specifying structure is an integral part of how LaTeX works.
  * LaTeX is extensible. If you want a new feature, you can look around for a free add-on or write one yourself. 

and some Disadvantages - 

  * Font selection is difficult 
  * LaTeX's not good at flowing text around pictures.
  * LaTeX encourages (almost insists on) structured writing and the separation of style from content. This is not the way that many people (especially non-programmers) are used to working.
  * Without a WYSIWYG front end, it's not always easy to find out how to do things.

LaTeX Source
~~~~~~~~~~~~

::

  %hello.tex - First LaTeX document
  \documentclass{article}

  \begin{document}
    Hello, World!
  \end{document}


Spaces
++++++

LaTeX ignores whitespaces. Multiple white spaces are treated as one space. An empty line between two lines of text is considered as a change of paragraphs. 

Special Characters
++++++++++++++++++

The characters ``~ # $ % ^ & _ { } \`` have special meanings associated with them.

These characters can be used in your document by adding a prefix backslash. ``\~ \# \% \$ \^ \& \_ \{ \} \textbackslash``

Comments
++++++++

% character is used to insert comments into a LaTeX document. All the text from the % character to the end of that line is ignored by LaTeX.


LaTeX Commands
++++++++++++++

* LaTeX commands are case sensitive. 
* They start with a backslash ``\``
* They come in two formats

  - a backslash followed by a name consisting of letters only. These command names are terminated by any non-letter. 
  - a backslash followed by exactly one non-character. 

* Some commands need to be given a parameter, which is enclosed in curly braces ``{ }``
* Some command support optional parameters, which are added after the name in square brackets ``[ ]``

LaTeX Environments
++++++++++++++++++

Environments are similar in their role, to commands, except that they effect a larger part of the document.

* They begin with a ``\begin`` and end with a ``\end``
* Nested environments are generally supported

Anything in LaTeX can be expressed in terms of Commands and Environments.

Hello, World!
~~~~~~~~~~~~~

::

  %hello.tex - First LaTeX document
  \documentclass{article}

  \begin{document}
    Hello, World!
  \end{document}

Now, look at what each line does. 


``%hello.tex - First LaTeX document``

  This line is a comment. Comments in LaTeX begin with a %

``\documentclass{article}``

  This line is a command and sets the documentclass to be used for this document to ``article``. If you want to change the appearance of the document, you simply have to change the documentclass. 


``\begin{document}``

  This line is the beginning of a LaTeX environment called ``document``. It informs LaTeX that the content of the document is beginning. Anything between the ``\documentclass`` line and this line is called the *preamble*

``Hello, World!``

  This is the text that is displayed in the document. 

``\end{document}``

  The ``document`` environment ends here. It tells LaTeX that the document is complete and anything written after this line will be ignored by LaTeX.

Compiling & Output
~~~~~~~~~~~~~~~~~~
``latex`` command can be used to get ``dvi`` output. But, we shall be using ``pdflatex`` all through this document and producing ``pdf`` output.

::

  $pdflatex hello.tex

  Output written on hello.pdf (1 page, 5733 bytes).
  Transcript written on hello.log.

.. .. image:: sample/hello.jpg



Document Structure
------------------

This section gives a basic idea about the general sturcture of a LaTeX document. LaTeX is different from other typesetting software in that, it requires the user to specify the logical and semantic structure of the text. Therefore, it helps (almost forces) the author to organize his text better and hence improving the structure and clarity of the document. 

``\documentclass``
~~~~~~~~~~~~~~~~~~

The type of the document to be created is specified using the ``\documentclass`` command. 
::

  \documentclass[options]{class}

Here, ``class`` defines the type of document that is to be created. The LaTeX distribution provides a variety of document class, that can be used for a variety of purposes. The ``options`` parameter customizes various properties of the document. The options have to be separated by commas. 

For example ``\documentclass[11pt, twoside, a4paper]{article}`` produces a document of the article class with the base font size as eleven points, and to produce a layout suitable for double sided printing on A4 paper. 

Some of the document classes that are available in LaTeX are ``article, report, book, slides, letter``


The document environment
~~~~~~~~~~~~~~~~~~~~~~~~
The text of the document is enclosed in between the commands ``\begin{document}`` and ``\end{document}`` which identify the beginning and the end of the document respectively. 

The reason for marking off the beginning of your text is that LaTeX allows you to insert extra setup specifications before it. The reason for marking off the end of your text is to provide a place for LaTeX to be programmed to do extra stuff automatically at the end of the document, like making an index.

A useful side-effect of marking the end of the document text is that you can store comments or temporary text underneath the \end{document} in the knowledge that LaTeX will never try to typeset them

Preamble
~~~~~~~~
Everything written in between the ``\documentclass`` command and the ``\begin{document}`` command is called the Preamble. It normally contains commands that effect the whole document. 

Packages
~~~~~~~~

While writing your document, you will probably find that there are some areas where basic LaTeX cannot solve your problem. If you want to include graphics, coloured text or source code from a file into your document, you need to enhance the capabilities of LaTeX. Such enhancements are called packages. Packages are activated with the  
::

  \usepackage[options]{package}

command, where package is the name of the package and options is a list of keywords that trigger special features in the package. Some packages come with the LaTeX2e distribution and others are provided separately. You can even write your own packages, if and when required. 

Top Matter
~~~~~~~~~~

At the beginning of most documents there will be information about the document itself, such as the title and date, and also information about the authors, such as name, address, email etc. All of this type of information within Latex is collectively referred to as top matter. Although never explicitly specified (there is no \topmatter command) you are likely to encounter the term within Latex documentation.

An example::

  \documentclass[11pt,a4paper,oneside]{report}
  \title{LaTeX - A Howto}
  \author{The FOSSEE Team}
  \date{August 2009}
  \maketitle

The ``\title``, ``\author`` and ``\date`` commands are self-explanaotry. You put the title, author name, and date in curly braces after the relevant command. If no date command is used, today's date is insert by default. 

Topmatter is always finished by the ``\maketitle`` command

Abstract
~~~~~~~~

As most research papers have an abstract, there are predefined commands for telling LaTeX which part of the content makes up the abstract. This should appear in its logical order, therefore, after the top matter, but before the main sections of the body. This command is available for the document class article and report, but not book. 
::

  \documentclass{article}
  \begin{abstract}
  Your abstract goes here...
  \end{abstract}
  \begin{document}
  ...
  \end{document}

By default, LaTeX will use the word “Abstract” as a title for your abstract, if you want to change it into anything else, e.g. “Executive Summary”, add the following line in the preamble::

    \renewcommand{\abstractname}{Executive Summary}

Sectioning Commands
~~~~~~~~~~~~~~~~~~~

The commands for inserting sections are fairly intuitive. Of course, certain commands are appropriate to different document classes. For example, a book has chapters but an article doesn’t.

Examples::
  
  \Chapter{LaTeX}

  \section{Introduction}

  \subsection{TeX & LaTeX}
  
  \subsubsection{TeX}

Notice that you do not need to specify section numbers. LaTeX will sort that out for you! Also, for sections, you do not need to markup which content belongs to a given block, using \begin and \end commands, for example. 

All the titles of the sections are added automatically to the table of contents (if you decide to insert one). But if you make manual styling changes to your heading, for example a very long title, or some special line-breaks or unusual font-play, this would appear in the Table of Contents as well, which you almost certainly don’t want. LaTeX allows you to give an optional extra version of the heading text which only gets used in the Table of Contents and any running heads, if they are in effect. This optional alternative heading goes in [square brackets] before the curly braces. 
::

  \section[Short Title]{This is a very long title and the Short Title will appear in the Table of Contents.}

Section Numbering
+++++++++++++++++

You don't need to explicitly do any section numbering as LaTeX does it automatically. Parts get roman numerals, Chapters and Sections get decimal numbering and Appendices are lettered. You can change the depth to which section numbering occurs, which is set to 2 by default. 

For example, if you want only the Parts, Chapters and Sections to be numbered and not the subsections, subsubsections etc., you can set the ``secnumdepth`` to 1 using the ``\setcounter`` command. 
::

  \setcounter{secnumdepth}{1}

To get an unnumbered section heading which does not go into the Table of Contents, follow the command name with an asterisk before the opening curly brace.
::

  \subsection*{Introduction}

All the divisional commands from ``\part*`` to ``\subparagraph*`` have this “starred” version which can be used on special occasions for an unnumbered heading when the setting of ``secnumdepth`` would normally mean it would be numbered.

Appendices
~~~~~~~~~~

The separate numbering of appendices is also supported by LaTeX. The \appendix macro can be used to indicate that following sections or chapters are to be numbered as appendices.
::

  \appendix
  \chapter{First Appendix}

  \appendix
  \section{First Appendix}

Table of Contents
~~~~~~~~~~~~~~~~~

All auto-numbered headings get entered in the Table of Contents (ToC) automatically. Just add the command ``\tableofcontents`` at the point where you want it placed. 

The counter ``tocdepth`` specifies what depth to take the ToC to. It can be set using the ``\setcounter`` command as shown below. 
::

  \setcounter{tocdepth}{3}

If you want the unnumbered section to be in the table of contents anyway, use the ``\addcontentsline`` command like this.
::

  \section*{Introduction}
  \addcontentsline{toc}{section}{Introduction}

Entries for the ToC are recorded each time you process your document, and re- produced the next time you process it, so you need to re-run LaTeX one extra time to ensure that all ToC pagenumber references are correctly calculated. We’ve already seen how to use the optional argument to the sectioning commands to add text to the ToC which is slightly different from the one printed in the body of the document. It is also possible to add extra lines to the ToC, to force extra or unnumbered section headings to be included.


Bibliography
~~~~~~~~~~~~
Any good research paper will have a whole list of references. LaTeX, therefore, has a sane way to manage your references. There are two ways to insert references into your LaTeX document:

1. You can embed them within the doucment itself. It's simpler, but it can be time consuming if you are writing several papers about similar subjects so that you often have to cite the same references
2. You can store them in an external BibTeX file and then link them to your current document. You can also use a BibTeX style to define how they should appear. This way you create a small databases of the references you might need, and use them as and when you need to cite them. 

We shall discuss this in more detail in the Bibliography section. 

Including files
~~~~~~~~~~~~~~~
When you are working on a large document, you might want to split the input files into multiple files. LaTeX has three methods for inserting one file into another when compiling. 

1. ``\input``

  It is equivalent to an automatic cut-paste just before compiling. To include ``file1.tex`` in our document, we just say
  ::
  
    \input{file1}


2. ``\include``

  It is similar to the ``\input`` command, except that it inserts a new page, each time it is executed. So, it is useful for inserting large blocks like new chapters. To inlcude chapter1.tex in our document, we say
  ::
    
    \include{chapter1}

3. ``\includeonly``

  This command is useful in restricting the ``\include`` commands that we wish to be executed. For example, if we have ``\include{chapter1}``, ``\include{chapter2}`` and ``\include{chapter3}`` in the document, but we wish to just verify the changes made to ``chapter1.tex`` and ignore the other chapters for a while, we could add the following command to the preamble.
  ::

    \includeonly{chapter1}

A note on filenames
+++++++++++++++++++

Never use filenames or directories that contain spaces. Make filenames as long or short as you would like, but strictly avoid spaces. Stick to upper or lower case letters (without accents), the digits, the hyphen and the full stop or period.

Typesetting Text
----------------

Line and Page Breaks
~~~~~~~~~~~~~~~~~~~~

Books are often typeset with each line having the same length. LaTeX inserts the necessary line breaks and spaces between words by optimizing the con- tents of a whole paragraph. If necessary, it also hyphenates words that would not fit comfortably on a line. How the paragraphs are typeset depends on the document class.

In special cases it might be necessary to order LaTeX to start a newline. 

``\\`` or ``\newline`` starts a newline without starting a new paragraph. 

``\\*`` additionally prohibits a page break after the line break. 

[Optional material::

  \linebreak[n], \nolinebreak[n], \pagebreak[n], \nopagebreak[n]

  \hyphenation

  \mbox

]

Symbols & More Special Characters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Quotation Marks
+++++++++++++++

You should not use the " for quotation marks as you would on a typewriter. In publishing there are special opening and closing quotation marks. In  A LaTeX, use two ` (grave accent) for opening quotation marks and two ' (vertical quote) for closing quotation marks. For single quotes you use just one of each.
::

  `` Here is an example of putting `text' in quotes ''

“ Here is an example of putting ‘text’ in quotes ”
Need to include an image as example. ?

Dashes and Hyphens
++++++++++++++++++

LaTeX has four kinds of dashes. Three of them can be accessed with different number of consecutive dashes. The fourth one is a mathematical symbol, the minus sign. 
::

  The names of these dashes are: `-' hyphen, `--' en-dash, `---' em-dash and `$-$' minus sign.

The names for these dashes are: ‘‐’ hyphen, ‘–’ en-dash, ‘—’ em-dash and ‘−’ minus sign.

Tilde(~)
++++++++

A character often seen in web addresses is the tilde. To generate this in LaTeX you can use ``\~`` but the result ˜ is not really what you want. Try ``$\sim$`` instead.
::

  http://www.rich.edu/\~{}bush\\
  http://www.clever.edu/$\sim$demo


http://www.rich.edu/˜bush

http://www.clever.edu/~demo

Ellipsis
++++++++

On a typewriter, a comma or a period takes the same amount of space as any other letter. In book printing, these characters occupy only a little space and are set very close to the preceding letter. Therefore, you cannot enter ‘ellipsis’ by just typing three dots, as the spacing would be wrong. Instead, there is a special command for these dots. It is called ``\ldots``

Emphasized Words
~~~~~~~~~~~~~~~~

If a text is typed using a typewriter, important words are emphasized by underlining them.
::

  \underline{text}

In printed books, however, words are emphasized by typesetting them in an *italic* font. LaTeX provides the command
::

 \emph{text}

to emphasize text. If you use emphasizing inside emphasized text, LaTeX uses normal font for emphasizing. 
::

  \emph{This is emphasized text, and \emph{this is emphasized text with normal font}, within emphasized text.}

*This is emphasized text, and* this is emphasized text with normal font, *within emphasized text.*


Cross References
~~~~~~~~~~~~~~~~

In books, reports and articles, there are often cross-references to figures, tables and special segments of text. LaTeX provides the following commands for cross referencing::

  \label{marker}, \ref{marker} and \pageref{marker} 

where ``marker`` is an identifier chosen by the user. LaTeX replaces ``\ref`` by the number of the section, subsection, figure, table, or theorem after which the corresponding ``\label`` command was issued. ``\pageref`` prints the page number of the page where the ``\label`` command occurred. 

As with the section titles, the numbers from the previous run are used. Therefore, to get the correct numbering, you will need to compile twice. 


Footnotes
~~~~~~~~~

With the command::

  \footnote{footnote text}

a footnote is printed at the foot of the current page. Footnotes should always be put after the word or sentence they refer to. Footnotes referring to a sentence or part of it should therefore be put after the comma or period.

[optional::

  \marginpar - Margin notes. 

]


Itemize, Enumerate, and Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

  \begin{enumerate}
    \item You can mix the list   environments to your taste:

    \begin{itemize}
      \item But it might start to look silly.
      \item[-] With a dash.
    \end{itemize}

  \item Therefore remember:

    \begin{description}
      \item[Stupid] things will not become smart 
       because they are in a list.
      \item[Smart] things, though, can be
       presented beautifully in a list
    \end{description}

  \end{enumerate}

1. You can mix the list environments to your taste:

   * But it might start to look silly

   - With a dash. 

2. Therefore remember:

  **Stupid** things will not become smart because they are in a list

  **Smart** things, though, can be presented beautifully in a list. 



Flushleft, Flushright, and Center
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The environments ``flushleft`` and ``flushright`` generate paragraphs that are either left- or right-aligned. The ``center`` environment generates centered text.


Quote, Quotation, and Verse
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``quote`` environment is useful for quotes, important phrases and examples.
::

  A typographical rule of thumb for the line length is:
  \begin{quote}
  On average, no line should
  be longer than 66 characters.
  \end{quote}
  This is why LaTeX pages have
  such large borders by default
  and also why multicolumn print
  is used in newspapers.

A typographical rule of thumb for the line length is:

  On average, no line should be longer than 66 characters.

This is why LaTeX pages have such large borders by default and also why multicolumn print is used in newspapers.
  

There are two similar environments: the quotation and the verse environments. The quotation environment is useful for longer quotes going over several paragraphs, because it indents the first line of each paragraph.

The verse environment is useful for poems where the line breaks are important. The lines are separated by issuing a \\\\ at the end of a line and an empty line after each verse.



Abstract
~~~~~~~~
In scientific publications it is customary to start with an abstract which gives the reader a quick overview of what to expect. LaTeX provides the abstract environment for this purpose. Normally abstract is used in documents typeset with the article document class. 
::

  \begin{abstract}
  The abstract abstract.
  \end{abstract}

Verbatim
~~~~~~~~
Text that is enclosed between ``\begin{verbatim}`` and ``\end{verbatim}`` will be directly printed, as if typed on a typewriter, with all line breaks and spaces, without any LaTeX command being executed.     
::

  \begin{verbatim}
  10 PRINT "HELLO WORLD ";
  20 GOTO 10
  \end{verbatim}


10 PRINT "HELLO WORLD ";

20 GOTO 10


Within a paragraph, similar behavior can be accessed with
::
  
  \verb+text+ 

The + is just an example of a delimiter character. You can use any character except letters, * or space.

The starred verstion of the verbatim environment emphasizes the spaces in the text. 
::

  \begin{verbatim*}
  10 PRINT "HELLO WORLD ";
  20 GOTO 10
  \end{verbatim*}

10␣PRINT␣"HELLO␣WORLD␣";

20␣GOTO␣10

Tables, Figures and Captions
----------------------------

The ``\tabular`` environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The tabular environment can be used to typeset beautiful tables with optional horizontal and vertical lines. LaTeX determines the width of the columns automatically.
::

  \begin{tabular}[pos]{table spec}

The table spec argument defines the format of the table. Use an ``l`` for a column of left-aligned text, ``r`` for right-aligned text, and ``c`` for centred text; ``p{width}`` for a column containing justified text with line breaks, and ``|`` for a vertical line.

If the text in a column is too wide for the page, LaTeX won’t automatically wrap it. Using ``p{width}`` you can define a special type of column which will wrap-around the text as in a normal paragraph.

The pos argument specifies the vertical position of the table relative to the baseline of the surrounding text. Use either of the letters ``t`` , ``b`` and ``c`` to specify table alignment at the top, bottom or center.

Within a tabular environment, ``&`` jumps to the next column, ``\\`` starts a new line and ``\hline`` inserts a horizontal line. You can add partial lines by using the ``\cline{i-j}``, where ``i`` and ``j`` are the column numbers the line should extend over.

::

  \begin{tabular}{|r|l|}
  \hline
  7C0 & hexadecimal \\
  3700 & octal \\ \cline{2-2}
  11111000000 & binary \\
  \hline \hline
  1984 & decimal \\
  \hline
  \end{tabular}

[include an image of a table, as example]

Importing Graphics
~~~~~~~~~~~~~~~~~~

Strictly speaking, LaTeX cannot manage pictures directly: in order to introduce graphics within documents, LaTeX just creates a box with the same size of the image you want to include and embeds the picture, without any other processing. This means you will have to take care that the images you want to include are in the right format to be included. This is not such a hard task because LaTeX supports the most common picture formats around.

We need to load the ``graphicx`` package in the preamble of the document to be able to include images. 
::

  \usepackage{graphicx}

When compiling with ``pdflatex`` command, (which we assume is being used all through this course) you can insert **jpg**, **png** and **pdf** files. 

::

  \includegraphics[optional arguments]{imagename}

A few ``optional arguments``:

  ``width=xx``
    specify the width of the imported image to ``xx``. 

  ``height=xx``
    specify the height of the imported image to ``xx``. 
    Specifying only the width or height of the image will scale the image whilst maintaining the aspect ratio. 

  ``keepaspectratio``
    This can be either set to true or false. When set to true, it will scale the image according to both width and height, without distorting the image so that it does not exceed both the width and the height dimensions. 

  ``scale=xx``
    Scale the image by a factor of ``xx``. For eg. ``scale=2``, will double the image size. 

  ``angle=xx``
    This option can be used to rotate the image by ``xx`` degrees, anti-clockwise. 


Floats
~~~~~~

Figures and Tables need special treatment, because they cannot be broken across pages. One method would be to start a new page every time a figure or a table is too large to fit on the present page. This approach would leave pages partially empty, which looks very bad.

The solution to this problem is to ‘float’ any figure or table that does not fit on the current page to a later page, while filling the current page with body text. LaTeX offers two environments for floating bodies; one for tables and one for figures. To take full advantage of these two environments it is important to understand approximately how LaTeX handles floats internally. 

Any material enclosed in a figure or table environment will be treated as floating matter. 
::

  \begin{figure}[placement specifier] or 
  \begin{table}[placement specifier]

Both float environments support an optional parameter called the placement specifier. This parameter is used to tell LaTeX about the locations to which the float is allowed to be moved. A placement specifier is constructed by building a string of float-placing permissions.

+-----------+-------------------------------------------------------------------+
| Specifier | Permission                                                        |
+-----------+-------------------------------------------------------------------+
|   h       |  Place the float here                                             |
|           |  (approximately at the same point it occurs in the source text)   |
+-----------+-------------------------------------------------------------------+
|   t       |  Position at the top of the page.                                 |
+-----------+-------------------------------------------------------------------+
|   b       |  Position at the bottom of the page.                              |
+-----------+-------------------------------------------------------------------+
|   p       |  Put on a special page for floats only.                           |
+-----------+-------------------------------------------------------------------+
|   !       |  Override internal parameters Latex uses for determining “good”   | 
|           |  float positions.                                                 |
+-----------+-------------------------------------------------------------------+
|   H       |  Places the float at precisely the location in the LaTeX code.    | 
|           |  Requires the float package. ``\usepackage{float}``.              |
|           |  This is somewhat equivalent to h!                                |
+-----------+-------------------------------------------------------------------+

Examples::

  \begin{table}[!hbp]
  \begin{tabular}{...}
  ... table data ...
  \end{tabular}
  \end{table}

  \begin{figure}[b]
    \includegraphics[scale=0.5]{image1.jpg}
  \end{figure}


Captions
~~~~~~~~

It is always good practice to add a caption to any figure or table. All you need to do is use the ``\caption{text}`` command within the float environment. LaTeX will automatically keep track of the numbering of figures, so you do not need to include this within the caption text.     

The location of the caption is traditionally underneath the float. However, it is up to you to therefore insert the caption command after the actual contents of the float (but still within the environment). If you place it before, then the caption will appear above the float.
::

  \begin{figure}[b]
    \caption{This is a caption at the top of the image}
    \includegraphics[scale=0.5]{image1.jpg}
  \end{figure}

  \begin{figure}[b]
    \includegraphics[scale=0.5]{image1.jpg}
    \caption{This is a caption at the bottom of the image}
  \end{figure}


List of Figures, Tables
~~~~~~~~~~~~~~~~~~~~~~~

Captions can be listed in a “List of Tables” or a “List of Figures” section by using the ``\listoftables`` or ``\listoffigures`` commands, respectively. The caption used for each table or figure will appear in these lists, along with the table or figure numbers, and page numbers that they appear on.

The ``\caption`` command also has an optional parameter, ``\caption[short]{long}`` which is used for the List of Tables or List of Figures. Typically the short description is for the caption listing, and the long description will be placed beside the figure or table. This is particularly useful if the caption is long, and only a “one-liner” is desired in the figure/table listing. 

Typesetting Math
----------------

If you wish to typset advanced mathematics, it is best to use the AMS-LaTeX bundle, which is a collection of packages and classes for mathematical typsetting. Note that LaTeX does, provide some basic features and environments for mathematical typsetting, but they are limited and in some cases even inconsistent. We shall stick to using the ``amsmath`` package from the AMS-LaTeX bundle, throughout this course. 

We load ``amsmath`` by issuing the ``\usepackage{amsmath}`` in the preamble. Through out this section, it is assumed that the ``amsmath`` package has been loaded. 

Math Mode
~~~~~~~~~

There are a few differences between the *math mode* and the *text mode*:

1. Most spaces and line breaks do not have any significance, as all spaces are either derived logically from the mathematical expressions, or have to be specified with special commands such as ``\,``, ``\quad`` or ``\qquad``

2. Empty lines are not allowed.  

3. Each letter is considered to be the name of a variable and will be typeset as such. If you want to typeset normal text within a formula, then you have to enter the text using the \text{...} command

Single Equations
~~~~~~~~~~~~~~~~

There are two ways to typeset mathematical equations in LaTeX - inline within a paragraph (*text style*), or the paragraph can be broken to typeset it separately (*display style*). 

A mathematical equation within a paragraph is entered between ``$`` and ``$``.

If you want the larger equations to be set apart from the paragraph, it is better to use the display style. To do this, you enclose the equations within ``\begin{equation}`` and ``\end{equation}``. You can then \label an equation number and refer to it somewhere else in the text by using the ``\eqref`` command. If you want to name the equation something specific, you ``\tag`` it instead. You can’t use ``\eqref`` with ``\tag``. If you donot want LaTeX to number a particular equation, use the starred version of equation using an ``\begin{equation*}`` and ``\end{equation*}``

[need to include images as examples?]

Building Blocks of a Mathematical Formula
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Greek Letters can are entered as ``\alpha, \beta, \gamma, \delta, ...`` for lowercase letters and ``\Alpha, \Beta, \Gamma, ...`` for uppercase ones. 

Exponents and Subscripts can be specified using the ^ and the _ character. Most math mode commands act only on the next character, so if you want a command to affect several characters, you have to group them together using curly braces: {...}.

The square root is entered as ``\sqrt``; the nth root is generated with ``\sqrt[n]``. The size of the root sign is determined automatically by LaTeX. If just the sign is needed, use ``\surd``.

To explicitly show a multiplication a dot may be shown. \cdot could be used, which typesets the dot to the centre. \cdots is three centered dots while \ldots sets the dots on the baseline. Besides that, there are \vdots for vertical and \ddots for diagonal dots.

A fraction can be typeset with the command ``\frac{...}{...}``

The integral operator is generated with ``\int``, the sum operator with ``\sum``, and the product operator with ``\prod``. The upper and lower limits are specified with ``^`` and ``_`` like subscripts and superscripts.

If you put ``\left`` in front of an opening delimiter and ``\right`` in front of a closing delimiter, LaTeX will automatically determine the correct size of the delimiter. Note that you must close every ``\left`` with a corresponding ``\right``.



Vertically Aligned Material
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Multiple Equations
++++++++++++++++++

For formulae running over several lines or for equation systems, you can use the environments ``align`` and ``align*`` instead of ``equation`` and ``equation*``. With ``align`` each line gets an equation number. The ``align*`` does not number anything. 

The ``align`` environments center the single equation around the ``&`` sign. The ``\\`` command breaks the lines. If you only want to enumerate some of equations, use ``\nonumber`` to remove the number. It has to be placed before the ``\\``.

Arrays and Matrices
+++++++++++++++++++


Bibliography
------------

You can produce a bibliography with the ``thebibliography`` environment.


--------------------------------------------------------

Acknowledgements, Attributions
------------------------------

1. *LaTeX Wikibook*

2. *The Not So Short Introduction to LaTeX2e* by Tobias Oetikar et. al. 

