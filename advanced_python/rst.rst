====
ReST
====

----------------------------
The Pythonic way to Document
----------------------------

.. author: FOSSEE
.. date: 2010-07-22 Thu


What is ReST? 
==============

  + Sage Docs - Linear Algebra | Sources
  + ReST is a lightweight markup language. 
  + Developed by the Python community 
  + Heavily used in documentation of Python code 

Why ReST? 
==========

  + Highly readable source format. 
  + Easy to learn and write. 
  + Simple yet Powerful markup that can produce html/LaTeX output. 

Tools used 
===========

  + You will need python-docutils to compile your ReST documents::

      sudo apt-get install python-docutils

  + To build websites, look at Sphinx, rest2web, etc. 
  + rst2html doesn't support math. We shall use Sphinx to see how math works::

      sudo apt-get install python-sphinx

Generating output 
==================

  + html::

      rst2html source.rst destination.html

  + LaTeX ::

      rst2latex source.rst destination.tex

  + Slide shows ::

      rst2s5 source.rst destination.html

Paragraph 
==========

  + The most basic structural element 
  + Just a chunk of text separated by blank lines. 
  + Must begin at the left edge margin. 
  + Indented paragraphs are output as quoted text. 
  + Example ::

      Sage provides standard constructions from linear algebra,
      e.g., the characteristic polynomial, echelon form, trace, 
      decomposition, etc., of a matrix.

Section Headings 
=================

  + Single line of text with adornment 
  + Adornment is underline alone or an over- and underline 
  + ``- = ` :  ' " ~  ^ _ *  + # <  >`` can be used for adornment 
  + All headings with same adornment are at same level 
  + **NOTE**- The over/under line should be at least as long as the heading
    ::

      Linear Algebra
      ==============
  
      Matrix spaces
      -------------
  
      Sparse Linear Algebra
      ---------------------


Text Styles 
============

     =======================    ====================
      Markup text                Resulting text    
     =======================    ====================
      ``*italics*``              *italics*     
      ``**strong**``             **strong**          
      ````inline literal````     ``inline literal``  
     =======================    ====================



Code Samples 
=============

  + To include code, end the prior paragraph with =::= 
  + Code needs to be indented one level 
  + The code block ends, when text falls back to the previous indentation 
  + For instance ::

      For example, each of the following is legal ::

        plot(x, y)         # plot x and y using default line style and color
        plot(x, y, 'bo')   # plot x and y using blue circle markers
        plot(y)            # plot y using x as index array 0..N-1
        plot(y, 'r+')      # ditto, but with red plusses

Math 
=====

  + ReST in itself doesn't support math 
  + Sphinx has support for math using ~jsmath~ or ~pngmath~ 
      ::

       :math: `3 \times 3`
  
       .. math:: 
  
       \sum_{n=0}^N x_n = y

Lists 
======

  + Three flavors - Enumerated, Bulleted, Definition 
  + Always start as a new paragraph --- preceeded by a new line 
  + Enumerated 

      Number or Letter followed by a =.=,  =)= or surrounded by =( )=.

    ::

      1) Numbers
      #) auto numbered 
      A. Upper case letters
      a) lower case letters
      i) roman numerals
      (I) more roman numerals


Lists ... 
==========

  + Bulleted lists

      Start a line with -, + or *

  ::

    * a bullet point using "*"
  
      - a sub-list using "-"
  
        + yet another sub-list
  
      - another item

Lists ... 
==========

  + Definition Lists 

    * Consist of Term, and it's definition. 
    * Term is one line phrase; Definition is one or more paragraphs 
    * Definition is indented relative to the term 
    * Blank lines are not allowed between term and it's definition 
  
  what
    Definition lists associate a term with a definition.

Tables 
=======

  + Simple Tables 

    * Each line is a row. 
    * The table ends with ~=~ 
    * Column Header is specified by using ~=~ 
    * Cells may span columns; ~-~ is used to specify cells spanning columns. 

::
  
  ============ ============ =========== 
   Header 1     Header 2     Header 3   
  ============ ============ =========== 
   body row 1   column 2     column 3   
   body row 2   Cells may span columns. 
  ------------ ------------------------ 
   body row 3   column 2     column 3    
  ============ ============ ===========
  

Tables... 
==========

Grid Tables 
------------

::

  +------------+------------+-----------+
  | Header 1   | Header 2   | Header 3  |
  +============+============+===========+
    body row 1   column 2     column 3   
  +------------+------------+-----------+
    body row 2   Cells may span columns. 
  +------------+------------+-----------+
    body row 3   Cells may    - Cells    
  +------------+ span rows.   - contain  
    body row 4                - blocks.  
  +------------+------------+-----------+

Links 
======

  + External links 
  
    Python_ is my favorite programming language. 
  
.. _Python: http://www.python.org/

  + Internal links 

    * To generate a link target, add a label to the location 
  
.. _example:
    * Titles & Section headings automatically produce link targets (in ReST) 
    * Linking to Target 
      + in ReST ::
      
          This is an example_ link.
          A Title
          =======
    
          `A Title`_ automatically generates hyperlink targets.

     + in Sphinx ::
    
         :ref: `This is an example <example>` link.
         This is an :ref: `example` link.
            

Footnotes 
==========
::

  This[#]_ gives auto-numbered[#]_ footnotes. 
  
  This[*]_ gives auto-symbol footnotes[*]_.
  
  .. [#] First auto numbered footnote
  .. [#] Second auto numbered footnote
  .. [*] First auto symbol footnote
  .. [*] Second auto symbol footnote



References 
===========

    + An Introduction to reStructured Text -- David Goodger
    + Quick reStructuredText
    + reStructuredText-- Bits and Pieces -- Christoph Reller


.. `An Introduction to reStructured Text`: http://docutils.sourceforge.net/docs/ref/rst/introduction.html
.. `Quick reStructuredText`: http://docutils.sourceforge.net/docs/user/rst/quickref.html
.. `reStructuredText-- Bits and Pieces`: http://people.ee.ethz.ch/~creller/web/tricks/reST.html

