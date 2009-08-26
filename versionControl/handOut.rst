
=================
 Version Control
=================

Introduction
============

The following words are from a blogpost "http://karlagius.com/2009/01/09/version-control-for-the-masses/"

"Version control is one of those weird, geeky things that never really gained much ground in non-geek fields, despite the fact that it’s blindingly useful.

Version control (or source control) is nothing more arcane than keeping copies of ones work as one make changes to it. On the surface, it’s all straight-forward; make a copy of every file before making any changes to it. That way, if something seriously messes up, one can always fall back to something that worked before, or at least compare the broken copy with one that used to work so one can figure out where it went off kilter. Accidentally deleted half of thesis and closed the word processor? No problem – out comes the backup."

Now, in the real world, it’s not so easy. One probably cooks up their own version control system without realizing it had such a geeky name. For instances files with names oldxxxxxx.py and latestxxxxxx.py. Every time to make some change in a file, one save it with different name then the original one. Luckily there are like, loads of version control systems out there to do this heavy lifting.

Why Use Version Control
=======================
 
One of idea behind Version Control Tools was to build onto very first step which can be creating a empty file, or writing a first buggy program for assignment, rather then simply loose it. So here are some reasons why is automated version control needed:

    - It will track the history and evolution of a project, so one don't have to do it manually. It allows to track what changes where made, when were they made, by whom and why.
    - For a team of people working on same project, revision control software makes it easier to collaborate. For example, when people more or less simultaneously make potentially incompatible changes, the software will help them to identify and resolve those conflicts.
    - It can help to recover from mistakes. If a change made at some moment of time, turns out to be in error in future, one can revert to an earlier version of one or more files. In fact, a really good revision control tool will even help in efficiently figure out exactly when a problem was introduced.

Most of these reasons are equally valid for the project having one man show, or hundred people. Besides projects, even it can be used to maintain assignments related to one particular subject/course, it will help manage things in way much better way. These tools can be used for better *resources management*. All codes, documents, presentation, assignments related to one course maintained in such a inventory can help avoiding accidental lose of data(deletion) and Internet hosting for version control will make the work immune to local hard-disk crash, unless hosting crashes itself.

Some of Version Control Tools available and used widely are:

     - cvs (Concurrent Version System)
     - svn (Subversion)
     - hg (Mercurial)
     - bzr (Bazaar)
     - git 

Each of above mentioned tools have sets of feature which it offers in unique way. For this session we are going to concentrate on hg (mercurial). After covering the basics of hg, one can easily try other tools, and use what-ever he/she is most comfortable with.

Learning the Lingo
==================

Each Version Control uses its own nomenclature for more or less the same features. Here are some of terms which are going to used through out the rest of session:

Basic Setup
-----------

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
-------------
     
     Add:
	Put a file into the repo for the first time, i.e. begin tracking it with Version Control.
     Revision:
	What version a file is on.
     Head/Tip:
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
-----------------

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
-------------------------

Based on how source/code management is carried out in a tool there are two categories of Version Control Systems(VCS):

      - Centralized VCS: 
      	In this kind of system all the revision control functions are performed on a shared server. If two developers try to change the same file at the same time, without some method of managing access the developers may end up overwriting each other's work. Centralized revision control systems solve this problem in one of two different "source management models": file locking and version merging. Both svn and cvs follows this kind of management.
   
      - Distributed VCS:
      	In a distributed model, every developer has their own repo. Diffs, commits, and reverts are all done locally, one needs Internet only to share the changes with others. It makes work faster, handles branching and merging in better way, with less management. hg, bzr and git uses this work flow.

Get Going with Hg:
==================

Why hg?
-------

	- It is easy to learn and use.
	- It is lightweight.
	- It scales excellently.
	- It is based on Python.

A small point to notice here, hg cant track binary files for changes, one can add them to repo, but wont be able to track changes made to it. And hg considers, odt, pdf files as binary.

Getting Started:
----------------

Following command tells the version of hg installed on machine: ::
   
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
------------------------

In Mercurial, everything happens inside a repository. The repository for a project contains all of the files that “belong to” that project, along with a historical record of the project's files. A repository is simply a directory tree in file-system that Mercurial treats as special.

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

