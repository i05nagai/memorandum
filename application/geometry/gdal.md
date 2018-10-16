---
title: gdal
---

## gdal


## Install
For OSX,

```
brew install gdal
```


## ogr2ogr
[GDAL: ogr2ogr](https://www.gdal.org/ogr2ogr.html)


### Usage


```
ogr2ogr --help-general
```

Show supported formats

```
ogr2ogr --formats
```

```
ogr2ogr -f csv -lco GEOMETRY=AS_WKT <output-filename>.csv <input-shapefile>.shp
```

* `-f <output-foramt>`
    * output format

## Reference
* [GDAL: GDAL \- Geospatial Data Abstraction Library](https://www.gdal.org/)
