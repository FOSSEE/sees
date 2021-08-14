---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #region slideshow={"slide_type": "slide"} -->
An introduction to Conda
======================

<br/>
<br/>
<br/>
<br/>

<center>
August 12, 2021
</center>

<center>
Department of Aerospace Engineering, IIT Bombay
</center>

<center>
Prabhu Ramachandran
</center>

<!-- #endregion -->


<!-- #region slideshow={"slide_type": "slide"} -->
Agenda
------

- Introduction to conda
- Basic usage and practices
- Conda environments

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
Why
------

- Very popular
- Helps manage large, complex, binary packages
- Do not have to be superuser/administrator


<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
Installation and setup
-------------

- Two popular installers: anaconda and miniconda


- Download/install miniconda for your operating system
- https://docs.conda.io/en/latest/miniconda.html
- Install it
- Activate it for your shell

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
Environments
---------

- Isolated Python universe
- Does not affect other environments
- Cheap to create
- Easy to maintain


<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
Preliminaries
------

- Make sure you have installed conda
- Start a terminal and activate conda

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
Let us get started
---------

- List the existing environments

```bash
$ conda info --envs
```

- Avoid messing with the base environment

- Use help

```bash
$ conda --help
$ conda info --help
$ conda create --help
```


<!-- #endregion -->


<!-- #region slideshow={"slide_type": "slide"} -->
Creating an environment
--------------

```bash
$ conda create --name myenv python numpy matplotlib ipython
```
or

```bash
$ conda create -n myenv python numpy matplotlib ipython
```

At least:

```bash
$ conda create -n myenv python
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
Specifying a Python version
-----------------------------

```bash
$ conda create -n myenv python=3.8
```

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
Activating and using environments
----------------------------------

```bash
$ conda activate myenv
(myenv) $
```
or

```bash
$ source activate myenv
(myenv) $
```

- Install packages
```bash
$ conda install scipy pandas
```
- Search
```bash
$ conda search scikit-learn
```

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
Activating and using environments
----------------------------------

- List

```bash
$ conda list

$ conda list -n otherenv
```

- Remove packages

```bash
$ conda uninstall scikit-learn
```

<!-- #endregion -->


<!-- #region slideshow={"slide_type": "slide"} -->
Updating packages/environments
----------------------------------

- Inside an environment

```bash
(myenv) $ conda update scipy
```

- In another environment

```bash
$ conda update -n myenv scipy
```

- Everything

```bash
$ conda update --all
```
<!-- #endregion -->


<!-- #region slideshow={"slide_type": "slide"} -->
Deactivating and removing an environment
--------------------------------

```bash
(myenv) $ conda deactivate
```

or

```bash
(myenv) $ deactivate
```

Switch to another:
```bash
(myenv) $ conda activate test
(test) $
```

Remove the environment

```bash
$ conda remove -n myenv --all
```

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
Conda channels
---------------

- Identified by a name: defaults, conda-forge
- Many user-created channels
- conda-forge among the most useful

- Adding at the top
```bash
$ conda config --add channels conda-forge
```
- Adding at the bottom
```bash
$ conda config --append channels new_channel
```
- Install from specific channel
```bash
$ conda install -c conda-forge pytorch
```

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
Sharing environments
-------------

- Dump list of packages
```bash
$ conda env export -n myenv > environment.yml
```

- Create
```bash
$ conda env create --file environment.yml
```

- OS specific:

```bash
$ conda list --explicit > pkgs.txt
```

```bash
$ conda create -n junk --file pkgs.txt
```
<!-- #endregion -->


<!-- #region slideshow={"slide_type": "slide"} -->
Miscellaneous
-------------

- Update conda
```bash
$ conda update conda
```
- Detailed info
```bash
$ conda search scipy --info
```

```bash
$ conda search -c conda-forge scipy=1.1
$ conda search -c defaults "scipy>1.7" --info
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
Learning more
-------------

- https://conda.io/projects/conda/en/latest/user-guide/index.html
- https://conda.io/projects/conda/en/latest/user-guide/cheatsheet.html

<!-- #endregion -->