To start a new repository use *hg init*: ::

   $ mkdir Fevicol
   $ cd Fevicol/
   $ echo "print 'Yeh Fevicol ka Majboot jod hai'" > feviStick.py
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

    $ hg clone Fevicol Fevicol-pull
    updating working directory
    0 files updated, 0 files merged, 0 files removed, 0 files unresolved

These local branches can prove really handy at times. It allows keep multiple copies of local branch for different purposes, say for debugging, testing, working version.
	
History or Logs:
----------------

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
---------------

There is feviStick.py file in repo created above with name Fevicol. *status(alias st)* command prints the revision history of the specified files or the entire project::

    $ cd Fevicol
    $ hg log
    $ hg status
    ? feviStick.py

"?" sign in front of file indicates that this file is not yet part of track record. *add* command is used to add new files to repo. ::

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

Similar to add there are other commands available for file management in repo. *copy (alias cp)* command is used to mark files as copied for the next commit. ::

   $ hg cp feviStick.py pidiLite.py
   $ hg st
   A pidiLite.py

*rename(alias mv)* rename files; equivalent of copy + remove. *tip* command shows newest revision in the repository. ::

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

*remove* command is used to remove files from a repo. ::

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
----------------

Pulling from repo:
~~~~~~~~~~~~~~~~~~

As mentioned earlier that repositories in Mercurial are self-contained. This means that the changeset just created exists only in Fevicol repository and not in previously cloned Fevicol-pull. There are a few ways that can be used to propagate this change into other repositories. ::

   $ hg clone Fevicol Fevicol-clone
   updating working directory
   2 files updated, 0 files merged, 0 files removed, 0 files unresolved

Or traverse into the any dir which is a working hg repo(using hg init) and pull command will download all changeset from main repo. ::

   $ mkdir Fevicol-pull
   $ cd Fevicol-pull
   $ hg init
   $ hg pull ../Fevicol
   pulling from ../Fevicol
   requesting all changes
   adding changesets
   adding manifests
   adding file changes
   added 2 changesets with 2 changes to 2 files
   (run 'hg update' to get a working copy)

*changeset* means a list of changes made to a file. In words of *hg help*, pull command is: ::

   pull changes from the specified source

    Pull changes from a remote repository to a local one.

    This finds all changes from the repository at the specified path
    or URL and adds them to the local repository. By default, this
    does not update the copy of the project in the working directory.

Some times, even before pulling changesets, one may need to see what changes would be pulled, Mercurial provides *hg incoming* to tell what changes *hg pull* would pull into repo, without actually pulling the changes. This command is really handy in case of avoiding unwanted changesets into the repo.

With Mercurial, *hg pull* does not(by default) touch the working directory. Instead there is *hg up (alias update, co, checkout)* command to do this. ::

    $ cd Fevicol-pull
    $ ls -a
    .  ..  .hg
    $ hg up
    2 files updated, 0 files merged, 0 files removed, 0 files unresolved
    $ ls -a
    .  ..  feviCol.py  feviStick.py  .hg
    
To update to specific version, give a version number to the *hg update* command. ::
   
    $ hg update 0
    0 files updated, 0 files merged, 1 files removed, 0 files unresolved
    $ hg parent
    changeset:   0:84f5e91f4de1
    user:        Shantanu <shantanu@fossee.in>
    date:        Fri Aug 21 23:37:13 2009 +0530
    summary:     First commit.

If no version number is specified *hg up* will update to the tip version. Version number of hg starts from 0. Compare *hg parent* output to the one before doing update to see the difference.

Making Changes:
~~~~~~~~~~~~~~~

After getting the desired version of local repo, one can make changes as he/she needs and then make them available(share) for others. For these operations we will be working in Fevicol-clone repo which we created earlier. It's often good practice to keep a “pristine” copy of a remote repository around, which you can then make temporary clones of to create sandboxes for each task you want to work on. ::

    $ cd Fevicol-clone/
    $ cat feviStick.py 
    print 'Yeh Fevicol ka Majboot jod hai'

This tagline is correct for feviCol.py but for feviStick.py it should be different. ::

    $ echo "print 'Ab no more Chip Chip'" > feviStick.py
    $ cat feviStick.py
    print 'Ab no more Chip Chip'
    $ hg st
    M feviStick.py

Mercurial's hg status command will tell us what Mercurial knows about the files in the repository. 'M' sign in front of feviStick.py indicates that Mercurial has noticed change.

