# Editing `.py` files

In the main text, I identify that common way to run long Python scripts without having to tab through a Jupyter Notebook is to use `.py` file, and run this in the command line. Ultimately, a `.py` file simply a text file of Python commands. For instance, say we have a file called `myscript.py` containing the following:

```
myname = "Tom"
print("Hello world, my name is " + myname)
```

Running `python myscript.py` in the command line will output the text `Hello world, my name is Tom`. I hope you can see how this would be useful to write long, complex processing scripts.

As stated, a `.py` file is simple a text file. You could write an entire software programme using only a plain-text editor such as Notepad (Windows) or TextEdit (macOS) if you wish, and some do - although I wouldn't recommend it! As your scripts get longer and more complex, it is nice to be able to write code in an environment that can help you with the small details - such as colour-coding code blocks to help you visualise structure (“syntax highlighting”); identifying errors in your code that will break your script; or by providing built-in functionality for running and debugging code.

If you are have used e.g. MATLAB or R (using RStudio), you will be familiar with an Integrated Development Environment (IDE). This editing environment provides you with a graphical user interface (GUI) application within which to edit your code, but also other windows for other functions, such as keeping track of variables or viewing figure outputs. If you are very familiar with this MATLAB/R-style interface, then there are similar-feeling IDEs available for you in Python - take a look into [spyder](https://www.spyder-ide.org/) or [PyCharm](https://www.jetbrains.com/pycharm/). 

However, IDEs have never quite taken off in the same way for Python development. It’s partly because of the wide range of purposes Python is used for beyond data science (including e.g. web development), the range of non-Python elements Python programmers often use (such as CLI-based environment management, `git`, or metadata files), and because of the development of modern alternative ways of doing data science, such as Jupyter Notebooks.

Instead, my own preferred method is to use a _code editor_. Out of the box, these are effectively just fancy-looking text editors. However, by using extensions, they rapidly become very powerful tools, and can become the mainstay of how you interact with data files. I use my code editor for Python, MATLAB, metadata management, ssh-ing into HPCs, and even to write the document you are reading now!

Out of all code editors, the most common is [Visual Studio Code](https://code.visualstudio.com/). As discussed above, it is effectively a fancy text editor, so there isn’t too much to say by way of a basic tutorial, but there is one [here](https://code.visualstudio.com/docs/python/python-tutorial) if you like (note that it’s telling you to install Python, environments, and packages in ways other than `conda` - ignore these tips!).

As alluded to, it is the library of _extensions_ that make VS Code truly powerful, but I wouldn’t worry about these. Most worth installing will be recommended to you as you open files. For instance, once you open the a `.py` file, the ‘Python’ add-on will be recommende in the bottom-right-hand corner. This will give you the recquisite tools for syntax highlighting, linting (automatically making sure your code is laid out appropriately), and environment management. Just take a look at the instructions for what you’re installing so that you know how to use it effectively.

I have also installed additional packages such as `black` (my preferred linter), the ‘Remote - SSH’ tool for accessing HPCs, tools for better git management, tools for previewing and linting markdown, csv, and Makefiles, and even an add-on for using Jupyter Notebooks within VS Code. I didn’t do this all on day one though! Just know that if there’s something you want to do with code or programming, there’s probably some way that VS code can help.