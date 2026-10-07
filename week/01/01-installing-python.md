# Installing Python

:::{note} Optional content: Install required for personal computers only
University workstations already have the necessary software installed.
:::

In order to run Python, it must be installed on your device. Installing Python and related tools on your personal device is optional, as **all class exercises can be completed using the University workstations**. However, having done so can be valuable for this course:

 - It allows you to work on exercises away from the University workstations.
 - You will gain experience of how Python installation works in the 'real world'.
 - The University setup of your Windows userspace is such that, after you have installed your Python environment, you must return to the same physical workstation every time to use your Python installation.

Installation should be simple in most cases, but there are always edge cases and difficulties that emerge. This is part of the "fun" of managing your own install: learning how to troubleshoot and manage issues when they arise is a key skill. We will try and help you to do this in this class, with one caveat:

:::{warning} **We cannot guarantee that your personal install will work**
**We will do our best to help you install Python on your own device, but please be aware we can't account for all possible setups and errors!** If we encounter an issue we can't resolve conveninently in class time, we will recommend you use a University workstation.
:::

## How to we install Python?

If you Google "how to install Python", you will find there are many competing ways to install Python on your computer. All (or most) of these methods will work, but some are more suited for our needs than others. If you install things in a rush, it is easily to lose track of your installation and get confused: 

```{figure} https://imgs.xkcd.com/comics/python_environment.png
:alt: xkcd webcomic
:class: bh-primary
:width: 450px
:align: center
[https://xkcd.com/1987/](https://xkcd.com/1987/)

```

We are going to use software called **conda** to manage our Python installation. Conda is a 'package manager' that is commonly used across the data sciences to manage Python installs. It allows you not only install technical software like Python, but also will install any 'dependencies' (other software that your desired software needs to run) in the background. As your needs become more complex, it will also carefully manage software versions to ensure everything can play together nicely.

:::{warning} What to do if you **already** have Python installed on your laptop
If you already have previous experience with Anaconda, Conda, or Miniconda, and still have it installed, you can keep your installation if it works for you. If you’d prefer to start fresh, **please uninstall your previous installation (e.g. Anaconda) first** and follow the instructions below. If you do not uninstall your previous installations, this may cause issues for you down the line.
:::

:::{danger} **If you have Windows version 10 or below, or a Chromebook**
:class: dropdown
Do not attempt to install Python on a Windows 7, 8, or 10 computer. This operating systems are no longer supported. You can use the university’s workstations for the exercises instead.

Installing Python on a Chromebook is not straightforward, and I cannot provide support for this. You can still use the university’s workstations to complete the exercises.
:::

## Install Conda

Unless you are experienced with Python installations (i.e. you have done this before), **please follow these instructions carefully**. Following alternative instructions or installation routes may impact your ability to follow instructions for the rest of the course.

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
**If you have a macOS machine**, you can download and run a PKG installer for [Apple Silicon machines](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.pkg) or [Intel machines](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-x86_64.pkg) from the respective links. During installation, follow the steps on screen by pressing `Continue`. By the 4th screen, you can choose a different installation path by clicking on "Change Install Location". Other options may be available behind the "Customise" button. If given the option, ensure that the installer performs 'package initialisation' for your shell. 

Once ready, click on Install. If everything went according to plan, the Summary page will report success.

**If you have a Linux machine**, follow the the instructions [here](https://github.com/conda-forge/miniforge?tab=readme-ov-file#unix-like-platforms-macos-linux--wsl). You will have to open your "terminal" app (or equivalent, depending on your OS), and copy and paste the terminal commands.
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

**Note:** be careful about getting this confused with similarly-named and similar-looking software, such as "Command Prompt", "Windows Powershell", or "Windows Terminal".

The prompt you opened should display a line like this:

```none
(base) C:\Windows\System32>
```

It might vary a little - the `(base)` is the important part! 

If you can't see `(base)`, try typing `conda init cmd.exe` and restart the prompt. If `conda` itself isn't recognised, try `C:\Users\<USERNAME>\miniforge3\Scripts\conda.exe init cmd.exe` and restart the prompt -- you will have add your username accordingly, and edit the installation path if you have chosen something different from the default.
```

:::

:::{tab-item} On MacOS and Linux
:sync: os
For these platforms, the terminal is available by default. You can open it by searching for "terminal" in the search bar.

The terminal you opened should display a line like this:
```
(base) myusername@mymachine ~ %
```
It might vary a little - the `(base)` is the important part! 

If `(base)` hasn't appeared, try typing `conda activate base`.

If the command line can't find `conda` either, try the following fixes in order:

1. Enter the command `~/miniforge3/bin/conda init zsh`  and restart the terminal.
2. Enter the command `~/miniforge3/bin/conda init bash`  and restart the terminal.
3. If this fails, manually activating `conda` with `source ~/miniforge3/bin/activate` might be temporary fix.

These commands assume you have chosen to install `miniconda` in the default install location, `/Users/myusername/miniforge3/`, which `~/miniforge3/` is shorthand for. You may need to edit the path if you have installed it elsewhere.

:::

::::

Now you should have an open command line interface (CLI) window open, with `conda` running. In the terminal, type:

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