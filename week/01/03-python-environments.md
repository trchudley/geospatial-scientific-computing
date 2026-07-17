# Python Environments

This page contains information on how to set up and manage a 'Python environment', through which will be loading scientific Python packages.

:::{note}
Installing JupyterLab and the python packages need to be done only **once** on the computer you are using. However, if you are using a workstation in a UoB lab, you will have to do it again if you change for another workstation or if the workstation is reset.
:::

## Why use environments?

There are three components to understand when setting up Python:

1. Actually installing Python (e.g. having, say, Python 3.12 on your system, and when you run the `python` command in your terminal, it will open it the Python interpreter).
2. Installing the many scientific packages that make Python useful for us (e.g. tools such as `pandas` or `rioxarray` or `matplotlib`, that we will cover in this course).
3. Managing environments so you can have multiple versions of Python with different combinations of versions and packages.

To conceptualise this, we can think of a fresh Python install like a new smartphone. Your phone will come with pre-installed apps such as phone, calendar, clock, notes, etc. In Python terms, our apps are known as **packages**, and those that come pre-installed are known as the **[Standard Library](https://docs.python.org/3/library/index.html)**. Examples include `os`, `datetime`, `random`, and `math`. They are generally designed provide basic functionality for interacting with the OS, opening files and data, and providing basic mathematical functionality.

To make proper use of your phone, the vast majority of users will not be happy with the basic apps on a smartphone. We will want to customise it by installing specific apps that are tailored and useful to you (e.g. WhatsApp, Instagram, etc). On smartphones, we do this via an app store. In Python, our ‘app stores’ are known as package managers, and there are multiple options such as `pip` or `conda`. We use these to install custom packages that we can use for specialist purposes (e.g. for opening geospatial data, or using statistical techniques).

There comes a point where you may have two contradictory uses for a phone that means you need more than one - think of employees who have a personal phone and a work phone, for legal or security reasons. To make the analogy slightly more contrived, imagine for some reason that Instagram and Outlook cannot be installed on the same phone. As a result, you might want a ‘social media’ version of your phone for doomscrolling and a ‘work’ version of your phone for checking your emails. These are analogous to Python environments. For example, for one task you might need the latest bleeding-edge version of a tool to take advantage of a recently added function (a required software/package/tool is known as a **dependency**). For another, you might be dependent on an ancient piece of code that requires a Python version from two decades ago. If these requirements are mutually exclusive, it won’t be possible to do both! These are known as **conflicting dependencies**. If you carry on adding more and more packages to one install, eventually it will break for reasons you often due to conflicting dependencies from different packages. As a result, you generally want to work with small, project-specific environments with the minimal packages necessary for a project.

## Prerequisites

In the [previous page](./02-installing-python.md), we ensured that the conda package manager is installed on your computer. You can test this by:

::::{tab-set}

:::{tab-item} On Windows
:sync: win
 - You are able to open **one of** the anaconda or miniforge prompt (depending on how Python was installed on your computer).
 - You can type `conda list` successfully.
 - You can type `python` and open a python interpreter.
:::

:::{tab-item} On MacOS and Linux
:sync: os
 - You are able to open the terminal.
 - You can type `conda list` successfully.
 - You can type `python` and open a python interpreter.
:::

::::

## Creating environments

When you have the command prompt open, you can check your environemnts by writing the following command, and hitting the return key:

```bash
conda env list
```

On a fresh install of conda, you should only see a `base` environment. You want to try and leave this environment alone unless specifically told otherwise.

We will create a new environment for Geospatial Scientific Computing, called `gsc`. We can do this through the following command:

```bash
conda create --name gsc
```

(if you want a differently named environment, then replace `gsc` with something else).

Rerunning `conda env list` should show you both environments - but with a `*` symbol next to `base`. This means `base` is currently your "active" environment. To continue our phone analogy above, this means we are currently using the `base` phone, and the apps we have installed on it. By running

```bash
conda activate gsc
```

We can switch to the `gsc` environment. Rerun `conda env list` and confirm that the `*` symbol is now next to `gsc`.

## Installing new packages

Within this course, we are going to be installing a number of further scientific python packages. For now, I am not going to be explaining what we have installed - that will become clear in the coming weeks. For now, just activate your `gsc` environment and install a series of software, including python, by listing them after the command `conda install -c conda-forge` as follows:

```bash
conda activate gsc
conda install -c conda-forge python numpy geopandas rioxarray matplotlib
```

(the command `install -c conda-forge` is telling `conda` to install the listed packages from the `conda-forge` repository, which you can think of as our "app store").

You may have to manually agree to an install prompt here (e.g. by typing `yes` or `y`).

Now that we have done this, we can access our installed environment at any time by running `conda activate gsc`. You can install and uninstall packages in this environment and never worry about altering or breaking anything outside of it. I would encourage you to create similar environments for other tasks - e.g. a `dissertation` environment should you be using python for your dissertation.

For more information about using `conda`, consult the quick start documentation [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
