.. highlight:: console

===============
Version Control
===============

At the end of this session, you will be able to:

-  Understand what Version Control is, and the need for it
-  Create and use repository on a daily basis
-  Clone existing repositories, from the web
-  View the history of a repository
-  Make changes to a repository and commit them
-  Work collaboratively with a team

Introduction
============

Version control is just a way to track your files over time and share them.
This allows you to go back to older versions when something goes wrong, see
what changed when and why, collaborate on a single piece of work with a bunch
of people.

Like this
`blog <http://karlagius.com/2009/01/09/version-control-for-the-masses/>`_
aptly points out, "Version control is one of those weird, geeky things that
never really gained much ground in non-geek fields, despite the fact that
it’s blindingly useful." In this course, we are going to see a handful of
such things, which are widely used in the programmer world, but not so much
in the scientific computing world, even when if they would be very useful.

Version control is just a way of backing up your files, before making changes
to it. Most people would have cooked up their own version control system,
without realizing, there are tools built by others, which make this task much
more organized and systematic. You surely would've saved your files, some
time or the other as ``oldproject.py``, ``latestproject.py`` and so on, or
date-tagging them as ``project-21-01-10.py``, ``project-20-02-10.py`` and so
on.

It is, in some ways, similar to playing a video game. We generally play games
in stages, saving the game, each time we finish a stage or complete a task.
We continue playing, but we could, if necessary, choose to go back to one of
the saved states and start over. In this manner we could change the state of
the game.

Why Use Version Control
=======================

We have seen that one of the main motivation to use a version system control
system is the ability to go back to a working version of the file, when
something stops working. Below are a few more advantages of using an
automated version control system.

    - It tracks the history and evolution of a project. It allows you to
      track what changes were made at what point of time, when and by whom.

    - If you are collaborating, as a team on a project, a version control
      system will make it much easier for you to collaborate. It allows you
      to work simultaneously on the same file, without worrying about merging
      your changes.

    - A good version control system will help you efficiently track down bugs
      and pin-point the changes that introduced the bug, reducing your
      debugging time.

Version control is as useful for a one man show, as it is for a big group of
people working on a project. As a student, you can use it to maintain your
course work, too. You could maintain a version controlled repository with all
your code, assignments, and other documents. Keeping your stuff version
controlled will help avoid accidental deletion of individual files etc.
Hosting it on a remote server will protect you from a local hard disk crash.

Git
===

Some of Version Control Tools available and used widely are:

  - ``cvs`` (Concurrent Versions System)
  - ``svn`` (Subversion)
  - ``hg`` (Mercurial)
  - ``git`` (Git)

Each of these tools have some unique functionality and their own merits and
de-merits. In this course, we shall learn to use Git. Once you know how to
use ``git``, you could easily try other tools and switch to one that you feel
most comfortable with.

Why ``git`` ?
------------

   - very fast and powerful.
   - lightweight.
   - scales excellently.
   - lots of projects use git and this gives the scope for contribute to
     various projects.

Installation
------------

- For Linux based systems, Git is available in most of package management. So
  for say Ubuntu systems::

   $ sudo apt-get install git-core

  will be all you need to install git. Similarly Fedora users can use yum to
  install git.

- For Windows, simply download and install msysGit from
  http://code.google.com/p/msysgit/downloads/list and follows the standard
  installation.

- On Mac OS X, git can be installed using MacPorts.

  $ sudo port install git-core

Just say ``git`` in your shell, to see some of the commands that ``git``
provides and say ``git version`` to see the version of ``git`` that has been
installed on your system.

In this section, we have seen

  - the motivation to use version control
  - an analogy of version control with playing a video game
  - how to check if Git is installed, and it's version using ``git version``
    command

Let there be a Repository
=========================

At the end of this section, you will be able to -

  - initialize a new repository,
  - obtain the status of a repository,
  - add new files to a repository,
  - take snapshots of a repository,
  - view the history of a repository,
  - and set your user information for ``git``

To start using Git and get the benefits of using a version control system, we
should first have a **repository**. A repository is a folder with all your
files and a store of all the changes that were made to it. To save disk
space, ``git`` doesn't save all the files, but only saves only a series of
changes made to the files.