It's somewhat helpful to know that feviStick.py was modified, but one might prefer to know exactly what changes were made to it. To do this, use the *hg diff* command. ::

    $ hg diff
    diff -r a7912d45f47c feviStick.py
    --- a/feviStick.py	 Sun Aug 23 22:34:35 2009 +0530
    +++ b/feviStick.py	 Sun Aug 23 22:47:49 2009 +0530
    @@ -1,1 +1,1 @@
    -print 'Yeh Fevicol ka Majboot jod hai'
    +print 'Ab no more Chip Chip'

We can modify files, build and test our changes, and use hg status and hg diff to review our changes, until we're satisfied with what we've done and arrive at a natural stopping point where we want to record our work in a new changeset. All the diffs prior to committing the changes would be done wrt earlier marked record.The hg commit command lets us create a new changeset.

Mercurial records your name and address with each change that you commit, so that you and others will later be able to tell who made each change. Mercurial tries to automatically figure out a sensible username to commit the change with. When we try to use *hg commit* there are various ways by which one can specify User name, some of those are:
	  
	  - Specify a -u option to the hg commit command on the command line, followed by a username.
	  - set HGUSER environment variable.
	  - Edit hgrc file present in .hg folder to set this property, add following lines to that file and Mercurial will read those parameters from that location. ::
	  
		[ui]
		username = Firstname Lastname <email.address@example.net>

For me the hgrc file looks like this: ::

    [paths]
    default = /home/baali/Fevicol
    [ui]
    username = Shantanu Choudhary <shantanu@fossee.in>

Once this parameter is set, *hg commit* command drops us into a text editor, to enter a message that will describe the modifications we've made in this changeset. This is called the commit message. It will be a record for readers of what we did and why, and it will be printed by hg log after we've finished committing. ::

    Changed tagline for feviStick.py.
    HG: Enter commit message.  Lines beginning with 'HG:' are removed.
    HG: --
    HG: user: Shantanu Choudhary <shantanu@fossee.in>
    HG: branch 'default'
    HG: changed feviStick.py 

This would be your default system editor(for me it is vim, one can set it also), where you can enter the log message in first line, once you are done with log message quit the editor using *[ESC] key ":wq"*.Once we've finished the commit, we can use the hg tip command to display the changeset we just created. ::

    $ hg tip
    changeset:   3:e1ab2aff4ddd
    tag:         tip
    user:        Shantanu Choudhary <shantanu@fossee.in>
    date:        Sun Aug 23 23:32:01 2009 +0530
    summary:     Changed tagline for feviStick.py. 

One can do above mentioned procedure using following one line command: ::

    $ hg ci -u "Shantanu <shantanu@fossee.in>" -m "Changed tagline for feviStick.py."

Sharing Changes:
~~~~~~~~~~~~~~~~

The *hg outgoing* command tells us what changes would be pushed into another repository. ::

    $ hg outgoing ../Fevicol
    comparing with ../Fevicol
    searching for changes
    changeset:   3:e1ab2aff4ddd
    tag:         tip
    user:        Shantanu Choudhary <shantanu@fossee.in>
    date:        Sun Aug 23 23:32:01 2009 +0530
    summary:     Changed tagline for feviStick.py.

And the *hg push* command does the actual push. ::

    $ hg push ../Fevicol
    pushing to ../Fevicol
    searching for changes
    adding changesets
    adding manifests
    adding file changes
    added 1 changesets with 1 changes to 1 files

As with hg pull, the hg push command does not update the working directory in the repository that it's pushing changes into. One has to use hg update to populate the changes in desired repo. ::

   $ cd ../Fevicol
   $ hg tip
   changeset:   3:e1ab2aff4ddd
   tag:         tip
   user:        Shantanu Choudhary <shantanu@fossee.in>
   date:        Sun Aug 23 23:32:01 2009 +0530
   summary:     Changed tagline for feviStick.py.
   $ cat feviStick.py
   print 'Yeh Fevicol ka Majboot jod hai'

changesets are imported, but update is yet to be done. ::

   $ hg up tip
   1 files updated, 0 files merged, 0 files removed, 0 files unresolved
   $ $ cat feviStick.py 
   print 'Ab no more Chip Chip'

