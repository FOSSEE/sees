
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
     Commit:
     	Upload a file to repository(if it has changed). The file gets a new revision number, and people can “check out” the latest one.
     Checking Message:
     	A short message describing what was changed.
     Change log/History:
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
      	In a distributed model, every developer has their own repo. Diffs, commits, and reverts are all done locally, one needs Internet only to share the changes with others. It makes work faster, handles branching and merging in better way, with less management. hg, bzr and git uses this work flow.

Get Going with Hg:
------------------

Why hg?
~~~~~~~

	- It is easy to learn and use.
	- It is lightweight.
	- It scales excellently.
	- It is based on Python.

Getting Started:
~~~~~~~~~~~~~~~~

Following command tells the version of hg installed on machine:
   
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

For specific command, just follow the command name after the help. ::

    $hg help diff
    hg diff [OPTION]... [-r REV1 [-r REV2]] [FILE]...

    diff repository (or selected files)
    Show differences between revisions for the specified files.
    Differences between files are shown using the unified diff format.
    NOTE:____________

Let there be Repository:
~~~~~~~~~~~~~~~~~~~~~~~~

In Mercurial, everything happens inside a repository. The repository for a project contains all of the files that “belong to” that project, along with a historical record of the project's files.A repository is simply a directory tree in filesystem that Mercurial treats as special.

There can be two ways to create a repo, either getting local copy for existing repo available on Internet or machine, or creating a new repo. For getting already existing repo hg uses command *"clone"* ::

      $hg clone http://hg.serpentine.com/tutorial/hello localCopyhello

      requesting all changes
      adding changesets
      adding manifests
      adding file changes
      added 5 changesets with 5 changes to 2 files
      updating working directory
      2 files updated, 0 files merged, 0 files removed, 0 files unresolved

If clone succeeded, there would be a local directory called localCopyhello, with some files: ::

      $ls localCopyhello/
      hello.c  Makefile

Every Mercurial repository is complete, self-contained, and independent. It contains its own private copy of a project's files and history.

To start a new repository hg uses *"init"*: ::

   $ mkdir feviCol
   $ cd feviCol/
   $ echo "print 'Yeh Fevicol ka Majboot jod hai!'" > feviStick.py
   $ ls -a
   .  ..  feviStick.py
   $ hg init
   $ ls -a
   .  ..  feviStick.py  .hg

*.hg* directory indicates that this new dir is now a repo.This is where Mercurial keeps all of its metadata for the repository.The contents of the .hg directory and its subdirectories are private to Mercurial. Rest all files are for the user to use them as they pleases.

Creating a branch of existing local repo is very easy via hg using clone command: ::
	
    $ hg clone localCopyhello newCopy
    updating working directory
    2 files updated, 0 files merged, 0 files removed, 0 files unresolved

newCopy is exact copy of already existing repo. And this command can be used to create branch of locally created repo also: ::

    $ hg clone feviCol feviCol-pull
    updating working directory
    0 files updated, 0 files merged, 0 files removed, 0 files unresolved

These local branches can prove really handy at times. It allows keep multiple copies of local branch for different purposes, say for debugging, testing, working version.
	
History or Logs:
~~~~~~~~~~~~~~~~	  

For the new repo created, first thing which can be tried is to check the logs/history. What changes were made and when and why, answers to all those questions are stored in logs safely. So for the the cloned repo the history can be viewed using command *"log"* (following commands are wrt localCopyhello repo). ::

    $hg log
    changeset:   4:2278160e78d4
    tag:         tip
    user:        Bryan O'Sullivan <bos@serpentine.com>
    date:        Sat Aug 16 22:16:53 2008 +0200
    summary:     Trim comments.

    changeset:   3:0272e0d5a517
    user:        Bryan O'Sullivan <bos@serpentine.com>
    date:        Sat Aug 16 22:08:02 2008 +0200
    summary:     Get make to generate the final binary from a .o file.

    changeset:   2:fef857204a0c
    user:        Bryan O'Sullivan <bos@serpentine.com>
    date:        Sat Aug 16 22:05:04 2008 +0200
    summary:     Introduce a typo into hello.c.

    changeset:   1:82e55d328c8c
    user:        mpm@selenic.com
    date:        Fri Aug 26 01:21:28 2005 -0700
    summary:     Create a makefile

    changeset:   0:0a04b987be5a
    user:        mpm@selenic.com
    date:        Fri Aug 26 01:20:50 2005 -0700
    summary:     Create a standard "hello, world" program

