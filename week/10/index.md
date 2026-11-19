# Introduction

Weeks 10 and 11 are dedicated to providing in-class time to work on your final project, and you are welcome to dedicate your time to that if you so wish.

However, this final content aims to provide practical recommendations for how you might take your skills forward. This class has aimed to provide a “menu” of basic building blocks that can be used to achieve more complex geospatial tasks: here, I aim to provide some pointers as to what those more complex tasks might be. It isn't meant to provide a comprehensive introduction to the tasks at hand, but instead provide tasters of what is available, and how you might go forward to develop these skills!

:::{tip} Learning Objectives
After this session, you should be able to
 - Think about how we might structure code to ensure it is clear and readable even as our analysis extends to hundreds or thousands of large files.
 - Explore how we can link the Python geospatial stack to machine learning workflows.
 - Identify what unique problems exist for applying machine learning workflows to satellite image data, and what tools are available to address these issues.
:::

---

:::{toc}
:context: children
:::

---

## Useful Online Material

 - `xarray` documentation: [parallel computing with `dask`](https://docs.xarray.dev/en/stable/user-guide/dask.html)
 - Software Carpentry: [Parallel Programming in Python](https://carpentries-incubator.github.io/lesson-parallel-python/)
 - [Random forest interpretability](https://kodu.ut.ee/~kmoch/geopython2025/Py_08/rf_interpretability.html) (University of Tartu Geopython course)
 - [Google's Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/prereqs-and-prework)
 - [Machine Learning in Google Earth Engine](https://developers.google.com/earth-engine/guides/machine-learning)
 - Satellite Embeddings
   - [Google Earth Engine guide to Satellite Embeddings](https://developers.google.com/earth-engine/tutorials/community/satellite-embedding-01-introduction)
   - [SpatialThoughts guide to Embeddings in `xarray`](https://www.geopythontutorials.com/notebooks/xarray_embeddings_similarity_search.html)
 - [PyTorch](https://pytorch.org/)
   - ['Learn the Basics'](https://pytorch.org/tutorials/beginner/basics/intro.html)
   - [`segmentation-models-pytorch`](https://github.com/qubvel-org/segmentation_models.pytorch)
 - [TorchGeo](https://torchgeo.readthedocs.io/)
   - [TorchGeo Documentation](https://docs.torchgeo.org/en/stable/index.html)
   - [TorchGeo Tutorials](https://docs.torchgeo.org/en/stable/tutorials/index.html)


<!-- 

---
#### draft planning notes

 - Outline of final project
 - Ideas
 - Fill in Blue feedback!

Opportunity for a bit of a catch-all week:
How to automate a data workflow?  -- https://earthdatascience.org/courses/use-data-open-source-python/earth-data-science-workflows/design-efficient-automated-data-workflows/
Data scaling - dask?

 - glob, functions, and looping to scale data
 - Introductory ML: Random forest?
 - Segementation/Segment Anything Model?
 - More DEM stuff
 - Satellite embeddings? -- https://www.geopythontutorials.com/notebooks/xarray_embeddings_similarity_search.html

Future opportunity to split this into two courses: one more focussed on geospatial scientific computing, and another on programmatic Earth Observation

TB-1: Geospatial Scientific Computing
1. Introduction to the Command Line Interface (nb: Windows users?) + Install Python?
2. Basic Python (& numpy?)
3. Scientific Python (pandas / statistics?)
4. Geospatial data vis (matplotlib [and cartopy?])
5. Vector Data (geopandas)
6. Gridded Data (xarray)
7. Spatiotemporal Analysis (combined geopandas/xarray)
8. Putting together a project for open distribution: project design, functions, packages, etc.
9. Git and GitHub

Assessment: [?] Focus on geopandas + ERA-5 data analysis rather than EO imagery. Submit/asssesed as 'proper' github repo.

TB-2: Programmatic Earth Observation
1. Raster Data (rioxarray)
2. Optical Satellite Data
3. Topographic Data (DEMs + possibly LiDAR/altimetry data?)
4. SAR (GRD/RTC only!)
5. Cloud computing (Google Earth Engine)
6. Machine Learning (PBIA)
7. OBIA (incl. Segmentation/SAM)
8. Deep Learning I (NNs)
9. Deep Learning II (CNNs) 

Assessment: as per original GSC analysis.

If TB-1 sessions 2-5 could be slotted into UG course, then TB-2 would make a nice second/third year course too...
 -->
