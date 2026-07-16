# Jupyter Notebooks

Now that we have set up a suitable conda environment, we can interface with Python as you have done before.

::::{tab-set}

:::{tab-item} On Windows
:sync: win
 - Open one of the anaconda or miniforge prompt (depending on how Python was installed on your computer).
 - Type `conda activate gsc` to open our environment.
 - Type `python` and open a python interpreter.
:::

:::{tab-item} On MacOS and Linux
:sync: os
 - Open the terminal.
 - Type `conda activate gsc` to open our environment.
 - Type `python` and open a python interpreter.
:::

::::

As before, this open up the Python prompt, which might look something like this:

```
Python 3.12.12 | packaged by conda-forge | (main, Oct 22 2025, 23:34:53) [Clang 19.1.7 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Cmd click to launch VS Code Native REPL
>>> 
```

The `>>>` indicates that it is waiting to accept your input.

Begin your journey by typing `1+1`, which should return `2`:

```bash
>>> 1+1
1
```

You are welcome to explore a variety of other options available to you, such as basic mathematical operations, setting variable names, or playing around with text (in the python world, we call text "strings"):

```bash
>>> 2*8
16
```

```bash
>>> (7 - 3) * 5
20
```

```bash
>>> print("Hello, World")
Hello, World!
```

It might begin to occur to you that typing individual commands into a terminal is not an efficient way we are going to run lots and lots of scientific code. 

Exit the Python terminal by typing `exit()`.

## Beyond the command line

This command line interface (CLI) is fine for exploring what Python can do, and you should definitely use it to explore basic data types etc. However, it’s hard to write multi-line commands (e.g. functions), or save scripts for repeat use. As a result, we tend to gravitate towards two other options:

1. The first is to write `.py` files, which are simply text files of Python commands that will be run one-by-one. These can be run through the Python interpreter (e.g. `python myscript.py`). This is useful for writing longer processing scripts that will be run autonomously to achieve tasks. 
2. The second is to use a ‘Jupyter Notebook’ (files with the suffix `.ipynb,` a vestigial reference to when these were known as iPython notebooks). These are mixed-media files run in your browser. You can combine text and code, and they are useful for when you are actively tinkering with the data (e.g. plotting, statistics, analysis, etc.), and making notes and wider documentation.

In this course, we will be using the latter as a beginner-friendly way of exploring Python and managing data. If you are interested in the latter, I have [written more about writing `.py` files in the appendix](../../backmatter/pyfiles.md)

## Installing Jupyter

:::{note}
Installing Jupyter only needs to be done once!
:::


The modern ‘data sciencey’ way of interacting with Python is through something called _Jupyter Notebooks_. These are mixed-media documents of text and code that allow you to annotate and iterate code production. If you want an example of what one looks like, then look no further than the next page of this very class - most of the pages displaying code here are actually Jupyter Notebooks!

Jupyter Lab, the software in wihch you make your Notebook, can be installed via `conda`. It is recommended to do this in either your `base` environment or a purpose built environment (e.g. `jupyter-env`). This is because you don’t want other packages creating conflicts with Jupyter. 

Run the following in the terminal to install Jupyter:

```bash
conda activate gsc
conda install jupyterlab
```

## Running Jupyter Notebooks

:::{note}
Running Jupyter needs to be done every time we want to work on our notebooks! 
:::

From now on, you will be able to open Jupyter Lab from the base environment as follows:

```bash
conda activate gsc
jupyter lab
```

I strongly recommend to start jupyter-lab from the folder where you want to work (i.e. where you have saved your notebooks and data).

The steps are as follows:

1. Open a miniforge prompt (or a terminal on Linux/macOS)
2. Navigate to the folder where you want to work by typing:
    ```
    cd C:\path\to\folder
    ```
    I recommend copying the path from the file explorer - see the video below for an example.
3. Activate the `gsc` environment by typing
   ```
   conda activate gsc
   ```
4. Start Jupyter by typing:
    ```
    jupyter lab
    ```

Jupyter Lab will then open from within your default browser.

This is best explained through the following video:

<div><iframe src="https://player.vimeo.com/video/1048667583?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Open the prompt, navigate to a folder and start JupyterLab"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

You will now be able to navigate your file directory from within the Jupyter Lab, and open new Jupyter Notebook documents.

---
<span style="font-size: 85%;">
This page builds upon CC-BY 4.0 content written by <a href="https://fabienmaussion.info/climate_risks/ready/02-install-jupyter.html">Fabien Maussion</a>.
</span>