We have talked of an example of how we cook up our own version control
systems. Git does almost the same thing with one major difference. It doesn't
keep track of individual files. It keeps snapshots of the whole directory (or
repository), instead of individual files.

A repository can either be started using an ``init`` command or an existing
repository could be **cloned**.

Let us look at creating our own repository, now. We can look at obtaining
already existing repositories, at a later stage.

Let's say we have a folder called ``book``, which has all the chapters of a
book as text files. Let us convert that folder, into a ``git`` repository.

::

    $ cd book/
    $ ls -a
    . .. chapter1.txt chapter2.txt chapter3.txt


We have three chapters in the folder. We convert this folder into a git
repository using the ``git init`` command

::

    $ git init
    Initialized empty Git repository in /tmp/book/.git/

    $ ls -a
    . .. .git chapter1.txt chapter2.txt chapter3.txt


The ``.git`` directory indicates that our book directory is now a ``git``
repository. Git keeps all the history of the changes made, and a few other
configuration files, etc. in this directory. The directory, ``book`` is
called the **working directory**.

Adding Files
------------

We now have a fresh repository, but all our files are not being tracked or
watched by ``git``, yet. We need to explicitly ask it to watch the files,
that we want it to. To see this, use the ``git status`` command.

::

    $ git status
    # On branch master
    #
    # Initial commit
    #
    # Untracked files:
    #   (use "git add <file>..." to include in what will be committed)
    #
    #	chapter1.txt
    #	chapter2.txt
    #	chapter3.txt
    nothing added to commit but untracked files present (use "git add" to track)

As we can see, Git tells us that the files, ``chapter1.txt``,
``chapter2.txt`` and ``chapter3.txt`` files are untracked files, which means
``git`` is not tracking the changes we make to those files.

The ``status`` command gives the *status* of our working-directory at any
particular point in time. Using this command after every ``git`` command you
use, is a good idea, at least until you are reasonably comfortable with the
use of git.

We shall now ask git to watch these files for changes.

::

    $ git add .

Note that there is a ``.`` at the end, which refers to the current directory,
like in Linux.

::

    $ git status
    # On branch master
    #
    # Initial commit
    #
    # Changes to be committed:
    #   (use "git rm --cached <file>..." to unstage)
    #
    #	new file:   chapter1.txt
    #	new file:   chapter2.txt
    #	new file:   chapter3.txt
    #

    $

This simply adds all the changes in the (working) directory, and the
untracked files to the list of changes to be committed in the next commit.
This is also referred to as, staging changes for the next commit. As
expected, the ``status`` command shows that all the files listed under the
changes to be committed list. We could also specify files individually, for
example

::

    $ git add chapter1.txt

**Note**: If you have deleted files, ``git status`` will show you that some
files have been deleted, but the changes have not been staged for commit. You
can, then, tell ``git`` to stop tracking these files, using the ``git rm
<filename>`` command. Look at ``git help remove`` for more details.

Taking Snapshots
----------------

We have added a set of new files to the repository, but we haven't told
git to remember these changes, i.e., to take a snapshot at this point
in time. We do this by using the ``commit`` command.

::

    $ git commit -author "Puneeth Chaganti <punchagan@fossee.in>" -m "Initial Commit."

The ``--author`` parameter allows us to specify the user details. It is a
general good practice to use full name followed by the email id. The ``-m``
parameter allows us to give the commit message --- a message describing the
changes that are being committed.

Git has now taken a snapshot of our repository and has attached our
description along with it. To see the status of the files in the repository,
use the ``git status`` command.

::

    $ git status
    # On branch master
    nothing to commit (working directory clean)

Git tells you that there are no changes pending to be committed and the
working directory is clean.

Snapshot's Thumbnail views
--------------------------

To see the history of the changes to our repository, we use ``git log``. We
can view the change that we just made to our repository.

::

    $ git log
    commit ce1acaabfc262f4b26269a90d5f3edd72761e11b
    Author: Puneeth Chaganti <punchagan@fossee.in>
    Date:   Sat Nov 12 12:36:06 2011

        Initial Commit.


As we already discussed, git keeps track of the changes that are made to the
files in the repository. Notice, that our ``log`` is showing a **changeset**.
A changeset is nothing but a set of changes made to the repository between
two consecutive commits (the action of taking snapshots). Notice that ``git``
also shows the date at which the commit was made and the description of the
changeset.

