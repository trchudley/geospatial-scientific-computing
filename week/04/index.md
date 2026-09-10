# Introduction

Week 4 introduces core packages for managing and manipulating gridded raster data, using Digital Elevation Models (DEMs) as a base single-band example.

:::{tip} Learning Objectives
After this session, you should be able to
 - Understand how $n$-dimensional grids of numbers can be represented within Python using `numpy` arrays and `xarray` data structures (`Dataset` and `DataArray`).
 - Understand how `rioxarray` extends `xarray` to handle raster-type data.
 - Execute common raster operations such as clipping, reprojecting, and resampling.
 - Understand how to perform mathematical operations on raster data, using digital elevation models (DEMs) as a base example.
:::

---

## Useful Online Material

 - Python for Geographic Data Analysis - [Chapter 7 - Raster data processing](https://pythongis.org/part1/chapter-03/index.html)
 - Introduction to GIS Programming - [`xarray`](https://geog-312.gishub.org/book/geospatial/xarray.html) and [`rioxarray`](https://geog-312.gishub.org/book/geospatial/rioxarray.html)
 - [`xarray` User Guide](https://docs.xarray.dev/en/stable/user-guide/index.html)
 - [`rioxarray` examples](https://corteva.github.io/rioxarray/stable/examples/examples.html)
 - [`xarray-spatial` User Guide](https://xarray-spatial.readthedocs.io/en/stable/user_guide/index.html)
 - [`cartopy` examples](https://cartopy.readthedocs.io/stable/gallery/index.html) 

---

#### draft planning notes

 - Raster fundamentals:
 - Landsat programme
 - xarray and rioxarray
   - Reading data
   - pixels, resolution, extent, CRS, nodata
 - reprojection
 - clipping/masking
 - mathematical operations:
   - Focal operations: slope, hillshade, smoothing, etc.
   - Local operations: decision trees?
   - Global operations: average stats, etc.
   - NOT ZONAL OPERATIONS - SAVE FOR LATER
 - USE DEMS AS AN EXAMPLE? KEEP THINGS SIMPLE. 1D...
 - downloading data?



- 4. Raster I: (rio)xarray, repojection, indices
   1. Raster and NDim data
   2. xarray and rioxarray
   3. Managing projections


 - Exercises: download data, preprocess, etc.
