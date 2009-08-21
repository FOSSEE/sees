
Version Control
===============

Introduction
------------

The following words are from a blogpost "http://karlagius.com/2009/01/09/version-control-for-the-masses/"

"Version control is one of those weird, geeky things that never really gained much ground in non-geek fields, despite the fact that it’s blindingly useful.

Version control (or source control) is nothing more arcane than keeping copies of ones work as one make changes to it. On the surface, it’s all straight-forward; make a copy of every file before making any changes to it. That way, if something seriously messes up, one can always fall back to something that worked before, or at least compare the broken copy with one that used to work so one can figure out where it went off kilter.Accidentally deleted half of thesis and closed the word processor? No problem – out comes the backup."

Now, in the real world, it’s not so easy. One probably cooks up their own version control system without realizing it had such a geeky name. For instances files with names oldxxxxxx.odt and latestxxxxxx.odt. Every time to make some change in a file, one save it with different name then the original one. Luckily there are like, loads of version control systems out there to do this heavy lifting.

Why Use Version Control
-----------------------

"Its the start which most people fail to attempt". 
One of idea behind Version Control Tools was to save that "one" step, to build onto it, rather then simply lose it. So here are some reasons why is automated version control needed:

    - It will track the history and evolution of a project, so one don't have to do it manually. It allows to track what changes where made, when were they made, by whom and why.
    - For a team on people working on same project, revision control software makes it easier to collaborate. For example, when people more or less simultaneously make potentially incompatible changes, the software will help them to identify and resolve those conflicts.
    - It can help to recover from mistakes. If a change made at some moment of time, turns out to be in error in future, one can revert to an earlier version of one or more files. In fact, a really good revision control tool will even help in efficiently figure out exactly when a problem was introduced.

Most of these reasons are equally valid for the project having one man show, or hundred people. Beyond this, even it can be used to maintain assignments related to one particular subject/course, it will help manage things in way much better way. Rather use these tools for *resource management*. All codes, documents, presentation, assignments related to one course maintained in such a inventory,and one would never need (excuse)/(face the embarrassament), "I accendently deleted my all data!"(for those who have actually done that after completing assignments), and Internet hosting for version control will make the work immune to local hard-disk crash, unless hosting crashes itself.

Some of Version Control Tools available and used widely are:

     - cvs (Concurrent Version System)
     - svn (Subversion)
     - hg (Mercurial)
     - bzr (Bazaar)
     - git 

Each of above mentioned tools have sets of feature which it offers in unique way. For this session we are going to concentrate on hg (mercurial). After covering the basics of hg, one can easily try other tools, and use what-ever he/she is most comfortable with.

Learning the Lingo
------------------

Each Version Control uses its own nomenclature for more or less the same features. Here are some of terms which are going to used through out the rest of session:

Basic Setup
~~~~~~~~~~~

     Repository(repo):
	The database/folder storing the files.
     Server:
	The computer storing the repo.
     Client:
	The computer connecting to the repo.
     Working Set/Working Copy:
     	Your local directory of files, where you make changes. This is what is present on client side.
     Trunk/Main:
	The “primary” location for code in the repo. Think of code as a family tree — the “trunk” is the main line. This is generally what is present on server.

Basic Actions
~~~~~~~~~~~~~
     
     Add:
	Put a file into the repo for the first time, i.e. begin tracking it with Version Control.
     Revision:
	What version a file is on.
     Head:
	The latest revision of the repo.
     Check out:
     	Initial download of repo onto machine.
     Check in:
     	Upload a file to repository(if it has changed). The file gets a new revision number, and people can “check out” the latest one.
     Checkin Message:
     	A short message describing what was changed.
     Changelog/History:
	A list of changes made to a file since it was created.
     Update/Sync:
	Synchronize local files with the latest from the repository on server. This get the latest revisions of all files.
     Revert:
	Throw away the local changes and reload the latest version from the repository.

Advanced Actions:
~~~~~~~~~~~~~~~~~

     Branch:
	Create a separate copy of a file/folder for private use (bug fixing, testing, etc).
     Diff/Change:
	Finding the differences between two files. Useful for seeing what changed between revisions.
     Merge (or patch):
     	Apply the changes from one file to another, to bring it up-to-date.
     Conflict:
	When pending changes to a file contradict each other (both changes cannot be applied).
     Resolve:
	Fixing the changes that contradict each other and checking in the correct version.
     
Types of Version Control:
~~~~~~~~~~~~~~~~~~~~~~~~~

Based on how source management is carried out in a tool there are two categories of Version Control Systems(VCS):

      - Centralized VCS: 
      	In this kind of system all the revision control functions are performed on a shared server. If two developers try to change the same file at the same time, without some method of managing access the developers may end up overwriting each other's work. Centralized revision control systems solve this problem in one of two different "source management models": file locking and version merging. Both svn and cvs follows this kind of management.
   
      - Distributed VCS:
      	In a distributed model, every developer has their own repo. Diffs, commits, and reverts are all done locally, one needs Internet only to share the changes with others. It makes work faster, handles branching and merging in better way, with less management. hg, bzr and git uses this workflow.

Get Going with Hg:
------------------

Reasons for selecting Hg rather then any other tools are:

	- It is easy to learn and use.
	- It is lightweight.
	- It scales excellently.
	- It is based on Python.

To get going with hg, following command gives the version. ::
   
   $hg version

   Mercurial Distributed SCM (version 1.1.2)
   Copyright (C) 2005-2008 Matt Mackall <mpm@selenic.com> and others
   This is free software; see the source for copying conditions. There is NO
   warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Built-in help, Mercurial provides a built-in help system. Following command will print a brief list of commands, along with a description of what each does. ::

   $hg help

   Mercurial Distributed SCM
   list of commands:
   add          add the specified files on the next commit
   addremove	-----------------------

	  
Suggested Reading:
------------------

	* http://karlagius.com/2009/01/09/version-control-for-the-masses/
	* http://betterexplained.com/articles/a-visual-guide-to-version-control/
	* http://en.wikipedia.org/wiki/Revision_control
	* http://hgbook.red-bean.com/
	* http://betterexplained.com/articles/intro-to-distributed-version-control-illustrated/
