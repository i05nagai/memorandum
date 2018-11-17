---
title: QGIS
---

## QGIS

## Install
For OSX,

```
brew tap osgeo/osgeo4mac
brew tap --repair

brew cask install xquartz
brew install qgis3
```

## Usage
Run the following in command line

```
qgis3
```

Convert to GeoJSON


* select Layers
* Right click selected layers
* Select `Export->Save Feature as`
* Configure exporting parameters
    * Choose format `GeoJSON`
    * Change CRS to `EPSG:4326` or `WGS 86`


Save as shapefile

* Select layers
* Right click selected layers
* Select `Export->Save Feature as`
* Configure exporting parameters
    * Choose format `ESRI Shapefile`
    * Change CRS to `EPSG:4326` or `WGS 86`

Conver Shapefile to WKT while changing coordinate system

* Change coordinate system with QGIS and Save it as new shapefile
* Convert the new shapefile to WKT with `gdal`

## Plugins
`Plugin->`

Lat Lon Tools

Quick WKT


## Reference
* [Adding Latitude and Longitude Data to Shapefiles \| Fulcrum Help Center](http://help.fulcrumapp.com/data/adding-latitude-and-longitude-data-to-shapefiles)
* [OSGeo/homebrew\-osgeo4mac: Mac homebrew tap for maintaining a stable work environment for the OSGeo\.org geospatial toolset](https://github.com/OSGeo/homebrew-osgeo4mac)
* [Documentation](https://qgis.org/en/docs/index.html)
* [Selecting a Geographic Coordinate System](https://www.maptools.com/selecting_a_coordinate_system)
