---
numbering: false
---

# External Resources

## Online Resouces for Geospatial Python

 - [Python for Geographic Analysis Textbook](https://pythongis.org/)
 - [Geographic Data Science Textbook](https://geographicdata.science/book/)
 - [Python Foundation for Spatial Analysis](https://courses.spatialthoughts.com/python-foundation.html)

## Online Resources for Scientific Computing

- Software Carpentry
  - [Programming with Python](https://swcarpentry.github.io/python-novice-inflammation/)
  - [Plotting an programming with Python](https://swcarpentry.github.io/python-novice-gapminder/)
  - [Version Control with Git](https://swcarpentry.github.io/git-novice/)
  - [The Unix Shell](https://swcarpentry.github.io/shell-novice/)
- [GitHub Learn](https://learn.github.com/skills)

## Python Tool Documentation

- [`conda` (Package Manager)](https://docs.conda.io)
- [`numpy`](https://numpy.org/)
- [`pandas`](https://pandas.pydata.org/)
- [`matplotlib`](https://matplotlib.org/)
- [`geopandas`](https://geopandas.org/)
- [`xarray`](https://docs.xarray.dev)
  - [`rioxarray`](https://corteva.github.io/rioxarray)
  - [`xarray-spatial`](https://xarray-spatial.readthedocs.io)
- [`pystac-client`](https://pystac-client.readthedocs.io)
  - [`odc-stac`](https://odc-stac.readthedocs.io)

## Data Resources

Some of these data sources require creating an account, but all are free to access. Be sure to cite the origin of your data in your projects and dissertations!

### Gridded Data

 - Satellite Data
   - [USGS EarthExplorer](https://earthexplorer.usgs.gov/) - A simple online GUI for downloading Landsat data, amongst other more niche USGS products.
   - [USGS Landsat Data Access summary](https://www.usgs.gov/landsat-missions/landsat-data-access)
   - [Copernicus Browser](https://browser.dataspace.copernicus.eu) - the 'official' way of downloading Sentinel-2 data.
   - [NASA EarthData Search](https://search.earthdata.nasa.gov) - Not quite as simple as EarthExplorer but useful for wider datasets, e.g. the Harmonised Landsat/Sentinel-2 (HLS) dataset.
   - [SentinelHub EO Browser](https://www.sentinel-hub.com/explore/eobrowser/)
 - Climate Data
   - [Copenicus Climate Data Store](https://cds.climate.copernicus.eu/) ([for ERA5 data - download tutorial here](https://confluence.ecmwf.int/spaces/CKB/pages/129135000/How+to+download+ERA5))
     - I recommend focussing on ERA5-Land data - e.g. [ERA5-Land monthly averaged data](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land-monthly-means?tab=download).
   - [HadUK-Grid Gridded Historic Climate Data](https://www.metoffice.gov.uk/research/climate/maps-and-data/data/haduk-grid/haduk-grid)

### Vector Data

- Administrative Boundaries
  - [Natural Earth](https://www.naturalearthdata.com/) - A good source for public domain political boundaries, as well as background maps.
  - [geoBoundaries](https://www.geoboundaries.org/) - An open database of political administrative boundaries.
- Political Data
  - [UK Office for National Statistics Open Geography Portal](https://geoportal.statistics.gov.uk/) - UK socio-political data.
  - [US Census Shapefiles](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html)
  - [Eurostat GISCO](https://ec.europa.eu/eurostat/web/gisco)
- Environmental Data
  - [HydroSHEDS database](https://www.hydrosheds.org/)
  - [OpenAQ Air Quality data](https://openaq.org)

### Tabular Data

 - Weather station data
   - [Meteostat weather and climate database](https://meteostat.net) - Conveniently download using a [simple python package](https://dev.meteostat.net/python). Try this first!
   - [MIDAS Open Data for UK meteorological stations](https://archive.ceda.ac.uk/tools/midas_stations) - Be sure to filter by "MIDAS Open Stations".
   - [UK Met Office Monthly met station data](https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data) - More limited datasets available but very easy to use.
   - [NCEI NOAA Climatology Network daily](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily) - search for daily data from globally available stations. 
   <!-- - [NCEI NOAA Integraded Surface Database (ISD)](https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database) - another global collation for hourly and daily data. -->

## Other Geospatal Python Courses

 - [UW Geospatial Data Analysis with Python Course](https://uwgda-jupyterbook.readthedocs.io)
 - [Duke Geospatial Data Science Course](https://ryan-lab-duke.github.io/gds-applications-site)
 - [Helsinki Geo-Python Course](https://geo-python-site.readthedocs.io)
 - [Helsinki Automating GIS Processes](https://autogis-site.readthedocs.io/en/latest/index.html)
