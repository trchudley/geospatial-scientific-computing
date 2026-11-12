# Structuring a Repository

In this course, we have aimed to learn how to write code for geospatial analysis that is open-source, shareable, and reproducible. Which begs the question - how do you encourage others to share and reproduce it? Understanding how we do this is the ultimate aim of this session.

However, before we begin to explore `git` and GitHub as a means to facilitate code sharing, our first aim should be to make sure we can organise our code in a way that is easy for others to understand. 

## Components of a Basic Repository

A repository (or "repo") is a file directory that contains everything necessary to reproduce your project: code, minimal data, information about dependencies, etc. Someone who has access to your repository should have all the necessary tools and information to reproduce the purpose of the repo.

A repository for the sort of code you will use to produce your final report might look as follows. This is presented as a 'directory tree': names ending in `/` are directories; everything else is a file.

```
my-project/
├── README.md
├── LICENSE
├── environment.yml
├── .gitignore
├── data/
│   ├── vector_file.gpkg
│   └── timeseries.csv
├── figures/
│   ├── figure1.png
│   ├── figure2.png
│   └── figure3.png
└── notebooks/
    ├── 1_download_data.ipynb
    ├── 2_process_data.ipynb
    └── 3_generate_figures.ipynb
```

We will go through each of these components in turn.

### README.md

Contains a high-level overview of the purpose of your code, the directory structure, contact details, etc. Think of this like the 'homepage' of your repository, that people can look at first to get an overview of the project. When sharing a reposotory on GitHub, the `README.md` is automatically displayed beneath the list of files when anyone visits your repository. It is written in Markdown (the same format as the text cells in your Jupyter notebooks), so you can use headings, lists, links, and code blocks.

A useful `README.md` will usually answer the following questions:

 - A title and a short description of the project. If it accompanies a report or paper, mention the context here.
 - A brief description of the directory structure and the key files.
 - How to recreate the software environment (e.g. `conda env create -f environment.yml`)
 - How to access or download any data that are not included in the repository.
 - Which notebooks or scripts to run, and in what order, and what outputs they will produce.
 - Author names, contact details, and a pointer to the license.

For instance, a minimal `README.md` might look like this:

````markdown
# Vegetation change in the Somerset Levels, 2016–2025

Code supporting my GEOGM0081 project report, which uses Landsat-8 and -9 imagery 
to measure changes in NDVI across the Somerset Levels.

## Repository structure

 - `data/` – small input datasets (see `data/README.md` for download instructions for larger files)
 - `notebooks/` – Jupyter notebooks, numbered in the order they should be run
 - `figures/` – figures produced by the notebooks

## Setup

Create and activate the conda environment, which will be called `somerset-ndvi`:

```
conda env create -f environment.yml
conda activate somerset-ndvi
```

## Usage

Run the notebooks in `notebooks/` in numerical order. Figures will be saved to `figures/`.

## License

Code is released under the MIT License (see `LICENSE`).
````

### LICENSE file

If you are going to share the code publicly, you should have a license which shows the terms under which you have released the code. There are [risks of not having a license when you share code publicly](https://choosealicense.com/no-permission/): without one, default copyright law applies, which may allow (or disallow) use that you do not intend!

A license is what definitively makes a project "open-source" - it is the "free as in speech" part of the open-source philosophy, explicitly allowing others to use and adapt the code.

For a generic coding project, the [MIT license](https://opensource.org/license/mit) is probably the most simple and permissive license you can choose. It does two things:

 1. It allows anyone to use, copy, modify, share, and even sell your code (including in non-open-source projects), **on the condition** that they include your copyright notice and a copy of the license with it. In plain language: you must be properly credited.
 2. It emphasises that the code is provided "as is", without any warranty, so you are not liable if something goes wrong when somebody else uses it.

To release your code under a license, you can include a text file called `LICENSE` (no file type suffix) that contains the text of the license. For instance, the MIT license is the following text, making sure to add the year and your name where identified:

```
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

:::{tip}
If you create a file named `LICENSE` through the GitHub website (**Add file** > **Create new file**), GitHub will offer a **Choose a license template** button that fills in the text, year, and your name for you.
:::

Other open-source licenses exist for different purposes. For text/data/media, [Creative Commons Attribution 4.0 International](https://choosealicense.com/licenses/cc-by-4.0/) (also known as "CC-BY 4.0") is probably best. There are [multiple Creative Commons licenses](https://creativecommons.org/about/cclicenses/) with additional restrictions. Note that Creative Commons licenses are not designed for software, so they are not a good choice for your code.

Additional restrictions offered by some licenses include:

 - that only noncommercial use is permitted; 
 - that no adaptations or derivations are allowed;
 - that adaptations are permitted so long as they are released under the same open-source licensing term. This is known as a "copyleft" license that can disrupt - for better and for worse - professional organisations using your code. The [GNU GPL](https://choosealicense.com/licenses/gpl-3.0/) is a well-known example for software.

A guide to choosing a license is available at [choosealicense.com](https://choosealicense.com/).

This course material is released under the MIT license for code and CC-BY 4.0 for text and figures.

### Environment/Requirements file

<!-- ORIGINAL:
`environment.yml` or `requirements.txt`. 

NB: show an example of what both might look like, with dependencies as `rioxarray`, `geopandas`, `matplotlib`. Explain the `environment.yml` is the appropriate choice for conda, so will be our preferred option here.
-->

Someone running your code needs to install the same Python packages you used. Rather than simply listing these in a `README.md`, we can provide a file that a package manager can read to recreate the environment automatically. There are two common formats.

As we have been using `conda` to manage our environments throughout this course, an `environment.yml` will be our preferred option. An `environment.yml` file is read by `conda` (or `mamba`). It specifies the name of the environment, which channels to download packages from, and the packages themselves (including Python itself):

```yaml
name: my-environment-name
channels:
  - conda-forge
dependencies:
  - python=3.12
  - geopandas
  - rioxarray
  - matplotlib
  - jupyterlab
```

Someone can then recreate and activate the environment by running:

```bash
conda env create -f environment.yml
conda activate my-environment-name
```

:::{tip}
You can optionally specify package versions (e.g. `geopandas=1.0` in `environment.yml` - note the different syntax), which makes it more likely your code will still run in several years' time. If you have installed packages with `conda install` as you went along, `conda env export --from-history` will print a list of the packages you explicitly asked for, which is a good starting point for your `environment.yml`.
:::

### .gitignore file

Contains a list of files that you _don't_ want `git` to track (and therefore don't want backed up or shared on GitHub). Each line is a file name or a pattern: `*` acts as a wildcard, and lines beginning with `#` are comments.

A typical example for your project might look as follows:

```
# macOS junk files
.DS_Store

# Windows junk files
Thumbs.db
desktop.ini

# Python and Jupyter junk files (trailing slash / indicates directories)
__pycache__/
.ipynb_checkpoints/

# Don't backup large gridded files
*.tif
*.tiff
*.nc
```

These are all junk and metadata files that Windows, macOS, Python and Jupyter produce automatically, which aren't useful or relevant for our project.

For our projects, it is probably worth also including `.tif` (and `.nc`) files if they are going to be large. Using an appropriate naming convention, you may be able to keep some: for instance, if your full multispectral images are large but your NDVI files are small, you could exclude `*multispectral.tif` files, which would keep files that don't end in `multispectral` (e.g. `*ndvi.tif`). Alternatively, you can exclude all `.tif` files and then make exceptions using `!`:

```
# Ignore all GeoTIFFs...
*.tif
# ...except NDVI outputs
!*ndvi.tif
```

You can have additional `.gitignore` files within each sub-directory to impose additional rules - say, for whatever reason, you only want to not back up `.csv` files within one subdirectory.

:::{note}
`.gitignore` only affects files that `git` is not already tracking. If you have already committed a file and later add it to `.gitignore`, you will also need to tell `git` to stop tracking it with `git rm --cached <filename>` (this leaves your local copy of the file untouched).
:::

<!-- ORIGINAL:
:::{warning} Hidden Files
Explain that beginning with a `.` makes it a hidden file, that might not be visible in a standard file explorer. Provide information on how to make this viewable in windows file explorer and macos finder.
:::
-->

:::{warning} Hidden Files
On macOS and Linux, any file or directory whose name begins with a `.` (such as `.gitignore`, or the `.git` directory we will meet in the next section) is a **hidden file**, and it will not show up in a file browser by default. Windows doesn't hide these files, but hides file extensions by default, which can cause confusion when creating files with no extension (such as `LICENSE`) or with only an extension (such as `.gitignore`).

To see these files:

 - **macOS Finder:** press {kbd}`Cmd` + {kbd}`Shift` + {kbd}`.` to toggle hidden files on and off.
 - **Windows File Explorer:** in Windows 11, select **View** > **Show** and tick **File name extensions** (and **Hidden items**). In Windows 10, tick both boxes in the **View** tab of the ribbon.
 - **Terminal:** `ls -a` (macOS/Linux) or `dir /a` (Windows Command Prompt) will list hidden files.

Some programs make it awkward to create these files: macOS Finder will refuse to name a file starting with `.`, and Windows Notepad may silently save `.gitignore` as `.gitignore.txt`. For the purposes of this course, it is easiest to create an empty file directly from the terminal (e.g. `touch .gitignore` on macOS/Linux, or `type nul > .gitignore` on Windows), and (if you aren't using a dedicated IDE) edit it within Jupyter Lab.
:::

### Your actual content

...within clearly named and described directories.
 
For your project, you might have the following:

 - `data` directory
   - Contains any required data. Do not include even moderately large files (larger than a few megabytes): `git` is not designed to track large binary files, and GitHub will warn you about files larger than 50 MB and reject files larger than 100 MB. Instead, include information in a new `README.md` describing where to download the data and where it should be stored / how it should be named for your code to run. Alternatively, include a Python file / notebook that does the hard work of downloading or recreating the necessary data.
 - `figures` directory
   - Contains the figures your code has produced. An additional `README.md` may describe the individual files.
 - `notebooks` directory
   - Contains the code/notebooks you can run. 
   - Should have suitable inline text/comments to explain what is going on to an interested user.
   - When a user has successfully followed all instructions to set up the environment / collate the necessary data, it should be possible simply to run any code from beginning to end with no other inputs, and the output data/figures will be recreated from scratch. 
   - An additional `README.md` may describe what order to run the code files, or what the intended outcomes might be.


Some other general guidance for your content:

 - **Use relative file paths.** A path like `C:/Users/myname/Documents/project/data/timeseries.csv` will only work on your computer. A path relative to the notebook, such as `Path("../data/timeseries.csv")` (using `pathlib`), will work for anyone who downloads the whole repository.
 - **Number your notebooks** (e.g. `1_download_data.ipynb`, `2_process_data.ipynb`) so the order in which they should be run is obvious.
 - **Check your notebooks run from top to bottom** before sharing them: in Jupyter Lab, use **Kernel** > **Restart Kernel and Run All Cells**. It is easy to accidentally rely on a cell you have since deleted, edited, or included in the wrong order.
 - **Use clear file and variable names.** `ndvi_2020_summer.tif` is much more helpful than `output2_final_v3.tif`.
 - **Do not include `geemap` map outputs.** These can also be large binary files which take up space. Make sure to "clear cell output" on these before uploading to a directory.

## What this looks like in practice

The purpose of structuring a repository in this way is so that others can intuitively find and use your code. The main way of sharing code is via GitHub, which we will learn how to use through the rest of this session.

I have shown an example of how I might share some code at [github.com/trchudley/geogm0081-example-repo](https://github.com/trchudley/geogm0081-example-repo). You are welcome to explore this on GitHub, or download it by clicking **Code** > **Download ZIP**. Feel free to examine this working example, and think about how you might begin to structure your own project code for sharing.

## Replicable, Reproducible, and Open Science

It has long been convention that a scientific paper should be "reproducible". Traditionally, this might have meant that a study is _replicable_ - that it contains detailed enough methods to reproduce the experiments within, and, [if the science is sound](https://en.wikipedia.org/wiki/Replication_crisis), then other scientists should be able to follow those instructions and reach the same results and conclusions. This is still a good principle to have in mind as you write your methods sections - I like to think of them as "the set of instructions I wish I had when I began the project". 

As science has transitioned towards more open methods and data (sometimes [mandated by funders](https://www.ukri.org/manage-your-award/publishing-your-research-findings/making-your-research-data-open/)), reproducibility has taken on a more specific meaning. If we can share the underlying data and code, then other scientists can use the original input data, code, methods, and analysis conditions to reproduce _the exact results_, and even _the exact figures_, presented in studies. This allows other scientists to examine the code for both useful methods they can use in their own work, and potential errors that could be improved in the future.

Some examples of these kinds of repositories from my own field are below. Take a look at them and see what you think - not all of them follow the exact outline I have described above, but some methods of sharing may feel more intuitive to you than others.

 - [Chudley _et al._ (2026) Data supporting "Seasonal ice dynamics control the timing of crevasse drainage at a fast-flowing outlet glacier"](https://github.com/trchudley/seasonal-crevasse-hydrology)
 - [Picton _et al._ (2025) Code associated with the manuscript "A reassessment of the role of atmospheric and oceanic forcing on ice dynamics at Jakobshavn Isbræ (Sermeq Kujalleq), Ilulissat Icefjord"](https://github.com/hannahpicton/jakobshavn_isbrae)
 - [Ryan _et al._ (2025) Code for "Meltwater ponding has an underestimated radiative effect on the surface of the Greenland Ice Sheet"](https://github.com/JohnnyRyan1/meltwater)

It is worth noting that science can be _open_ without being perfectly _reproducible_. This is noted by my colleagues at the Geological Survey of Denmark and Greenland (GEUS) in their [Greenland ice discharge repository README](https://github.com/GEUS-Glaciology-and-Climate/ice_discharge). They note that every line of code needed to recreate their dataset is viewable in this repository, but to reproduce the work would also require ~100 GB of input velocity data, which is not shared. People can still inspect, use, and critique the code, but won't be able to recreate the outputs without additional data.

You might have to decide what level of openness and reproducibility is useful for your future work. In my own repository I linked to above, it is certainly possible to recreate every output figure from my source paper. However, the source data for the paper comes from over 800 individually classified Sentinel-2 scenes, which I have not shared - instead, I share `.csv` files of the abstracted data, which is much more efficient to share in a repository format. So is this technically reproducible, from beginning to end? It is a reality of working with 'big data' that sharing the source datasets might not be possible due to vast data sizes. However, I have separately made available [the U-Net I used to classify the imagery](https://github.com/trchudley/crevasse-hydrology-unet), so users would be able to reproduce the source data if they wanted to!

## Summary

We have seen how we might structure our code into user-friendly directory structures, known as repositories, that allow people to inspect and reuse our code. This is the end goal for how our code should look when we come to submit our project reports.

In the next section, we will see how we can begin to track and share this code.
