# Introduction

Week 7 introduces further ways we can interact with vector and gridded data to quantify change across space and time.

:::{tip} Learning Objectives
After this session, you should be able to
 - Understand how vector data can be used to clip and manipulate raster data.
 - Obtain spatial samples and statistics (point, line, and polygon) of gridded data.
 - Think about how to scale these tools to extract information across time-series.
:::

---

## Useful Online Material

 - Project Pythia Foundations -- [`xarray`](https://foundations.projectpythia.org/core/xarray/)
 - Spatial Thoughts Tutorials
   - [`xarray` for Raster Data Processsing](https://www.geopythontutorials.com/notebooks/xarray_raster_styling_analysis.html)
   - [`xarray` for Climate Data Processing](https://www.geopythontutorials.com/notebooks/xarray_aggregating_time_series.html)
 - [`xarray` User Guide](https://docs.xarray.dev/en/stable/user-guide/index.html)
 - Optional additional packages:
   - [`geocube` User Guide](https://vylor.github.io/geocube/stable/)
   - [`exactextract` User Guide](https://isciences.github.io/exactextract/index.html)
   - [`xarray-spatial` zonal module](https://xarray-spatial.readthedocs.io/en/stable/user_guide/zonal.html)
 - [Keeley _et al._ (2009)](https://www.researchgate.net/publication/228638145_Fire_intensity_fire_severity_and_burn_severity_a_brief_review_and_suggested_usage):  Fire intensity, fire severity and burn severity: a brief review and suggested usage  

<!-- #### draft planning notes

1. Combining vector and gridded data
   1. Plotting
   2. Clipping
   3. Vectorisation
2. Point and spatial sampling
   1. Sampling
   2. Calculating zonal statistics
3. Time-series analysis
   1. Differencing: relative change, percent change, thresholding
   2. Creating statistics through time

PATHWAY:

 - Geopandas and xarray, plot together
 - Clip
 - Sample raster data
 - zonal statistics
 - zonal time-series

-->