By default, this command prints a brief paragraph of output for each change to the project that was recorded.The fields in a record of output from hg log are as follows:

   - changeset: This field has the format of a number, followed by a colon, followed by a hexadecimal (or hex) string. These are identifiers for the changeset. The hex string is a unique identifier: the same hex string will always refer to the same changeset in every copy of this repository. 
   - user: The identity of the person who created the changeset.
   - date: The date and time on which the changeset was created, and the timezone in which it was created.
   - summary: The first line of the text message that the creator of the changeset entered to describe the changeset.
   - tag: A tag is another way to identify a changeset, by giving it an easy-to-remember name.

To narrow the output of hg log down to a single revision, use the -r (or --rev) option. ::
   
   $hg log -r 3
   changeset:   3:0272e0d5a517
   user:        Bryan O'Sullivan <bos@serpentine.com>
   date:        Sat Aug 16 22:08:02 2008 +0200
   summary:     Get make to generate the final binary from a .o file.

*range notation* can be used to get history of several revisions without having to list each one. ::

   $ hg log -r 2:4
   changeset:   2:fef857204a0c
   user:        Bryan O'Sullivan <bos@serpentine.com>
   date:        Sat Aug 16 22:05:04 2008 +0200
   summary:     Introduce a typo into hello.c.

   changeset:   3:0272e0d5a517
   user:        Bryan O'Sullivan <bos@serpentine.com>
   date:        Sat Aug 16 22:08:02 2008 +0200
   summary:     Get make to generate the final binary from a .o file.

   changeset:   4:2278160e78d4
   tag:         tip
   user:        Bryan O'Sullivan <bos@serpentine.com>
   date:        Sat Aug 16 22:16:53 2008 +0200
   summary:     Trim comments.

The hg log  command's -v (or --verbose) option gives you this extra detail. ::

    $ hg log -v -r 3
    changeset:   3:0272e0d5a517
    user:        Bryan O'Sullivan <bos@serpentine.com>
    date:        Sat Aug 16 22:08:02 2008 +0200
    files:       Makefile
    description:
    Get make to generate the final binary from a .o file.

Making Changes:
~~~~~~~~~~~~~~~

There is feviStick.py file in repo created above with name feviCol. ::

    $ cd feviCol
    $ hg log
    $ hg status
    ? feviStick.py

*status(st)* command prints the revision history of the specified files or the entire project. "?" sign in front of file indicates that this file is not yet part of track record. *add* command is used to add new files to repo. ::

    $ hg add feviStick.py
    $ hg st
    A feviStick.py

So file is now part of repository(A symbol). Use *commit (alias ci)* command to make changes effective(this command would be explained in more details in later parts). ::
   
   $ hg ci -u "Shantanu <shantanu@fossee.in>" -m "First commit."
   $ hg log
   changeset:   0:84f5e91f4de1
   tag:         tip
   user:        Shantanu <shantanu@fossee.in>
   date:        Fri Aug 21 23:37:13 2009 +0530
   summary:     First commit.

Similar to add there are other commands available for file management in repo. ::

   $ hg cp feviStick.py pidiLite.py
   $ hg st
   A pidiLite.py

*copy (alias cp)* command is used to mark files as copied for the next commit. ::

   $ hg rename pidiLite.py feviCol.py
   $ hg st
   A feviCol.py
   $ hg ci -u "Shantanu <shantanu@fossee.in>" -m "Renamed pidiLite.py."
   $ hg tip
   changeset:   1:d948fb4137c5
   tag:         tip
   user:        Shantanu <shantanu@fossee.in>
   date:        Sat Aug 22 00:11:25 2009 +0530
   summary:     Renamed pidiLite.py.

*rename(alias mv)* rename files; equivalent of copy + remove. *tip* command shows newest revision in the repository.. ::

   $ hg remove feviCol.py
   $ hg st
   R feviCol.py

R status of files denotes, file is marked as to be removed by the previous command *remove*. To add the file again to repo, one can use *revert* command, which restore individual files or dirs to an earlier state. ::

  $ ls
  feviStick.py
  $ hg revert feviCol.py
  $ ls
  feviCol.py  feviStick.py

Sharing Changes:
~~~~~~~~~~~~~~~~

As mentioned earlier that repositories in Mercurial are self-contained. This means that the changeset just created exists only in Fevicol repository and not in previously cloned feviVol-pull. There are a few ways that can be used to propagate this change into other repositories.

Suggested Reading:
------------------

	* http://karlagius.com/2009/01/09/version-control-for-the-masses/
	* http://betterexplained.com/articles/a-visual-guide-to-version-control/
	* http://en.wikipedia.org/wiki/Revision_control
	* http://hgbook.red-bean.com/
	* http://betterexplained.com/articles/intro-to-distributed-version-control-illustrated/