User information
----------------

But there are two things, that can be changed. Firstly, it is unnecessary to
keep typing the user information each and every time we make a commit.
Secondly, it is not very convenient to enter a multi-line commit message from
the terminal.

We solve the problem of the username by setting it, using the ``config``
command.

::
    $ git config --global user.name "Puneeth Chaganti"
    $ git config --global user.email "punchagan@fossee.in"

This is a global setting for all the projects that we are working on. We
could also set the details, at a repository level. We shall look at this in
due course.

Let us now make another commit to see if this has taken effect. Let us
add author information to all the chapters that we have.

::

    Author: Puneeth Chaganti


Once we have added this to all the files, let us commit this change. We again
used the ``git commit`` command to commit the changes that we have made.

::

    $ git commit

We are now prompted with a window of our favorite editor. We can now type out
our commit message in the editor window. Unlike before, now we can
comfortably type a longer multi-line message.

There are some recommended practices for commit messages, too. It is a
general practice to have a summary line in the commit message which is no
longer than 60 to 65 characters giving a summary of the change committed.
This is followed up with an explanation of why this was changed, what is the
effect of this change, known bugs/issues remaining, if any, etc.

::

    Add author info to all the chapters

    All the chapters must have an author info. Added Puneeth Chaganti
    as the author. New authors can be added in newlines.

``git log`` should now show us both the changes that we have made. Notice
that the username settings are being used and also, the summary of the
changeset shows only the first line in the description that we have added.
Also, notice that ``git`` shows the commits in the reverse chronological
order, which is useful.

In this section, we have learned to -

  - initialize a new repository using ``git init``,
  - get the status of a repository using ``git status``,
  - use the ``git help`` to get help about any ``git`` command,
  - make commits of changes to files, using ``git commit``
  - view the history of the repository using the ``git log`` command,
  - and, set our user information in the global configuration.

But why commit?
===============

At the end of this section, you will be able to -

  - undo changes to your repository,
  - view the differences between any two states of a repository,
  - understand how revisions are numbered and use it as arguments to
    commands,

You must already be wondering, why we need all the overhead of
``commit`` and ``log``, etc. What is all this fuss about? "Isn't it
just a waste of time?"

Reverting Changes
-----------------

While you were wondering, let's say your friend walks in and together you
make a lot of changes.

1. You replace all the occurrences of ``&`` in ``chapter1.txt`` with
``and``.
2. You delete the ``chapter3.txt`` file.

::

    $ rm chapter3.txt
    $ git status

    # On branch master
    # Changes not staged for commit:
    #   (use "git add/rm <file>..." to update what will be committed)
    #   (use "git checkout -- <file>..." to discard changes in working directory)
    #
    #	deleted:    chapter3.txt
    #
    no changes added to commit (use "git add" and/or "git commit -a")


But after a while, you realize that these changes are unwarranted. You want
to go back to the previous state, undoing all the changes that you made,
after your friend arrived.

The undo in your editor may allow undoing the first change (if you haven't
closed it after making the changes) but there's no way you could get back
your ``chapter3.txt`` file, using your editor. But don't worry. Git to the
rescue!

As the output of the ``git status`` is telling us, we can use the
``checkout`` command to discard changes in the working directory.  We could
either discard all the changes at once, or do it one file at a time.

::

    $ git checkout chapter3.txt
    $ git status

You can see that the changes to chapter1.txt are still untouched. To undo all
the changes to the repository, we can use the ``checkout`` command with a
``.`` as an argument. But, let's not do it, since we wish to commit these
changes.

Viewing Changes
---------------

Let's say we now want to ``commit`` these changes, but we are not sure of all
the changes that we have made to the file, since it's been a while after we
made the changes. We could use the ``diff`` command to see all the changes
that have been made in the file.

::

    $ git diff
    diff --git a/chapter1.txt b/chapter1.txt
    index d082bea..bfe8449 100644
    --- a/chapter1.txt
    +++ b/chapter1.txt
    @@ -1,5 +1,5 @@
    -Introduction & Motivation
    -Creating & Getting repositories
    +Introduction and Motivation
    +Creating and Getting repositories
     Revision history
    -Making & sharing changes
    -Merges & Conflicts
    +Making and sharing changes
    +Merges and Conflicts

