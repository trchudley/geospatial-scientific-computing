# Introduction

Week 2 introduces core scientific Python packages for managing tabular data and plotting.

:::{tip} Learning Objectives
After this session, you should be able to
 - Understand `numpy` and the `numpy.array` object as a basic building block of scientific Python.
 - Understand how to create effective plots using the `matplotlib` library.
 - Create and read tabular data using the `pandas` library and the `DataFrame` structure.
 - Use `pandas` functions to perform basic data analysis on tabular data, including statistical analysis and time-series analysis.
:::

---

:::{toc}
:context: children
:::

---

## Useful Online Material

 - Project Python Foundations Course
   - [`numpy`](https://foundations.projectpythia.org/core/numpy/)
   - [`matplotlib`](https://foundations.projectpythia.org/core/matplotlib/)
   - [`pandas`](https://foundations.projectpythia.org/core/pandas/)
 - Practical Data Science for Python:
   - [Numpy](https://practicaldatascience.org/notebooks/class_2/week_2/10_why_numpy.html)
   - [Pandas](https://practicaldatascience.org/notebooks/class_3/week_2/00_intro_to_pandas.html)
   - [Data Visualisation](https://practicaldatascience.org/notebooks/class_5/week_1/1.1.2_effective_plotting_practices.html)
 - W3 Schools [Pandas Tutorial](https://www.w3schools.com/python/pandas/default.asp)
 - Python for Geographica Data Analysis Textbooks
   - [Chapter 3 - Introduction to data analysis](https://pythongis.org/part1/chapter-03/index.html)
   - [Chapter 4 - Introduction to data visulaisation](https://pythongis.org/part1/chapter-03/index.html)
 - Earth Data Science Textbooks -- [Scientific Data Structures](https://earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/)
 - Software Carpentry -- [Plotting and Programming with Python](https://swcarpentry.github.io/python-novice-gapminder/)
 - Package Documentation
   - [`numpy` User Guide](https://numpy.org/doc/stable/user/index.html)
   - [`numpy`: the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)
   - [`pandas` User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
   - [`matplotlib` User Guide](https://matplotlib.org/stable/users/index.html)
 - [`matplotlib` "cheatsheets"](https://matplotlib.org/cheatsheets/)

---
<span style="font-size: 85%;">
Some content from this session builds upon CC-BY 4.0 content written by others. Elements of the `numpy` and `matplotlib` material are taken from <a href="https://foundations.projectpythia.org/">Project Pythia</a> and <a href="https://pythongis.org/index.html">Tenkanen <i>et al.</i></a>.
</span>


<!-- 
---


TOM M NOTES

Hi Tom,

I think the only things I'd maybe additionally mention in the foundation model section is the DINO series of models which are becoming very popular in remote sensing as an alternative to satellite embeddings, especially for things such as depth estimation and feature extraction. (Vision models often need higher resolution imagery (<10m) than embedding models).

It could also be useful to mention that foundation models, as opposed to traditional deep learning models, are designed to be fine-tuned with limited compute and datasets as they have already been trained, and therefore can be fine-tuned and inferenced on local hardware. This can be done on CPU although, GPU (CUDA or MLX) is preferable as you mention.

And that all the latest deep learning models,  how to use them, and what hardware they require can be found for free on huggingface. Very useful for students that are interested in deep learning as the large companies (Meta, Nvidia, Google) all provide guides and setups for installation of the latest models.

Cheers,
Tom.

#### draft planning notes 

1. Core Python Modules: Numpy, Pandas, and Matplotlib
   1. Numpy
      1. Arrays, dtype, shape, indexing, slicing, booling indexing, broadcasting, opeations (mean, median, std, sum, min, max, nan)
   2. Plotting
      1. Matplotlib scatter, histogram, line, bar, imshow
      2. Controlling plot looks
      3. Colormaps
   3. Pandas
      1. DataFrame, series, reading csv, selecting commons, filtering rows, sorting, groupby
      2. Temporal averaging etc.
   4. Scipy?
      1. Statistics etc.?

Exercises:
 - Analyse provided data: e.g. climate data, mauna loa CO2 record

## Sections

1. Scientific Packages
2. Pandas
3. [Plotting](plotting.ipynb)

 -->