Merging the Work:
~~~~~~~~~~~~~~~~~

This is next aspect of any version control, how to merge work done by various participants of project in a way that no one looses changes being made, and still remains updated. Here is simple case study which can help understanding why merging is required: 

Two persons, A and B are contributing on same project. Both starts from cloning the same online repo(lets say present state X), so that both have a working local repo. Now A edits one of file, commits the changes and pushes to the repo, hence changing the state of repo to Y, but B, have not updated his repo, makes a change in one of files and reaches to a different state Z. Now when A pulls repo from B, his repo will have multiple heads. This stage is clearly ambiguous, the repo of A is not consistent, it has multiple heads, and from here, whatever changes he makes can take whatsoever direction if it is not fixed, and hence A will have to merge changes so that everything becomes consistent again.

Lets see how this work with working repo, we will use Fevicol and Fevicol-clone repositories created earlier. For now, the status of both repo is: ::

    $ cd Fevicol-clone
    $ hg tip
    changeset:   3:e1ab2aff4ddd
    tag:         tip
    user:        Shantanu Choudhary <shantanu@fossee.in>
    date:        Sun Aug 23 23:32:01 2009 +0530
    summary:     Changed tagline for feviStick.py.

The tagline for feviCol.py is not complete, so we make changes in that file in this repo. ::

    $ echo "print 'Yeh Fevicol ka Majboot jod hai, tootega nahin'" > feviStick.py
    $ hg st
    M feviStick.py

And commit the changes made ::

    $ hg ci -u "Shantanu <shantanu@fossee.in>" -m "Updated tag line for feviCol.py."
    $ hg st
    $ hg tip
    changeset:   4:caf986b15e05
    tag:         tip
    user:        Shantanu <shantanu@fossee.in>
    date:        Tue Aug 25 16:28:24 2009 +0530
    summary:     Updated tag line for feviCol.py.

Now we will make some changes on Fevicol repo. We will add new file here ::

    $ cd Fevicol
    $ echo "print 'Jor laga ke hayyiya'" > firstAdd.py
    $ hg st
    ? firstAdd.py
    $ hg add firstAdd.py
    $ hg st
    A firstAdd.py
    $ hg ci -u "Shantanu <shantanu@fossee.in>" -m "Added firsAdd.py."
    $ hg tip
    changeset:   4:fadbd6492cc4
    tag:         tip
    user:        Shantanu <shantanu@fossee.in>
    date:        Tue Aug 25 16:46:24 2009 +0530
    summary:     Added firsAdd.py.
    
So now we have two repo, who have different commit history and tree, now if we try to pull changes from one to another, this is how it goes(we are still in Fevicol repo): ::

    $ hg pull ../Fevicol-clone 
    pulling from ../Fevicol-clone
    searching for changes
    adding changesets
    adding manifests
    adding file changes
    added 1 changesets with 1 changes to 1 files (+1 heads)
    (run 'hg heads' to see heads, 'hg merge' to merge)

There we go, since both repo were on different track, hg pull command in last line gives some heading from here. *hg heads* command show current repository heads or show branch heads. ::

    $ hg heads
    changeset:   5:caf986b15e05
    tag:         tip
    parent:      3:e1ab2aff4ddd
    user:        Shantanu <shantanu@fossee.in>
    date:        Tue Aug 25 16:28:24 2009 +0530
    summary:     Updated tag line for feviCol.py.

    changeset:   4:fadbd6492cc4
    user:        Shantanu <shantanu@fossee.in>
    date:        Tue Aug 25 16:46:24 2009 +0530
    summary:     Added firsAdd.py.
    