You see some cryptic output, but it's essentially giving you the list of
changes made to the file. All the lines that were deleted are preceded by a
``-`` and all the new-lines are preceded by a ``+``. You can see that the
``&`` occurrences have been replaces with ``and``.

We should note here that, the ``diff`` wouldn't make much sense, if we had
some binary files like ``.jpg`` or ``.pdf`` files. We would see some
gibberish in the output.

.. Gittified until till here.

Let us now commit this change.
::

    $ hg commit

    Replace all occurrences of & with and

    On the suggestion of Madhusudan C S.

    HG: Enter commit message.  Lines beginning with 'HG:' are removed.
    HG: Leave message empty to abort commit.

::

    $ hg log

We can see the history of all the commits that we have made in our
project. This gives us a brief description of all the changes made, by
showing us the summary line of all the commits. What if we want to get more
details?

We can pass an additional argument, ``-v`` or ``--verbose``,  to ``hg log``
to get the whole commit message, instead of just the summary.

::

    $ hg log -v

As you can see, the logs have started getting longer (and hence have been
dropped from the output) and getting out of our screen. Also, we are not
always, interested to see the whole history of the project. It would often
suffice to see the last few commits.

To limit the output of ``hg log``, we could use the ``-l`` or ``--limit``
argument
::

    $ hg log -v -l3

This will give us log of only the last three commits and not the whole
history of the project.

Revision Numbering
------------------

Often, the level of detail provided by the commit messages is also not
enough. We would want to see what *exactly* changed with a commit, probably
as a ``diff``. We could do that using **revision numbers**.

Have a look at the logs that the previous ``log`` command has
printed and look at the ``changeset`` line. It shows a number followed
by a semi-colon and some long hexa-decimal string. The number is
called the **revision number**. It is an identifier for the commit,
and can be along with various commands to specify the revision number,
if required.

Let's say we wish to see the changes between revision 1 and revision 2. We
shall use the ``diff`` command to do this.
::

    $ hg diff -r1 -r2

The diff command takes two revision numbers as arguments and gives the
changes made from revision in the first argument to revision in the second
argument.
::

    $ hg diff -r0 -r2

The above command will show all the changes made after revision 0 up to
revision 2.

The revision number can also be passed as an argument to many other commands.
For instance, we can check the logs of the very first commit, by saying
::

    $ hg log -r0
    changeset:   0:cbf6e2a375b4
    tag:         tip
    user:        punchagan@shrike.aero.iitb.ac.in
    date:        Fri Jan 28 14:04:07 2011 +0530
    summary:     Initial Commit

You could also specify a range of commits whose logs you would like to
see. Say, we would like to see the last two commits,
::

    $ hg log -r0:2

You could also see the changes made to a particular file, in the
specified range of the commits. Say, we wish to see the changes made
to the ``chapter2.txt`` file in the last two commits.
::

    $ hg log -r0:2 chapter2.txt
    changeset:   1:3163b8db10bb
    user:        Puneeth Chaganti <punchagan@fossee.in>
    date:        Fri Jan 28 16:21:29 2011 +0530
    summary:     Add author info to all the chapters

Notice that it shows only the logs of revision 1, since no changes
were made to the specified file in the second commit.

In this section, we have learnt to -

  - undo changes to the repository using ``hg revert``,
  - view changes done to the repository using ``hg diff``
  - use revision numbers as arguments to different ``hg`` commands

Collaborating with Mercurial
============================

At the end of this section, you will be able to -

  - clone existing repositories,
  - share your repositories with peers,
  - use version control for collaborating with your peers,

When motivating the use of version control systems, we spoke a lot about
collaboration and sharing our changes with our peers. Let us now see how we
can share our project with our peers and collaborate with them.

Cloning Repositories
--------------------

For this purpose let us create a central repository, a copy of our
repository, which is different from the one in which we are working. The
``clone`` command is used to **clone** or replicate an existing repository.

::

    $ hg clone book book-repo

This creates a copy of our repository, ``book``, with the name ``book-repo``.
The syntax of the ``clone`` command is -- ``hg clone SOURCE [DEST]``, where
the optional argument DEST is being represented in brackets. Here we are
giving book-repo as the destination.

