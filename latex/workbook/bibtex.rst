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