To get better understanding of what is going on hg have a tool known as *glog* which shows revision history alongside an ASCII revision graph. ::
     
    $ hg glog
    o  changeset:   5:caf986b15e05
    |  tag:         tip
    |  parent:      3:e1ab2aff4ddd
    |  user:        Shantanu <shantanu@fossee.in>
    |  date:        Tue Aug 25 16:28:24 2009 +0530
    |  summary:     Updated tag line for feviCol.py.
    |
    | @  changeset:   4:fadbd6492cc4
    |/   user:        Shantanu <shantanu@fossee.in>
    |    date:        Tue Aug 25 16:46:24 2009 +0530
    |    summary:     Added firsAdd.py.
    |
    o  changeset:   3:e1ab2aff4ddd
    |  user:        Shantanu Choudhary <shantanu@fossee.in>
    |  date:        Sun Aug 23 23:32:01 2009 +0530
    |  summary:     Changed tagline for feviStick.py.
    |
    o  changeset:   2:a7912d45f47c
    |  user:        Shantanu <shantanu@fossee.in>
    |  date:        Sun Aug 23 22:34:35 2009 +0530
    |  summary:     Updated Content.
    |
    o  changeset:   1:d948fb4137c5
    |  user:        Shantanu <shantanu@fossee.in>
    |  date:        Sat Aug 22 00:11:25 2009 +0530
    |  summary:     Renamed pidiLite.py.
    |
    o  changeset:   0:84f5e91f4de1
       user:        Shantanu <shantanu@fossee.in>
       date:        Fri Aug 21 23:37:13 2009 +0530
       summary:     First commit.

To bring repo on single track/branch once again we will have to merge these two branches. Without merging them even hg update wont work for obvious reason of confusing track record. ::

    $ hg up
    abort: crosses branches (use 'hg merge' or 'hg update -C')

*hg merge* command merge working directory with another revision. ::

    $ hg merge
    1 files updated, 0 files merged, 0 files removed, 0 files unresolved
    (branch merge, don't forget to commit) 
    $ hg tip 
    changeset:   5:caf986b15e05
    tag:         tip
    parent:      3:e1ab2aff4ddd
    user:        Shantanu <shantanu@fossee.in>
    date:        Tue Aug 25 16:28:24 2009 +0530
    summary:     Updated tag line for feviCol.py.

After merging two branches, until we commit the results of merge it will keep on showing two heads. ::

    $ hg ci -u "Shantanu <shantanu@fossee.in>" -m "Merged branches of add and tag line."
    $ hg heads 
    changeset:   6:edbe97209954
    tag:         tip
    parent:      4:fadbd6492cc4
    parent:      5:caf986b15e05
    user:        Shantanu <shantanu@fossee.in>
    date:        Tue Aug 25 17:06:03 2009 +0530
    summary:     Merged branches of add and tag line.

Here is brief and meaningful output of glog ::

    $ hg glog 
    @    changeset:   6:edbe97209954
    |\   tag:         tip
    | |  parent:      4:fadbd6492cc4
    | |  parent:      5:caf986b15e05
    | |  user:        Shantanu <shantanu@fossee.in>
    | |  date:        Tue Aug 25 17:06:03 2009 +0530
    | |  summary:     Merged branches of add and tag line.
    | |
    | o  changeset:   5:caf986b15e05
    | |  parent:      3:e1ab2aff4ddd
    | |  user:        Shantanu <shantanu@fossee.in>
    | |  date:        Tue Aug 25 16:28:24 2009 +0530
    | |  summary:     Updated tag line for feviCol.py.
    | |
    o |  changeset:   4:fadbd6492cc4
    |/   user:        Shantanu <shantanu@fossee.in>
    |    date:        Tue Aug 25 16:46:24 2009 +0530
    |    summary:     Added firsAdd.py.

And we are back on track.

Workflow:
=========

This is chain of steps which can be followed for working against a project that has a centralized copy, you may want to make sure you're up to date first. This means pulling its changes and then updating. 

For example: ::
    
    $ hg pull
    $ hg update

This will grab the remote changes from the location you first cloned from. Then it will apply the changes. You can do this in one go with: ::

    $ hg pull -u

Now let's say you make some changes. You edit a file and you want to commit your change. You can do this with: ::

    $ hg commit

An editor will pop-up asking you to write a message describing your change. This is required. When you're done for the day, and you have required changesets sitting in your repository. Before pushing to upstream make sure to pull and update and merge branches if required, once everything looks okay and you have single track, push the changes, ::

    $ hg push

Suggested Reading:
==================

	* http://karlagius.com/2009/01/09/version-control-for-the-masses/
	* http://betterexplained.com/articles/a-visual-guide-to-version-control/
	* http://en.wikipedia.org/wiki/Revision_control
	* http://hgbook.red-bean.com/
	* http://betterexplained.com/articles/intro-to-distributed-version-control-illustrated/
	* http://wiki.alliedmods.net/Mercurial_Tutorial