The clone command can be used to replicate already existing repositories,
either on your own machine or on some remote machine somewhere on the
network. Since, ``hg`` maintains a copy of the full repository with every
copy of the repository, the two copies that we have are exactly equivalent.

``book-repo`` is the repository we shall be using as a central repository
and share it with our peers.

Sharing Repositories
--------------------

A mercurial repository can be shared in multiple ways. We shall use the
``http`` protocol to share the repository. Mercurial comes inbuilt with a
tiny server that can be used to share your repository over the network. To
start sharing the repository, we say

::

    $ cd ../book-repo
    $ hg serve

This will start serving the repository on the network on the port 8000.
Anybody in your network can access the repository in their browsers. Let us
see how it looks, in our own browser. We open the url `http://localhost:8000`
in our browser.

Let's say, our friend Madhu, now wants  to clone this repository. He will use
our ip-address and the port on which  we are serving the repository, to clone
the repository. Instead of using two machines, for the purposes of
demonstration, we shall clone into our own machine, with a different name.

::

    $ hg clone http://192.168.1.101:8000 book-madhu

This will clone the repository to the folder, ``book-madhu``. The log of the
repository will, obviously, be the same as our original repository.

::

    $ hg log

Sharing Changes
---------------

Let's say, Madhu now makes some changes to the repository.

1. He adds his name to the Authors list.
2. He moves down the Getting repositories part into a different section.

::

    $ hg diff
    diff -r 98f7f4a1bb4d chapter1.txt
    --- a/chapter1.txt	Fri Jan 28 16:24:42 2011 +0530
    +++ b/chapter1.txt	Fri Jan 28 23:03:37 2011 +0530
    @@ -2,6 +2,7 @@
                            =======================

     Author: Puneeth Chaganti
    +        Madhusudan CS
     Date: 2011-01-28 13:58:47 IST


    @@ -9,8 +10,9 @@
     Table of Contents
     =================
     1 Introduction and Motivation
    -2 Creating and Getting repositories
    +2 Creating
     3 Revision history
     4 Making and sharing changes
    -5 Merges and Conflicts
    +5 Getting repositories
    +6 Merges and Conflicts

He then commits these changes and **pushes** them to the central repository
that we have created.

::

    $ hg commit
    $ hg push
    pushing to http://192.168.1.101:8000
    searching for changes
    ssl required

The push failed, obviously, since we have not taken care of access rights
etc. It doesn't make much sense to allow anybody to make changes to a public
repository, by default. We will need to make changes to the settings of the
repository to allow this. **Note**: This is obviously not a safe way to share
your repository, but for our purposes, this is sufficient.

We add the following lines to the ``.hg/hgrc`` of the ``book-repo``
repository.
::

    [web]
    push_ssl=False
    allow_push=*

This will allow anybody to push to the repository, now.

By the way, this ``hgrc`` is a repository level configuration file. We could
also set the details of the user information in this file.

Madhusudan can now push and his changes will appear in the central
repository.

::

    $ hg push

Let's confirm it in the web interface that we started with the ``hg serve``
command.

Pulling Changes
---------------

Let us now **pull** these changes into our original repository ``book`` that
we have been working with. Before pulling the changes, we can use the command
``hg incoming`` to see the changes that have been made to the repository
after our last **pull** and the changesets that will be coming into our
repository after we do a **pull**.

::

    $ hg incoming
    abort: repository default not found!

What is going on here? This is because, we didn't clone our repository
``book`` from the central repository ``book-repo``. We can now add the
location of the central repository to the ``hgrc`` file, of this project.

::

    [paths]
    default = /home/punchagan/book-repo

Now, we can check the incoming changes.

::

    $ hg incoming
    searching for changes
    changeset:   3:3cd54926dbea
    tag:         tip
    user:        Madhusudan CS <madhusudancs@fossee.in>
    date:        Fri Jan 28 23:08:25 2011 +0530
    summary:     Add myself as author; Move getting repositories to section 5


To now **pull** these changes, we use the ``pull`` command.

::

    $ hg pull
    pulling from /home/punchagan/book-repo
    searching for changes
    adding changesets
    adding manifests
    adding file changes
    added 1 changesets with 1 changes to 1 files
    (run 'hg update' to get a working copy)


