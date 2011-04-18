Session-1
=========

1. What do you know about the GNU/Linux Naming controversy?

#. ______ represents current directory

#. ``./`` represents parent directory. T/F?

#. The command ``PWD`` gives the present working directory. T/F?

#. Directory names cannot have spaces in them. T/F?

#. _________ gives a quick description of the command, given it's name

#. _________ command is used to change present working directory

#. _________ command is used to change present working directory

#. Explore the use of ``rmdir`` command.

#. Read up about the root user and the ``sudo`` command. 

Session-2
=========

Elementary Regex
----------------

In computing, regular expressions provide a concise and flexible means for identifying strings of text of interest, such as particular characters, words, or patterns of characters. A regular expression (often shortened to regex or regexp) is written in a formal language that can be interpreted by a regular expression processor, a program that either serves as a parser generator or examines text and identifies parts that match the provided specification.

Regular expressions are used by many text editors, utilities, and programming languages to search and manipulate text based on patterns. For example, Perl, Ruby and Tcl have a powerful regular expression engine built directly into their syntax. Several utilities provided by Unix distributions—including the editor *ed* and the filter *grep* — were the first to popularize the concept of regular expressions.


Regular Expressions are a feature of UNIX. They describe a pattern to match, a sequence of characters, not words, within a line of text. Here is a quick summary of the special characters used in the grep tool and their meaning: 

* ^ (Caret)        =    match expression at the start of a line, as in ^A.
* $ (Question)     =    match expression at the end of a line, as in A$.
* \ (Back Slash)   =    turn off the special meaning of the next character, as in \^.
* [ ] (Brackets)   =    match any one of the enclosed characters, as in [aeiou].
                      Use Hyphen "-" for a range, as in [0-9].
* [^ ]             =    match any one character except those enclosed in [ ], as in [^0-9].
* . (Period)       =    match a single character of any value, except end of line.
* * (Asterisk)     =    match zero or more of the preceding character or expression.
* \{x,y\}          =    match x to y occurrences of the preceding.
* \{x\}            =    match exactly x occurrences of the preceding.
* \{x,\}           =    match x or more occurrences of the preceding.



Here are some examples using grep:

*    grep smug files         {search files for lines with 'smug'}
*    grep '^smug' files      {'smug' at the start of a line}
*    grep 'smug$' files      {'smug' at the end of a line}
*    grep '^smug$' files     {lines containing only 'smug'}
*    grep '\^s' files        {lines starting with '^s', "\" escapes the ^}
*    grep '[Ss]mug' files    {search for 'Smug' or 'smug'}
*    grep 'B[oO][bB]' files  {search for BOB, Bob, BOb or BoB }
*    grep '^$' files         {search for blank lines}
*   grep '[0-9][0-9]' file  {search for pairs of numeric digits}

Lazy quantification
~~~~~~~~~~~~~~~~~~~

The standard quantifiers in regular expressions are greedy, meaning they match as much as they can, only giving back as necessary to match the remainder of the regex. For example, someone new to regexes wishing to find the first instance of an item between < and > symbols in this example:
::

	Another whale explosion occurred on <January 26>, <2004>.

...would likely come up with the pattern <.*>, or similar. However, this pattern will actually return "<January 26>, <2004>" instead of the "<January 26>" which might be expected, because the `*` quantifier is greedy — it will consume as many characters as possible from the input, and "January 26>, <2004" has more characters than "January 26".

Though this problem can be avoided in a number of ways (e.g., by specifying the text that is not to be matched: <[^>]*>), modern regular expression tools allow a quantifier to be specified as *lazy* (also known as non-greedy, reluctant, minimal, or ungreedy) by putting a question mark after the quantifier (e.g., <.*?>), or by using a modifier which reverses the greediness of quantifiers (though changing the meaning of the standard quantifiers can be confusing). By using a lazy quantifier, the expression tries the minimal match first. Though in the previous example lazy matching is used to select one of many matching results, in some cases it can also be used to improve performance when greedy matching would require more backtracking.

1. grep the marks of the students who scored above 75 in atleast one
subject. 

2. grep the marks of all the students whose names begin with an 's'

3. grep the marks of all the students whose names begin with
consonants. 

4. generate a word frequency list for ``wonderland.txt``. Hint: use
``grep``,  ``tr``, ``sort``, ``uniq`` (or anything else that you
want)

5. change the results.sh script to accept the input files also as
arguments. 

6. Show the lines from 10 to 20 of a file

Session-3
=========

1. Write a shell script that will take a filename as input and check
if it is executable. 

#. Modify the script in the previous step, to remove the execute
permissions, if the file is executable. 

#. Write a shell script to remove all executable files from a
 directory, when a directory is given as argument. 

