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
2
```

You have run your first python command! Admittedly, it was a little anticlimactic. 

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

This command line interface (CLI) is fine for exploring what Python can do, and you should definitely use it to explore basic data types, or quickly check that certain things are possible/installed/etc. However, it’s hard to write complex multi-line commands, or save scripts for repeat use. As a result, we tend to gravitate towards two other options:

1. The first is to write `.py` files, which are simply text files of Python commands that will be run one-by-one. These can be run through the Python interpreter (e.g. `python myscript.py`). This is useful for writing longer processing scripts that will be run autonomously to achieve tasks. 
2. The second is to use a ‘Jupyter Notebook’ (files with the suffix `.ipynb,` a vestigial reference to when these were known as iPython notebooks). These are mixed-media files run in your browser. You can combine text and code, and they are useful for when you are actively tinkering with the data (e.g. plotting, statistics, analysis, etc.), and making notes and wider documentation.

In this course, we will be using the latter as a beginner-friendly way of exploring Python and managing data. If you are interested in the latter, I have [written more about writing `.py` files in the appendix](../../backmatter/pyfiles.md)

## Installing Jupyter

:::{note}
Installing Jupyter only needs to be done once!
:::


The modern way that data scientists tend to interact with Python is through something called _Jupyter Notebooks_. These are mixed-media documents of text and code that allow you to annotate and iterate code production. If you want an example of what one looks like, then look no further than this website - most of the pages displaying code here are actually Jupyter Notebooks!

<!-- Jupyter Lab, the software in wihch you make your Notebook, can be installed via `conda`. It is recommended to do this in either your `base` environment or a purpose built environment (e.g. `jupyter-env`). This is because you don’t want other packages creating conflicts with Jupyter.  -->

To make things simple for this course, we can install Jupyter in our `gsc` environment by running the following in our terminal:

```bash
conda activate gsc
conda install jupyterlab
```

## Running Jupyter Lab

:::{note}
Running Jupyter needs to be done every time we want to work on our notebooks! 
:::

From now on, you will be able to open Jupyter Lab from the base environment as follows:

```bash
conda activate gsc
jupyter lab
```

A new page will open in your browser. On the left side, you should be able to see a list of files/folders, starting from the folder from which you opened the Jupyter Lab instance. As a result, I strongly recommend to start Jupyter Lab the folder where you want to work (i.e. where you have saved your notebooks and data.

The steps are as follows:


::::{tab-set}

:::{tab-item} On Windows
:sync: win
1. Open a miniforge prompt.
2. Navigate to the directory where you want to work by typing:
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


<div><iframe src="https://player.vimeo.com/video/1048667583?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Open the prompt, navigate to a folder and start JupyterLab"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>
:::

:::{tab-item} On MacOS and Linux
:sync: os
1. Open the
2. Navigate to the folder where you want to work by typing:
    ```
    cd /Users/username/my/working/directory
    ```
    I recommend copying the path from the file explorer. On MacOS, you can do this by finding your directory within the Finder. Right-click on the directory, hold the `Option` key, and click the `Copy "Directory" as Pathname" option. You can then paste this into the terminal.
3. Activate the `gsc` environment by typing
   ```
   conda activate gsc
   ```
4. Start Jupyter by typing:
    ```
    jupyter lab
    ```
:::

::::

Jupyter Lab will then open as a page within your default browser. You will now be able to navigate your file directory from within the Jupyter Lab, and open new Jupyter Notebook documents.

## Create and edit a Jupyter Notebook

With your Jupyter Lab open, create a new Notebook (e.g. by clicking a tile in the 'Notebook' main space, or through `File > New > Notebook`). This will create, and open, a Noteobok in the directory you are currently in (as shown in the File Browser on the left).

You will notice an empty box that you can type in at the top of the new tab. Write `print("Hello World")` into the box. Then, with the cell selected either click the play button (▶) at the top of the page, or use the keyboard shortcut `Shift + Enter`.

You will see `"Hello World"` appear beneath the cell. This is the output of the command we chose.

Next, click the "+" button to add a new cell beneath the one you have connected. In the top bar, there is a drop-down menu, currently set to `Code`. Change it to `Markdown`. Within the box, write a sentence of your choosing, and then press `Shift + Enter`. You will find that this is now rendered as text. Jupyter Notebook recognises special text (headers, links, italics, bold, lists, etc.) using a special system known as "Markdown". Understanding the finer points of Markdown is not necessary in this course, but the basics can be taught in two minutes by using a friendly Markdown preview tool such as [Markdown Live Preview](https://markdownlivepreview.com/). In the linked website, edit the raw text on the left-hand panel to see how it is rendered in the right-hand panel. Then, try and replicate some of this within your own Jupyter Notebook.

This is the building blocks of a Jupyter Notebook: a combination of "code blocks" and "text blocks" that allow you to intersperse chunks of code with descriptions of what you are doing. By chaining these together, you can create longer descriptive documents of code and text (like much of this website!).

Now that we have done the boring bit (installed Conda, Python, and Jupyter), we can begin to play and learn Python proper... 

---
<span style="font-size: 85%;">
This page builds upon CC-BY 4.0 content written by <a href="https://fabienmaussion.info/climate_risks/ready/02-install-jupyter.html">Fabien Maussion</a>.
</span>