*Note* that ``hg`` is giving us a message, asking us to run a ``hg update``
 to get a working copy. Let us try to understand what this is.

As already explained, ``.hg`` folder has all the information about the
changesets of the repository. When we do a ``pull`` the changesets from the
remote repository are pulled to our repository, but our working directory is
not affected by these changes. To see this, we could use the ``hg parent``
command.

::

    $ hg parent
    changeset:   2:98f7f4a1bb4d
    user:        Puneeth Chaganti <punchagan@fossee.in>
    date:        Fri Jan 28 16:24:42 2011 +0530
    summary:     Replace all occurrences of & with and

As we can see, the parent is still our last commit, and the changes made by
Madhusudan are still not in our working directory. To get these changes we do
the update as suggested by ``hg``.

::

    $ hg up
    1 files updated, 0 files merged, 0 files removed, 0 files unresolved
    $ hg parent
    changeset:   3:3cd54926dbea
    tag:         tip
    user:        Madhusudan CS <madhusudancs@fossee.in>
    date:        Fri Jan 28 23:08:25 2011 +0530
    summary:     Add myself as author; Move getting repositories to section 5

As expected the **update** command updates the parent to the latest changes
that we just pulled from the remote repository.

The update command can also be used to go back into an older revision, by
specifying the revision to which we want to go to.

::

    $ hg up -r1
    1 files updated, 0 files merged, 0 files removed, 0 files unresolved
    $ hg parent
    changeset:   1:3163b8db10bb
    user:        Puneeth Chaganti <punchagan@fossee.in>
    date:        Fri Jan 28 16:21:29 2011 +0530
    summary:     Add author info to all the chapters
    $ hg cat chapter1.txt
    # Displays the contents of the chapter1.txt file as in revision 1.

To return to the latest revision we just use the ``up`` or ``update`` command
without specifying any revision number.

::

    $ hg up
    1 files updated, 0 files merged, 0 files removed, 0 files unresolved
    $ hg parent
    changeset:   3:3cd54926dbea
    tag:         tip
    user:        Madhusudan CS <madhusudancs@fossee.in>
    date:        Fri Jan 28 23:08:25 2011 +0530
    summary:     Add myself as author; Move getting repositories to section 5

Simultaneous Changes
--------------------

Ok, we have been talking about collaboration, but this is a nice situation,
where I was not changing anything while Madhusudan was changing the file,
incidentally.

Now, let's say, both of us are editing the file at the same time, but
different parts of it.  Say, I change the title of the section 2.
::

    $ hg diff
    diff -r 3cd54926dbea chapter1.txt
    --- a/chapter1.txt	Fri Jan 28 23:08:25 2011 +0530
    +++ b/chapter1.txt	Fri Jan 28 23:45:19 2011 +0530
    @@ -10,7 +10,7 @@
     Table of Contents
     =================
     1 Introduction and Motivation
    -2 Creating
    +2 Creating repositories
     3 Revision history
     4 Making and sharing changes
     5 Getting repositories
    $ hg commit
    $ hg push
    pushing to /home/punchagan/book-repo
    searching for changes
    adding changesets
    adding manifests
    adding file changes
    added 1 changesets with 1 changes to 1 files

Also, let us assume Madhusudan adds an additional section called References.
::

    $ hg diff
    diff -r 3cd54926dbea chapter1.txt
    --- a/chapter1.txt	Fri Jan 28 23:08:25 2011 +0530
    +++ b/chapter1.txt	Fri Jan 28 23:47:05 2011 +0530
    @@ -15,4 +15,4 @@
     4 Making and sharing changes
     5 Getting repositories
     6 Merges and Conflicts
    -
    +7 References
    $ hg commit
    $ hg log

Let us now compare the logs of the two repositories. You can see that both
the repositories have their topmost revision numbered as 4, but they are both
different. The identification number given to each revision is a local
identification. The hexadecimal string following that number is the actual
unique identification of that changeset, which will be unique across
repositories.

What happens now, when Madhusudan tries to push his changes to the central
repository?

::

    $ hg push
    pushing to http://192.168.1.101:8000
    searching for changes
    abort: push creates new remote heads!
    (did you forget to merge? use push -f to force)


The push failed! This is because, both of us have made changes, and they need
to be merged somehow. **Don't**, just for this one instance, take the advice
given by ``mercurial``. Using the ``-f`` would be disastrous. We will leave
out a discussion of that, for this course.

