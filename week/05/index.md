# Introduction

Week 5 builds upon Week 4 by introducing multi-band optical satellite data, considering how we manage, manipulate, and download data sources such as Landsat and Sentinel-2 imagery.

:::{tip} Learning Objectives
After this session, you should be able to
 - Understand how we can use `xarray` and `rioxarray` to represent and work with 'real' multispectral satellite data.
 - Perform simple band maths and some more complicated classification techniques suited for multispectral analysis.
 - Understand how to search for and download satellite data through online GUI interfaces and Python APIs.
:::

---

:::{toc}
:context: children
:::

---

## Useful Online Material

 - Spatial Thoughts Tutorials -- [Processing Satellite Images with `xarray`](https://www.geopythontutorials.com/notebooks/xarray_processing_satellite_images.html)
 - Earth Data Science Textbook -- [Multispectral Remote Sensing Data in Python](https://earthdatascience.org/courses/use-data-open-source-python/multispectral-remote-sensing/)
 - Microsoft Planetary Computer 
   - [Data Catalog](https://planetarycomputer.microsoft.com/CATALOG) (note the 'Example Notebook' tab within each dataset).
   - [Reading Data from the STAC API](https://planetarycomputer.microsoft.com/docs/quickstarts/reading-stac/) (Note: focusses on searching for data; does not include easy  `odc-stac` downloads)
 - `odc-stac`
   - [Main documentation](https://odc-stac.readthedocs.io/en/latest/)
   - [Access Sentinel-2 Data on the Microsoft Planetary Computer](https://odc-stac.readthedocs.io/en/latest/notebooks/stac-load-S2-ms.html)
 - [USGS Landsat landing page](https://www.usgs.gov/landsat-missions/)
 - [ESA Sentinel-2 landing page](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-2)
 - [USGS Earth Explorer](https://earthexplorer.usgs.gov/)
 - [Copernicus Data Browser for Sentinel-2](https://dataspace.copernicus.eu/data-collections/copernicus-sentinel-missions/sentinel-2)

<!-- ---
#### draft planning notes

NEED TO SPLIT THESE OUT


 - mathematical operations:
   - Focal operations: slope, hillshade, smoothing, etc.
   - Local operations: decision trees?
   - Global operations: average stats, etc.


 - sampling raster data
   - Zonal statistic
   - Point sampling (through time?)
   - rasterisizing and vectorising data?
 - Downloading data?

 - rasterisating and vectorisation
 - band maths? -->
