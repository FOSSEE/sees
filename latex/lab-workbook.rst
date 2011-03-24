 Exercises
===========

Lab-1
-----

#. Compile and produce a pdf output of ``example1.tex``.

#. Modify ``example1.tex`` replacing ``LaTeX`` with {\\LaTeX}.

#. Add a title, author and date to the document.

#. What happens if {\\date} is replaced by {\\date{IIT, Bombay}} ?

#. Debug and compile examples 2, 3, 4, 5

#. Provide a document (pdf and source) with a TOC, but has been compiled
   only once. Exercise for Debugging.

#. What happens when you add the following {} code to the document from
   the previous question?

   ::

             \renewcommand{\contentsname}{What is Here?}

#. Experiment with setting the secnumdepth counter to 1, 0, -1.

#. Debug and compile example 6.

#. Experiment with the options of {\\documentclass}.

   -  10pt, 11pt, 12pt sets the size of the text of the document.

   -  onecolumn, twocolumn

   -  draft — makes {} highlight problems in typesetting to be looked at
      by a human.

Lab-2
-----

#. {\\newpage} command adds a page break. Add some page breaks to
   example 6 and see how the command works.

#. Try out the commands {\\pagestyle} and {\\thispagestyle} with the
   following parameters and look at the outputs obtained.

   -  ``empty``,

   -  ``plain``,

   -  ``heading``

#. Add the following description list describing the options to
   {\\includegraphics} command to a document and look at the output.

   ::

       \begin{description}
       \item[{\texttt{width=x}, \texttt{height=x}}] 
       If only the height or width is specified, the image is scaled, maintaining the aspect ratio.

       \item[{\texttt{keepaspectratio}}]  
       This parameter can either be set to true or false. When set to true, the image is scaled according to both width and height, without changing the aspect ratio, so that it does not exceed both the width and the height dimensions.

       \item[{\texttt{angle=x}}] 
       This option can be used to rotate the image by \texttt{x} degrees, counter-clockwise.

       \end{description}

#. {\\ldots} is used to get ellipsis in {} documents.

#. Read the manual of listings package and learn how to include a set of
   lines from a file into a {} document. Include a few lines from your
   previous lab exercises of ULT.

#. To change the line spacing of your document {\\usepackage{setspace}}
   and then specify the line spacing of your document, using
   {\\doublespace}, {\\onehalfspace}, etc.

#. Debug and compile examples 9, 10

Lab-3
-----

#. Debug and compile example 7.

#. BibTeX is another way of handling bibliography. Look at bibtex.rst
   and change draft.tex to use BibTeX.

#. As you would’ve already observed, {} compilation produces a lot of
   other files along with the pdf output.

   -  .log — gives a log of what happened during last compilation.

   -  .toc — stores section headers. Edit this file and observe changes
      in this document to see how the compilation of {} works and why
      two compilations are required for table of contents to work.

   -  .aux — used to share information between consecutive compiler
      runs.

#. Prepare a presentation in beamer with solutions to any 10 problems
   from the Lab workbook.

#. Debug and compile example 8.

#. Finish the incomplete parts of the draft to obtain the complete
   output of the sample document that we started out to prepare.