Madhusudan now needs to pull the new changes that have been pushed to the
repository after his last pull and **merge** them with his changes.

::

    $ hg pull
    pulling from http://192.168.1.101:8000
    searching for changes
    adding changesets
    adding manifests
    adding file changes
    added 1 changesets with 1 changes to 1 files (+1 heads)
    (run 'hg heads' to see heads, 'hg merge' to merge)
    $ hg merge
    merging chapter1.txt
    0 files updated, 1 files merged, 0 files removed, 0 files unresolved
    (branch merge, dont forget to commit)


We have now pull the changes from the central repository and merged them with
the changes in our repository. But, ``hg`` is warning us not to forget to
commit. Let's see what is the status of the repository at this point in time.

::

    $ hg st
    M chapter1.txt
    $ hg diff
    diff -r bd57162c31f6 chapter1.txt
    --- a/chapter1.txt	Fri Jan 28 23:51:52 2011 +0530
    +++ b/chapter1.txt	Sat Jan 29 00:00:39 2011 +0530
    @@ -10,7 +10,7 @@
     Table of Contents
     =================
     1 Introduction and Motivation
    -2 Creating
    +2 Creating repositories
     3 Revision history
     4 Making and sharing changes
     5 Getting repositories

As you can see, the changes pushed by us, changing the name of the section 2,
have now been made in the repository of Madhusudan. We will now need to
commit these changes.

::

    $ hg commit

We shall be using a commit message that makes it clear that we are merging.
We can now push this changes to the central repository. We could also check
the changes that will be pushed, before pushing them, using the ``hg
outgoing`` command.
::

    $ hg outgoing
    tag:         tip
    parent:      5:bd57162c31f6
    parent:      4:5c88c36f60de
    user:        Madhusudan CS <madhusudancs@fossee.in>
    date:        Sat Jan 29 00:02:53 2011 +0530
    summary:     Merge heads.

    changeset:   5:bd57162c31f6
    parent:      3:3cd54926dbea
    user:        Madhusudan CS <madhusudancs@fossee.in>
    date:        Fri Jan 28 23:51:52 2011 +0530
    summary:     Add additional References section
    $ hg push
    pushing to http://192.168.1.101:8000
    searching for changes
    adding changesets
    adding manifests
    adding file changes
    added 2 changesets with 2 changes to 1 files

The changes have now been successfully pushed! Let us look at the web
interface of the repo, to see that the changes have actually taken place. Let
us also have a look at the graph to, try and understand what has happened.

As we can see, a branch was created, when both of us started editing the file
simultaneously, and was then merged by Madhusudan CS.

Simultaneous Conflicting Changes
--------------------------------

We were lucky this time, in that we were editing separate parts of the file.
What will happen if we edited the same portion of the file, at the same time?
How would merges work? This will be the last thing that we are going to see
in this part of the course.

Let's say both of us edit the title of the section 6.

Let's say, I make the following changes, commit them and push them.

::

    $ hg diff
    diff -r ce3469a9446f chapter1.txt
    --- a/chapter1.txt	Sat Jan 29 00:02:53 2011 +0530
    +++ b/chapter1.txt	Sat Jan 29 10:30:21 2011 +0530
    @@ -14,5 +14,5 @@
     3 Revision history
     4 Making and sharing changes
     5 Getting repositories
    -6 Merges and Conflicts
    +6 Merging and resolving conflicts
     7 References
    $ hg commit
    $ hg push
    ...
    added 1 changesets with 1 changes to 1 files

Meanwhile, let's say Madhusudan was changing the same section title, as
follows.

::

    $ hg diff
    diff -r ce3469a9446f chapter1.txt
    --- a/chapter1.txt	Sat Jan 29 00:02:53 2011 +0530
    +++ b/chapter1.txt	Sat Jan 29 10:35:29 2011 +0530
    @@ -14,5 +14,5 @@
     3 Revision history
     4 Making and sharing changes
     5 Getting repositories
    -6 Merges and Conflicts
    +6 Simple Merges and Merges with Conflicts
     7 References
    $ hg commit
    $ hg push
    pushing to http://192.168.1.101:8000
    searching for changes
    abort: push creates new remote heads!
    (did you forget to merge? use push -f to force)
    $ hg pull
    ...
    added 1 changesets with 1 changes to 1 files (+1 heads)
    (run 'hg heads' to see heads, 'hg merge' to merge)
    $ hg merge
    0 files updated, 1 files merged, 0 files removed, 0 files unresolved
    (branch merge, dont forget to commit)


