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
venv and pip: an introduction
======================

<br/>
<br/>
<br/>
<br/>

<center>
August 22, 2021
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

- Introduction to venv and pip
- Basic usage and practices
- Using with conda

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
Why
------

- The default option for Python
- Similar to conda but predates it

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
Installation
-------------

- Part of your default Python install!
- Built-in usually

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
Getting started
---------

- Create an environments

```bash
$ python -m venv --help
```

```bash
$ python -m venv myenv
```

- Creates a directory `myenv`
- Is not self-contained but is isolated


<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
Activation/Deactivation
-------------------------

- On Linux/MacOS
```bash
$ source myenv/bin/activate
```

- On Windows
```bash
> .\myenv\Scripts\activate
```

```bash
$ python
>>> import sys
>>> sys.prefix
```

```bash
$ deactivate

$ rm -rf myenv
```

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
Other options
---------

- Inherit parent packages

```bash
$ python -m venv myenv --system-site-packages
```

- Can also upgrade using `--upgrade`

<!-- #endregion -->


<!-- #region slideshow={"slide_type": "slide"} -->
Installation of packages
------------------

```bash
$ python -m pip install numpy ipython
```

- Specific versions

```bash
$ python -m pip install vtk==9.0.1
```

- Remove

```bash
$ python -m pip uninstall vtk
```

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
More on installation
------------------

- Install from source directory
```bash
$ python -m pip install .
```

- Editable installation

```bash
$ python -m pip install --editable .
```
- Or `-e`
- `--no-cache-dir`: Do not use the cached wheels
- `--force-reinstall`: what it says
- `--no-binary`: use if binary wheel is busted
- The last will force a source build


<!-- #endregion -->


<!-- #region slideshow={"slide_type": "slide"} -->
More commands
------------------

```bash
$ python -m pip help
```

```bash
$ python -m pip list
```

```bash
$ python -m pip show numpy
```

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
Requirements
--------------

- Create a requirements
```bash
$ python -m pip freeze
```

- Use this to install

```bash
$ python -m pip install -r requirements.txt
```

<!-- #endregion -->


<!-- #region slideshow={"slide_type": "slide"} -->
Conda + requirements?
-----------------

```bash
$ cat environment.yml
name: myenv
...
dependencies:
  - python=3.8
  - ipython
  - pip
  - pip:
      - vtk
      - mayavi

```

- Use this directly with conda

```bash
$ conda env create
```

- `--file fname.yml` if not `environment.yml`

<!-- #endregion -->


<!-- #region slideshow={"slide_type": "slide"} -->
More information
------------------

- https://packaging.python.org/guides/
- https://realpython.com/python-wheels/

<!-- #endregion -->
