# Consolidation Week

Week 6 is consolidation week, with no formal teaching. Congratulations on making it halfway through the course!

In the time before we reconvene, there are two things I would like you to do. The first is to begin to consider the topic of your final assessment; the second is to sign up to the services we will be learning how to use in the second half of term.

## Formative Work

As dicussed within the Week 5 lecture and [exercise material](../05/exercises-week-05.ipynb#extension-task-project-proposal), your formative project proposal is due in Week 7. This will allow you to receive feedback on an idea for your final project report. The full brief for the formative assessment [can be found on the course blackboard](https://www.ole.bris.ac.uk/ultra/courses/_269813_1/outline), under 'Unit Assessment'.

## Ensure access to new services

We will be using a couple of new tools in the second half of term that require additional sign-ups and installations (thankfully, nothing as complex as our initial Python install). Please ensure you have completed the following steps:

### Google Earth Engine

Ensure you have created GitHub and Google Earth Engine accounts necessary for teaching in the second half of term. If you do not have access to Google Earth Engine account, you will need to:

- Ensure you have a Google account.
- Sign up for Google Earth Engine by following the [following instructions](https://courses.spatialthoughts.com/gee-sign-up.html).

### Github

#### Sign up for GitHub

If you do not have a GitHub account, sign up for one at [https://github.com/signup](https://github.com/signup).

#### Install Git

Ensure that `git` is installed on your local machine. Depending on your install method, this can take a while, so **you should do this _before_ the `git` session in Week 9**.


::::{tab-set}

:::{tab-item} On Windows
:sync: win
Download [the Windows installer for the official Git downloads page](https://git-scm.com/install/windows).

Once downloaded, run the installer to begin setup. As you progress through the installer screens, you can keep most of the default settings. However, there will be option to "Adjust PATH Environment": here, ensure the setting selected is _“Git from the command line and also from 3rd-party software”_. This ensures `git` will be available from within the Miniforge prompt automatically.
:::

:::{tab-item} On MacOS
:sync: os
Within your terminal, run the command:

```bash
xcode-select --install
```

You may have to continue to prompt the install, either in the terminal (by typing `y` or `yes`), or in an installation wizard window that pops up.
:::

::::

After installation, typing a command such as `git --version` or `git help -a` should return reasonable responses.

<!-- 
:::
For your final project, you will use geospatial data to assess and report on land use change over an area of your choice. 

An outline for such a project might be:

  1. Download satellite images to assess change over a period of interest, using e.g. normalised difference indices to map a type of surface (vegetation, snow, water, etc.).
  2. Generate statistical summaries of these data outputs. For instance, you might wish to threshold the NDI data and measure the change in classified area through time, or create a vector data boundary and calculate zonal statistics (mean values, etc. - this will be taught in the second half of term).
  3. Link the observed changes to underlying causes - for examples, anomalies in climate data (also to be taught in the second half of term) or other known events from third-party data.

Consolidation week provides an opportunity for you to consider what the topic of your choice might be, and to explore whether this topic is feasible to detect in available satellite data. Below, I provide a number of examples of topics that you are welcome to choose, but you may also be inspired to pick your own topic as well. 

:::{note} **Example Topics** (click to show)
:class: dropdown
 - Monitoring vegetation loss following e.g. wildfires or deforestation.
 - Tracking snowline elevations in response to winter climates.
 - Recording the urbanisation of fast-growing cities.
 - Observing other large-scale human influences on the landscape (afforestation, the creation/destruction of reservoirs, etc.).
 - The impact of drought years on vegetation.
:::

A good tool to explore preliminary changes is the Google Earth Timelapse tool, available at [https://earthengine.google.com/timelapse/](https://earthengine.google.com/timelapse/). This might provide an indicator of whether a certain event has made a visible mark on the landscape in medium-resolution optical satellite imagery.

Once you've found an event that might interest you, return to the material you have already been taught. Search for and download two suitable optical satellite data (I recommend using Landsat products) to show the before/after of your land use change, and produce appropriate figures. You may also wish to show NDI values to test that your land use change is able to be monitored using quantitative values. 
-->