What happens now actually depends on how Mercurial is configured and the
programs available in your machine. You will either get a diff view with 3
panes or ``merge`` will insert markers in your file at the points where the
conflicts occur.

If you get a 3 pane view, the first pane is the actual file, where you make
changes, to resolve the conflicts. The second pane shows the changes that you
made, to the file. The last pane shows the changes that you pulled from the
original repo. Once you are satisfied with the changes, save and quit.

If you have a very minimal system, you might end up getting a file with
change markers, the original file being backed up. Open the file and resolve
the conflicts, deleting the markers. Once you are done, you need to tell
mercurial that you have resolved the conflicts manually.

::

    $ hg resolve -m chapter1.txt

Whatever be the process you have used for the merge, you will now need to
commit your changes, just like the simple merge that we performed.

::

    $ hg commit -m "Merge heads."
    $ hg push

We could look at the graph of the changes, in our web interface, being served
by the ``hg serve`` command. From the graph it is clear, how the merging has
occurred.

That brings us to the end of this tutorial on Mercurial. What we have covered
is nothing close to all the features of Mercurial. We've only scratched the
surface, but let's hope that this will get you started and you will be able
to organize your work and projects, better.

In this section, we have learnt how to -

- clone repositories, using ``hg clone``,
- serve our repositories via ``http`` using ``hg serve``,
- push changes to a repository using ``hg push``,
- check the changesets in a repository after last pull, using ``hg
  incoming``,
- pull changes from a repository using ``hg pull`` ,
- update the working directory, using ``hg update``,
- merge two heads, using ``hg merge``,
- and resolve conflicts using ``hg resolve``.

Additional Reading
==================

It is strongly recommended that you to go through the following topics, once
you are comfortable with using Mercurial on a day-to-day basis.

1. ``.hgignore``
#. ``hg rollback``
#. ``hg bisect``
#. ``hg backout``


References
==========

    - `A Visual Guide to Version Control <http://betterexplained.com/articles/a-visual-guide-to-version-control/>`_
    - `Version Control for the Masses <http://karlagius.com/2009/01/09/version-control-for-the-masses/>`_
    - `(Illustrated) Intro to Distributed Version Control <http://betterexplained.com/articles/intro-to-distributed-version-control-illustrated/>`_
    - `Understanding Mercurial <http://mercurial.selenic.com/wiki/UnderstandingMercurial>`_
    - `A Tutorial on Using Mercurial <http://mercurial.selenic.com/wiki/Tutorial>`_
    - `Hg Init: a Mercurial tutorial <http://hginit.com/>`_
    - `Beginners Guides <http://mercurial.selenic.com/wiki/BeginnersGuides>`_
    - `Software Carpentry <http://software-carpentry.org/4_0/vc/>`_


Appendix A - Definitions
========================

Definitions of a few commonly used terms.

Add
    Begin tracking a file (or a set of files) with Version Control.

Branch
    A diverged line of development.

Changeset
    An atomic collection of changes to the files in a repository.

Clone
    Creating a copy of an existing repository; New repo is self-contained.

Commit
    Taking a snapshot of the changes made in the repository (after the
    previous snapshot)

Conflict
    Occurs when two changesets have overlapping sections that have been
    modified.

Head
    A changeset with no child changesets.

History
    Cumulative of all the changesets of a repository.

Merge
    Combining two separate changesets into one merge changeset.

Repository (repo)
    - Loosely speaking, the folder with all the files and a store
      of the change history.
    - Strictly speaking, only the ``.hg`` directory that contains the change
      history.

Revert
    Going back to previous committed state of working directory or a file.

Revision
    A particular changeset.

Server
    A machine which serves the repository.

Tip
    Most recently changed head in a repository.

Update
    Updating the working directory to a particular revision or to the tip
    revision.

Working Directory
    The directory where all of the files and directories of the project are
    present.

..
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: nil
   fill-column: 77
   End:

