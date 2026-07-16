# Installing Python

:::{note} Install required for personal computers only
University workstations already have the necessary software installed.
:::

In order to run Python, it must be installed on the computer you are working from.

Installing Python on your device is optional, as **all class exercises can be completed using the University workstations**. However, installing Python and related tools on your own device can be valuable for this course:

 - It allows you to work on exercises at home.
 - You will gain experience of how Python installation works in the 'real world'.
 - The University installation is such that you must return to the same physical workstation every time.


There are many ways to install Python on your computer. Most methods work, but some are more suited for our needs than others. It is easily to lose track of your installation and get confused: 

```{figure} https://imgs.xkcd.com/comics/python_environment.png
:alt: xkcd webcomic
:class: bh-primary
:width: 450px
:align: center
[https://xkcd.com/1987/](https://xkcd.com/1987/)

```

We are going to use a software called [**conda**](https://docs.conda.io/) to manage our Python installation. Conda is a 'package manager' that is commonly used across the data sciences to manage Python installs. It allows you not only install technical software like Python, but also will install any 'dependencies' (other software that your desired software needs to run) in the background. As your needs become more complex, it will also carefully manage software versions to ensure everything can play together nicely.

Unless you are experienced with Python installations (i.e. you have done this before), please follow these instructions carefully.

:::{warning} What to do if you **already** have python installed on your laptop
**If you already have Anaconda, Conda, or Miniconda installed from a previous experience:**

You can keep your installation if it works for you. If you’d prefer to start fresh, **uninstall Anaconda first** and follow the instructions below.
:::

:::{danger} **If you have Windows version 10 or below, or a Chromebook**
:class: dropdown
Do not attempt to install Python on a Windows 7, 8, or 10 computer. This operating systems are no longer supported. You can use the university’s workstations for the exercises instead.

Installing Python on a Chromebook is not straightforward, and I cannot provide support for this. You can still use the university’s workstations to complete the exercises.
:::

## Install Conda

We will install Conda using a minimal installation option, called [Miniforge](https://github.com/conda-forge/miniforge). 

::::{tab-set}

:::{tab-item} On Windows
:sync: win
Download [the Windows installer](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) amd double-click the `.exe` file to execute it.

Follow the prompts, taking note of the options to "Create start menu shortcuts" and "Add Miniforge3 to my PATH environment variable".
I'd recommend you to **not** add Miniforge3 to the PATH environment variable, as it can cause conflicts with other software (it is ticked off per default).
Without Miniforge3 on the path, the most convenient way to use the installed software (such as commands conda and mamba) will be via the "Miniforge Prompt" installed to the start menu (see [](test-install) below).

```{admonition} Important! About the installation location
:class: warning

Choose a folder located in where there is enough space available, for example in your user directory (e.g. `C:\Users\yourname\Miniforge3`). Do not install in a folder with special characters in the name (e.g. accents), as this can cause issues with conda.

:::

:::{tab-item} On MacOS and Linux
:sync: os
If you have a macOS machine, you can download and run a PKG installer for [Apple Silicon machines](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.pkg) or [Intel machines](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-x86_64.pkg) from the respective links. If given the option, ensure that the installer performs 'package initialisation' for your shell.

If you have a Linux machine, follow the the instructions [here](https://github.com/conda-forge/miniforge?tab=readme-ov-file#unix-like-platforms-macos-linux--wsl). You will have to open your "terminal" app (or equivalent, depending on your OS), and copy and paste the terminal commands.
:::

::::

### Testing your installation

::::{tab-set}

:::{tab-item} On Windows
:sync: win
On Windows, open the `miniforge prompt` (from the Start menu, search for and open "miniforge prompt"):

```{image} ../../img/miniforge.png
:alt: miniforge prompt
:class: bg-primary mb-1
:width: 400px
```

The prompt you opened should display a line like this:

```none
(base) C:\Windows\System32>
```

:::

:::{tab-item} On MacOS and Linux
:sync: os
For these platforms, the terminal is available by default. You can open it by searching for "terminal" in the search bar.
:::

::::

Now you should have a terminal window open. In the terminal, type:

```bash
conda list
```

You should see a long list of package names.

If you type:

```bash
python
```

A new python prompt should appear, with something like:

```
Python 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:17:27) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

You can type `exit()` to get out of the python interpreter.

---

<span style="font-size: 85%;">
This page builds upon CC-BY 4.0 content written by <a href="https://fabienmaussion.info/climate_risks/ready/01-installation.html">Fabien Maussion</a>.
</span>